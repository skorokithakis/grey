import sys

import black
import delegator

PEP8_LINE_LENGTH_NOT = 120


def get_black_executable():
    """Returns executable information about Black."""
    return (sys.executable, black.__file__.rstrip('cdo'))


def main():
    """Runs White."""
    python, black = get_black_executable()
    # Prepare the additional command-line arguments.
    args = ' '.join(sys.argv[1:])
    # Spawn a subprocess.
    c = delegator.run(
        f"{python} {black} {args} --line-length {PEP8_LINE_LENGTH_NOT}"
    )
    # Print output.
    print(c.out)
    print(c.err)
    # Exit the status code.
    sys.exit(c.return_code)


if __name__ == '__main__':
    main()
