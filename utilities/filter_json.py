import json


class ParseData:
    def __init__(self, response):
        self.response = response

    def get_data(self):
        data = None
        try:
            data = json.loads(self.response)
        except Exception as e:
            print(e)

        if data:
            cs = data.get("commit_status")

            useful_data = {
                "repository_link": data.get("repository").get("links").get("html").get("href"),
                "commit_full_name": cs.get("repository").get("full_name"),
                "commit_type": cs.get("type"),
                "commit_branch": cs.get("refname"),
                "commit_state": cs.get("state"),
                "commit_hash": cs.get("commit").get("hash"),
                "commit_updated_date": cs.get("updated_on"),
                "commit_name": cs.get("name"),
                "commit_url": cs.get("url")
            }

            return useful_data
        else:
            raise Exception("Data cannot be loaded")
