import setuptools

__version__ = '0.0.0.0'

REPO_NAME = "customer_churn_prediction"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "churn-prediction"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"

setuptools.setup(
      name="churn-prediction",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End ML Learning implementation for customer churn prediction",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=setuptools.find_packages(where='src')
)