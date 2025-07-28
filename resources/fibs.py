from flask.views import MethodView
from flask_smorest import Blueprint, abort

def fibonacci(n: int) -> list[int]:
  """
  Return the first `n` Fibonacci numbers starting from 0.

  Args:
    n (int): The number of Fibonacci numbers to generate.

  Returns:
    list[int]: A list of the first `n` Fibonacci numbers.

  Raises:
    ValueError: If `n` is negative or greater than limit 20577.

  NOTE:
    The limit can be changed using sys.setrecursionlimit() and sys.set_int_max_str_digits() to higher values
    to avoid recursive stack crash and integer string conversion
  """

  a = 0
  b = 1

  fibs = []
  if n < 0:
    raise ValueError(f"n={n} is negative. Please use a positive number")
  elif n > 20577:
    raise ValueError(f"n={n} is too large. Please use a number smaller than 20578")
  elif n == 0:
    return [0]
  elif n == 1:
    return [0, 1]
  else:
    fibs = [0, 1]
    for i in range(2, n+1):
      c = a + b
      a = b
      b = c
      fibs.append(c)

  return fibs

blp = Blueprint("fibs", __name__, description="fibonacci operations")

@blp.route("/fibs/<int:seq_no>")
class Fibonacci(MethodView):
  def get(self, seq_no):
    try:
      seq = int(seq_no)
      fibs = fibonacci(seq)

      return str(fibs[seq])
    except (ValueError, IndexError) as e:
      abort(422, message=f"{type(e).__name__}: {e.args[0]}")
