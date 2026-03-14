import sys
from apps.worker.repo_indexer import index_repo

if __name__ == "__main__":
    repo = sys.argv[1]
    index_repo(repo)