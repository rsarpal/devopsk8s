
#!/bin/bash

url=`curl -Ls -o /dev/null -w %{url_effective} https://en.wikipedia.org/wiki/Special:Random`

curl -v 'http://localhost:8081/graphql' \
  -X POST \
  -H 'Accept: application/json' \
  -H 'content-type: application/json' \
  --data-raw '{"query":"mutation {\n  addTodo(text: \"'${url}'\") {\n    todo {\n      text\n    }\n  }\n}\n","variables":null}' \
  --compressed