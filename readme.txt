originally https://github.com/Kosat/telegram-messages-dump

---

Usage:

Normal mode:
  telegram-messages-dump -c <chat_name> -p <phone_num> [-l <count>] [-o <file>] [-cl] [...]
  telegram-messages-dump --chat=<chat_name> --phone=<phone_num> [--limit=<count>] [--out <file>]

Continuous mode:
  telegram-messages-dump --continue -p <phone_num> -o <file> [-cl] [...]
  telegram-messages-dump --continue=<MSG_ID> -p <phone_num> -o <file> -e <exporter> -c <chat_name>
