import json
import re
import subprocess

def test_portal():
    with open('index.html', encoding='utf-8') as f:
        html = f.read()

    # 1. Check embedded curriculum json
    prefix = 'const CURRICULUM = '
    start = html.find(prefix)
    assert start != -1, "CURRICULUM not found in index.html"
    start += len(prefix)
    end = html.find(';\n\n    // State', start)
    assert end != -1, "End of CURRICULUM not found"
    
    curriculum = json.loads(html[start:end])

    domains = curriculum['domains']
    assert len(domains) == 21, f"Expected 21 domains, got {len(domains)}"

    all_topics = []
    for d in domains:
        assert 'code' in d and 'title' in d and 'topics' in d
        assert len(d['topics']) > 0, f"Domain {d['code']} has no topics"
        all_topics.extend(d['topics'])

    assert len(all_topics) == 117, f"Expected 117 topics, got {len(all_topics)}"
    
    labs = [t for t in all_topics if t['isLab']]
    assert len(labs) == 28, f"Expected 28 follow-along labs, got {len(labs)}"

    # Check ascending order of topic timestamps
    prev_sec = -1
    for t in all_topics:
        sec = t['timeSec']
        assert sec >= prev_sec, f"Topic {t['id']} timestamp {t['timestamp']} is not in ascending order"
        prev_sec = sec

    # 2. Check UI elements
    required_ids = [
        'ytPlayer',
        'protocolWarning',
        'theaterBtn',
        'themeBtn',
        'headerProgressText',
        'nowPlayingTitle',
        'prevTopicBtn',
        'nextTopicBtn',
        'locateTopicBtn',
        'insertTimestampBtn',
        'togglePreviewBtn',
        'exportNotesBtn',
        'copyNotesBtn',
        'clearNotesBtn',
        'notesInput',
        'notesPreviewMode',
        'notesWordCount',
        'overallProgressFill',
        'overallProgressPct',
        'overallProgressTopics',
        'overallProgressLabs',
        'topicSearch',
        'searchClearBtn',
        'filterLabsBtn',
        'filterMatchCount',
        'expandAllBtn',
        'collapseAllBtn',
        'resetProgressBtn',
        'domainListContainer',
        'toastContainer'
    ]

    for req_id in required_ids:
        assert f'id="{req_id}"' in html, f"Missing required element id='{req_id}'"

    # 3. Check JavaScript functions
    required_funcs = [
        'seekTo',
        'fallbackSeek',
        'renderCurriculum',
        'toggleTopicCompleted',
        'toggleDomainCompleted',
        'updateDomainStats',
        'updateOverallProgress',
        'setActiveTopic',
        'getNavigableTopics',
        'togglePlayPause',
        'toggleFullscreen',
        'renderMarkdown',
        'insertCurrentTimestamp',
        'togglePreview',
        'showToast'
    ]
    for fn in required_funcs:
        assert f'function {fn}' in html, f"Missing required JS function {fn}"

    # 4. Check CSS features
    assert 'data-theme="light"' in html, "Light theme CSS missing"
    assert 'body.theater-mode' in html, "Theater mode CSS missing"
    assert '.ts-chip' in html, "Timestamp chip CSS missing"
    assert '.lab-badge' in html, "Lab badge CSS missing"
    assert '.domain-checkbox' in html, "Domain-level checkbox CSS missing"

    # 5. Check YouTube API script & postMessage listener
    assert 'https://www.youtube.com/iframe_api' in html, "YouTube IFrame API script tag missing"
    assert 'infoDelivery' in html, "YouTube postMessage listener missing"

    # 6. Check keyboard shortcuts coverage
    shortcuts = ['Alt+T', 'toggleTheater', 'togglePlayPause', 'toggleFullscreen', 'seekTo']
    for sc in shortcuts:
        assert sc in html, f"Shortcut handler for '{sc}' missing in script"

    # 7. Deep Markdown Renderer Execution Test via Node.js
    node_test_script = """
    const fs = require('fs');
    const html = fs.readFileSync('index.html', 'utf8');

    // Extract renderMarkdown function
    const fnStart = html.indexOf('function renderMarkdown(');
    if (fnStart === -1) throw new Error('renderMarkdown not found');
    const fnEnd = html.indexOf('\\n    // Toggle Preview', fnStart);
    if (fnEnd === -1) throw new Error('renderMarkdown end not found');

    const fnCode = html.slice(fnStart, fnEnd);
    eval(fnCode);

    // Test cases
    const testNotes = `# CCDV-F Notes
- [01:11:47] — Agent SDK Follow Along
- 02:05:43 — Prompt caching

\`\`\`python
# Time 01:11:47 should NOT be replaced inside code block
const testTime = "01:11:47";
\`\`\`

Here is \`code 01:23\` inline.
Check [Exam Guide](https://www.exampro.co/ccdv-f).

1. First topic
2. Second topic

---
Quote:
> Sandboxing is critical.
`;

    const rendered = renderMarkdown(testNotes);

    // 1. Assert code block timestamp isolation
    if (rendered.includes('<pre><code>') && rendered.includes('<button class="ts-chip"')) {
        const start = rendered.indexOf('<pre><code>');
        const end = rendered.indexOf('</code></pre>');
        const codeBlock = rendered.substring(start, end);
        if (codeBlock.includes('ts-chip') || codeBlock.includes('<button')) {
            throw new Error('Code block contained injected timestamp button! Code isolation failed.');
        }
    } else {
        throw new Error('Expected pre/code blocks in rendered output');
    }

    // 2. Assert inline code isolation
    const inlineMatch = rendered.match(/<code>(.*?)<\\/code>/);
    if (!inlineMatch || inlineMatch[1].includes('<button')) {
        throw new Error('Inline code contained injected timestamp button!');
    }

    // 3. Assert deep-link timestamp chip creation
    if (!rendered.includes('data-sec="4307"') || !rendered.includes('▶ 01:11:47')) {
        throw new Error('Expected deep-link chip for 01:11:47 (4307 sec)');
    }
    if (!rendered.includes('data-sec="7543"') || !rendered.includes('▶ 02:05:43')) {
        throw new Error('Expected deep-link chip for 02:05:43 (7543 sec)');
    }

    // 4. Assert links rendered
    if (!rendered.includes('<a href="https://www.exampro.co/ccdv-f" target="_blank"')) {
        throw new Error('Expected markdown hyperlink to be rendered');
    }

    // 5. Assert horizontal rule
    if (!rendered.includes('<hr>')) {
        throw new Error('Expected horizontal rule <hr>');
    }

    // 6. Assert lists
    if (!rendered.includes('<ul>') || !rendered.includes('</ul>')) {
        throw new Error('Expected unordered list <ul>');
    }
    if (!rendered.includes('<ol>') || !rendered.includes('</ol>')) {
        throw new Error('Expected ordered list <ol>');
    }

    console.log('Node.js Deep Markdown Tests: ALL PASSED!');
    """

    res = subprocess.run(['node', '-e', node_test_script], capture_output=True, text=True)
    if res.returncode != 0:
        print("Node test stderr:", res.stderr)
        raise AssertionError(f"Node.js deep markdown verification failed: {res.stderr}")
    print(res.stdout.strip())

    print("ALL TESTS PASSED SUCCESSFULLY!")
    print(f"Verified: {len(domains)} Domains, {len(all_topics)} Topics, {len(labs)} Labs")

if __name__ == '__main__':
    test_portal()
