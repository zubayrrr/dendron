
- Areas: [[devlog.linux]]

---

To recursively set permissions for all files to a specific value, you should exclude the directories in the path otherwise the directories will have same permissions as the files, see: [[devlog.The Effect of Permissions on Directories]]

To mitigate this, we can combine [[devlog.find]] and [[devlog.chmod]] commands together

Example

- `find ~ -type f -exec chmod 640 {} \;` for all files
- `find ~ -type d -exec chmod 750 {} \;` for all directories
