from typing import Optional, Type

import visafx
from langchain.tools import BaseTool
from pydantic import BaseModel, Field


class VISAFXRateInput(BaseModel):
    amount: float = Field(description='The amount to convert.')
    from_curr: str = Field(description='The currency to convert from.')
    to_curr: str = Field(description='The currency to convert to.')


class VISAFXRate(BaseTool):

    name = "visa_fx_rate"
    description = ('A Visa FX rate tool.'
                   'Input should be an amount, a currency to convert from, and a currency to convert to. '
                   'The output will be the converted amount and the FX rate.')

    args_schema: Optional[Type[BaseModel]] = VISAFXRateInput

    def _run(self, amount: str, from_curr: str, to_curr: str) -> str:
        # the from_curr and to_curr are reversed in the API
        r = visafx.rates(amount, from_curr=to_curr, to_curr=from_curr)
        return (f'Amount: {amount}\n'
                f'From: {from_curr}\n'
                f'To: {to_curr}\n'
                f'Converted Amount: {r.convertedAmount}\n'
                f'FX Rate: {r.fxRateWithAdditionalFee}\n')

    async def _arun(self, url: str) -> str:
        raise NotImplementedError("This tool does not support async")
