import re


def parse_result_website(raw):
    if not raw.startswith('<!DOCTYPE html>'):
        return 'ERROR: No HTML Received'
    re_main = re.compile(r'(?s)<main>\n<article><p>(.*)</p></article>\n</main>')
    main_part = re_main.search(raw)

    if not main_part:
        return 'ERROR: No main part in website'

    main_text = main_part.group(1)

    if main_text.startswith("That's the right answer"):
        return 'SUCCESS - Answer accepted'

    if main_text.startswith('You gave an answer too recently'):
        time = re.search(r'(?:(\d+)m )?(?:(\d+)s)', main_text)
        minutes, seconds = time.groups()
        return f'ERROR: Cooldown {minutes if minutes else 0}m {seconds}s'

    if main_text.startswith("That's not the right answer"):
        reason = re.search(r'your answer is too (\w*)', main_text)
        return 'WRONG ANSWER:' + (f' - Too {reason.group(1)}' if reason else '')

    if main_text.startswith("You don't seem to be solving the right level"):
        return 'ALREADY SOLVED'

    return None


def parse_solution_from_website(raw, part):
    if not raw.startswith('<!DOCTYPE html>'):
        print('No HTML Received')
        return None
    re_answer = re.compile(r'<p>Your puzzle answer was <code>(.*)</code>.</p>')
    answers = re_answer.findall(raw)
    if len(answers) < part:
        print('Unable to find solution for part', part, 'on Website')
        return None
    return answers[part-1]


def parse_example_from_website(raw):
    if not raw.startswith('<!DOCTYPE html>'):
        print('No HTML Received')
        return None
    re_example = re.compile(r'[eE]xample:</p>\n<pre><code>(.*?)</code></pre>', re.DOTALL)
    example = re_example.findall(raw)
    if len(example) > 1:
        print('ERROR: Multiple Examples found')
        return False
    return example[0]
