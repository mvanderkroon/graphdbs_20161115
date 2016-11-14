docker run \
--publish=7575:7474 \
--publish=7688:7687 \
--volume=/datadrive/neo4j_tut/data:/data \
--ulimit=nofile=40000:40000 \
--env=NEO4J_dbms_memory_pagecache_size=4G \
--env=NEO4J_dbms_memory_heap_maxSize=4000 \
--volume=/datadrive/neo4j_tut/logs:/logs neo4j:3.0

docker run \
--publish=7474:7474 \
--publish=7687:7687 \
--volume=/datadrive/neo4j/data:/data \
--ulimit=nofile=40000:40000 \
--env=NEO4J_dbms_memory_pagecache_size=4G \
--env=NEO4J_dbms_memory_heap_maxSize=4000 \
--volume=/datadrive/neo4j/logs:/logs neo4j:3.0

# user:neo4j
# password:password
