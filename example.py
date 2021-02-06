#!/usr/bin/env python3
import apps

project = apps.Project(
    APPS=['starlette_cli']
)

if __name__ == '__main__':
    project.apps['cli'].entry_point()
else:
    app = project.starlette()
