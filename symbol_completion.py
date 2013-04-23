import sublime, sublime_plugin
import re

word_pattern = re.compile('\w+')

class SymbolCompletion(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        completions = []
        # move current view to the start
        views = sublime.active_window().views()
        views.remove(view)
        views.insert(0, view)

        keys = set()
        for v in views:
            for symbol in v.symbols():
                key = word_pattern.search(symbol[1]).group()
                if not key in keys:
                    keys.add(key)
                    completions.append((key, key))

        return completions
