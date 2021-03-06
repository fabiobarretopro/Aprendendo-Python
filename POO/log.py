class LogMixin:
    @staticmethod
    def write(msg):
        with open("log.log.txt", "a+") as file:
            file.write(msg)
            file.write("\n")

    def log_info(self, msg):
        self.write(f"INFO: {msg}")

    def log_erro(self, msg):
        self.write(f"ERRO: {msg}")
