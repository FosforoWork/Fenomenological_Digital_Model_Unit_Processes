"""
Toy bi-objective problem: minimise SQUARED distances to two fixed points A, B.

    f1(x) = (x1 - A1)^2 + (x2 - A2)^2
    f2(x) = (x1 - B1)^2 + (x2 - B2)^2

Decision variable:  x = (x1, x2) in [-10, 15]^2
Reference points:   A = (0, 0),  B = (2, 2)

Why squared distance instead of Euclidean?
    The squared form gives a SMOOTH CONVEX FRONT in objective space (rather
    than a straight line) and a faster-decaying gradient far from the
    optima, which makes the parameters of NSGA-II actually matter at
    short generation counts. Students still get a closed-form answer.

Analytical Pareto-optimal set (decision space):
    The line segment from A to B,  i.e.  x = (2t, 2t) for t in [0,1].

Analytical Pareto front (objective space):
    With x = (2t, 2t):
        f1 = 8 t^2
        f2 = 8 (1 - t)^2
    Eliminating t:
        sqrt(f1) + sqrt(f2) = 2 * sqrt(2)
    i.e.  f2 = (2*sqrt(2) - sqrt(f1))^2,  f1 in [0, 8].
    This is a CONVEX curve passing through (0, 8) and (8, 0).

Useful diagnostics:
    - For ANY x in the box,  f1 + f2 = 2(x1-1)^2 + 2(x2-1)^2 + 4,
      so min(f1+f2) = 4 attained only at the segment midpoint x = (1,1).
      Therefore 'min(f1+f2)' is NOT a coverage metric. We use:
        * purity   = fraction of returned points actually on the front
        * coverage = range of f1 spanned, normalised to [0,1]
"""

import numpy as np
import matplotlib.pyplot as plt
from pymoo.core.problem import ElementwiseProblem


# --- Problem geometry ---------------------------------------------------------

A = np.array([0.0, 0.0])
B = np.array([2.0, 2.0])
XL = np.array([-10.0, -10.0])
XU = np.array([15.0, 15.0])

F_MAX = float(np.sum((B - A) ** 2))   # = 8.0, max value of f1 or f2 on the front


class TwoPointSquared(ElementwiseProblem):
    """Minimise (squared distance to A, squared distance to B)."""

    def __init__(self):
        super().__init__(n_var=2, n_obj=2, n_ieq_constr=0, xl=XL, xu=XU)

    def _evaluate(self, x, out, *args, **kwargs):
        f1 = (x[0] - A[0]) ** 2 + (x[1] - A[1]) ** 2
        f2 = (x[0] - B[0]) ** 2 + (x[1] - B[1]) ** 2
        out["F"] = [f1, f2]


# --- Analytical curves --------------------------------------------------------

def analytical_front(n=400):
    """(n,2) array of points on the true Pareto front in objective space."""
    t = np.linspace(0.0, 1.0, n)
    f1 = F_MAX * t ** 2
    f2 = F_MAX * (1.0 - t) ** 2
    return np.column_stack([f1, f2])


def analytical_set(n=400):
    """(n,2) array of points on the true Pareto-optimal set in decision space."""
    t = np.linspace(0.0, 1.0, n)
    return np.outer(1 - t, A) + np.outer(t, B)


# --- Quality metrics ----------------------------------------------------------

def purity(F, tol=1e-2):
    """Fraction of returned objective-space points that lie on the analytical
    front within tolerance.

    A point (f1, f2) is on the front iff sqrt(f1) + sqrt(f2) = 2*sqrt(2).
    """
    sf = np.sqrt(np.maximum(F, 0.0))
    residual = np.abs(sf[:, 0] + sf[:, 1] - 2.0 * np.sqrt(2.0))
    return float(np.mean(residual <= tol))


def coverage(F):
    """Range of f1 covered by the returned front, normalised to [0, 1].
    1.0 means the front spans from one extreme of the analytical front
    to the other."""
    return float((F[:, 0].max() - F[:, 0].min()) / F_MAX)


# --- Plotting helpers ---------------------------------------------------------

def _decorate_decision(ax):
    seg = analytical_set()
    ax.plot(seg[:, 0], seg[:, 1], "k--", lw=1, label="True Pareto set")
    ax.scatter(*A, c="black", marker="*", s=120, zorder=5, label="A=(0,0)")
    ax.scatter(*B, c="black", marker="P", s=120, zorder=5, label="B=(2,2)")
    ax.set_xlabel("x1"); ax.set_ylabel("x2")
    ax.set_title("Decision space")
    ax.set_xlim(XL[0] - 0.5, XU[0] + 0.5)
    ax.set_ylim(XL[1] - 0.5, XU[1] + 0.5)
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)


def _decorate_objective(ax):
    front = analytical_front()
    ax.plot(front[:, 0], front[:, 1], "k--", lw=1, label="True Pareto front")
    ax.set_xlabel("f1 = ||x - A||^2")
    ax.set_ylabel("f2 = ||x - B||^2")
    ax.set_title("Objective space")
    ax.set_xlim(-0.5, 9.0)
    ax.set_ylim(-0.5, 9.0)
    ax.grid(alpha=0.3)


def make_overlay_axes(title):
    """1x2 figure for overlaying multiple runs."""
    fig, (ax_dec, ax_obj) = plt.subplots(1, 2, figsize=(11, 5))
    fig.suptitle(title)
    _decorate_decision(ax_dec)
    _decorate_objective(ax_obj)
    return fig, ax_dec, ax_obj


def decorate_panel(ax_dec, ax_obj):
    """Decorate a pre-existing pair of axes (used by the multi-panel sweeps)."""
    _decorate_decision(ax_dec)
    _decorate_objective(ax_obj)
