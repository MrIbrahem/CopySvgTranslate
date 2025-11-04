import warnings
warnings.warn(
    "Package 'CopySVGTranslate' has been renamed to 'CopySVGTranslation'. "
    "Please install the new package: pip install CopySVGTranslation",
    DeprecationWarning,
)
from CopySVGTranslation import *  # re-export
