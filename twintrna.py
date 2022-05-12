import twint
import nest_asyncio

nest_asyncio.apply()

c = twint.Config()

c.Search = ' '

c.Since = '2013-01-01'
c.Until = '2014-12-31'

c.Hide_output = True

c.Store_json = True
c.Output = ''

twint.run.Search(c)

