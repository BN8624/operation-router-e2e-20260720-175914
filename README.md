# Operation Router Controlled E2E
This public repository exists only to validate the Operation Router execution path.
The test must:
1. Modify one documentation line.
2. Commit directly to `main`.
3. Push to `origin/main`.
4. Trigger GitHub Actions.
5. Leave the test issue open.
6. Create no branch or pull request.
No credentials, personal data, private logs, or environment details belong in this repository.

## Usage

```bash
python src/slugcli.py Hello World
# hello-world

python src/slugcli.py --max-length 8 Hello World
# hello-wo

python src/slugcli.py --json Hello World
# {"slug": "hello-world"}
```
