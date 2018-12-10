from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):

    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        src = os.path.abspath(self._task.args.get('src', None))
        with open(src) as f:
            template_data = f.read()
        result['text/html'] = self._templar.do_template(template_data,
                                                        preserve_trailing_newlines=True,
                                                        escape_backslashes=False)
        return result
