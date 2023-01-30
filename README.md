<!-- Badges -->
[![Contributors][contributors-badge]][contributors-wlink]
[![Stars][stars-badge]][stars-wlink]
[![License][license-badge]][license-wlink]
[![Version][version-badge]][version-wlink]

<!-- School Logo Header -->
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Logo_esilv_png_blanc.png/600px-Logo_esilv_png_blanc.png" alt="ESILV LOGO" width="100" height="100"> 
<img src="https://cdn.livestorm.co/uploads/organization/avatar/458c155c-0eb6-4400-9aa5-417e61f64b3f/29eb3e3a-7095-4752-8b3a-9a6c3279b09f.png?v=1602173188" alt="POLE DE VINCI LOGO" width="100" height="100">

<!-- Project's Part 01 Header -->
# 👋 **Smart City Robot**
<div align="center">
    <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png"  width="150">
    <img src="https://cdn.discordapp.com/attachments/1016726123134058526/1069603350892523560/image.png" width="90" height="170">
</div>

<!-- Presenting the project -->
# 💫 **Project Overview**
    
This project was proposed as part of a competition on systems programming Multi-agent, one of the domains of AI.Our scenario consists of two teams of robots (called agents) moving in the streets of a city (a 2D Map). The goal of each team is to win as much money as possible. Money is a reward for achieving some
tasks. Tasks include the acquisition and transportation of goods. 

These tasks can be created by the system (environment) or by one of the teams of agents. It
There are two types of tasks: simple tasks (first come, first served) and tasks that require auctions. A team can accept a task that is
auction by bidding. The amount of the auction is the reward. If both teams bid, the lowest bid is naturally winning. 

If a job is not completed in time, the corresponding team is fined (a part Reward). A paid task has a pre-defined reward.

The aim of this project is to develop the agents, their environment and its management. 
First, we will consider mono-agent teams and robots must move randomly in the environment. 
The robots will then enriched with intelligent behavior so that they can move efficiently.

# ❄️ **Rules of the game**

Teams need to decide on tasks and how to proceed, meaning is to find the resources and how to navigate the map taking into account targets such as stores, warehouses, charging stations and storage facilities. 

A team is composed of different types of agents. The agents differ in their speed, their displacement in the city (Different algorithms such that the random move, the move A*, the use of a path already stored, etc.), the battery charge and the volume of goods they can transport. 

The goods can be handed over to a teammate, stored, delivered as part of a task completed, recovered from a storage facility and discharged. These actions may occur at their respective specific locations. Officers have a battery charge that decreases as they move from one place to another. They must ensure that they never break down and must so plan their visits to charging stations accordingly. Move from a location to another, as well as charging the battery to a charging station, are actions are only partially completed at each stage and may require
several stages. 

Tournament points are distributed according to the sum of rewards a team has at the end of the simulation. To get the most points, one team must beat the other and exceed a certain threshold. If a team has a significant debt, points are deducted.

# 🧿 **Technologies Used**

The main programming language that we will use is Python, the library Tkinter especially.
The tkinter package ("Tk interface") is the standard Python interface to the Tcl/Tk GUI toolkit. 
Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

## 💎 **How to Download and check if Tkinter works**
Running python -m tkinter from the command line should open a window demonstrating a simple Tk interface, 
letting you know that tkinter is properly installed on your system, and also showing what version of Tcl/Tk is installed, 
so you can read the Tcl/Tk documentation specific to that version.

<img href="https://imgur.com/AgBLeeC"><img src="https://i.imgur.com/AgBLeeC.png" title="source: imgur.com">

<!-- Markdown Badges Variables -->
[contributors-badge]: https://img.shields.io/github/contributors/Miroshino/Smart-City-Robot.svg?style=for-the-badge
[contributors-wlink]: https://github.com/Miroshino/Smart-City-Robot/graphs/contributors

[stars-badge]: https://img.shields.io/github/stars/Miroshino/Smart-City-Robot.svg?style=for-the-badge
[stars-wlink]: https://github.com/Miroshino/Smart-City-Robot/stargazers

[license-badge]: https://img.shields.io/github/license/Miroshino/Smart-City-Robot.svg?style=for-the-badge
[license-wlink]: ttps://github.com/Miroshino/Smart-City-Robot/blob/master/LICENSE.txt

[version-badge]: https://img.shields.io/badge/Version-v1.0.0-green?style=for-the-badge
[version-wlink]: https://github.com/Miroshino/Smart-City-Robot
