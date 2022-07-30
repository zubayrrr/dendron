
- Areas: [[devlog.linux]]

---

- Stores passwords on behalf of `/etc/passwd` in an encrypted format
- Hash of the password and other attributes such as a password's expiration date
- It is only readable by the root account
- Contains 9 comma separated fields

<!-- end list -->

1.  Username - it is how the corresponding line is connected to `/etc/passwd`
2.  The password, the entire string between the colons

<!-- end list -->

- The other seven fields related to password expiration, last password change, minimum maximum password age, so on.
- If the password field contains an `*` or `!`, it means the user cannot login using the password, other login methods, like key based authentication or switching users is still allowed.
- Password format is set to `$type$salt$hash`
  - $type:
    - `1` [[MD5]]
    - `2a` [[Blowfish]]
    - `2y` [[Eksblowfish]]
    - `5` [[SHA256]]
    - `6` [[SHA512]]
  - $salt: A salt combined with the password is added to the hashing process to enforce the uniqueness of hash generated. $salt is random but not secret. It helps mitigate attacks such as [[Rainbow table]]s.
- Never edit the shadow file manually, use a command line tool designed for doing so.

Check [[Man Pages]] `man shadow`
