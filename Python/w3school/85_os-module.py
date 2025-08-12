# os модуль используется для взаимодействия с операционной системой. Он предоставляет функции для работы с файловой системой, путями, переменными окружения, процессами и другими системными возможностями.
# модуль pathlib — более современный и объектно-ориентированный способ работы с путями.
import os

current_dir = os.getcwd()
print(f"current directory: {current_dir}")

# Show files in directory
entries = os.listdir(current_dir)
print("directory contents: ", entries)

# Delete a File
os.remove("demofile.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Rename file
os.rename("myfile.txt", "renamed_file.txt")

# Create folder
os.mkdir("any_name_dir")


# Delete Folder
# Note: You can only remove empty folders.
# To delete an entire folder, use the os.rmdir() method:
os.rmdir("any_name_dir")

# Объединение путей (кроссплатформенно)
full_path = os.path.join("/home/user", "docs", "file.txt")
print(f"Full path is: {full_path}")

# Получение информации (метаданных) о файле или директории
# Получение информации о файле "21-1_os-module.py"
file_info = os.stat("21-1_os-module.py")

# Печать полной информации о файле (включая время последнего изменения, доступа, права и т.д.)
print("All info: ", file_info)

# Вывод размера файла в байтах
print("File size: ", file_info.st_size, "bytes")

"""
OS Methods
os._exit()                     Exits the process with the specified status
os.abort()                     Terminates a running process immediately
os.access()                    Uses the real uid/gid to check access to a path
os.add_dll_directory()         Adds a path to the DLL search path
os.chdir()                     Change the current working directory
os.chflags()                   Sets the flags of path to the numeric flags
os.chmod()                     Changes the mode of path to the numeric mode
os.chown()                     Changes the owner and group id of a specified path to the specified numeric owner id and group id
os.chroot()                    Changes the root directory of the current process to a specified path
os.close()                     Closes the specified file descriptor
os.closerange()                Closes all file descriptors from fd_low to fd_high
os.confstr()                   Returns string-valued system configuration values
os.cpu_count()                 Returns the number of CPUs present in the system
os.ctermid()                   Returns the filename associated with the controlling terminal of the process
os.device_encoding()           Returns the encoding of the device associated with the file descriptor, if it is connected to a terminal
os.dup()                       Duplicates a file descriptor
os.dup2()                      Duplicates a file descriptor to a given value
os.fchdir()                    Changes the current working directory to a directory opened by os.open()
os.fchmod()                    Changes the mode of a file to the specified numeric mode
os.fchown()                    Changes the owner and group id of a file to the numeric uid and gid
os.fdatasync()                 Forces write of file to disc - not forces update of metadata
os.fdopen()                    Returns an open file object connected to a file
os.fork()                      Forks a child process
os.forkpty()                   Forks a child process, using a new pseudo-terminal as the child's controlling terminal
os.fpathconf()                 Returns system configuration information relevant to an open file
os.fsdecode()                  Decodes a file path
os.fsencode()                  Encodes a file path
os.fspath()                    Returns the file system representation of a path
os.fstat()                     Returns the status of a file
os.fstatvfs()                  Returns information about the file system of a file
os.fsync()                     Forces write of file with file descriptor fd to disk
os.ftruncate()                 Truncates a file to a specified length
os.fwalk()                     
os.get_blocking()              Returns the blocking mode information of the file descriptor
os.get_exec_path()             Returns a list of directories, in which the system looks for named executable programs
os.get_handle_inheritable()                   
os.get_inheritable()           Returns the inheritable flag of the file descriptor
os.get_terminal_size()         Returns the size of a terminal as a pair of columns and lines
os.getcwd()                    Returns the current working directory
os.getcwdb()                   Returns the current working directory in bytestring
os.getegid()                   Return the effective group id of the current process
os.getenv()                    Returns the value of the environment variable key
os.getenvb()                   Returns the value of the environment variable key, in bytes
os.geteuid()                   Returns the effective user id of the current process
os.getgid()                    Returns the real group id of the current process
os.getgrouplist()              Returns a list of all group ids for a specified user
os.getgroups()                 Returns a list of supplementary group ids associated with the current process
os.getloadavg()                Returns the load average over the last 1, 5, and 15 minutes
os.getlogin()                  Returns the name of the user logged in to the terminal
os.getpgid()                   Returns the process group id of a specific process id
os.getpgrp()                   Returns the current process group id
os.getpid()                    Returns the process id of the current process
os.getppid()                   Returns the parent process id of the current process
os.getpriority()               Returns the scheduling priority of a process, process group, or user
os.getresgid()                 Returns the current process' real, effective, and saved group ids
os.getresuid()                 Returns the current process' real, effective, and saved user ids
os.getsid()                    Returns the session id of a process
os.getuid()                    Returns the current process' real user id
os.initgroups()                Initializes a group access list showing all the member groups of a user plus the group id
os.isatty()                    Returns whether a file descriptor is open and connected to a tty(-like) device or not.
os.kill()                      Sends a signal to the process with the specified process id
os.killpg()                    Sends a signal to the process with the specified process id
os.lchflags()                  Changes the flags of a path to the numeric flags
os.lchmod()                    Changes the mode of path to the numeric mode
os.lchown()                    Changes the owner and group id of path to the numeric uid and gid
os.link()                      Creates a hard link pointing to source named destination
os.listdir()                   Returns a list of the names of the entries in a directory
os.lockf()                     Applies, tests, or removes a POSIX lock on an open file
os.lseek()                     Sets the current position of file descriptor to the defined position
os.lstat()                     Returns the status of a file or file descriptor, but does not follow symbolic links
os.major()                     Returns the device major number from raw device number
os.makedev()                   Returns a raw device number from the specified major and minor device numbers
os.makedirs()                  Creates a directory recursively
os.memfd_create()              Create an anonymous file and returns a file descriptor
os.minor()                     Returns the device minor number from raw device number
os.mkdir()                     Creates a directory (with a specified mode)
os.mkfifo()                    Creates a FIFO named path (with a specified mode)
os.mknod()                      
os.nice()                      
os.open()                      
os.openpty()                      
os.pathconf()                      
os.pipe()                      
os.pipe2()                      
os.plock()                      
os.popen()                      
os.posix_fadvise()                      
os.posix_fallocate()                      
os.posix_spawn()                      
os.posix_spawnp()                      
os.pread()                      
os.preadv()                      
os.putenv()                      
os.pwrite()                      
os.pwritev()                      
os.read()                      
os.readlink()                      
os.readv()                      
os.register_at_fork()                      
os.remove()                      
os.removedirs()                      
os.removexattr()                      
os.rename()                      
os.renames()                      
os.replace()                      
os.rmdir()                      
os.scandir()                      
os.sched_get_priority_max()                      
os.sched_get_priority_min()                      
os.sched_getaffinity()                      
os.sched_getparam()                      
os.sched_getscheduler()                      
os.sched_rr_get_interval()                      
os.sched_setaffinity()                      
os.sched_setparam()                      
os.sched_setscheduler()                      
os.sched_yield()                      
os.sendfile()                      
os.set_blocking()                      
os.set_handle_inheritable()                      
os.set_inheritable()                      
os.setegid()                      
os.seteuid()                      
os.setgid()                      
os.setgroups()                      
os.setpgid()                      
os.setpriority()                      
os.setregid()                      
os.setresgid()                      
os.setresuid()                      
os.setreuid()                      
os.setsid()                      
os.setuid()                      
os.setxattr()                      
os.spawnl()                      
os.spawnle()                      
os.spawnlp()                      
os.spawnlpe()                      
os.spawnv()                      
os.spawnve()                      
os.spawnvp()                      
os.spawnvpe()                      
os.startfile()                      
os.stat()                      
os.statvfs()                      
os.strerror()                      
os.symlink()                      
os.sync()                      
os.sysconf()                      
os.system()                      
os.tcgetpgrp()                      
os.tcsetpgrp()                      
os.times()                      
os.truncate()                      
os.ttyname()                      
os.umask()                      
os.uname()                      
os.unlink()                      
os.unsetenv()                      
os.urandom()                      
os.utime()                      
os.wait()                      
os.wait3()                      
os.wait4()                      
os.waitid()                      
os.waitpid()                      
os.walk()                      
os.write()                      
os.writev()                      
"""
"""
OS Objects
os.altsep                      
os.confstr_names            Returns a dictionary of the names and integer values that is accepted as parameter for the os.confstr() method
os.curdir                      
os.defpath                      
os.devnull                      
os.environ                      
os.environb                      
os.extsep                      
os.linesep                      
os.name                     Find the name of the current OS
os.pardir                      
os.pathconf_names                      
os.pathsep                      
os.sep                      
os.supports_bytes_environ                      
os.supports_dir_fd                      
os.supports_effective_ids                      
os.supports_fd                      
os.supports_follow_symlinks                      
os.sysconf_names                      
"""

"""
OS Constants
os.CLD_CONTINUED                      
os.CLD_DUMPED                      
os.CLD_EXITED                      
os.CLD_TRAPPED                      
os.EX_CANTCREAT           Exit code that indicates: User specified output file could not be created
os.EX_CONFIG              Exit code that indicates: Some kind of configuration error occurred
os.EX_DATAERR             Exit code that indicates: Input data was incorrect
os.EX_IOERR               Exit code that indicates: An error occurred while doing input/output on some file
os.EX_NOHOST              Exit code that indicates: The host did not exist
os.EX_NOINPUT             Exit code that indicates: The input file did not exist or was not readable
os.EX_NOPERM              Exit code that indicates: Insufficient permissions to perform the operation
os.EX_NOTFOUND            Exit code that indicates: Entry not found
os.EX_NOUSER              Exit code that indicates: The user does not exists
os.EX_OK                  Exit code that indicates: No error occurred
os.EX_OSERR               Exit code that indicates: An operating system error was detected
os.EX_OSFILE              Exit code that indicates: Error in a system file
os.EX_PROTOCOL            Exit code that indicates: Protocol exchange was illegal, invalid, or not understood
os.EX_SOFTWARE            Exit code that indicates: An internal software produced an error
os.EX_TEMPFAIL            Exit code that indicates: A temporary failure occurred
os.EX_UNAVAILABLE         Exit code that indicates: A required service is unavailable
os.EX_USAGE               Exit code that indicates: The command was used incorrectly
os.F_LOCK                   
os.F_OK                   Tests the existence of the path
os.F_TEST                      
os.F_TLOCK                      
os.F_ULOCK                      
os.GRND_NONBLOCK                      
os.GRND_RANDOM                      
os.MFD_ALLOW_SEALING                      
os.MFD_CLOEXEC                      
os.MFD_HUGETLB                      
os.MFD_HUGE_16GB                      
os.MFD_HUGE_16MB                      
os.MFD_HUGE_1GB                      
os.MFD_HUGE_1MB                      
os.MFD_HUGE_256MB                      
os.MFD_HUGE_2GB                      
os.MFD_HUGE_2MB                      
os.MFD_HUGE_32MB                      
os.MFD_HUGE_512KB                      
os.MFD_HUGE_512MB                      
os.MFD_HUGE_64KB                      
os.MFD_HUGE_8MB                      
os.MFD_HUGE_MASK                      
os.MFD_HUGE_SHIFT                      
os.O_APPEND                      
os.O_ASYNC                      
os.O_BINARY                      
os.O_CLOEXEC                      
os.O_CREAT                      
os.O_DIRECT                      
os.O_DIRECTORY                      
os.O_DSYNC                      
os.O_EXCL                      
os.O_EXLOCK                      
os.O_NDELAY                      
os.O_NOATIME                      
os.O_NOCTTY                      
os.O_NOFOLLOW                      
os.O_NOINHERIT                      
os.O_NONBLOCK                      
os.O_PATH                      
os.O_RANDOM                      
os.O_RDONLY                      
os.O_RDWR                      
os.O_RSYNC                      
os.O_SEQUENTIAL                      
os.O_SHLOCK                      
os.O_SHORT_LIVED                      
os.O_SYNC                      
os.O_TEMPORARY                      
os.O_TEXT                      
os.O_TMPFILE                      
os.O_TRUNC                      
os.O_WRONLY                      
os.POSIX_FADV_DONTNEED                      
os.POSIX_FADV_NOREUSE                      
os.POSIX_FADV_NORMAL                      
os.POSIX_FADV_RANDOM                      
os.POSIX_FADV_SEQUENTIAL                      
os.POSIX_FADV_WILLNEED                      
os.PRIO_PGRP                      
os.PRIO_PROCESS                      
os.PRIO_USER                      
os.P_ALL                      
os.P_DETACH                      
os.P_NOWAIT                      
os.P_NOWAITO                      
os.P_OVERLAY                      
os.P_PGID                      
os.P_PID                      
os.P_WAIT                      
os.RTLD_DEEPBIND                      
os.RTLD_GLOBAL                      
os.RTLD_LAZY                      
os.RTLD_LOCAL                      
os.RTLD_NODELETE                      
os.RTLD_NOLOAD                      
os.RTLD_NOW                      
os.RWF_DSYNC                      
os.RWF_HIPRI                      
os.RWF_NOWAIT                      
os.RWF_SYNC                      
os.R_OK                   Tests the readability of the path
os.SCHED_BATCH                      
os.SCHED_FIFO                      
os.SCHED_IDLE                      
os.SCHED_OTHER                      
os.SCHED_RESET_ON_FORK                      
os.SCHED_RR                      
os.SCHED_SPORADIC                      
os.SEEK_CUR                      
os.SEEK_END                      
os.SEEK_SET                      
os.SF_MNOWAIT                      
os.SF_NODISKIO                      
os.SF_SYNC                      
os.WCONTINUED                      
os.WCOREDUMP(status)                      
os.WEXITED                      
os.WEXITSTATUS(status)                      
os.WIFCONTINUED(status)                      
os.WIFEXITED(status)                      
os.WIFSIGNALED(status)                      
os.WIFSTOPPED(status)                      
os.WNOHANG                      
os.WNOWAIT                      
os.WSTOPPED                      
os.WSTOPSIG(status)                      
os.WTERMSIG(status)                      
os.WUNTRACED                      
os.W_OK                   Tests the writability of the path
os.XATTR_CREATE                      
os.XATTR_REPLACE                      
os.XATTR_SIZE_MAX                      
os.X_OK                   Tests the executability of the path
"""

"""
OS Classes
class os.DirEntry                      
class os.PathLike                      
class os.sched_param(sched_priority)                      
class os.stat_result                      
class os.terminal_size                      
"""
