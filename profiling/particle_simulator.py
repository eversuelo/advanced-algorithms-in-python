"""A particle simulator used to demonstrate profiling in Python.

Each particle has a position (x, y) measured from the origin (0, 0) and an
angular speed `ang_vel` (the rotation direction is encoded by its sign:
positive = counter-clockwise, negative = clockwise).

The particles rotate around the origin. At any instant the linear velocity
(vx, vy) is perpendicular to the position vector (x, y) and its magnitude is
proportional to the distance from the center, so points farther out move faster
-- exactly like points painted on a spinning disk.

        y
        ^
        |        (x, y)  position vector
        |       /
        |      /  . ----> (vx, vy)  velocity, perpendicular to position
        |     /  .
        |    / .
        +---/-------------> x
       (0,0) origin
"""

import sys
from random import uniform
from timeit import timeit


class Particle:
    """A single particle, defined by its position and angular velocity."""

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel  # sign sets the rotation direction


class ParticleSimulator:
    """Advances a collection of particles through time."""

    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        """Evolve the system by a total time `dt`.

        We integrate the motion in small Euler steps. The direction of motion is
        always perpendicular to the line joining the particle and the center. We
        take the *unit* tangent vector and step along it by an amount
        proportional to the angular velocity, so every particle keeps a constant
        linear speed and conserves its distance to the origin.

        This inner loop is the hot path -- profile this method. Note the square
        root in step 1: it is the kind of per-iteration cost a profiler exposes.
        """
        timestep = 0.00001
        nsteps = int(dt / timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 1. calculate the direction (unit tangent vector)
                norm = (p.x ** 2 + p.y ** 2) ** 0.5
                v_x = -p.y / norm
                v_y = p.x / norm

                # 2. calculate the displacement
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 3. repeat for all the time steps


def visualize(simulator):
    """Plot the particle trajectories (optional, needs matplotlib)."""
    import matplotlib.pyplot as plt
    from matplotlib import animation

    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect="equal")
    (line,) = ax.plot(X, Y, "ro")

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(i):
        simulator.evolve(0.01)
        x = [p.x for p in simulator.particles]
        y = [p.y for p in simulator.particles]
        line.set_data(x, y)
        return (line,)

    anim = animation.FuncAnimation(
        fig, animate, init_func=init, blit=True, interval=10
    )
    plt.show()
    return anim


def test_visualize():
    """A handful of particles, easy to verify by eye when plotted."""
    particles = [
        Particle(0.3, 0.5, +1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, +3),
    ]
    simulator = ParticleSimulator(particles)
    visualize(simulator)


def test_evolve():
    """Unit test: verify evolve() against known-good reference coordinates.

    These numbers were produced by a correct run of the simulation. They check
    the *intended logic* regardless of implementation details, so we can rewrite
    evolve() during optimization and still trust the result if this test passes.
    """
    particles = [
        Particle(0.3, 0.5, +1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, +3),
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)
    p0, p1, p2 = particles

    def fequal(a, b, eps=1e-5):
        return abs(a - b) < eps

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)
    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)
    assert fequal(p2.x, 0.191358)
    assert fequal(p2.y, -0.365227)
    print("test_evolve: OK (matches reference coordinates)")


def benchmark():
    """Build a random 1000-particle system and evolve it -- what we profile."""
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0))
        for i in range(1000)
    ]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)


if __name__ == "__main__":
    # Run "python particle_simulator.py --visualize" to SEE the particles move.
    if "--visualize" in sys.argv or "-v" in sys.argv:
        test_visualize()
        sys.exit()

    # 1. Make it run / make it right: confirm the simulation is correct.
    test_evolve()

    # 2. Make it fast: measure before optimizing.
    elapsed = timeit("benchmark()", setup="from __main__ import benchmark", number=1)
    print(f"benchmark(): {elapsed:.3f}s for 1000 particles")
    print()
    print("Tip: run  python particle_simulator.py --visualize  to watch the animation.")
    print("Profile it with:  python -m cProfile -s tottime particle_simulator.py")
