# Reference Home Lab — ver392026

```mermaid
flowchart LR
 Mac[MacBook Air M1\nControl Plane + ARO + light AI]
 Mini[Older Mac mini\nlogs + evidence + knowledge + vector DB]
 iPad[iPad\nobservability dashboard]
 Phone[Phone\nalerts + remote approval]
 Nvidia[Optional NVIDIA/Linux\nheavy local inference]
 Cloud[Cloud/API\nfrontier reasoning + burst]
 Mac --- Mini
 Mac --- iPad
 Phone --- Mac
 Mac -. optional .- Nvidia
 Mac -. local-first .- Cloud
```

This is a reference topology, not a requirement. ARO should run across one laptop, a small home lab, or a larger heterogeneous environment. Keep secrets, real evidence, and internal network details out of public configuration.
