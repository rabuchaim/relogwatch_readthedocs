.. relogWatch documentation master file, created by
   sphinx-quickstart on Fri Mar 15 14:35:29 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
.. include:: globals.rst

.. image:: _static/relogwatch.png
  :width: 500
  :alt: watching ya!
  :align: center

.. raw:: html

   <div align="center"><a class="center" href="https://relogwatch.readthedocs.io/en/latest/">English Version Available - https://relogwatch.readthedocs.io/en/latest/</a></div><br>

.. attention:: Nem todas as repetições de linhas de log geradas por um mesmo endereço IP devem ser consideradas como **abuso**, mas todos os **abusos** são repetições de linhas de log geradas por um mesmo endereço IP.

   .. **Como podemos afirmar se está ou não ocorrendo abuso em um serviço?** 
   .. Abuso são repetições em linhas de log a partir de um mesmo endereço. Um alto número de autenticações com falha a partir de um único endereço IP é um abuso que pode indicar uma tentative de descoberta de senha por tentativa e erro, o conhecido "brute force attack". Mas também pode indicar uma aplicação esquecida no ambiente com uma senha desatualizada.
   .. Da mesma forma, um alto número de autenticações com sucesso originadas a partir de um endereço IP mas com usernames diferentes também pode ser um abuso, e isso pode indicar uma exposição de senha de vários usuários. Mas também pode indicar uma empresa com muitos funcionários, e cada um dele com conta de email da sua empresa, o que é um uso legítimo e o acesso ao seu serviço deve ser protegido contra bloqueios.



Documentação do relogWatch v1.5.0
=================================

.. toctree::
   :maxdepth: 2
   :caption: Conteúdo:

   whatis
   isforme
   prepareenv
   installation
   configuration
   faq

|br|
|br|
|br|
|br|

:Author: Ricardo Abuchaim - ricardoabuchaim@gmail.com
:Version: 1.5.0 - **Release**: 2024/03/20