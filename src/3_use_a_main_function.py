#endregion
#region # USE A MAIN FUNCTION (WHY?)
# =============================================================================
# USE A MAIN FUNCTION (WHY?)
# =============================================================================
# otherwise the code will run when it is imported
# here is an example of that happening and being a pain in the butt
from src.utils.garbage import add_two_numbers
# it still works... 
# but it is a pain in the butt
add_two_numbers(1, 2)

from src.utils.garbage_with_main import add_two_numbers_2
# this works without all the extra stuff
add_two_numbers_2(1, 2)