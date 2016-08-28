from coalib.bearlib.abstractions.Linter import linter
from coalib.results.RESULT_SEVERITY import RESULT_SEVERITY


@linter(executable='infer',
        output_format='regex',
        output_regex=(r'(.+):(?P<line>.+): '
                      r'(?P<severity>error|warning): (?P<message>.*)'),
        severity_map={'error': RESULT_SEVERITY.MAJOR,
                      'warning': RESULT_SEVERITY.NORMAL})
class InferBear:
    LANGUAGES = {"Java"}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    ASCIINEMA_URL = 'https://asciinema.org/a/1g2k0la7xo5az9t8f1v5zy66q'
    CAN_DETECT = {'Security'}

    @staticmethod
    def create_arguments(filename, file, config_file):
        return ('-npd',  '--', 'javac', filename)
