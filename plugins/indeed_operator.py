from typing import Any, Optional

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import requests
from bs4 import BeautifulSoup

base_url = "https://indeed.com"

class IndeedOperator(BaseOperator):
    """
    """

    template_fields = ('sql',)
    template_ext = ('.sql',)
    ui_color = '#4682B4'


    @apply_defaults
    def __init__(
        self,
        *,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
    
    def placeholder(self):
        city = 'remote'
        


    

    def execute(self, context: Any) -> None:
        hook = self.get_hook()
        hook.run(self.sql, autocommit=self.autocommit, parameters=self.parameters)