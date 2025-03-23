<p align="center">
  <H1 align="center">OverPC - 3.0.0</H1>
  <p align="center">OverPC</p>
  <p align="center">电脑终结者</p>
</p>

![GitHub Followers](https://img.shields.io/badge/dynamic/json?color=green&label=GitHub%20Followers&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dgithub%26queryKey%3DGVSADS)
![Total Repos](https://img.shields.io/badge/dynamic/json?color=orange&label=Total%20Repos&query=%24.total_count&url=https%3A%2F%2Fapi.github.com%2Fsearch%2Frepositories%3Fq%3Duser%3AGVSADS)
![GitHub Stars](https://img.shields.io/github/stars/GVSADS/OverPC?style=flat&label=Github%20Stars)
---
# "OverPC" and "Termination" Virus Sample Repository (病毒样本仓库)

## **Disclaimer (免责声明)**

### **English Version**

**WARNING: This repository contains potentially harmful code. Do not download, clone, or use this code unless you fully understand the risks and have taken appropriate precautions.**

This repository is intended for educational, research, or security analysis purposes only. The code provided here is a sample of malicious software (virus) and should only be used in a controlled, isolated environment. By accessing or using this repository, you acknowledge and accept the following terms:

1. **No Warranty**: The code is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the code or the use or other dealings in the code.

2. **Use at Your Own Risk**: You are solely responsible for any consequences that may arise from the use of this code. The authors of this repository do not assume any responsibility for any damage, loss, or harm caused by the use of this code, including but not limited to data loss, system corruption, or legal consequences.

3. **Isolation and Safety**: If you choose to use this code, you must do so in a secure, isolated environment, such as a virtual machine or sandbox, that is completely disconnected from any production systems or networks. Do not run this code on any system that you are not willing to risk losing access to or damaging.

4. **Legal Compliance**: You are responsible for ensuring that your use of this code complies with all applicable laws and regulations in your jurisdiction. The authors of this repository do not condone or support the use of this code for any illegal or malicious purposes.

5. **Educational Use Only**: This repository is intended solely for educational or research purposes. It is not intended to be used in any production environment or for any commercial purposes.

6. **No Support**: The authors of this repository do not provide any support, assistance, or guidance for the use of this code. If you choose to use this code, you do so entirely at your own discretion and risk.

7. **License**: This code is provided under the MIT License. However, the license does not grant you the right to use this code for any illegal or malicious purposes. You are solely responsible for ensuring that your use of this code complies with all applicable laws and regulations.

By accessing or using this repository, you agree to these terms and acknowledge that you understand the risks associated with the use of this code.

### **中文版本**

**警告：此仓库包含潜在的有害代码。除非您完全了解风险并采取了适当的预防措施，否则请勿下载、克隆或使用此代码。**

本仓库仅用于教育、研究或安全分析目的。此处提供的代码是恶意软件（病毒）的样本，只能在受控的隔离环境中使用。通过访问或使用此仓库，您承认并接受以下条款：

1. **无担保**：代码按“原样”提供，不提供任何形式的明示或暗示的担保，包括但不限于适销性、特定用途适用性和非侵权的担保。作者或版权持有者在任何情况下均不对任何索赔、损害或其他责任负责，无论是在合同、侵权或其他行为中产生的，与代码或代码的使用或其他交易有关。

2. **风险自负**：您对因使用此代码而可能产生的任何后果负全部责任。本仓库的作者不承担因使用此代码而导致的任何损害、损失或伤害的责任，包括但不限于数据丢失、系统损坏或法律后果。

3. **隔离与安全**：如果您选择使用此代码，您必须在安全、隔离的环境中执行，例如虚拟机或沙箱，且完全断开与任何生产系统或网络的连接。请勿在您不愿意失去访问权限或损坏的任何系统上运行此代码。

4. **法律合规**：您有责任确保您使用此代码的行为符合您所在司法管辖区的所有适用法律和法规。本仓库的作者不认可或支持将此代码用于任何非法或恶意目的。

5. **仅限教育用途**：本仓库仅用于教育或研究目的。不得在任何生产环境中或用于任何商业用途。

6. **无支持**：本仓库的作者不提供任何使用此代码的支持、帮助或指导。如果您选择使用此代码，您将完全自行决定并承担风险；项目已经完全停止维护，作者不对项目任何后果负责。

7. **许可证**：本代码根据MIT许可证提供。但是，该许可证并未授予您将此代码用于任何非法或恶意目的的权利。您有责任确保您使用此代码的行为符合所有适用的法律和法规。

通过访问或使用此仓库，您同意这些条款，并承认您了解与此代码使用相关的风险。

---

## **Introduction (介绍)**

### **English Version**

This repository contains a sample of malicious software (virus) that is intended for educational or research purposes only. The code is provided to help individuals understand how viruses work, how they can be analyzed, and how to protect against them. It is not intended to be used for any malicious or illegal purposes.

The code in this repository is designed to demonstrate various techniques used by malicious software, including but not limited to:

- **Self-replication**: The ability of the virus to copy itself to other files or systems.
- **Payload Execution**: The ability of the virus to execute malicious actions, such as deleting files, modifying system settings, or stealing data.
- **Persistence**: The ability of the virus to remain active on a system even after a reboot or other attempts to remove it.
- **Evasion Techniques**: The ability of the virus to evade detection by antivirus software or other security measures.

This code is provided as a learning tool for those who are interested in studying the behavior of malicious software. It is not intended to be used in any production environment or for any commercial purposes.

### **中文版本**

本仓库包含一个恶意软件（病毒）样本，仅用于教育或研究目的。提供此代码的目的是帮助个人了解病毒的工作原理、如何分析病毒以及如何防范病毒。本代码不应用于任何恶意或非法目的。

本仓库中的代码旨在展示恶意软件使用的各种技术，包括但不限于：

- **自我复制**：病毒将自身复制到其他文件或系统的能力。
- **有效负载执行**：病毒执行恶意操作的能力，例如删除文件、修改系统设置或窃取数据。
- **持久性**：病毒在系统重新启动或其他尝试删除它的操作后仍保持活动的能力。
- **规避技术**：病毒逃避防病毒软件或其他安全措施检测的能力。

本代码作为学习工具提供给那些对研究恶意软件行为感兴趣的人。它不应用于任何生产环境或任何商业目的。

---

## **Usage Instructions (使用说明)**

### **English Version**

If you choose to use this code, please follow these instructions carefully to minimize the risk of harm:

1. **Isolation**: Always run the code in a secure, isolated environment, such as a virtual machine (VM) or sandbox. Ensure that the environment is completely disconnected from any production systems or networks.

2. **Backup**: Before running the code, make sure to back up any important data or systems that you do not want to risk losing.

3. **Monitoring**: Monitor the environment closely while the code is running. Be prepared to shut down the environment immediately if necessary.

4. **Analysis**: Use the code only for the purpose of analyzing its behavior. Do not attempt to modify or distribute the code unless you fully understand the risks and have taken appropriate precautions.

5. **Legal Compliance**: Ensure that your use of the code complies with all applicable laws and regulations in your jurisdiction.

### **中文版本**

如果您选择使用此代码，请仔细遵循以下说明以尽量减少损害风险：

1. **隔离**：始终在安全的隔离环境（例如虚拟机或沙箱）中运行代码。确保该环境完全断开与任何生产系统或网络的连接。

2. **备份**：在运行代码之前，请确保备份您不希望丢失的任何重要数据或系统。

3. **监控**：在代码运行时密切监控环境。必要时立即关闭环境。

4. **分析**：仅将代码用于分析其行为的目的。除非您完全了解风险并采取了适当的预防措施，否则请勿尝试修改或分发代码。

5. **法律合规**：确保您使用代码的行为符合您所在司法管辖区的所有适用法律和法规。

---

## **License (许可证)**

### **English Version**

This code is licensed under the MIT License. However, the license does not grant you the right to use this code for any illegal or malicious purposes. You are solely responsible for ensuring that your use of this code complies with all applicable laws and regulations.

### **中文版本**

本代码根据MIT许可证提供。但是，该许可证并未授予您将此代码用于任何非法或恶意目的的权利。您有责任确保您使用此代码的行为符合所有适用的法律和法规。

---

## **Contact Information (联系信息)**

### **English Version**

If you have any questions or concerns about this repository, please contact the author at [wyt18222152539wyt@163.com]. However, please note that no support or assistance will be provided for the use of this code.

### **中文版本**

如果您对本仓库有任何疑问或疑虑，请通过[wyt18222152539wyt@163.com]与作者联系。但请注意，不会提供任何使用此代码的支持或帮助。

---

## **Conclusion (结论)**

### **English Version**

This repository is intended solely for educational or research purposes. The code provided here is potentially harmful and should only be used in a controlled, isolated environment. By accessing or using this repository, you acknowledge and accept the risks associated with the use of this code.

### **中文版本**

本仓库仅用于教育或研究目的。此处提供的代码具有潜在危害，只能在受控的隔离环境中使用。通过访问或使用此仓库，您承认并接受与此代码使用相关的风险。