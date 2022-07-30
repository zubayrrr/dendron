
- Contain a series of spinning rigid metal platters, one on top of the other, very close but not touching.
- Read and write heads must move over spinning platters to read and write.
- Uses power to driver motors which results in noise and heat.
- They're magnetic drives
- Internal interface - [[devlog.PATA]], [[SATA]], [[devlog.SCSI]]
- External interface - [[USB]], eSATA, [[devlog.SCSI]], SAS

### Magnetic Drive Characteristics

- Rotational Speed - 5,400 RPM, 7,200 RPM, 10,000 RPM, 15,000 RPM (faster is better).
- Pysical Sizes - 2.5", 3.5" - Eg: SATA 2.5, SATA 3.5

### HDD Security

#### HDD Password

- Password must be entered on boot up
- Password is stored with the disk firmware

#### Trusted platform module

- TPM
- Stored disk encryption keys
- Verifies machine startup integrity

#### LoJack

- Tracking mechanism for stolen laptops
- Can be enabled from BIOS/UEFI - sometimes also stored on HDD (in form of software)
