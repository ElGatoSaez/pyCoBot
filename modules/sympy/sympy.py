# -*- coding: utf-8 -*-

import logging
try:
    from sympy.solvers import solve
    from sympy import Symbol
    from sympy.core import sympify
except ImportError:
    logging.error("m_algebra: Sympy no está instalado.")


class algebra:
    def __init__(self, core, client):
        try:
            solve
        except:
            return -1

        core.addCommandHandler("calcx", self, chelp="Resuelve X en una ecuación"
            ". Sintaxis: calcx <ecuación>")
        core.addCommandHandler("calcxy", self, chelp="Resuelve X e Y en una ecu"
            "ación. Sintaxis: calcxy <ecuación>")

    def calcx(self, bot, cli, ev):
        if len(ev.splitd) < 1:
            cli.notice("Error: Faltan parametros")

        expr = " ".join(ev.splitd)

        expr = expr.replace("=", "-")

        pr = sympify(expr)
        x = Symbol('x')
        res = solve(pr, x)
        cli.notice(ev.target, res)

    def calcxy(self, bot, cli, ev):
        if len(ev.splitd) < 1:
            cli.notice("Error: Faltan parametros")

        expr = " ".join(ev.splitd)

        expr = expr.replace("=", "-")

        pr = sympify(expr)
        x = Symbol('x')
        y = Symbol('y')
        res = solve(pr, x, y)
        cli.notice(ev.target, res)