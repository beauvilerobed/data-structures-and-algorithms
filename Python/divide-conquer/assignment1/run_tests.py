import sys
import pytest

if __name__ == '__main__':
  args = ['-v', '-vrxs']

  if len(sys.argv) > 1:
      args.extend(sys.argv[1:])

  sys.exit(pytest.main(args))