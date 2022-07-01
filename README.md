# tgBioRotator

```shell
cp .env.example .env
vim .env
# update api id and api hash
docker-compose up -d
docker-compose exec worker python tg/authorize.py
docker-compose exec worker python
```
```python
from utils import add_phrase
add_phrase("Backend dev 25y.o")
# ...
add_phrase("I'm a teapod")
exit()
```
