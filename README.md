[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## Updated on 2025.03.28
> Usage instructions: [here](./docs/README.md#usage)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href=#SLAM>SLAM</a></li>
    <li><a href=#SFM>SFM</a></li>
    <li><a href=#Visual-Localization>Visual Localization</a></li>
    <li><a href=#Keypoint-Detection>Keypoint Detection</a></li>
    <li><a href=#Image-Matching>Image Matching</a></li>
    <li><a href=#NeRF>NeRF</a></li>
    <li><a href=#Inference>Inference</a></li>
    <li><a href=#Distributed-Deep-Learning>Distributed Deep Learning</a></li>
    <li><a href=#GNN-System>GNN System</a></li>
  </ol>
</details>

## SLAM

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2023-06-01**|**Event-based Visual Odometry with Full Temporal Resolution via Continuous-time Gaussian Process Regression**|Jianeng Wang et.al.|[2306.01188](http://arxiv.org/abs/2306.01188)|null|
|**2023-05-28**|**OSPC: Online Sequential Photometric Calibration**|Jawad Haidar et.al.|[2305.17673](http://arxiv.org/abs/2305.17673)|null|
|**2023-05-15**|**Event Camera-based Visual Odometry for Dynamic Motion Tracking of a Legged Robot Using Adaptive Time Surface**|Shifan Zhu et.al.|[2305.08962](http://arxiv.org/abs/2305.08962)|null|
|**2023-05-10**|**Transformer-based model for monocular visual odometry: a video understanding approach**|André O. Françani et.al.|[2305.06121](http://arxiv.org/abs/2305.06121)|**[link](https://github.com/aofrancani/tsformer-vo)**|
|**2023-04-29**|**Modality-invariant Visual Odometry for Embodied Vision**|Marius Memmel et.al.|[2305.00348](http://arxiv.org/abs/2305.00348)|**[link](https://github.com/memmelma/vo-transformer)**|
|**2023-04-21**|**FSNet: Redesign Self-Supervised MonoDepth for Full-Scale Depth Prediction for Autonomous Driving**|Yuxuan Liu et.al.|[2304.10719](http://arxiv.org/abs/2304.10719)|null|
|**2023-04-18**|**Visual-LiDAR Odometry and Mapping with Monocular Scale Correction and Motion Compensation**|Hanyu Cai et.al.|[2304.08978](http://arxiv.org/abs/2304.08978)|null|
|**2023-04-12**|**SiLK -- Simple Learned Keypoints**|Pierre Gleize et.al.|[2304.06194](http://arxiv.org/abs/2304.06194)|**[link](https://github.com/facebookresearch/silk)**|
|**2023-04-11**|**ClusterFusion: Real-time Relative Positioning and Dense Reconstruction for UAV Cluster**|Yifei Dong et.al.|[2304.04943](http://arxiv.org/abs/2304.04943)|null|
|**2023-03-21**|**Learning a Depth Covariance Function**|Eric Dexheimer et.al.|[2303.12157](http://arxiv.org/abs/2303.12157)|null|
|**2023-03-21**|**Online Learning of Wheel Odometry Correction for Mobile Robots with Attention-based Neural Network**|Alessandro Navone et.al.|[2303.11725](http://arxiv.org/abs/2303.11725)|null|
|**2023-03-20**|**VR-SLAM: A Visual-Range Simultaneous Localization and Mapping System using Monocular Camera and Ultra-wideband Sensors**|Thien Hoang Nguyen et.al.|[2303.10903](http://arxiv.org/abs/2303.10903)|null|
|**2023-03-17**|**CoVIO: Online Continual Learning for Visual-Inertial Odometry**|Niclas Vödisch et.al.|[2303.10149](http://arxiv.org/abs/2303.10149)|**[link](https://github.com/robot-learning-freiburg/CL-SLAM)**|
|**2023-03-15**|**UMS-VINS: United Monocular-Stereo Features for Visual-Inertial Tightly Coupled Odometry**|Chaoyang Jiang et.al.|[2303.08550](http://arxiv.org/abs/2303.08550)|null|
|**2023-03-13**|**Discovering Multiple Algorithm Configurations**|Leonid Keselman et.al.|[2303.07434](http://arxiv.org/abs/2303.07434)|null|
|**2023-03-09**|**Virtual Inverse Perspective Mapping for Simultaneous Pose and Motion Estimation**|Masahiro Hirano et.al.|[2303.05192](http://arxiv.org/abs/2303.05192)|null|
|**2023-03-16**|**Stereo Event-based Visual-Inertial Odometry**|Kunfeng Wang et.al.|[2303.05086](http://arxiv.org/abs/2303.05086)|**[link](https://github.com/wkunfeng/sevio)**|
|**2023-03-07**|**Long Distance GNSS-Denied Visual Inertial Navigation for Autonomous Fixed Wing Unmanned Air Vehicles: SO(3) Manifold Filter based on Virtual Vision Sensor**|Eduardo Gallo et.al.|[2303.03804](http://arxiv.org/abs/2303.03804)|null|
|**2023-03-03**|**Lightweight, Uncertainty-Aware Conformalized Visual Odometry**|Alex C. Stutts et.al.|[2303.02207](http://arxiv.org/abs/2303.02207)|null|
|**2023-02-24**|**FLSea: Underwater Visual-Inertial and Stereo-Vision Forward-Looking Datasets**|Yelena Randall et.al.|[2302.12772](http://arxiv.org/abs/2302.12772)|null|
|**2023-02-27**|**CP+: Camera Poses Augmentation with Large-scale LiDAR Maps**|Jiadi Cui et.al.|[2302.12198](http://arxiv.org/abs/2302.12198)|null|
|**2023-02-19**|**EdgeVO: An Efficient and Accurate Edge-based Visual Odometry**|Hui Zhao et.al.|[2302.09493](http://arxiv.org/abs/2302.09493)|null|
|**2023-01-27**|**HDPV-SLAM: Hybrid Depth-augmented Panoramic Visual SLAM for Mobile Mapping System with Tilted LiDAR and Panoramic Visual Camera**|Mostafa Ahmadi et.al.|[2301.11823](http://arxiv.org/abs/2301.11823)|null|
|**2023-01-26**|**Distributed Optimization Methods for Multi-Robot Systems: Part I -- A Tutorial**|Ola Shorinwa et.al.|[2301.11313](http://arxiv.org/abs/2301.11313)|null|
|**2023-01-24**|**Generalized Object Search**|Kaiyu Zheng et.al.|[2301.10121](http://arxiv.org/abs/2301.10121)|null|
|**2023-01-22**|**Improving Autonomous Vehicle Mapping and Navigation in Work Zones Using Crowdsourcing Vehicle Trajectories**|Hanlin Chen et.al.|[2301.09194](http://arxiv.org/abs/2301.09194)|null|
|**2023-01-21**|**Dense RGB SLAM with Neural Implicit Maps**|Heng Li et.al.|[2301.08930](http://arxiv.org/abs/2301.08930)|null|
|**2023-01-18**|**Extended FastSLAM Using Cellular Multipath Component Delays and Angular Information**|Junshi Chen et.al.|[2301.07560](http://arxiv.org/abs/2301.07560)|null|
|**2023-01-17**|**COVINS-G: A Generic Back-end for Collaborative Visual-Inertial SLAM**|Manthan Patel et.al.|[2301.07147](http://arxiv.org/abs/2301.07147)|**[link](https://github.com/VIS4ROB-lab/covins)**|
|**2023-01-31**|**Swarm-SLAM : Sparse Decentralized Collaborative Simultaneous Localization and Mapping Framework for Multi-Robot Systems**|Pierre-Yves Lajoie et.al.|[2301.06230](http://arxiv.org/abs/2301.06230)|**[link](https://github.com/mistlab/swarm-slam)**|
|**2023-01-13**|**A LiDAR-Inertial-Visual SLAM System with Loop Detection**|Kangcheng Liu et.al.|[2301.05604](http://arxiv.org/abs/2301.05604)|null|
|**2023-01-11**|**AdaptSLAM: Edge-Assisted Adaptive SLAM with Resource Constraints via Uncertainty Minimization**|Ying Chen et.al.|[2301.04620](http://arxiv.org/abs/2301.04620)|**[link](https://github.com/i3tyc/adaptslam)**|
|**2023-01-12**|**TBV Radar SLAM -- trust but verify loop candidates**|Daniel Adolfsson et.al.|[2301.04397](http://arxiv.org/abs/2301.04397)|**[link](https://github.com/dan11003/tbv_slam_public)**|
|**2022-12-31**|**Digital Twin-Enabled Domain Adaptation for Zero-Touch UAV Networks: Survey and Challenges**|Maxwell McManus et.al.|[2301.03359](http://arxiv.org/abs/2301.03359)|null|
|**2023-01-09**|**Motion Addition and Motion Optimization**|Liqun Qi et.al.|[2301.03174](http://arxiv.org/abs/2301.03174)|null|
|**2023-01-08**|**Towards Open World NeRF-Based SLAM**|Daniil Lisus et.al.|[2301.03102](http://arxiv.org/abs/2301.03102)|null|
|**2023-01-06**|**CyberLoc: Towards Accurate Long-term Visual Localization**|Liu Liu et.al.|[2301.02403](http://arxiv.org/abs/2301.02403)|null|
|**2023-01-03**|**LunarNav: Crater-based Localization for Long-range Autonomous Lunar Rover Navigation**|Shreyansh Daftry et.al.|[2301.01350](http://arxiv.org/abs/2301.01350)|null|
|**2022-12-31**|**4Seasons: Benchmarking Visual SLAM and Long-Term Localization for Autonomous Driving in Challenging Conditions**|Patrick Wenzel et.al.|[2301.01147](http://arxiv.org/abs/2301.01147)|null|
|**2023-01-03**|**BS3D: Building-scale 3D Reconstruction from RGB-D Images**|Janne Mustaniemi et.al.|[2301.01057](http://arxiv.org/abs/2301.01057)|null|
|**2023-01-10**|**An Event-based Algorithm for Simultaneous 6-DOF Camera Pose Tracking and Mapping**|Masoud Dayani Najafabadi et.al.|[2301.00618](http://arxiv.org/abs/2301.00618)|**[link](https://github.com/m-dayani/eorb_slam)**|
|**2022-12-25**|**A Combined Approach Toward Consistent Reconstructions of Indoor Spaces Based on 6D RGB-D Odometry and KinectFusion**|Nadia Figueroa et.al.|[2212.14772](http://arxiv.org/abs/2212.14772)|null|
|**2022-12-29**|**An Enhanced LiDAR-Inertial SLAM System for Robotics Localization and Mapping**|Kangcheng Liu et.al.|[2212.14209](http://arxiv.org/abs/2212.14209)|**[link](https://github.com/KangchengLiu/slam_resources)**|
|**2022-12-27**|**Clock and Orientation-Robust Simultaneous Radio Localization and Mapping at Millimeter Wave Bands**|Felipe Gómez-Cuba et.al.|[2212.13477](http://arxiv.org/abs/2212.13477)|**[link](https://github.com/gomezcuba/castro-5g)**|
|**2022-12-26**|**ESVIO: Event-based Stereo Visual Inertial Odometry**|Peiyu Chen et.al.|[2212.13184](http://arxiv.org/abs/2212.13184)|**[link](https://github.com/arclab-hku/event_based_vo-vio-slam)**|
|**2022-12-24**|**A Comprehensive Review on Autonomous Navigation**|Saeid Nahavandi et.al.|[2212.12808](http://arxiv.org/abs/2212.12808)|null|
|**2022-12-23**|**Radio SLAM for 6G Systems at THz Frequencies: Design and Experimental Validation**|Marina Lotti et.al.|[2212.12388](http://arxiv.org/abs/2212.12388)|null|
|**2022-12-23**|**Implementation of a Blind navigation method in outdoors/indoors areas**|Mohammad Javadian Farzaneh et.al.|[2212.12185](http://arxiv.org/abs/2212.12185)|null|
|**2022-12-22**|**S-Graphs+: Real-time Localization and Mapping leveraging Hierarchical Representations**|Hriday Bavle et.al.|[2212.11770](http://arxiv.org/abs/2212.11770)|**[link](https://github.com/snt-arg/s_graphs_docker)**|
|**2022-12-22**|**Active SLAM: A Review On Last Decade**|Muhammad Farhan Ahmed et.al.|[2212.11654](http://arxiv.org/abs/2212.11654)|null|
|**2022-12-27**|**Motion, Unit Dual Quaternion and Motion Optimization**|Liqun Qi et.al.|[2212.11593](http://arxiv.org/abs/2212.11593)|null|
|**2022-12-22**|**Vision-Based Environmental Perception for Autonomous Driving**|Fei Liu et.al.|[2212.11453](http://arxiv.org/abs/2212.11453)|null|
|**2022-12-19**|**Mu $^{2}$ SLAM: Multitask, Multilingual Speech and Language Models**|Yong Cheng et.al.|[2212.09553](http://arxiv.org/abs/2212.09553)|null|
|**2022-12-16**|**Cartographer_glass: 2D Graph SLAM Framework using LiDAR for Glass Environments**|Lasitha Weerakoon et.al.|[2212.08633](http://arxiv.org/abs/2212.08633)|null|
|**2022-12-16**|**rWiFiSLAM: Effective WiFi Ranging based SLAM System in Ambient Environments**|Bo Wei et.al.|[2212.08418](http://arxiv.org/abs/2212.08418)|null|
|**2023-03-02**|**AirVO: An Illumination-Robust Point-Line Visual Odometry**|Kuan Xu et.al.|[2212.07595](http://arxiv.org/abs/2212.07595)|**[link](https://github.com/xukuanHIT/AirVO)**|
|**2022-12-14**|**Autonomous Vehicle Navigation with LIDAR using Path Planning**|Rahul M K et.al.|[2212.07155](http://arxiv.org/abs/2212.07155)|null|
|**2022-12-14**|**RIS-Enabled and Access-Point-Free Simultaneous Radio Localization and Mapping**|Hyowon Kim et.al.|[2212.07141](http://arxiv.org/abs/2212.07141)|null|
|**2022-12-13**|**Know What You Don't Know: Consistency in Sliding Window Filtering with Unobservable States Applied to Visual-Inertial SLAM (Extended Version)**|Daniil Lisus et.al.|[2212.06923](http://arxiv.org/abs/2212.06923)|null|
|**2022-12-13**|**SST: Real-time End-to-end Monocular 3D Reconstruction via Sparse Spatial-Temporal Guidance**|Chenyangguang Zhang et.al.|[2212.06524](http://arxiv.org/abs/2212.06524)|null|
|**2022-12-13**|**Localization and Navigation System for Indoor Mobile Robot**|Yanbaihui Liu et.al.|[2212.06391](http://arxiv.org/abs/2212.06391)|null|
|**2022-12-12**|**Evaluation of RGB-D SLAM in Large Indoor Environments**|Kirill Muravyev et.al.|[2212.05980](http://arxiv.org/abs/2212.05980)|null|
|**2022-12-19**|**A Light-Weight LiDAR-Inertial SLAM System with Loop Closing**|Kangcheng Liu et.al.|[2212.05743](http://arxiv.org/abs/2212.05743)|**[link](https://github.com/KangchengLiu/deep-learning-localization-mapping)**|
|**2022-12-12**|**An Integrated LiDAR-SLAM System for Complex Environment with Noisy Point Clouds**|Kangcheng Liu et.al.|[2212.05705](http://arxiv.org/abs/2212.05705)|**[link](https://github.com/KangchengLiu/deep-learning-localization-mapping)**|
|**2022-12-09**|**SLAM for Visually Impaired People: A Survey**|Marziyeh Bamdad et.al.|[2212.04745](http://arxiv.org/abs/2212.04745)|null|
|**2022-12-09**|**Ego-Body Pose Estimation via Ego-Head Pose Estimation**|Jiaman Li et.al.|[2212.04636](http://arxiv.org/abs/2212.04636)|null|
|**2022-12-06**|**Receding Horizon Planning with Rule Hierarchies for Autonomous Vehicles**|Sushant Veer et.al.|[2212.03323](http://arxiv.org/abs/2212.03323)|**[link](https://github.com/nvlabs/rule-hierarchies)**|
|**2022-12-06**|**PRISM: Probabilistic Real-Time Inference in Spatial World Models**|Atanas Mirchev et.al.|[2212.02988](http://arxiv.org/abs/2212.02988)|null|
|**2022-12-06**|**RGB-L: Enhancing Indirect Visual SLAM using LiDAR-based Dense Depth Maps**|Florian Sauerbeck et.al.|[2212.02085](http://arxiv.org/abs/2212.02085)|**[link](https://github.com/tumftm/orb_slam3_rgbl)**|
|**2022-12-05**|**DL-SLOT: Dynamic LiDAR SLAM and object tracking based on collaborative graph optimization**|Xuebo Tian et.al.|[2212.02077](http://arxiv.org/abs/2212.02077)|null|
|**2022-12-05**|**ObjectMatch: Robust Registration using Canonical Object Correspondences**|Can Gümeli et.al.|[2212.01985](http://arxiv.org/abs/2212.01985)|null|
|**2022-12-02**|**Sparse SPN: Depth Completion from Sparse Keypoints**|Yuqun Wu et.al.|[2212.00987](http://arxiv.org/abs/2212.00987)|null|
|**2022-12-01**|**maplab 2.0 -- A Modular and Multi-Modal Mapping Framework**|Andrei Cramariuc et.al.|[2212.00654](http://arxiv.org/abs/2212.00654)|**[link](https://github.com/ethz-asl/maplab)**|
|**2022-12-01**|**AstroSLAM: Autonomous Monocular Navigation in the Vicinity of a Celestial Small Body -- Theory and Experiments**|Mehregan Dor et.al.|[2212.00350](http://arxiv.org/abs/2212.00350)|null|
|**2022-11-30**|**MVRackLay: Monocular Multi-View Layout Estimation for Warehouse Racks and Shelves**|Pranjali Pathre et.al.|[2211.16882](http://arxiv.org/abs/2211.16882)|null|
|**2022-11-29**|**PatchMatch-Stereo-Panorama, a fast dense reconstruction from 360° video images**|Hartmut Surmann et.al.|[2211.16266](http://arxiv.org/abs/2211.16266)|**[link](https://github.com/roblabwh/patchmatch)**|
|**2022-11-29**|**MmWave Mapping and SLAM for 5G and Beyond**|Yu Ge et.al.|[2211.16024](http://arxiv.org/abs/2211.16024)|null|
|**2022-11-28**|**Safety-quantifiable Line Feature-based Monocular Visual Localization with 3D Prior Map**|Xi Zheng et.al.|[2211.15127](http://arxiv.org/abs/2211.15127)|null|
|**2022-11-29**|**BALF: Simple and Efficient Blur Aware Local Feature Detector**|Zhenjun Zhao et.al.|[2211.14731](http://arxiv.org/abs/2211.14731)|null|
|**2022-11-27**|**Development of a Modular Real-time Shared-control System for a Smart Wheelchair**|Vaishanth Ramaraj et.al.|[2211.14711](http://arxiv.org/abs/2211.14711)|null|
|**2022-11-26**|**A1 SLAM: Quadruped SLAM using the A1's Onboard Sensors**|Jerred Chen et.al.|[2211.14432](http://arxiv.org/abs/2211.14432)|**[link](https://github.com/jerredchen/a1_slam)**|
|**2022-11-23**|**ActiveRMAP: Radiance Field for Active Mapping And Planning**|Huangying Zhan et.al.|[2211.12656](http://arxiv.org/abs/2211.12656)|null|
|**2022-11-22**|**Vision-based localization methods under GPS-denied conditions**|Zihao Lu et.al.|[2211.11988](http://arxiv.org/abs/2211.11988)|null|
|**2022-11-21**|**Towards Live 3D Reconstruction from Wearable Video: An Evaluation of V-SLAM, NeRF, and Videogrammetry Techniques**|David Ramirez et.al.|[2211.11836](http://arxiv.org/abs/2211.11836)|null|
|**2022-11-21**|**ESLAM: Efficient Dense SLAM System Based on Hybrid Representation of Signed Distance Fields**|Mohammad Mahdi Johari et.al.|[2211.11704](http://arxiv.org/abs/2211.11704)|null|
|**2022-11-24**|**Data Fusion for Multipath-Based SLAM: Combing Information from Multiple Propagation Paths**|Erik Leitinger et.al.|[2211.09241](http://arxiv.org/abs/2211.09241)|null|
|**2022-11-16**|**Self-supervised Egomotion and Depth Learning via Bi-directional Coarse-to-Fine Scale Recovery**|Hao Qu et.al.|[2211.08904](http://arxiv.org/abs/2211.08904)|null|
|**2022-11-20**|**Detecting Line Segments in Motion-blurred Images with Events**|Huai Yu et.al.|[2211.07365](http://arxiv.org/abs/2211.07365)|**[link](https://github.com/lh9171338/FE-LSD)**|
|**2022-11-13**|**Automatic Eye-in-Hand Calibration using EKF**|Aditya Ramakrishnan et.al.|[2211.06881](http://arxiv.org/abs/2211.06881)|null|
|**2022-11-12**|**Active View Planning for Visual SLAM in Outdoor Environments Based on Continuous Information Modeling**|Zhihao Wang et.al.|[2211.06557](http://arxiv.org/abs/2211.06557)|**[link](https://github.com/hitsz-nrsl/iglov)**|
|**2022-11-11**|**Multi-domain Cooperative SLAM: The Enabler for Integrated Sensing and Communications**|Jie Yang et.al.|[2211.05982](http://arxiv.org/abs/2211.05982)|null|
|**2022-11-10**|**Online Stochastic Variational Gaussian Process Mapping for Large-Scale SLAM in Real Time**|Ignacio Torroba et.al.|[2211.05601](http://arxiv.org/abs/2211.05601)|**[link](https://github.com/ignaciotb/uwexploration)**|
|**2022-11-07**|**When Geometry is not Enough: Using Reflector Markers in Lidar SLAM**|Gerhard Kurz et.al.|[2211.03484](http://arxiv.org/abs/2211.03484)|null|
|**2022-11-07**|**Detecting Invalid Map Merges in Lifelong SLAM**|Matthias Holoch et.al.|[2211.03423](http://arxiv.org/abs/2211.03423)|null|
|**2022-11-06**|**Wheel-SLAM: Simultaneous Localization and Terrain Mapping Using One Wheel-mounted IMU**|Yibin Wu et.al.|[2211.03174](http://arxiv.org/abs/2211.03174)|**[link](https://github.com/i2nav-whu/wheel-slam)**|
|**2022-11-07**|**Lidar-level localization with radar? The CFEAR approach to accurate, fast and robust large-scale radar odometry in diverse environments**|Daniel Adolfsson et.al.|[2211.02445](http://arxiv.org/abs/2211.02445)|**[link](https://github.com/dan11003/cfear_evaluation)**|
|**2022-11-03**|**DyOb-SLAM : Dynamic Object Tracking SLAM System**|Rushmian Annoy Wadud et.al.|[2211.01941](http://arxiv.org/abs/2211.01941)|null|
|**2022-11-03**|**Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid Robot Teleoperation using SLAM**|Yang Chen et.al.|[2211.01749](http://arxiv.org/abs/2211.01749)|null|
|**2022-11-04**|**$D^2$ SLAM: Decentralized and Distributed Collaborative Visual-inertial SLAM System for Aerial Swarm**|Hao Xu et.al.|[2211.01538](http://arxiv.org/abs/2211.01538)|**[link](https://github.com/hkust-aerial-robotics/d2slam)**|
|**2022-11-02**|**Semantic SuperPoint: A Deep Semantic Descriptor**|Gabriel S. Gama et.al.|[2211.01098](http://arxiv.org/abs/2211.01098)|**[link](https://github.com/gabriel-sgama/semantic-superpoint)**|
|**2022-11-02**|**Ambiguity-Aware Multi-Object Pose Optimization for Visually-Assisted Robot Manipulation**|Myung-Hwan Jeon et.al.|[2211.00960](http://arxiv.org/abs/2211.00960)|**[link](https://github.com/rpmsnu/prima6d)**|
|**2022-10-31**|**Mapping Extended Landmarks for Radar SLAM**|Shuai Sun et.al.|[2210.17207](http://arxiv.org/abs/2210.17207)|null|
|**2022-10-25**|**MAROAM: Map-based Radar SLAM through Two-step Feature Selection**|Dequan Wang et.al.|[2210.13797](http://arxiv.org/abs/2210.13797)|null|
|**2022-10-25**|**S3E: A Large-scale Multimodal Dataset for Collaborative SLAM**|Dapeng Feng et.al.|[2210.13723](http://arxiv.org/abs/2210.13723)|**[link](https://github.com/pengyu-team/s3e)**|
|**2022-10-24**|**NeRF-SLAM: Real-Time Dense Monocular SLAM with Neural Radiance Fields**|Antoni Rosinol et.al.|[2210.13641](http://arxiv.org/abs/2210.13641)|**[link](https://github.com/ToniRV/NeRF-SLAM)**|
|**2022-10-24**|**Compact simultaneous label-free autofluorescence multi-harmonic (SLAM) microscopy for user-friendly photodamage-monitored imaging**|Geng Wang et.al.|[2210.13556](http://arxiv.org/abs/2210.13556)|null|
|**2022-10-28**|**VP-SLAM: A Monocular Real-time Visual SLAM with Points, Lines and Vanishing Points**|Andreas Georgis et.al.|[2210.12756](http://arxiv.org/abs/2210.12756)|null|
|**2022-10-22**|**SLAM: Semantic Learning based Activation Map for Weakly Supervised Semantic Segmentation**|Junliang Chen et.al.|[2210.12417](http://arxiv.org/abs/2210.12417)|null|
|**2022-10-21**|**DCL-SLAM: A Distributed Collaborative LiDAR SLAM Framework for a Robotic Swarm**|Shipeng Zhong et.al.|[2210.11978](http://arxiv.org/abs/2210.11978)|**[link](https://github.com/pengyu-team/dcl-slam)**|
|**2022-10-21**|**Motion Primitives Based Kinodynamic RRT for Autonomous Vehicle Navigation in Complex Environments**|Shubham Kedia et.al.|[2210.11652](http://arxiv.org/abs/2210.11652)|null|
|**2022-10-22**|**Visual SLAM: What are the Current Trends and What to Expect?**|Ali Tourani et.al.|[2210.10491](http://arxiv.org/abs/2210.10491)|null|
|**2022-10-18**|**Split-KalmanNet: A Robust Model-Based Deep Learning Approach for SLAM**|Geon Choi et.al.|[2210.09636](http://arxiv.org/abs/2210.09636)|null|
|**2022-10-16**|**D2SLAM: Semantic visual SLAM based on the influence of Depth for Dynamic environments**|Ayman Beghdadi et.al.|[2210.08647](http://arxiv.org/abs/2210.08647)|null|
|**2022-10-16**|**Indoor Smartphone SLAM with Learned Echoic Location Features**|Wenjie Luo et.al.|[2210.08493](http://arxiv.org/abs/2210.08493)|null|
|**2022-10-15**|**Self-Improving SLAM in Dynamic Environments: Learning When to Mask**|Adrian Bojko et.al.|[2210.08350](http://arxiv.org/abs/2210.08350)|**[link](https://github.com/adrianbojko/consinv-dataset)**|
|**2022-10-13**|**Design and Evaluation of a Generic Visual SLAM Framework for Multi-Camera Systems**|Pushyami Kaveti et.al.|[2210.07315](http://arxiv.org/abs/2210.07315)|**[link](https://github.com/neufieldrobotics/multicamslam)**|
|**2022-10-12**|**RING++: Roto-translation Invariant Gram for Global Localization on a Sparse Scan Map**|Xuecheng Xu et.al.|[2210.05984](http://arxiv.org/abs/2210.05984)|**[link](https://github.com/MaverickPeter/MR_SLAM)**|
|**2022-10-11**|**Observability Analysis of Graph SLAM-Based Joint Calibration of Multiple Microphone Arrays and Sound Source Localization**|Yuanzheng He et.al.|[2210.05600](http://arxiv.org/abs/2210.05600)|null|
|**2022-10-11**|**Autonomous Asteroid Characterization Through Nanosatellite Swarming**|Kaitlin Dennison et.al.|[2210.05518](http://arxiv.org/abs/2210.05518)|null|
|**2022-10-11**|**DeepMLE: A Robust Deep Maximum Likelihood Estimator for Two-view Structure from Motion**|Yuxi Xiao et.al.|[2210.05517](http://arxiv.org/abs/2210.05517)|null|
|**2022-10-11**|**Multi-Object Navigation with dynamically learned neural implicit representations**|Pierre Marza et.al.|[2210.05129](http://arxiv.org/abs/2210.05129)|**[link](https://github.com/PierreMarza/dynamic_implicit_representations)**|
|**2022-10-12**|**Spectral Sparsification for Communication-Efficient Collaborative Rotation and Translation Estimation**|Yulun Tian et.al.|[2210.05020](http://arxiv.org/abs/2210.05020)|null|
|**2022-10-10**|**Using Detection, Tracking and Prediction in Visual SLAM to Achieve Real-time Semantic Mapping of Dynamic Scenarios**|Xingyu Chen et.al.|[2210.04562](http://arxiv.org/abs/2210.04562)|null|
|**2022-10-09**|**Fusing Event-based Camera and Radar for SLAM Using Spiking Neural Networks with Continual STDP Learning**|Ali Safa et.al.|[2210.04236](http://arxiv.org/abs/2210.04236)|null|
|**2022-10-06**|**SCORE: A Second-Order Conic Initialization for Range-Aided SLAM**|Alan Papalia et.al.|[2210.03177](http://arxiv.org/abs/2210.03177)|**[link](https://github.com/marineroboticsgroup/score)**|
|**2022-10-06**|**Feature-Realistic Neural Fusion for Real-Time, Open Set Scene Understanding**|Kirill Mazur et.al.|[2210.03043](http://arxiv.org/abs/2210.03043)|null|
|**2022-10-06**|**Feasibility on Detecting Door Slamming towards Monitoring Early Signs of Domestic Violence**|Osian Morgan et.al.|[2210.02642](http://arxiv.org/abs/2210.02642)|null|
|**2022-10-05**|**MOTSLAM: MOT-assisted monocular dynamic SLAM using single-view depth estimation**|Hanwei Zhang et.al.|[2210.02038](http://arxiv.org/abs/2210.02038)|null|
|**2022-10-04**|**O2S: Open-source open shuttle**|Nwankwo Linus et.al.|[2210.01627](http://arxiv.org/abs/2210.01627)|null|
|**2022-10-04**|**Wi-Closure: Reliable and Efficient Search of Inter-robot Loop Closures Using Wireless Sensing**|Weiying Wang et.al.|[2210.01320](http://arxiv.org/abs/2210.01320)|null|
|**2022-10-03**|**Probabilistic Volumetric Fusion for Dense Monocular SLAM**|Antoni Rosinol et.al.|[2210.01276](http://arxiv.org/abs/2210.01276)|null|
|**2022-10-03**|**DRACo-SLAM: Distributed Robust Acoustic Communication-efficient SLAM for Imaging Sonar Equipped Underwater Robot Teams**|John McConnell et.al.|[2210.00867](http://arxiv.org/abs/2210.00867)|**[link](https://github.com/jake3991/draco-slam)**|
|**2022-10-03**|**A Benchmark for Multi-Modal Lidar SLAM with Ground Truth in GNSS-Denied Environments**|Ha Sier et.al.|[2210.00812](http://arxiv.org/abs/2210.00812)|**[link](https://github.com/tiers/tiers-lidars-dataset-enhanced)**|
|**2022-10-01**|**Det-SLAM: A semantic visual SLAM for highly dynamic scenes using Detectron2**|Ali Eslamian et.al.|[2210.00278](http://arxiv.org/abs/2210.00278)|null|
|**2022-09-30**|**PyPose: A Library for Robot Learning with Physics-based Optimization**|Chen Wang et.al.|[2209.15428](http://arxiv.org/abs/2209.15428)|**[link](https://github.com/pypose/pypose)**|
|**2022-09-29**|**DirectTracker: 3D Multi-Object Tracking Using Direct Image Alignment and Photometric Bundle Adjustment**|Mariia Gladkova et.al.|[2209.14965](http://arxiv.org/abs/2209.14965)|null|
|**2022-09-28**|**Robust Incremental Smoothing and Mapping (riSAM)**|Daniel McGann et.al.|[2209.14359](http://arxiv.org/abs/2209.14359)|null|
|**2022-09-27**|**Orbeez-SLAM: A Real-time Monocular Visual SLAM with ORB Features and NeRF-realized Mapping**|Chi-Ming Chung et.al.|[2209.13274](http://arxiv.org/abs/2209.13274)|**[link](https://github.com/MarvinChung/Orbeez-slam)**|
|**2022-09-24**|**Graph Neural Networks for Multi-Robot Active Information Acquisition**|Mariliza Tzes et.al.|[2209.12091](http://arxiv.org/abs/2209.12091)|null|
|**2022-09-24**|**Closing the Loop: Graph Networks to Unify Semantic Objects and Visual Features for Multi-object Scenes**|Jonathan J. Y. Kim et.al.|[2209.11894](http://arxiv.org/abs/2209.11894)|null|
|**2022-09-23**|**involve-MI: Informative Planning with High-Dimensional Non-Parametric Beliefs**|Gilad Rotman et.al.|[2209.11591](http://arxiv.org/abs/2209.11591)|null|
|**2022-09-23**|**Automatic Sign Reading and Localization for Semantic Mapping with an Office Robot**|David Balaban et.al.|[2209.11432](http://arxiv.org/abs/2209.11432)|null|
|**2022-09-22**|**SQ-SLAM: Monocular Semantic SLAM Based on Superquadric Object Representation**|Xiao Han et.al.|[2209.10817](http://arxiv.org/abs/2209.10817)|null|
|**2022-09-22**|**Acoustic SLAM based on the Direction-of-Arrival and the Direct-to-Reverberant Energy Ratio**|Wenhao Qiu et.al.|[2209.10726](http://arxiv.org/abs/2209.10726)|null|
|**2022-09-21**|**Visual Localization and Mapping in Dynamic and Changing Environments**|João Carlos Virgolino Soares et.al.|[2209.10710](http://arxiv.org/abs/2209.10710)|null|
|**2022-09-20**|**Uncertainty-Aware Tightly-Coupled GPS Fused LIO-SLAM**|Sabir Hossain et.al.|[2209.10047](http://arxiv.org/abs/2209.10047)|null|
|**2022-09-20**|**WGICP: Differentiable Weighted GICP-Based Lidar Odometry**|Sanghyun Son et.al.|[2209.09777](http://arxiv.org/abs/2209.09777)|null|
|**2022-09-20**|**PADLoC: LiDAR-Based Deep Loop Closure Detection and Registration using Panoptic Attention**|José Arce et.al.|[2209.09699](http://arxiv.org/abs/2209.09699)|**[link](https://github.com/robot-learning-freiburg/PADLoC)**|
|**2022-09-19**|**MeSLAM: Memory Efficient SLAM based on Neural Fields**|Evgenii Kruzhkov et.al.|[2209.09357](http://arxiv.org/abs/2209.09357)|null|
|**2022-09-19**|**LMBAO: A Landmark Map for Bundle Adjustment Odometry in LiDAR SLAM**|Letian Zhang et.al.|[2209.08810](http://arxiv.org/abs/2209.08810)|null|
|**2022-09-18**|**HGI-SLAM: Loop Closure With Human and Geometric Importance Features**|Shuhul Mujoo et.al.|[2209.08608](http://arxiv.org/abs/2209.08608)|null|
|**2022-09-18**|**Data-driven Loop Closure Detection in Bathymetric Point Clouds for Underwater SLAM**|Jiarui Tan et.al.|[2209.08578](http://arxiv.org/abs/2209.08578)|**[link](https://github.com/tjr16/bathy_nn_learning)**|
|**2022-09-17**|**DytanVO: Joint Refinement of Visual Odometry and Motion Segmentation in Dynamic Environments**|Shihao Shen et.al.|[2209.08430](http://arxiv.org/abs/2209.08430)|**[link](https://github.com/geniussh/dytanvo)**|
|**2022-09-17**|**OA-SLAM: Leveraging Objects for Camera Relocalization in Visual SLAM**|Matthieu Zins et.al.|[2209.08338](http://arxiv.org/abs/2209.08338)|null|
|**2022-09-17**|**PlaneSLAM: Plane-based LiDAR SLAM for Motion Planning in Structured 3D Environments**|Adam Dai et.al.|[2209.08248](http://arxiv.org/abs/2209.08248)|**[link](https://github.com/stanford-navlab/planeslam)**|
|**2022-09-16**|**ViWiD: Leveraging WiFi for Robust and Resource-Efficient SLAM**|Aditya Arun et.al.|[2209.08091](http://arxiv.org/abs/2209.08091)|null|
|**2022-09-16**|**iDF-SLAM: End-to-End RGB-D SLAM with Neural Implicit Mapping and Deep Feature Tracking**|Yuhang Ming et.al.|[2209.07919](http://arxiv.org/abs/2209.07919)|null|
|**2022-09-16**|**TwistSLAM++: Fusing multiple modalities for accurate dynamic semantic SLAM**|Mathieu Gonzalez et.al.|[2209.07888](http://arxiv.org/abs/2209.07888)|null|
|**2022-09-15**|**Landmark Management in the Application of Radar SLAM**|Shuai Sun et.al.|[2209.07199](http://arxiv.org/abs/2209.07199)|**[link](https://github.com/shuai000/slam_landmarkmanagement)**|
|**2022-09-15**|**PROB-SLAM: Real-time Visual SLAM Based on Probabilistic Graph Optimization**|Xianwei Meng et.al.|[2209.07061](http://arxiv.org/abs/2209.07061)|null|
|**2022-09-14**|**Semantic Visual Simultaneous Localization and Mapping: A Survey**|Kaiqi Chen et.al.|[2209.06428](http://arxiv.org/abs/2209.06428)|null|
|**2022-09-13**|**Optimizing SLAM Evaluation Footprint Through Dynamic Range Coverage Analysis of Datasets**|Islam Ali et.al.|[2209.06316](http://arxiv.org/abs/2209.06316)|null|
|**2022-09-12**|**A Review on Visual-SLAM: Advancements from Geometric Modelling to Learning-based Semantic Scene Understanding**|Tin Lai et.al.|[2209.05222](http://arxiv.org/abs/2209.05222)|null|
|**2022-09-12**|**Attitude-Guided Loop Closure for Cameras with Negative Plane**|Ze Wang et.al.|[2209.05167](http://arxiv.org/abs/2209.05167)|**[link](https://github.com/flysoaryun/lf-vio-loop)**|
|**2022-09-09**|**General Place Recognition Survey: Towards the Real-world Autonomy Age**|Peng Yin et.al.|[2209.04497](http://arxiv.org/abs/2209.04497)|**[link](https://github.com/MetaSLAM/GPRS)**|
|**2022-09-08**|**ExplORB-SLAM: Active Visual SLAM Exploiting the Pose-graph Topology**|Julio A. Placed et.al.|[2209.03693](http://arxiv.org/abs/2209.03693)|**[link](https://github.com/julioplaced/explorb-slam)**|
|**2022-09-08**|**R $^3$ LIVE++: A Robust, Real-time, Radiance reconstruction package with a tightly-coupled LiDAR-Inertial-Visual state Estimator**|Jiarong Lin et.al.|[2209.03666](http://arxiv.org/abs/2209.03666)|**[link](https://github.com/hku-mars/r3live)**|
|**2022-09-06**|**Group- $k$ Consistent Measurement Set Maximization for Robust Outlier Detection**|Brendon Forsgren et.al.|[2209.02658](http://arxiv.org/abs/2209.02658)|**[link](https://bitbucket.org/jmangelson/gkcm)**|
|**2022-09-05**|**Neuromorphic Visual Odometry with Resonator Networks**|Alpha Renner et.al.|[2209.02000](http://arxiv.org/abs/2209.02000)|null|
|**2022-09-05**|**MuCaSLAM: CNN-Based Frame Quality Assessment for Mobile Robot with Omnidirectional Visual SLAM**|Pavel Karpyshev et.al.|[2209.01936](http://arxiv.org/abs/2209.01936)|null|
|**2022-09-05**|**ElasticROS: An Elastically Collaborative Robot Operation System for Fog and Cloud Robotics**|Boyi Liu et.al.|[2209.01774](http://arxiv.org/abs/2209.01774)|null|
|**2022-09-04**|**CloudVision: DNN-based Visual Localization of Autonomous Robots using Prebuilt LiDAR Point Cloud**|Evgeny Yudin et.al.|[2209.01605](http://arxiv.org/abs/2209.01605)|null|
|**2022-08-31**|**PFilter: Building Persistent Maps through Feature Filtering for Fast and Accurate LiDAR-based SLAM**|Yifan Duan et.al.|[2208.14848](http://arxiv.org/abs/2208.14848)|null|
|**2022-08-30**|**BioSLAM: A Bio-inspired Lifelong Memory System for General Place Recognition**|Peng Yin et.al.|[2208.14543](http://arxiv.org/abs/2208.14543)|null|
|**2022-08-27**|**Learning to SLAM on the Fly in Unknown Environments: A Continual Learning Approach for Drones in Visually Ambiguous Scenes**|Ali Safa et.al.|[2208.12997](http://arxiv.org/abs/2208.12997)|null|
|**2022-08-25**|**FusionPortable: A Multi-Sensor Campus-Scene Dataset for Evaluation of Localization and Mapping Accuracy on Diverse Platforms**|Jianhao Jiao et.al.|[2208.11865](http://arxiv.org/abs/2208.11865)|null|
|**2022-08-25**|**Lidar SLAM for Autonomous Driving Vehicles**|Farhad Aghili et.al.|[2208.11855](http://arxiv.org/abs/2208.11855)|null|
|**2022-08-24**|**DynaVINS: A Visual-Inertial SLAM for Dynamic Environments**|Seungwon Song et.al.|[2208.11500](http://arxiv.org/abs/2208.11500)|**[link](https://github.com/url-kaist/dynavins)**|
|**2022-08-22**|**Doppler Exploitation in Bistatic mmWave Radio SLAM**|Yu Ge et.al.|[2208.10204](http://arxiv.org/abs/2208.10204)|null|
|**2022-08-21**|**Hilti-Oxford Dataset: A Millimetre-Accurate Benchmark for Simultaneous Localization and Mapping**|Lintong Zhang et.al.|[2208.09825](http://arxiv.org/abs/2208.09825)|**[link](https://github.com/hilti-research/hilti-slam-challenge-2022)**|
|**2022-08-26**|**JVLDLoc: a Joint Optimization of Visual-LiDAR Constraints and Direction Priors for Localization in Driving Scenario**|Longrui Dong et.al.|[2208.09777](http://arxiv.org/abs/2208.09777)|null|
|**2022-08-15**|**BoW3D: Bag of Words for Real-time Loop Closing in 3D LiDAR SLAM**|Yunge Cui et.al.|[2208.07473](http://arxiv.org/abs/2208.07473)|**[link](https://github.com/yungecui/bow3d)**|
|**2022-08-12**|**Handling Constrained Optimization in Factor Graphs for Autonomous Navigation**|Barbara Bazzana et.al.|[2208.06325](http://arxiv.org/abs/2208.06325)|null|
|**2022-08-11**|**RelPose: Predicting Probabilistic Relative Rotation for Single Objects in the Wild**|Jason Y. Zhang et.al.|[2208.05963](http://arxiv.org/abs/2208.05963)|null|
|**2022-08-08**|**Visual-Inertial Multi-Instance Dynamic SLAM with Object-level Relocalisation**|Yifei Ren et.al.|[2208.04274](http://arxiv.org/abs/2208.04274)|**[link](https://github.com/smartroboticslab/vimid)**|
|**2022-08-08**|**SLAM-TKA: Real-time Intra-operative Measurement of Tibial Resection Plane in Conventional Total Knee Arthroplasty**|Shuai Zhang et.al.|[2208.03945](http://arxiv.org/abs/2208.03945)|**[link](https://github.com/zsustc/calibration)**|
|**2022-08-05**|**A Survey on Visual Map Localization Using LiDARs and Cameras**|Elhousni Mahdi et.al.|[2208.03376](http://arxiv.org/abs/2208.03376)|null|
|**2022-08-04**|**SROS2: Usable Cyber Security Tools for ROS 2**|Victor Mayoral Vilches et.al.|[2208.02615](http://arxiv.org/abs/2208.02615)|**[link](https://github.com/ros-swg/turtlebot3_demo)**|
|**2022-08-03**|**Evaluation and comparison of eight popular Lidar and Visual SLAM algorithms**|Bharath Garigipati et.al.|[2208.02063](http://arxiv.org/abs/2208.02063)|null|
|**2022-08-02**|**Present and Future of SLAM in Extreme Underground Environments**|Kamak Ebadi et.al.|[2208.01787](http://arxiv.org/abs/2208.01787)|null|
|**2022-08-01**|**Visual-Inertial SLAM with Tightly-Coupled Dropout-Tolerant GPS Fusion**|Simon Boche et.al.|[2208.00709](http://arxiv.org/abs/2208.00709)|null|
|**2022-07-29**|**Neural Density-Distance Fields**|Itsuki Ueda et.al.|[2207.14455](http://arxiv.org/abs/2207.14455)|**[link](https://github.com/ueda0319/neddf)**|
|**2022-07-25**|**DeepFusion: Real-Time Dense 3D Reconstruction for Monocular SLAM using Single-View Depth and Gradient Predictions**|Tristan Laidlow et.al.|[2207.12244](http://arxiv.org/abs/2207.12244)|null|
|**2022-07-25**|**Scalable Fiducial Tag Localization on a 3D Prior Map via Graph-Theoretic Global Tag-Map Registration**|Kenji Koide et.al.|[2207.11942](http://arxiv.org/abs/2207.11942)|null|
|**2022-07-22**|**NeurAR: Neural Uncertainty for Autonomous 3D Reconstruction**|Yunlong Ran et.al.|[2207.10985](http://arxiv.org/abs/2207.10985)|null|
|**2022-07-22**|**Dense RGB-D-Inertial SLAM with Map Deformations**|Tristan Laidlow et.al.|[2207.10940](http://arxiv.org/abs/2207.10940)|null|
|**2022-07-22**|**PLD-SLAM: A Real-Time Visual SLAM Using Points and Line Segments in Dynamic Scenes**|BaoSheng Zhang et.al.|[2207.10916](http://arxiv.org/abs/2207.10916)|null|
|**2022-07-21**|**Multi-Event-Camera Depth Estimation and Outlier Rejection by Refocused Events Fusion**|Suman Ghosh et.al.|[2207.10494](http://arxiv.org/abs/2207.10494)|**[link](https://github.com/tub-rip/dvs_mcemvs)**|
|**2022-07-21**|**Online Localisation and Colored Mesh Reconstruction Architecture for 3D Visual Feedback in Robotic Exploration Missions**|Quentin Serdel et.al.|[2207.10489](http://arxiv.org/abs/2207.10489)|**[link](https://github.com/onera/olcmr)**|
|**2022-07-21**|**On applicability of von Karman's momentum theory in predicting the water entry load of V-shaped structures with varying initial velocity**|Yujin Lu et.al.|[2207.10413](http://arxiv.org/abs/2207.10413)|null|
|**2022-07-19**|**Hybrid Belief Pruning with Guarantees for Viewpoint-Dependent Semantic SLAM**|Tuvy Lemberg et.al.|[2207.09103](http://arxiv.org/abs/2207.09103)|null|
|**2022-07-18**|**DeFlowSLAM: Self-Supervised Scene Motion Decomposition for Dynamic Dense SLAM**|Weicai Ye et.al.|[2207.08794](http://arxiv.org/abs/2207.08794)|**[link](https://github.com/zju3dv/DeFlowSLAM)**|
|**2022-07-18**|**Revisiting PatchMatch Multi-View Stereo for Urban 3D Reconstruction**|Marco Orsingher et.al.|[2207.08439](http://arxiv.org/abs/2207.08439)|null|
|**2022-07-18**|**ORB-based SLAM accelerator on SoC FPGA**|Vibhakar Vemulapati et.al.|[2207.08405](http://arxiv.org/abs/2207.08405)|null|
|**2022-07-14**|**Challenges of SLAM in extremely unstructured environments: the DLR Planetary Stereo, Solid-State LiDAR, Inertial Dataset**|Riccardo Giubilato et.al.|[2207.06815](http://arxiv.org/abs/2207.06815)|null|
|**2022-07-14**|**Semi-supervised Vector-Quantization in Visual SLAM using HGCN**|Amir Zarringhalam et.al.|[2207.06738](http://arxiv.org/abs/2207.06738)|null|
|**2022-07-14**|**Self-supervised Vector-Quantization in Visual SLAM using Deep Convolutional Autoencoders**|Amir Zarringhalam et.al.|[2207.06732](http://arxiv.org/abs/2207.06732)|null|
|**2022-07-13**|**SLAM: SLO-Aware Memory Optimization for Serverless Applications**|Gor Safaryan et.al.|[2207.06183](http://arxiv.org/abs/2207.06183)|null|
|**2022-07-19**|**Structure PLP-SLAM: Efficient Sparse Mapping and Localization using Point, Line and Plane for Monocular, RGB-D and Stereo Cameras**|Fangwen Shu et.al.|[2207.06058](http://arxiv.org/abs/2207.06058)|**[link](https://github.com/peterfws/structure-plp-slam)**|
|**2022-07-12**|**Accelerating Certifiable Estimation with Preconditioned Eigensolvers**|David M. Rosen et.al.|[2207.05257](http://arxiv.org/abs/2207.05257)|null|
|**2022-07-12**|**Robust Key-Frame Stereo Visual SLAM with low-threshold Point and Line Features**|Meiyu Zhi et.al.|[2207.05244](http://arxiv.org/abs/2207.05244)|null|
|**2022-07-14**|**SLAM Backends with Objects in Motion: A Unifying Framework and Tutorial**|Chih-Yuan Chiu et.al.|[2207.05043](http://arxiv.org/abs/2207.05043)|null|
|**2022-07-08**|**BlindSpotNet: Seeing Where We Cannot See**|Taichi Fukuda et.al.|[2207.03870](http://arxiv.org/abs/2207.03870)|null|
|**2022-07-08**|**Continuous Target-free Extrinsic Calibration of a Multi-Sensor System from a Sequence of Static Viewpoints**|Philipp Glira et.al.|[2207.03785](http://arxiv.org/abs/2207.03785)|null|
|**2022-07-08**|**Distributed Ranging SLAM for Multiple Robots with Ultra-WideBand and Odometry Measurements**|Ran Liu et.al.|[2207.03700](http://arxiv.org/abs/2207.03700)|null|
|**2022-07-07**|**RWT-SLAM: Robust Visual SLAM for Highly Weak-textured Environments**|Qihao Peng et.al.|[2207.03539](http://arxiv.org/abs/2207.03539)|null|
|**2022-07-06**|**VI-SLAM2tag: Low-Effort Labeled Dataset Collection for Fingerprinting-Based Indoor Localization**|Marius Laska et.al.|[2207.02668](http://arxiv.org/abs/2207.02668)|null|
|**2022-07-06**|**A Novel Hybrid Endoscopic Dataset for Evaluating Machine Learning-based Photometric Image Enhancement Models**|Axel Garcia-Vega et.al.|[2207.02396](http://arxiv.org/abs/2207.02396)|null|
|**2022-07-04**|**VECtor: A Versatile Event-Centric Benchmark for Multi-Sensor SLAM**|Ling Gao et.al.|[2207.01404](http://arxiv.org/abs/2207.01404)|null|
|**2022-07-04**|**VIP-SLAM: An Efficient Tightly-Coupled RGB-D Visual Inertial Planar SLAM**|Danpeng Chen et.al.|[2207.01158](http://arxiv.org/abs/2207.01158)|null|
|**2022-07-03**|**Wireless Channel Prediction in Partially Observed Environments**|Mingsheng Yin et.al.|[2207.00934](http://arxiv.org/abs/2207.00934)|null|
|**2022-07-01**|**A Survey on Active Simultaneous Localization and Mapping: State of the Art and New Frontiers**|Julio A. Placed et.al.|[2207.00254](http://arxiv.org/abs/2207.00254)|null|
|**2022-07-01**|**Keeping Less is More: Point Sparsification for Visual SLAM**|Yeonsoo Park et.al.|[2207.00225](http://arxiv.org/abs/2207.00225)|null|
|**2022-06-30**|**Controlled and impulsive compression of an entrapped air bubble during impact**|Utkarsh Jain et.al.|[2206.15297](http://arxiv.org/abs/2206.15297)|null|
|**2022-06-30**|**Neural Rendering for Stereo 3D Reconstruction of Deformable Tissues in Robotic Surgery**|Yuehao Wang et.al.|[2206.15255](http://arxiv.org/abs/2206.15255)|**[link](https://github.com/med-air/endonerf)**|
|**2022-06-27**|**IBISCape: A Simulated Benchmark for multi-modal SLAM Systems Evaluation in Large-scale Dynamic Environments**|Abanob Soliman et.al.|[2206.13455](http://arxiv.org/abs/2206.13455)|**[link](https://github.com/AbanobSoliman/IBISCape)**|
|**2022-06-26**|**An Efficient Global Optimality Certificate for Landmark-Based SLAM**|Connor Holmes et.al.|[2206.12961](http://arxiv.org/abs/2206.12961)|**[link](https://github.com/holmesco/se-sync-landmarks)**|
|**2022-06-21**|**Object Structural Points Representation for Graph-based Semantic Monocular Localization and Mapping**|Davide Tateo et.al.|[2206.10263](http://arxiv.org/abs/2206.10263)|**[link](https://github.com/airlab-polimi/c-slam)**|
|**2022-06-20**|**Data Fusion for Radio Frequency SLAM with Robust Sampling**|Erik Leitinger et.al.|[2206.09746](http://arxiv.org/abs/2206.09746)|null|
|**2022-06-19**|**RF-LIO: Removal-First Tightly-coupled Lidar Inertial Odometry in High Dynamic Environments**|Chenglong Qian et.al.|[2206.09463](http://arxiv.org/abs/2206.09463)|null|
|**2022-06-17**|**Efficient WiFi LiDAR SLAM for Autonomous Robots in Large Environments**|Khairuldanial Ismail et.al.|[2206.08733](http://arxiv.org/abs/2206.08733)|null|
|**2022-06-17**|**An Algorithm for the SE(3)-Transformation on Neural Implicit Maps for Remapping Functions**|Yijun Yuan et.al.|[2206.08712](http://arxiv.org/abs/2206.08712)|**[link](https://github.com/jarrome/imt_mapping)**|
|**2022-06-13**|**ICP Algorithm: Theory, Practice And Its SLAM-oriented Taxonomy**|Hao Bai et.al.|[2206.06435](http://arxiv.org/abs/2206.06435)|null|
|**2022-06-10**|**Experimental Evaluation of Visual-Inertial Odometry Systems for Arable Farming**|Javier Cremona et.al.|[2206.05066](http://arxiv.org/abs/2206.05066)|**[link](https://github.com/cifasis/slam_agricultural_evaluation)**|
|**2022-06-09**|**SparseFormer: Attention-based Depth Completion Network**|Frederik Warburg et.al.|[2206.04557](http://arxiv.org/abs/2206.04557)|null|
|**2022-06-07**|**Robot Self-Calibration Using Actuated 3D Sensors**|Arne Peters et.al.|[2206.03430](http://arxiv.org/abs/2206.03430)|null|
|**2022-06-07**|**Object Scan Context: Object-centric Spatial Descriptor for Place Recognition within 3D Point Cloud Map**|Haodong Yuan et.al.|[2206.03062](http://arxiv.org/abs/2206.03062)|null|
|**2022-06-05**|**DarkSLAM: GAN-assisted Visual SLAM for Reliable Operation in Low-light Conditions**|Alena Savinykh et.al.|[2206.02199](http://arxiv.org/abs/2206.02199)|null|
|**2022-06-04**|**C $^3$ Fusion: Consistent Contrastive Colon Fusion, Towards Deep SLAM in Colonoscopy**|Erez Posner et.al.|[2206.01961](http://arxiv.org/abs/2206.01961)|null|
|**2022-06-01**|**PaGO-LOAM: Robust Ground-Optimized LiDAR Odometry**|Dong-Uk Seo et.al.|[2206.00266](http://arxiv.org/abs/2206.00266)|**[link](https://github.com/url-kaist/alterground-lego-loam)**|
|**2022-05-27**|**A Look at Improving Robustness in Visual-inertial SLAM by Moment Matching**|Arno Solin et.al.|[2205.13821](http://arxiv.org/abs/2205.13821)|null|
|**2022-05-31**|**LAMP 2.0: A Robust Multi-Robot SLAM System for Operation in Challenging Large-Scale Underground Environments**|Yun Chang et.al.|[2205.13135](http://arxiv.org/abs/2205.13135)|**[link](https://github.com/nebula-autonomy/nebula-multirobot-dataset)**|
|**2022-05-25**|**Wildcat: Online Continuous-Time 3D Lidar-Inertial SLAM**|Milad Ramezani et.al.|[2205.12595](http://arxiv.org/abs/2205.12595)|null|
|**2022-05-24**|**Loop Closure Prioritization for Efficient and Scalable Multi-Robot SLAM**|Christopher E. Denniston et.al.|[2205.12402](http://arxiv.org/abs/2205.12402)|**[link](https://github.com/nebula-autonomy/lamp)**|
|**2022-05-22**|**ALITA: A Large-scale Incremental Dataset for Long-term Autonomy**|Peng Yin et.al.|[2205.10737](http://arxiv.org/abs/2205.10737)|**[link](https://github.com/metaslam/alita)**|
|**2022-05-19**|**FogROS 2: An Adaptive and Extensible Platform for Cloud and Fog Robotics Using ROS 2**|Jeffrey Ichnowski et.al.|[2205.09778](http://arxiv.org/abs/2205.09778)|**[link](https://github.com/BerkeleyAutomation/FogROS2)**|
|**2022-05-17**|**Global Data Association for SLAM with 3D Grassmannian Manifold Objects**|Parker C. Lusk et.al.|[2205.08556](http://arxiv.org/abs/2205.08556)|null|
|**2022-05-19**|**Cluster on Wheels**|Yuanyuan Yang et.al.|[2205.08151](http://arxiv.org/abs/2205.08151)|null|
|**2022-05-12**|**Dynamic Dense RGB-D SLAM using Learning-based Visual Odometry**|Shihao Shen et.al.|[2205.05916](http://arxiv.org/abs/2205.05916)|**[link](https://github.com/geniussh/dynamic-dense-rgbd-slam-with-tartanvo)**|
|**2022-05-12**|**S3E-GNN: Sparse Spatial Scene Embedding with Graph Neural Networks for Camera Relocalization**|Ran Cheng et.al.|[2205.05861](http://arxiv.org/abs/2205.05861)|null|
|**2022-05-14**|**Multi-modal Semantic SLAM for Complex Dynamic Environments**|Han Wang et.al.|[2205.04300](http://arxiv.org/abs/2205.04300)|**[link](https://github.com/wh200720041/mms_slam)**|
|**2022-05-06**|**OROS: Orchestrating ROS-driven Collaborative Connected Robots in Mission-Critical Operations**|Carmen Delgado et.al.|[2205.03256](http://arxiv.org/abs/2205.03256)|null|
|**2022-05-05**|**CNN-Augmented Visual-Inertial SLAM with Planar Constraints**|Pan Ji et.al.|[2205.02940](http://arxiv.org/abs/2205.02940)|null|
|**2022-05-05**|**PMBM-based SLAM Filters in 5G mmWave Vehicular Networks**|Hyowon Kim et.al.|[2205.02502](http://arxiv.org/abs/2205.02502)|null|
|**2022-05-04**|**BodySLAM: Joint Camera Localisation, Mapping, and Human Motion Tracking**|Dorian Henning et.al.|[2205.02301](http://arxiv.org/abs/2205.02301)|null|
|**2022-05-04**|**A Global Asymptotic Convergent Observer for SLAM**|Seyed Hamed Hashemi et.al.|[2205.01953](http://arxiv.org/abs/2205.01953)|null|
|**2022-05-04**|**Symmetry and Uncertainty-Aware Object SLAM for 6DoF Object Pose Estimation**|Nathaniel Merrill et.al.|[2205.01823](http://arxiv.org/abs/2205.01823)|**[link](https://github.com/rpng/suo_slam)**|
|**2022-05-03**|**GeoRefine: Self-Supervised Online Depth Refinement for Accurate Dense Mapping**|Pan Ji et.al.|[2205.01656](http://arxiv.org/abs/2205.01656)|null|
|**2022-04-29**|**Struct-MDC: Mesh-Refined Unsupervised Depth Completion Leveraging Structural Regularities from Visual SLAM**|Jinwoo Jeon et.al.|[2204.13877](http://arxiv.org/abs/2204.13877)|**[link](https://github.com/url-kaist/Struct-MDC)**|
|**2022-04-27**|**The Revisiting Problem in Simultaneous Localization and Mapping: A Survey on Visual Loop Closure Detection**|Konstantinos A. Tsintotas et.al.|[2204.12831](http://arxiv.org/abs/2204.12831)|null|
|**2022-04-27**|**Dynamic Registration: Joint Ego Motion Estimation and 3D Moving Object Detection in Dynamic Environment**|Wenyu Li et.al.|[2204.12769](http://arxiv.org/abs/2204.12769)|null|
|**2022-04-29**|**MLO: Multi-Object Tracking and Lidar Odometry in Dynamic Environment**|Tingchen Ma et.al.|[2204.11621](http://arxiv.org/abs/2204.11621)|null|
|**2022-04-23**|**Indoor simultaneous localization and mapping based on fringe projection profilometry**|Yang Zhao et.al.|[2204.11020](http://arxiv.org/abs/2204.11020)|null|
|**2022-04-22**|**Enough is Enough: Towards Autonomous Uncertainty-driven Stopping Criteria**|Julio A. Placed et.al.|[2204.10631](http://arxiv.org/abs/2204.10631)|null|
|**2022-04-22**|**Fast Autonomous Robotic Exploration Using the Underlying Graph Structure**|Julio A. Placed et.al.|[2204.10610](http://arxiv.org/abs/2204.10610)|null|
|**2022-04-22**|**Making Parameterization and Constrains of Object Landmark Globally Consistent via SPD(3) Manifold and Improved Cost Functions**|Yutong Hu et.al.|[2204.10552](http://arxiv.org/abs/2204.10552)|null|
|**2022-04-22**|**Implicit Object Mapping With Noisy Data**|Jad Abou-Chakra et.al.|[2204.10516](http://arxiv.org/abs/2204.10516)|**[link](https://github.com/jc211/implicit_object_reconstruction_dataset)**|
|**2022-04-19**|**Photometric single-view dense 3D reconstruction in endoscopy**|Victor M. Batlle et.al.|[2204.09083](http://arxiv.org/abs/2204.09083)|null|
|**2022-04-18**|**Pulsar skips: Understanding variations in the regular periods of rotating neutron stars**|Clayton Miller et.al.|[2204.08449](http://arxiv.org/abs/2204.08449)|null|
|**2022-04-18**|**Tracking monocular camera pose and deformation for SLAM inside the human body**|Juan J. Gomez Rodriguez et.al.|[2204.08309](http://arxiv.org/abs/2204.08309)|null|
|**2022-04-18**|**Mapping While Following: 2D LiDAR SLAM in Indoor Dynamic Environments with a Person Tracker**|Hanjing Ye et.al.|[2204.08163](http://arxiv.org/abs/2204.08163)|null|
|**2022-04-14**|**ViViD++: Vision for Visibility Dataset**|Alex Junho Lee et.al.|[2204.06183](http://arxiv.org/abs/2204.06183)|null|
|**2022-04-12**|**HiTPR: Hierarchical Transformer for Place Recognition in Point Cloud**|Zhixing Hou et.al.|[2204.05481](http://arxiv.org/abs/2204.05481)|null|
|**2022-04-12**|**RGB-D Semantic SLAM for Surgical Robot Navigation in the Operating Room**|Cong Gao et.al.|[2204.05467](http://arxiv.org/abs/2204.05467)|null|
|**2022-04-11**|**Optimized SC-F-LOAM: Optimized Fast LiDAR Odometry and Mapping Using Scan Context**|Lizhou Liao et.al.|[2204.04932](http://arxiv.org/abs/2204.04932)|**[link](https://github.com/SlamCabbage/Optimized-SC-F-LOAM)**|
|**2022-04-04**|**Monitoring social distancing with single image depth estimation**|Alessio Mingozzi et.al.|[2204.01693](http://arxiv.org/abs/2204.01693)|null|
|**2022-04-01**|**Bi-directional Loop Closure for Visual SLAM**|Ihtisham Ali et.al.|[2204.01524](http://arxiv.org/abs/2204.01524)|null|
|**2022-04-04**|**IMOT: General-Purpose, Fast and Robust Estimation for Spatial Perception Problems with Outliers**|Lei Sun et.al.|[2204.01324](http://arxiv.org/abs/2204.01324)|**[link](https://github.com/leisun-98/tivm-master)**|
|**2022-04-03**|**Indoor Navigation Assistance for Visually Impaired People via Dynamic SLAM and Panoptic Segmentation with an RGB-D Sensor**|Wenyan Ou et.al.|[2204.01154](http://arxiv.org/abs/2204.01154)|null|
|**2022-04-02**|**UrbanFly: Uncertainty-Aware Planning for Navigation Amongst High-Rises with Monocular Visual-Inertial SLAM Maps**|Ayyappa Swamy Thatavarthy et.al.|[2204.00865](http://arxiv.org/abs/2204.00865)|**[link](https://github.com/sudarshan-s-harithas/urbanfly)**|
|**2022-03-31**|**Curiosity Driven Self-supervised Tactile Exploration of Unknown Objects**|Yujie Lu et.al.|[2204.00035](http://arxiv.org/abs/2204.00035)|null|
|**2022-03-30**|**GTP-SLAM: Game-Theoretic Priors for Simultaneous Localization and Mapping in Multi-Agent Scenarios**|Chih-Yuan Chiu et.al.|[2203.16690](http://arxiv.org/abs/2203.16690)|null|
|**2022-03-29**|**Indoor SLAM Using a Foot-mounted IMU and the local Magnetic Field**|Mostafa Osman et.al.|[2203.15866](http://arxiv.org/abs/2203.15866)|null|
|**2022-03-29**|**Eventor: An Efficient Event-Based Monocular Multi-View Stereo Accelerator on FPGA Platform**|Mingjun Li et.al.|[2203.15439](http://arxiv.org/abs/2203.15439)|null|
|**2022-03-29**|**Sparse Image based Navigation Architecture to Mitigate the need of precise Localization in Mobile Robots**|Pranay Mathur et.al.|[2203.15272](http://arxiv.org/abs/2203.15272)|null|
|**2022-03-28**|**Are High-Resolution Event Cameras Really Needed?**|Daniel Gehrig et.al.|[2203.14672](http://arxiv.org/abs/2203.14672)|null|
|**2022-03-25**|**Spectral Measurement Sparsification for Pose-Graph SLAM**|Kevin J. Doherty et.al.|[2203.13897](http://arxiv.org/abs/2203.13897)|**[link](https://github.com/MarineRoboticsGroup/mac)**|
|**2022-03-25**|**FD-SLAM: 3-D Reconstruction Using Features and Dense Matching**|Xingrui Yang et.al.|[2203.13861](http://arxiv.org/abs/2203.13861)|null|
|**2022-03-25**|**Gravity-constrained point cloud registration**|Vladimír Kubelka et.al.|[2203.13799](http://arxiv.org/abs/2203.13799)|null|
|**2022-03-24**|**MD-SLAM: Multi-cue Direct SLAM**|Luca Di Giammarino et.al.|[2203.13237](http://arxiv.org/abs/2203.13237)|**[link](https://github.com/digiamm/md_slam)**|
|**2022-03-24**|**Unsupervised Simultaneous Learning for Camera Re-Localization and Depth Estimation from Video**|Shun Taguchi et.al.|[2203.12804](http://arxiv.org/abs/2203.12804)|null|
|**2022-03-19**|**Hybrid Active and Passive Sensing for SLAM in Wireless Communication Systems**|Jie Yang et.al.|[2203.10267](http://arxiv.org/abs/2203.10267)|null|
|**2022-03-16**|**Any Way You Look At It: Semantic Crossview Localization and Mapping with LiDAR**|Ian D. Miller et.al.|[2203.08925](http://arxiv.org/abs/2203.08925)|**[link](https://github.com/iandouglas96/cross_view_slam)**|
|**2022-03-15**|**Neural RF SLAM for unsupervised positioning and mapping with channel state information**|Shreya Kadambi et.al.|[2203.08264](http://arxiv.org/abs/2203.08264)|null|
|**2022-03-15**|**Simultaneous Localisation and Mapping with Quadric Surfaces**|Tristan Laidlow et.al.|[2203.08040](http://arxiv.org/abs/2203.08040)|null|
|**2022-03-14**|**Drift Reduced Navigation with Deep Explainable Features**|Mohd Omama et.al.|[2203.06897](http://arxiv.org/abs/2203.06897)|**[link](https://github.com/mohdomama/drndef)**|
|**2022-03-11**|**An Efficient Accelerator for Deep Learning-based Point Cloud Registration on FPGAs**|Keisuke Sugiura et.al.|[2203.05763](http://arxiv.org/abs/2203.05763)|null|
|**2022-03-10**|**High Definition, Inexpensive, Underwater Mapping**|Bharat Joshi et.al.|[2203.05640](http://arxiv.org/abs/2203.05640)|**[link](https://github.com/autonomousfieldroboticslab/gopro_ros)**|
|**2022-03-10**|**SelfTune: Metrically Scaled Monocular Depth Estimation through Self-Supervised Learning**|Jaehoon Choi et.al.|[2203.05332](http://arxiv.org/abs/2203.05332)|null|
|**2022-03-08**|**Tune your Place Recognition: Self-Supervised Domain Calibration via Robust SLAM**|Pierre-Yves Lajoie et.al.|[2203.04446](http://arxiv.org/abs/2203.04446)|**[link](https://github.com/mistlab/vpr-calibration-and-uncertainty)**|
|**2022-03-08**|**SLAM-Supported Self-Training for 6D Object Pose Estimation**|Ziqi Lu et.al.|[2203.04424](http://arxiv.org/abs/2203.04424)|**[link](https://github.com/520xyxyzq/slam-super-6d)**|
|**2022-03-08**|**An Online Semantic Mapping System for Extending and Enhancing Visual SLAM**|Thorsten Hempel et.al.|[2203.03944](http://arxiv.org/abs/2203.03944)|null|
|**2022-03-07**|**Multi-Modal Lidar Dataset for Benchmarking General-Purpose Localization and Mapping Algorithms**|Qingqing Li et.al.|[2203.03454](http://arxiv.org/abs/2203.03454)|**[link](https://github.com/tiers/tiers-lidars-dataset)**|
|**2022-03-07**|**OverlapTransformer: An Efficient and Rotation-Invariant Transformer Network for LiDAR-Based Place Recognition**|Junyi Ma et.al.|[2203.03397](http://arxiv.org/abs/2203.03397)|**[link](https://github.com/haomo-ai/OverlapTransformer)**|
|**2022-03-06**|**Minimum Cost Multicuts for Incorrect Landmark Edge Detection in Pose-graph SLAM**|Kazushi Aiba et.al.|[2203.02887](http://arxiv.org/abs/2203.02887)|null|
|**2022-03-06**|**RGB-D SLAM in Indoor Planar Environments with Multiple Large Dynamic Objects**|Ran Long et.al.|[2203.02882](http://arxiv.org/abs/2203.02882)|null|
|**2022-03-03**|**STUN: Self-Teaching Uncertainty Estimation for Place Recognition**|Kaiwen Cai et.al.|[2203.01851](http://arxiv.org/abs/2203.01851)|**[link](https://github.com/ramdrop/stun)**|
|**2022-03-03**|**Continual SLAM: Beyond Lifelong Simultaneous Localization and Mapping through Continual Learning**|Niclas Vödisch et.al.|[2203.01578](http://arxiv.org/abs/2203.01578)|**[link](https://github.com/robot-learning-freiburg/CL-SLAM)**|
|**2022-03-02**|**FAST-LIVO: Fast and Tightly-coupled Sparse-Direct LiDAR-Inertial-Visual Odometry**|Chunran Zheng et.al.|[2203.00893](http://arxiv.org/abs/2203.00893)|**[link](https://github.com/hku-mars/fast-livo)**|
|**2022-03-02**|**Distributed Riemannian Optimization with Lazy Communication for Collaborative Geometric Estimation**|Yulun Tian et.al.|[2203.00851](http://arxiv.org/abs/2203.00851)|null|
|**2022-03-01**|**Descriptellation: Deep Learned Constellation Descriptors for SLAM**|Chunwei Xing et.al.|[2203.00567](http://arxiv.org/abs/2203.00567)|null|
|**2022-03-01**|**Collaborative Robot Mapping using Spectral Graph Analysis**|Lukas Bernreiter et.al.|[2203.00308](http://arxiv.org/abs/2203.00308)|null|
|**2022-02-26**|**RL-PGO: Reinforcement Learning-based Planar Pose-Graph Optimization**|Nikolaos Kourtzanidis et.al.|[2202.13221](http://arxiv.org/abs/2202.13221)|**[link](https://github.com/Nick-Kou/RL-PGO)**|
|**2022-02-25**|**Probabilistic Data Association for Semantic SLAM at Scale**|Elad Michael et.al.|[2202.12802](http://arxiv.org/abs/2202.12802)|**[link](https://github.com/eladmichael/probabilisticsemslam)**|
|**2022-02-24**|**TwistSLAM: Constrained SLAM in Dynamic Environment**|Mathieu Gonzalez et.al.|[2202.12384](http://arxiv.org/abs/2202.12384)|null|
|**2022-02-24**|**Light Robust Monocular Depth Estimation For Outdoor Environment Via Monochrome And Color Camera Fusion**|Hyeonsoo Jang et.al.|[2202.12108](http://arxiv.org/abs/2202.12108)|null|
|**2022-02-23**|**MITI: SLAM Benchmark for Laparoscopic Surgery**|Regine Hartwig et.al.|[2202.11496](http://arxiv.org/abs/2202.11496)|null|
|**2022-02-23**|**DL-SLOT: Dynamic Lidar SLAM and Object Tracking Based On Graph Optimization**|Xuebo Tian et.al.|[2202.11431](http://arxiv.org/abs/2202.11431)|null|
|**2022-02-23**|**Are We Ready for Robust and Resilient SLAM? A Framework For Quantitative Characterization of SLAM Datasets**|Islam Ali et.al.|[2202.11312](http://arxiv.org/abs/2202.11312)|null|
|**2022-02-22**|**SAGE: SLAM with Appearance and Geometry Prior for Endoscopy**|Xingtong Liu et.al.|[2202.09487](http://arxiv.org/abs/2202.09487)|**[link](https://github.com/lppllppl920/sage-slam)**|
|**2022-02-18**|**OKVIS2: Realtime Scalable Visual-Inertial SLAM with Loop Closure**|Stefan Leutenegger et.al.|[2202.09199](http://arxiv.org/abs/2202.09199)|null|
|**2022-02-18**|**MultiRes-NetVLAD: Augmenting Place Recognition Training with Low-Resolution Imagery**|Ahmad Khaliq et.al.|[2202.09146](http://arxiv.org/abs/2202.09146)|**[link](https://github.com/ahmedest61/multires-netvlad)**|
|**2022-02-18**|**An Energy-Efficient and Runtime-Reconfigurable FPGA-Based Accelerator for Robotic Localization Systems**|Qiang Liu et.al.|[2202.08952](http://arxiv.org/abs/2202.08952)|null|
|**2022-02-17**|**Continuous-Time vs. Discrete-Time Vision-based SLAM: A Comparative Study**|Giovanni Cioffi et.al.|[2202.08894](http://arxiv.org/abs/2202.08894)|**[link](https://github.com/uzh-rpg/rpg_vision-based_slam)**|
|**2022-02-17**|**LiDAR-Inertial 3D SLAM with Plane Constraint for Multi-story Building**|Jiashi Zhang et.al.|[2202.08487](http://arxiv.org/abs/2202.08487)|null|
|**2022-02-16**|**Virtual Maps for Autonomous Exploration of Cluttered Underwater Environments**|Jinkun Wang et.al.|[2202.08359](http://arxiv.org/abs/2202.08359)|null|
|**2022-02-11**|**Overhead Image Factors for Underwater Sonar-based SLAM**|John McConnell et.al.|[2202.05811](http://arxiv.org/abs/2202.05811)|null|
|**2022-02-10**|**Scale Estimation with Dual Quadrics for Monocular Object SLAM**|Shuangfu Song et.al.|[2202.04816](http://arxiv.org/abs/2202.04816)|null|
|**2022-02-08**|**A Novel Image Descriptor with Aggregated Semantic Skeleton Representation for Long-term Visual Place Recognition**|Nie Jiwei et.al.|[2202.03677](http://arxiv.org/abs/2202.03677)|null|
|**2022-01-25**|**Autonomous Vehicles: Open-Source Technologies, Considerations, and Development**|Oussama Saoudi et.al.|[2202.03148](http://arxiv.org/abs/2202.03148)|null|
|**2022-02-07**|**Temporal Point Cloud Completion with Pose Disturbance**|Jieqi Shi et.al.|[2202.03084](http://arxiv.org/abs/2202.03084)|null|
|**2022-02-04**|**DYP-SLAM: A Real-time Visual SLAM Based on YOLO and Probability in Dynamic Environments**|Xinggang Hu et.al.|[2202.01938](http://arxiv.org/abs/2202.01938)|null|
|**2022-02-01**|**A Model for Multi-View Residual Covariances based on Perspective Deformation**|Alejandro Fontan et.al.|[2202.00765](http://arxiv.org/abs/2202.00765)|null|
|**2022-01-30**|**Joint Vehicular Localization and Reflective Mapping Based on Team Channel-SLAM**|Xinghe Chu et.al.|[2201.12726](http://arxiv.org/abs/2201.12726)|null|
|**2022-01-28**|**RGB-D SLAM Using Attention Guided Frame Association**|Ali Caglayan et.al.|[2201.12047](http://arxiv.org/abs/2201.12047)|null|
|**2022-02-04**|**Learning to Act with Affordance-Aware Multimodal Neural SLAM**|Zhiwei Jia et.al.|[2201.09862](http://arxiv.org/abs/2201.09862)|**[link](https://github.com/amazon-research/multimodal-neuralslam)**|
|**2022-01-22**|**Phase-SLAM: Phase Based Simultaneous Localization and Mapping for Mobile Structured Light Illumination Systems**|Xi Zheng et.al.|[2201.09048](http://arxiv.org/abs/2201.09048)|**[link](https://github.com/zhengxi-git/phase-slam)**|
|**2022-01-17**|**SC-LiDAR-SLAM: a Front-end Agnostic Versatile LiDAR SLAM System**|Giseop Kim et.al.|[2201.06423](http://arxiv.org/abs/2201.06423)|null|
|**2022-01-14**|**SRVIO: Super Robust Visual Inertial Odometry for dynamic environments and challenging Loop-closure conditions**|Ali Samadzadeh et.al.|[2201.05386](http://arxiv.org/abs/2201.05386)|**[link](https://github.com/aa-samad/srvio)**|
|**2022-01-19**|**Multi-Hypothesis Scan Matching through Clustering**|Giorgio Iavicoli et.al.|[2201.03814](http://arxiv.org/abs/2201.03814)|null|
|**2022-01-11**|**Performance Guarantees for Spectral Initialization in Rotation Averaging and Pose-Graph SLAM**|Kevin J. Doherty et.al.|[2201.03773](http://arxiv.org/abs/2201.03773)|null|
|**2022-01-10**|**High-resolution Ecosystem Mapping in Repetitive Environments Using Dual Camera SLAM**|Brian M. Hopkinson et.al.|[2201.03364](http://arxiv.org/abs/2201.03364)|**[link](https://github.com/bmhopkinson/hyslam)**|
|**2022-01-10**|**Why-So-Deep: Towards Boosting Previously Trained Models for Visual Place Recognition**|M. Usman Maqbool Bhutta et.al.|[2201.03212](http://arxiv.org/abs/2201.03212)|**[link](https://github.com/UsmanMaqbool/why-so-deep)**|
|**2022-01-04**|**Formulations of Hydrodynamic Force in the Transition Stage of the Water Entry of Linear Wedges with Constant and Varying Speeds**|Xueliang Wen et.al.|[2201.00959](http://arxiv.org/abs/2201.00959)|null|
|**2021-12-29**|**Efficient Belief Space Planning in High-Dimensional State Spaces using PIVOT: Predictive Incremental Variable Ordering Tactic**|Khen Elimelech et.al.|[2112.14428](http://arxiv.org/abs/2112.14428)|null|
|**2021-12-19**|**M2DGR: A Multi-sensor and Multi-scenario SLAM Dataset for Ground Robots**|Jie Yin et.al.|[2112.13659](http://arxiv.org/abs/2112.13659)|**[link](https://github.com/SJTU-ViSYS/M2DGR)**|
|**2021-12-27**|**UV-SLAM: Unconstrained Line-based SLAM Using Vanishing Points for Structural Mapping**|Hyunjun Lim et.al.|[2112.13515](http://arxiv.org/abs/2112.13515)|**[link](https://github.com/url-kaist/uv-slam)**|
|**2021-12-25**|**Simultaneous Location of Rail Vehicles and Mapping of Environment with Multiple LiDARs**|Yusheng Wang et.al.|[2112.13224](http://arxiv.org/abs/2112.13224)|null|
|**2021-12-25**|**Edge Robotics: Edge-Computing-Accelerated Multi-Robot Simultaneous Localization and Mapping**|Peng Huang et.al.|[2112.13222](http://arxiv.org/abs/2112.13222)|null|
|**2021-12-24**|**3D Point Cloud Reconstruction and SLAM as an Input**|Ziyu Li et.al.|[2112.12907](http://arxiv.org/abs/2112.12907)|null|
|**2021-12-22**|**NICE-SLAM: Neural Implicit Scalable Encoding for SLAM**|Zihan Zhu et.al.|[2112.12130](http://arxiv.org/abs/2112.12130)|**[link](https://github.com/cvg/nice-slam)**|
|**2021-12-18**|**Fast and Robust Registration of Partially Overlapping Point Clouds**|Eduardo Arnold et.al.|[2112.09922](http://arxiv.org/abs/2112.09922)|**[link](https://github.com/eduardohenriquearnold/fastreg)**|
|**2021-12-17**|**Symmetry-aware Neural Architecture for Embodied Visual Navigation**|Shuang Liu et.al.|[2112.09515](http://arxiv.org/abs/2112.09515)|null|
|**2021-12-27**|**Homography Decomposition Networks for Planar Object Tracking**|Xinrui Zhan et.al.|[2112.07909](http://arxiv.org/abs/2112.07909)|**[link](https://github.com/zhanxinrui/hdn)**|
|**2021-12-14**|**Autonomous Navigation System from Simultaneous Localization and Mapping**|Micheal Caracciolo et.al.|[2112.07723](http://arxiv.org/abs/2112.07723)|**[link](https://github.com/michealcarac/VSLAM-Mapping)**|
|**2021-12-12**|**360-DFPE: Leveraging Monocular 360-Layouts for Direct Floor Plan Estimation**|Bolivar Solarte et.al.|[2112.06180](http://arxiv.org/abs/2112.06180)|**[link](https://github.com/EnriqueSolarte/direct_360_FPE)**|
|**2021-12-11**|**Simultaneous Localization and Mapping: Through the Lens of Nonlinear Optimization**|Amay Saxena et.al.|[2112.05921](http://arxiv.org/abs/2112.05921)|null|
|**2021-12-07**|**Hybrid Visual SLAM for Underwater Vehicle Manipulator Systems**|Gideon Billings et.al.|[2112.03826](http://arxiv.org/abs/2112.03826)|**[link](https://github.com/gidobot/uwslam)**|
|**2021-12-05**|**Iterated Posterior Linearization PMB Filter for 5G SLAM**|Yu Ge et.al.|[2112.02575](http://arxiv.org/abs/2112.02575)|null|
|**2021-12-03**|**Fast Direct Stereo Visual SLAM**|Jiawei Mo et.al.|[2112.01890](http://arxiv.org/abs/2112.01890)|**[link](https://github.com/irvlab/direct_stereo_slam)**|
|**2021-12-02**|**MegBA: A High-Performance and Distributed Library for Large-Scale Bundle Adjustment**|Jie Ren et.al.|[2112.01349](http://arxiv.org/abs/2112.01349)|**[link](https://github.com/megviirobot/megba)**|
|**2021-12-01**|**Research on Event Accumulator Settings for Event-Based SLAM**|Kun Xiao et.al.|[2112.00427](http://arxiv.org/abs/2112.00427)|**[link](https://github.com/robin-shaun/event-slam-accumulator-settings)**|
|**2021-11-29**|**An in-depth experimental study of sensor usage and visual reasoning of robots navigating in real environments**|Assem Sadek et.al.|[2111.14666](http://arxiv.org/abs/2111.14666)|null|
|**2021-11-29**|**Deployment of Aerial Robots after a major fire of an industrial hall with hazardous substances, a report**|Hartmut Surmann et.al.|[2111.14542](http://arxiv.org/abs/2111.14542)|null|
|**2021-11-24**|**Automatic Mapping with Obstacle Identification for Indoor Human Mobility Assessment**|V. Ayala-Alfaro et.al.|[2111.12690](http://arxiv.org/abs/2111.12690)|null|
|**2021-11-24**|**Autonomous bot with ML-based reactive navigation for indoor environment**|Yash Srivastava et.al.|[2111.12542](http://arxiv.org/abs/2111.12542)|null|
|**2021-11-22**|**A General Framework for Lifelong Localization and Mapping in Changing Environment**|Min Zhao et.al.|[2111.10946](http://arxiv.org/abs/2111.10946)|**[link](https://github.com/sanduan168/lifelong-slam-dataset)**|
|**2021-11-17**|**Probabilistic Spatial Distribution Prior Based Attentional Keypoints Matching Network**|Xiaoming Zhao et.al.|[2111.09006](http://arxiv.org/abs/2111.09006)|null|
|**2021-11-10**|**Comparing dominance of tennis' big three via multiple-output Bayesian quantile regression models**|Bruno Santos et.al.|[2111.05631](http://arxiv.org/abs/2111.05631)|null|
|**2021-11-10**|**TomoSLAM: factor graph optimization for rotation angle refinement in microtomography**|Mark Griguletskii et.al.|[2111.05562](http://arxiv.org/abs/2111.05562)|null|
|**2021-11-07**|**Hierarchical Segment-based Optimization for SLAM**|Yuxin Tian et.al.|[2111.04101](http://arxiv.org/abs/2111.04101)|null|
|**2021-11-07**|**Online Mutual Adaptation of Deep Depth Prediction and Visual SLAM**|Shing Yan Loo et.al.|[2111.04096](http://arxiv.org/abs/2111.04096)|null|
|**2021-11-05**|**MSC-VO: Exploiting Manhattan and Structural Constraints for Visual Odometry**|Joan P. Company-Corcoles et.al.|[2111.03408](http://arxiv.org/abs/2111.03408)|null|
|**2021-10-31**|**Loop closure detection using local 3D deep descriptors**|Youjie Zhou et.al.|[2111.00440](http://arxiv.org/abs/2111.00440)|**[link](https://github.com/yiming107/l3d_loop_closure)**|
|**2021-10-27**|**Millimeter Wave Wireless Assisted Robot Navigation with Link State Classification**|Mingsheng Yin et.al.|[2110.14789](http://arxiv.org/abs/2110.14789)|**[link](https://github.com/nyu-wireless/mmwRobotNav)**|
|**2021-10-27**|**Efficient Placard Discovery for Semantic Mapping During Frontier Exploration**|David Balaban et.al.|[2110.14742](http://arxiv.org/abs/2110.14742)|null|
|**2021-10-26**|**Robust Multi-view Registration of Point Sets with Laplacian Mixture Model**|Jin Zhang et.al.|[2110.13744](http://arxiv.org/abs/2110.13744)|null|
|**2021-10-25**|**WOLF: A modular estimation framework for robotics based on factor graphs**|Joan Sola et.al.|[2110.12919](http://arxiv.org/abs/2110.12919)|null|
|**2021-10-21**|**Real-Time Ground-Plane Refined LiDAR SLAM**|Fan Yang et.al.|[2110.11517](http://arxiv.org/abs/2110.11517)|null|
|**2021-10-21**|**SymbioLCD: Ensemble-Based Loop Closure Detection using CNN-Extracted Objects and Visual Bag-of-Words**|Jonathan J. Y. Kim et.al.|[2110.11491](http://arxiv.org/abs/2110.11491)|null|
|**2021-10-21**|**InterpolationSLAM: A Novel Robust Visual SLAM System in Rotational Motion**|Zhenkun Zhu et.al.|[2110.11040](http://arxiv.org/abs/2110.11040)|null|
|**2021-10-20**|**SLAM: A Unified Encoder for Speech and Language Modeling via Speech-Text Joint Pre-Training**|Ankur Bapna et.al.|[2110.10329](http://arxiv.org/abs/2110.10329)|null|
|**2021-10-18**|**Enhancing exploration algorithms for navigation with visual SLAM**|Kirill Muravyev et.al.|[2110.09156](http://arxiv.org/abs/2110.09156)|null|
|**2021-10-18**|**Accurate and Robust Object-oriented SLAM with 3D Quadric Landmark Construction in Outdoor Environment**|Rui Tian et.al.|[2110.08977](http://arxiv.org/abs/2110.08977)|null|
|**2021-10-16**|**Partial Hierarchical Pose Graph Optimization for SLAM**|Alexander Korovko et.al.|[2110.08639](http://arxiv.org/abs/2110.08639)|null|
|**2021-10-14**|**Active SLAM over Continuous Trajectory and Control: A Covariance-Feedback Approach**|Shumon Koga et.al.|[2110.07546](http://arxiv.org/abs/2110.07546)|null|
|**2021-10-13**|**Collaborative Radio SLAM for Multiple Robots based on WiFi Fingerprint Similarity**|Ran Liu et.al.|[2110.06541](http://arxiv.org/abs/2110.06541)|null|
|**2021-10-12**|**Learning Efficient Multi-Agent Cooperative Visual Exploration**|Chao Yu et.al.|[2110.05734](http://arxiv.org/abs/2110.05734)|null|
|**2021-10-07**|**Self-Supervised Depth Completion for Active Stereo**|Frederik Warburg et.al.|[2110.03234](http://arxiv.org/abs/2110.03234)|null|
|**2021-10-06**|**InterpolationSLAM: A Novel Robust Visual SLAM System in Rotating Scenes**|Zhenkun Zhu et.al.|[2110.02593](http://arxiv.org/abs/2110.02593)|null|
|**2021-10-03**|**AEROS: Adaptive RObust least-Squares for Graph-Based SLAM**|Milad Ramezani et.al.|[2110.02018](http://arxiv.org/abs/2110.02018)|null|
|**2021-10-04**|**Fast Uncertainty Quantification for Active Graph SLAM**|Julio A. Placed et.al.|[2110.01289](http://arxiv.org/abs/2110.01289)|**[link](https://github.com/julioplaced/active_graph_slam)**|
|**2021-10-04**|**Geometry-based Graph Pruning for Lifelong SLAM**|Gerhard Kurz et.al.|[2110.01286](http://arxiv.org/abs/2110.01286)|null|
|**2021-10-03**|**Quadrotor Control on $SU(2)\times R^3$ with SLAM Integration**|Marcus Greiff et.al.|[2110.01099](http://arxiv.org/abs/2110.01099)|null|
|**2021-10-02**|**Online Incremental Non-Gaussian Inference for SLAM Using Normalizing Flows**|Qiangqiang Huang et.al.|[2110.00876](http://arxiv.org/abs/2110.00876)|**[link](https://github.com/marineroboticsgroup/nf-isam)**|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## SFM

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2023-06-10**|**3D reconstruction using Structure for Motion**|Kshitij Karnawat et.al.|[2306.06360](http://arxiv.org/abs/2306.06360)|**[link](https://github.com/kshitijkarnawat/structure-from-motion)**|
|**2023-06-02**|**Self-supervised Interest Point Detection and Description for Fisheye and Perspective Images**|Marcela Mera-Trujillo et.al.|[2306.01938](http://arxiv.org/abs/2306.01938)|null|
|**2023-05-31**|**FlowCam: Training Generalizable 3D Radiance Fields without Camera Poses via Pixel-Aligned Scene Flow**|Cameron Smith et.al.|[2306.00180](http://arxiv.org/abs/2306.00180)|null|
|**2023-05-19**|**SIDAR: Synthetic Image Dataset for Alignment & Restoration**|Monika Kwiatkowski et.al.|[2305.12036](http://arxiv.org/abs/2305.12036)|**[link](https://github.com/niika/SIDAR)**|
|**2023-05-09**|**Eiffel Tower: A Deep-Sea Underwater Dataset for Long-Term Visual Localization**|Clémentin Boittiaux et.al.|[2305.05301](http://arxiv.org/abs/2305.05301)|**[link](https://github.com/clementinboittiaux/sfm-pipeline)**|
|**2023-05-09**|**Rotation Synchronization via Deep Matrix Factorization**|Gk Tejus et.al.|[2305.05268](http://arxiv.org/abs/2305.05268)|**[link](https://github.com/gktejus/DMF-Synch)**|
|**2023-04-20**|**A Comparative Neural Radiance Field (NeRF) 3D Analysis of Camera Poses from HoloLens Trajectories and Structure from Motion**|Miriam Jäger et.al.|[2304.10664](http://arxiv.org/abs/2304.10664)|null|
|**2023-04-14**|**Fusing Structure from Motion and Simulation-Augmented Pose Regression from Optical Flow for Challenging Indoor Environments**|Felix Ott et.al.|[2304.07250](http://arxiv.org/abs/2304.07250)|null|
|**2023-04-12**|**Visual Localization using Imperfect 3D Models from the Internet**|Vojtech Panek et.al.|[2304.05947](http://arxiv.org/abs/2304.05947)|**[link](https://github.com/v-pnk/cadloc)**|
|**2023-04-08**|**Photometric Correction for Infrared Sensors**|Jincheng Zhang et.al.|[2304.03930](http://arxiv.org/abs/2304.03930)|null|
|**2023-04-07**|**DualRefine: Self-Supervised Depth and Pose Estimation Through Iterative Epipolar Sampling and Refinement Toward Equilibrium**|Antyanta Bangunharcana et.al.|[2304.03560](http://arxiv.org/abs/2304.03560)|**[link](https://github.com/antabangun/dualrefine)**|
|**2023-04-05**|**Semantic Validation in Structure from Motion**|Joseph Rowell et.al.|[2304.02420](http://arxiv.org/abs/2304.02420)|**[link](https://github.com/joerowelll/comp0132_rjxz25)**|
|**2023-03-31**|**Learning Internal Representations of 3D Transformations from 2D Projected Inputs**|Marissa Connor et.al.|[2303.17776](http://arxiv.org/abs/2303.17776)|null|
|**2023-03-30**|**3D Line Mapping Revisited**|Shaohui Liu et.al.|[2303.17504](http://arxiv.org/abs/2303.17504)|**[link](https://github.com/cvg/limap)**|
|**2023-03-27**|**TMO: Textured Mesh Acquisition of Objects with a Mobile Device by using Differentiable Rendering**|Jaehoon Choi et.al.|[2303.15060](http://arxiv.org/abs/2303.15060)|null|
|**2023-03-26**|**On the Importance of Accurate Geometry Data for Dense 3D Vision Tasks**|HyunJun Jung et.al.|[2303.14840](http://arxiv.org/abs/2303.14840)|**[link](https://github.com/junggy/hammer-dataset)**|
|**2023-03-24**|**Seeing Through the Glass: Neural 3D Reconstruction of Object Inside a Transparent Container**|Jinguang Tong et.al.|[2303.13805](http://arxiv.org/abs/2303.13805)|**[link](https://github.com/hirotong/reneus)**|
|**2023-03-24**|**Progressively Optimized Local Radiance Fields for Robust View Synthesis**|Andreas Meuleman et.al.|[2303.13791](http://arxiv.org/abs/2303.13791)|null|
|**2023-03-15**|**RefiNeRF: Modelling dynamic neural radiance fields with inconsistent or missing camera parameters**|Shuja Khalid et.al.|[2303.08695](http://arxiv.org/abs/2303.08695)|null|
|**2023-03-09**|**Revisiting Rotation Averaging: Uncertainties and Robust Losses**|Ganlin Zhang et.al.|[2303.05195](http://arxiv.org/abs/2303.05195)|**[link](https://github.com/zhangganlin/globalsfmpy)**|
|**2023-02-28**|**Nonlinear Intensity, Scale and Rotation Invariant Matching for Multimodal Images**|Zhongli Fan et.al.|[2302.14239](http://arxiv.org/abs/2302.14239)|**[link](https://github.com/zhongli-fan/nisr)**|
|**2023-03-25**|**BLiRF: Bandlimited Radiance Fields for Dynamic Scene Modeling**|Sameera Ramasinghe et.al.|[2302.13543](http://arxiv.org/abs/2302.13543)|null|
|**2023-02-21**|**EC-SfM: Efficient Covisibility-based Structure-from-Motion for Both Sequential and Unordered Images**|Zhichao Ye et.al.|[2302.10544](http://arxiv.org/abs/2302.10544)|**[link](https://github.com/openxrlab/xrsfm)**|
|**2023-02-18**|**Bridge Damage Cause Estimation Using Multiple Images Based on Visual Question Answering**|Tatsuro Yamane et.al.|[2302.09208](http://arxiv.org/abs/2302.09208)|null|
|**2023-02-12**|**Uncertainty-Driven Dense Two-View Structure from Motion**|Weirong Chen et.al.|[2302.00523](http://arxiv.org/abs/2302.00523)|null|
|**2023-01-28**|**AdaSfM: From Coarse Global to Fine Incremental Adaptive Structure from Motion**|Yu Chen et.al.|[2301.12135](http://arxiv.org/abs/2301.12135)|null|
|**2023-01-20**|**A vision-based autonomous UAV inspection framework for unknown tunnel construction sites with dynamic obstacles**|Zhefan Xu et.al.|[2301.08422](http://arxiv.org/abs/2301.08422)|**[link](https://github.com/zhefan-xu/cerlab-uav-autonomy)**|
|**2023-03-21**|**Robust Dynamic Radiance Fields**|Yu-Lun Liu et.al.|[2301.02239](http://arxiv.org/abs/2301.02239)|**[link](https://github.com/facebookresearch/robust-dynrf)**|
|**2022-12-24**|**Polarimetric Multi-View Inverse Rendering**|Jinyu Zhao et.al.|[2212.12721](http://arxiv.org/abs/2212.12721)|null|
|**2022-12-13**|**Accidental Turntables: Learning 3D Pose by Watching Objects Turn**|Zezhou Cheng et.al.|[2212.06300](http://arxiv.org/abs/2212.06300)|null|
|**2022-12-04**|**3D Object Aided Self-Supervised Monocular Depth Estimation**|Songlin Wei et.al.|[2212.01768](http://arxiv.org/abs/2212.01768)|null|
|**2022-12-02**|**High-Res Facial Appearance Capture from Polarized Smartphone Images**|Dejan Azinović et.al.|[2212.01160](http://arxiv.org/abs/2212.01160)|null|
|**2022-11-28**|**FeatureBooster: Boosting Feature Descriptors with a Lightweight Neural Network**|Xinjiang Wang et.al.|[2211.15069](http://arxiv.org/abs/2211.15069)|**[link](https://github.com/sjtu-visys/featurebooster)**|
|**2022-11-24**|**JigsawPlan: Room Layout Jigsaw Puzzle Extreme Structure from Motion using Diffusion Models**|Sepidehsadat Hosseini et.al.|[2211.13785](http://arxiv.org/abs/2211.13785)|null|
|**2022-11-24**|**SfM-TTR: Using Structure from Motion for Test-Time Refinement of Single-View Depth Networks**|Sergio Izquierdo et.al.|[2211.13551](http://arxiv.org/abs/2211.13551)|**[link](https://github.com/serizba/sfm-ttr)**|
|**2022-11-22**|**Level-S $^2$ fM: Structure from Motion on Neural Level Set of Implicit Surfaces**|Yuxi Xiao et.al.|[2211.12018](http://arxiv.org/abs/2211.12018)|**[link](https://github.com/henry123-boy/Level-S2FM_official)**|
|**2022-11-21**|**Towards Live 3D Reconstruction from Wearable Video: An Evaluation of V-SLAM, NeRF, and Videogrammetry Techniques**|David Ramirez et.al.|[2211.11836](http://arxiv.org/abs/2211.11836)|null|
|**2022-11-14**|**Controllable GAN Synthesis Using Non-Rigid Structure-from-Motion**|René Haas et.al.|[2211.07195](http://arxiv.org/abs/2211.07195)|null|
|**2022-10-13**|**Quantifying and analyzing rock trait distributions of rocky fault scarps using a deep learning approach**|Zhiang Chen et.al.|[2210.07349](http://arxiv.org/abs/2210.07349)|null|
|**2022-10-11**|**DeepMLE: A Robust Deep Maximum Likelihood Estimator for Two-view Structure from Motion**|Yuxi Xiao et.al.|[2210.05517](http://arxiv.org/abs/2210.05517)|null|
|**2022-10-07**|**Leveraging Structure from Motion to Localize Inaccessible Bus Stops**|Indu Panigrahi et.al.|[2210.03646](http://arxiv.org/abs/2210.03646)|**[link](https://github.com/ind1010/SfM_for_BusEdge)**|
|**2022-10-01**|**Structure-Aware NeRF without Posed Camera via Epipolar Constraint**|Shu Chen et.al.|[2210.00183](http://arxiv.org/abs/2210.00183)|**[link](https://github.com/xtu-pr-lab/sanerf)**|
|**2022-10-05**|**FAST-LIO, Then Bayesian ICP, Then GTSFM**|Jerred Chen et.al.|[2210.00146](http://arxiv.org/abs/2210.00146)|null|
|**2022-09-20**|**BuFF: Burst Feature Finder for Light-Constrained 3D Reconstruction**|Ahalya Ravendran et.al.|[2209.09470](http://arxiv.org/abs/2209.09470)|null|
|**2022-09-19**|**A Hybrid Cable-Driven Robot for Non-Destructive Leafy Plant Monitoring and Mass Estimation using Structure from Motion**|Gerry Chen et.al.|[2209.08690](http://arxiv.org/abs/2209.08690)|null|
|**2022-09-14**|**End-to-End Multi-View Structure-from-Motion with Hypercorrelation Volumes**|Qiao Chen et.al.|[2209.06926](http://arxiv.org/abs/2209.06926)|null|
|**2022-09-07**|**Deployment of Aerial Robots during the Flood Disaster in Erftstadt / Blessem in July 2021**|Hartmut Surmann et.al.|[2209.03084](http://arxiv.org/abs/2209.03084)|null|
|**2022-08-27**|**Weakly and Semi-Supervised Detection, Segmentation and Tracking of Table Grapes with Limited and Noisy Data**|Thomas A. Ciarfuglia et.al.|[2208.13001](http://arxiv.org/abs/2208.13001)|null|
|**2022-08-12**|**Handling Constrained Optimization in Factor Graphs for Autonomous Navigation**|Barbara Bazzana et.al.|[2208.06325](http://arxiv.org/abs/2208.06325)|null|
|**2022-08-04**|**Globally Consistent Video Depth and Pose Estimation with Efficient Test-Time Training**|Yao-Chih Lee et.al.|[2208.02709](http://arxiv.org/abs/2208.02709)|**[link](https://github.com/yaochih/gcvd-release)**|
|**2022-07-31**|**One Object at a Time: Accurate and Robust Structure From Motion for Robots**|Aravind Battaje et.al.|[2208.00487](http://arxiv.org/abs/2208.00487)|null|
|**2022-07-23**|**Detection and Initial Assessment of Lunar Landing Sites Using Neural Networks**|Daniel Posada et.al.|[2207.11413](http://arxiv.org/abs/2207.11413)|null|
|**2022-07-25**|**MeshLoc: Mesh-Based Visual Localization**|Vojtech Panek et.al.|[2207.10762](http://arxiv.org/abs/2207.10762)|**[link](https://github.com/tsattler/meshloc_release)**|
|**2022-07-19**|**ParticleSfM: Exploiting Dense Point Trajectories for Localizing Moving Cameras in the Wild**|Wang Zhao et.al.|[2207.09137](http://arxiv.org/abs/2207.09137)|**[link](https://github.com/bytedance/particle-sfm)**|
|**2022-07-16**|**Organic Priors in Non-Rigid Structure from Motion**|Suryansh Kumar et.al.|[2207.06262](http://arxiv.org/abs/2207.06262)|null|
|**2022-07-06**|**A Novel Hybrid Endoscopic Dataset for Evaluating Machine Learning-based Photometric Image Enhancement Models**|Axel Garcia-Vega et.al.|[2207.02396](http://arxiv.org/abs/2207.02396)|null|
|**2022-06-24**|**Parallel Structure from Motion for UAV Images via Weighted Connected Dominating Set**|San Jiang et.al.|[2206.11499](http://arxiv.org/abs/2206.11499)|null|
|**2022-06-13**|**TC-SfM: Robust Track-Community-Based Structure-from-Motion**|Lei Wang et.al.|[2206.05866](http://arxiv.org/abs/2206.05866)|null|
|**2022-06-10**|**EigenFairing: 3D Model Fairing using Image Coherence**|Pragyana Mishra et.al.|[2206.05309](http://arxiv.org/abs/2206.05309)|null|
|**2022-06-01**|**Semantic Room Wireframe Detection from a Single View**|David Gillsjö et.al.|[2206.00491](http://arxiv.org/abs/2206.00491)|**[link](https://github.com/davidgillsjo/srw-net)**|
|**2022-05-31**|**Geo-Neus: Geometry-Consistent Neural Implicit Surfaces Learning for Multi-view Reconstruction**|Qiancheng Fu et.al.|[2205.15848](http://arxiv.org/abs/2205.15848)|null|
|**2022-05-09**|**Is my Depth Ground-Truth Good Enough? HAMMER -- Highly Accurate Multi-Modal Dataset for DEnse 3D Scene Regression**|HyunJun Jung et.al.|[2205.04565](http://arxiv.org/abs/2205.04565)|null|
|**2022-05-07**|**Optimizing Terrain Mapping and Landing Site Detection for Autonomous UAVs**|Pedro F. Proença et.al.|[2205.03522](http://arxiv.org/abs/2205.03522)|null|
|**2022-05-06**|**EVIMO2: An Event Camera Dataset for Motion Segmentation, Optical Flow, Structure from Motion, and Visual Inertial Odometry in Indoor Scenes with Monocular or Stereo Algorithms**|Levi Burner et.al.|[2205.03467](http://arxiv.org/abs/2205.03467)|null|
|**2022-04-20**|**Learned Monocular Depth Priors in Visual-Inertial Initialization**|Yunwen Zhou et.al.|[2204.09171](http://arxiv.org/abs/2204.09171)|null|
|**2022-04-10**|**Deep Non-rigid Structure-from-Motion: A Sequence-to-Sequence Translation Perspective**|Hui Deng et.al.|[2204.04730](http://arxiv.org/abs/2204.04730)|null|
|**2022-04-08**|**Constrained Bundle Adjustment for Structure From Motion Using Uncalibrated Multi-Camera Systems**|Debao Huang et.al.|[2204.04145](http://arxiv.org/abs/2204.04145)|null|
|**2022-04-07**|**SurroundDepth: Entangling Surrounding Views for Self-Supervised Multi-Camera Depth Estimation**|Yi Wei et.al.|[2204.03636](http://arxiv.org/abs/2204.03636)|**[link](https://github.com/weiyithu/surrounddepth)**|
|**2022-04-06**|**Georeferencing of Photovoltaic Modules from Aerial Infrared Videos using Structure-from-Motion**|Lukas Bommes et.al.|[2204.02733](http://arxiv.org/abs/2204.02733)|**[link](https://github.com/lukasbommes/pv-hawk)**|
|**2022-04-05**|**Depth-Guided Sparse Structure-from-Motion for Movies and TV Shows**|Sheng Liu et.al.|[2204.02509](http://arxiv.org/abs/2204.02509)|**[link](https://github.com/amazon-research/small-baseline-camera-tracking)**|
|**2022-03-31**|**Fast, Accurate and Memory-Efficient Partial Permutation Synchronization**|Shaohan Li et.al.|[2203.16505](http://arxiv.org/abs/2203.16505)|null|
|**2022-03-28**|**Visual Odometry for RGB-D Cameras**|Afonso Fontes et.al.|[2203.15119](http://arxiv.org/abs/2203.15119)|null|
|**2022-03-28**|**Optimizing Elimination Templates by Greedy Parameter Search**|Evgeniy Martyushev et.al.|[2203.14901](http://arxiv.org/abs/2203.14901)|**[link](https://github.com/martyushev/eliminationtemplates)**|
|**2022-03-23**|**Event-Based Dense Reconstruction Pipeline**|Kun Xiao et.al.|[2203.12270](http://arxiv.org/abs/2203.12270)|null|
|**2022-03-21**|**DiffPoseNet: Direct Differentiable Camera Pose Estimation**|Chethan M. Parameshwara et.al.|[2203.11174](http://arxiv.org/abs/2203.11174)|null|
|**2022-03-02**|**Asynchronous Optimisation for Event-based Visual Odometry**|Daqi Liu et.al.|[2203.01037](http://arxiv.org/abs/2203.01037)|null|
|**2022-03-02**|**Distributed Riemannian Optimization with Lazy Communication for Collaborative Geometric Estimation**|Yulun Tian et.al.|[2203.00851](http://arxiv.org/abs/2203.00851)|null|
|**2022-02-18**|**MultiRes-NetVLAD: Augmenting Place Recognition Training with Low-Resolution Imagery**|Ahmad Khaliq et.al.|[2202.09146](http://arxiv.org/abs/2202.09146)|**[link](https://github.com/ahmedest61/multires-netvlad)**|
|**2022-01-20**|**GeoFill: Reference-Based Image Inpainting of Scenes with Complex Geometry**|Yunhan Zhao et.al.|[2201.08131](http://arxiv.org/abs/2201.08131)|null|
|**2022-01-13**|**Scalable Cluster-Consistency Statistics for Robust Multi-Object Matching**|Yunpeng Shi et.al.|[2201.04797](http://arxiv.org/abs/2201.04797)|**[link](https://github.com/yunpeng-shi/fcc)**|
|**2022-01-10**|**High-resolution Ecosystem Mapping in Repetitive Environments Using Dual Camera SLAM**|Brian M. Hopkinson et.al.|[2201.03364](http://arxiv.org/abs/2201.03364)|**[link](https://github.com/bmhopkinson/hyslam)**|
|**2022-01-06**|**De-rendering 3D Objects in the Wild**|Felix Wimbauer et.al.|[2201.02279](http://arxiv.org/abs/2201.02279)|**[link](https://github.com/brummi/derender3d)**|
|**2021-12-29**|**On the Instability of Relative Pose Estimation and RANSAC's Role**|Hongyi Fan et.al.|[2112.14651](http://arxiv.org/abs/2112.14651)|null|
|**2021-12-16**|**Road-aware Monocular Structure from Motion and Homography Estimation**|Wei Sui et.al.|[2112.08635](http://arxiv.org/abs/2112.08635)|null|
|**2021-12-10**|**Critical configurations for three projective views**|Martin Bråtelund et.al.|[2112.05478](http://arxiv.org/abs/2112.05478)|null|
|**2021-12-09**|**Critical configurations for two projective views, a new approach**|Martin Bråtelund et.al.|[2112.05074](http://arxiv.org/abs/2112.05074)|null|
|**2021-12-06**|**Dense Depth Priors for Neural Radiance Fields from Sparse Input Views**|Barbara Roessle et.al.|[2112.03288](http://arxiv.org/abs/2112.03288)|**[link](https://github.com/barbararoessle/dense_depth_priors_nerf)**|
|**2021-12-10**|**MegBA: A High-Performance and Distributed Library for Large-Scale Bundle Adjustment**|Jie Ren et.al.|[2112.01349](http://arxiv.org/abs/2112.01349)|**[link](https://github.com/megviirobot/megba)**|
|**2021-11-11**|**Multi-Resolution Elevation Mapping and Safe Landing Site Detection with Applications to Planetary Rotorcraft**|Pascal Schoppmann et.al.|[2111.06271](http://arxiv.org/abs/2111.06271)|null|
|**2021-11-10**|**Damage Estimation and Localization from Sparse Aerial Imagery**|Rene Garcia Franceschini et.al.|[2111.03708](http://arxiv.org/abs/2111.03708)|null|
|**2021-11-03**|**Event and Activity Recognition in Video Surveillance for Cyber-Physical Systems**|Swarnabja Bhaumik et.al.|[2111.02064](http://arxiv.org/abs/2111.02064)|null|
|**2021-10-14**|**Modeling dynamic target deformation in camera calibration**|Annika Hagemann et.al.|[2110.07322](http://arxiv.org/abs/2110.07322)|null|
|**2021-10-13**|**Hyperspectral 3D Mapping of Underwater Environments**|Maxime Ferrera et.al.|[2110.06571](http://arxiv.org/abs/2110.06571)|null|
|**2021-09-24**|**Automatic Map Update Using Dashcam Videos**|Aziza Zhanabatyrova et.al.|[2109.12131](http://arxiv.org/abs/2109.12131)|null|
|**2021-09-16**|**Rotation Averaging in a Split Second: A Primal-Dual Method and a Closed-Form for Cycle Graphs**|Gabriel Moreira et.al.|[2109.08046](http://arxiv.org/abs/2109.08046)|**[link](https://github.com/gabmoreira/maks)**|
|**2021-09-06**|**Single-Camera 3D Head Fitting for Mixed Reality Clinical Applications**|Tejas Mane et.al.|[2109.02740](http://arxiv.org/abs/2109.02740)|null|
|**2021-09-02**|**Dynamic Scene Novel View Synthesis via Deferred Spatio-temporal Consistency**|Beatrix-Emőke Fülöp-Balogh et.al.|[2109.01018](http://arxiv.org/abs/2109.01018)|null|
|**2021-09-01**|**On the Limits of Pseudo Ground Truth in Visual Camera Re-localisation**|Eric Brachmann et.al.|[2109.00524](http://arxiv.org/abs/2109.00524)|**[link](https://github.com/tsattler/visloc_pseudo_gt_limitations)**|
|**2021-08-31**|**DensePose 3D: Lifting Canonical Surface Maps of Articulated Objects to the Third Dimension**|Roman Shapovalov et.al.|[2109.00033](http://arxiv.org/abs/2109.00033)|null|
|**2021-08-29**|**Solving Viewing Graph Optimization for Simultaneous Position and Rotation Registration**|Seyed-Mahdi Nasiri et.al.|[2108.12876](http://arxiv.org/abs/2108.12876)|null|
|**2021-08-23**|**Burst Imaging for Light-Constrained Structure-From-Motion**|Ahalya Ravendran et.al.|[2108.09895](http://arxiv.org/abs/2108.09895)|null|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## Visual Localization

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2023-06-13**|**GeneCIS: A Benchmark for General Conditional Image Similarity**|Sagar Vaze et.al.|[2306.07969](http://arxiv.org/abs/2306.07969)|null|
|**2023-06-13**|**MOFI: Learning Image Representations from Noisy Entity Annotated Images**|Wentao Wu et.al.|[2306.07952](http://arxiv.org/abs/2306.07952)|**[link](https://github.com/apple/ml-mofi)**|
|**2023-06-12**|**Zero-shot Composed Text-Image Retrieval**|Yikun Liu et.al.|[2306.07272](http://arxiv.org/abs/2306.07272)|**[link](https://github.com/Code-kunkun/ZS-CIR)**|
|**2023-06-12**|**Sticker820K: Empowering Interactive Retrieval with Stickers**|Sijie Zhao et.al.|[2306.06870](http://arxiv.org/abs/2306.06870)|null|
|**2023-06-11**|**Self-Enhancement Improves Text-Image Retrieval in Foundation Visual-Language Models**|Yuguang Yang et.al.|[2306.06691](http://arxiv.org/abs/2306.06691)|null|
|**2023-06-03**|**Relieving Triplet Ambiguity: Consensus Network for Language-Guided Image Retrieval**|Xu Zhang et.al.|[2306.02092](http://arxiv.org/abs/2306.02092)|null|
|**2023-06-03**|**Class Anchor Margin Loss for Content-Based Image Retrieval**|Alexandru Ghita et.al.|[2306.00630](http://arxiv.org/abs/2306.00630)|null|
|**2023-05-31**|**Chatting Makes Perfect -- Chat-based Image Retrieval**|Matan Levy et.al.|[2305.20062](http://arxiv.org/abs/2305.20062)|**[link](https://github.com/levymsn/ChatIR)**|
|**2023-05-31**|**Probabilistic Uncertainty Quantification of Prediction Models with Application to Visual Localization**|Junan Chen et.al.|[2305.20044](http://arxiv.org/abs/2305.20044)|null|
|**2023-05-30**|**A Recipe for Efficient SBIR Models: Combining Relative Triplet Loss with Batch Normalization and Knowledge Distillation**|Omar Seddati et.al.|[2305.18988](http://arxiv.org/abs/2305.18988)|null|
|**2023-05-29**|**Synfeal: A Data-Driven Simulator for End-to-End Camera Localization**|Daniel Coelho et.al.|[2305.18260](http://arxiv.org/abs/2305.18260)|**[link](https://github.com/danielcoelho112/synfeal)**|
|**2023-05-29**|**Nanoscale visualization of the thermally-driven evolution of antiferromagnetic domains in FeTe thin films**|Shrinkhala Sharma et.al.|[2305.18197](http://arxiv.org/abs/2305.18197)|null|
|**2023-05-29**|**TReR: A Lightweight Transformer Re-Ranking Approach for 3D LiDAR Place Recognition**|Tiago Barros et.al.|[2305.18013](http://arxiv.org/abs/2305.18013)|null|
|**2023-05-28**|**ConaCLIP: Exploring Distillation of Fully-Connected Knowledge Interaction Graph for Lightweight Text-Image Retrieval**|Jiapeng Wang et.al.|[2305.17652](http://arxiv.org/abs/2305.17652)|null|
|**2023-06-01**|**FACTUAL: A Benchmark for Faithful and Consistent Textual Scene Graph Parsing**|Zhuang Li et.al.|[2305.17497](http://arxiv.org/abs/2305.17497)|**[link](https://github.com/zhuang-li/factual)**|
|**2023-05-27**|**Pentagon-Match (PMatch): Identification of View-Invariant Planar Feature for Local Feature Matching-Based Homography Estimation**|Yueh-Cheng Huang et.al.|[2305.17463](http://arxiv.org/abs/2305.17463)|null|
|**2023-05-26**|**Generating Images with Multimodal Language Models**|Jing Yu Koh et.al.|[2305.17216](http://arxiv.org/abs/2305.17216)|**[link](https://github.com/kohjingyu/gill)**|
|**2023-05-25**|**Candidate Set Re-ranking for Composed Image Retrieval with Dual Multi-modal Encoder**|Zheyuan Liu et.al.|[2305.16304](http://arxiv.org/abs/2305.16304)|**[link](https://github.com/Cuberick-Orion/Candidate-Reranking-CIR)**|
|**2023-05-23**|**Leveraging BEV Representation for 360-degree Visual Place Recognition**|Xuecheng Xu et.al.|[2305.13814](http://arxiv.org/abs/2305.13814)|**[link](https://github.com/maverickpeter/vdisco)**|
|**2023-05-23**|**EDIS: Entity-Driven Image Search over Multimodal Web Content**|Siqi Liu et.al.|[2305.13631](http://arxiv.org/abs/2305.13631)|**[link](https://github.com/emerisly/edis)**|
|**2023-05-20**|**DAC: Detector-Agnostic Spatial Covariances for Deep Local Features**|Javier Tirado-Garín et.al.|[2305.12250](http://arxiv.org/abs/2305.12250)|**[link](https://github.com/javrtg/dac)**|
|**2023-05-19**|**Towards More Transparent and Accurate Cancer Diagnosis with an Unsupervised CAE Approach**|Zahra Tabatabaei et.al.|[2305.11728](http://arxiv.org/abs/2305.11728)|null|
|**2023-05-19**|**Learning Sequence Descriptor based on Spatiotemporal Attention for Visual Place Recognition**|Fenglin Zhang et.al.|[2305.11467](http://arxiv.org/abs/2305.11467)|**[link](https://github.com/tiev-tongji/spatio-temporal-seqvpr)**|
|**2023-05-12**|**IMAGINATOR: Pre-Trained Image+Text Joint Embeddings using Word-Level Grounding of Images**|Varuna Krishna et.al.|[2305.10438](http://arxiv.org/abs/2305.10438)|null|
|**2023-05-17**|**Self-Training Boosted Multi-Faceted Matching Network for Composed Image Retrieval**|Haokun Wen et.al.|[2305.09979](http://arxiv.org/abs/2305.09979)|null|
|**2023-05-13**|**Illumination-insensitive Binary Descriptor for Visual Measurement Based on Local Inter-patch Invariance**|Xinyu Lin et.al.|[2305.07943](http://arxiv.org/abs/2305.07943)|**[link](https://github.com/roylin1229/IIB_descriptor)**|
|**2023-05-11**|**Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems**|Nathan Hughes et.al.|[2305.07154](http://arxiv.org/abs/2305.07154)|**[link](https://github.com/mit-spark/hydra)**|
|**2023-05-09**|**Visual Place Recognition with Low-Resolution Images**|Mihnea-Alexandru Tomita et.al.|[2305.05776](http://arxiv.org/abs/2305.05776)|null|
|**2023-05-09**|**Vision-Language Models in Remote Sensing: Current Progress and Future Trends**|Congcong Wen et.al.|[2305.05726](http://arxiv.org/abs/2305.05726)|null|
|**2023-05-09**|**An Evaluation and Ranking of Different Voting Schemes for Improved Visual Place Recognition**|Maria Waheed et.al.|[2305.05705](http://arxiv.org/abs/2305.05705)|null|
|**2023-05-09**|**Region-based Contrastive Pretraining for Medical Image Retrieval with Anatomic Query**|Ho Hin Lee et.al.|[2305.05598](http://arxiv.org/abs/2305.05598)|null|
|**2023-05-09**|**ColonMapper: topological mapping and localization for colonoscopy**|Javier Morlana et.al.|[2305.05546](http://arxiv.org/abs/2305.05546)|null|
|**2023-05-09**|**Eiffel Tower: A Deep-Sea Underwater Dataset for Long-Term Visual Localization**|Clémentin Boittiaux et.al.|[2305.05301](http://arxiv.org/abs/2305.05301)|**[link](https://github.com/clementinboittiaux/sfm-pipeline)**|
|**2023-05-09**|**Patch-DrosoNet: Classifying Image Partitions With Fly-Inspired Models For Lightweight Visual Place Recognition**|Bruno Arcanjo et.al.|[2305.05256](http://arxiv.org/abs/2305.05256)|null|
|**2023-05-09**|**Adapt and Align to Improve Zero-Shot Sketch-Based Image Retrieval**|Shiyin Dong et.al.|[2305.05144](http://arxiv.org/abs/2305.05144)|null|
|**2023-05-08**|**Hierarchical Visual Localization Based on Sparse Feature Pyramid for Adaptive Reduction of Keypoint Map Size**|Andrei Potapov et.al.|[2305.04856](http://arxiv.org/abs/2305.04856)|null|
|**2023-05-08**|**Privacy-Preserving Representations are not Enough -- Recovering Scene Content from Camera Poses**|Kunal Chelani et.al.|[2305.04603](http://arxiv.org/abs/2305.04603)|**[link](https://github.com/kunalchelani/objectpositioningfromposes)**|
|**2023-05-06**|**Keyword-Based Diverse Image Retrieval by Semantics-aware Contrastive Learning and Transformer**|Minyi Zhao et.al.|[2305.04072](http://arxiv.org/abs/2305.04072)|null|
|**2023-05-06**|**Fairness in Image Search: A Study of Occupational Stereotyping in Image Retrieval and its Debiasing**|Swagatika Dash et.al.|[2305.03881](http://arxiv.org/abs/2305.03881)|**[link](https://github.com/swagatikadash010/gender_age)**|
|**2023-05-05**|**COLA: How to adapt vision-language models to Compose Objects Localized with Attributes?**|Arijit Ray et.al.|[2305.03689](http://arxiv.org/abs/2305.03689)|**[link](https://github.com/arijitray1993/COLA)**|
|**2023-05-05**|**HSCNet++: Hierarchical Scene Coordinate Classification and Regression for Visual Localization with Transformer**|Shuzhe Wang et.al.|[2305.03595](http://arxiv.org/abs/2305.03595)|null|
|**2023-05-05**|**WWFedCBMIR: World-Wide Federated Content-Based Medical Image Retrieval**|Zahra Tabatabaei et.al.|[2305.03383](http://arxiv.org/abs/2305.03383)|null|
|**2023-05-04**|**Boundary-aware Backward-Compatible Representation via Adversarial Learning in Image Retrieval**|Tan Pan et.al.|[2305.02610](http://arxiv.org/abs/2305.02610)|**[link](https://github.com/ashespt/advbct)**|
|**2023-05-03**|**Learning-based Relational Object Matching Across Views**|Cathrin Elich et.al.|[2305.02398](http://arxiv.org/abs/2305.02398)|null|
|**2023-05-05**|**A Neural Divide-and-Conquer Reasoning Framework for Image Retrieval from Linguistically Complex Text**|Yunxin Li et.al.|[2305.02265](http://arxiv.org/abs/2305.02265)|**[link](https://github.com/yunxinli/ndcr)**|
|**2023-05-03**|**AV-SAM: Segment Anything Model Meets Audio-Visual Localization and Segmentation**|Shentong Mo et.al.|[2305.01836](http://arxiv.org/abs/2305.01836)|null|
|**2023-04-30**|**Second-order Anisotropic Gaussian Directional Derivative Filters for Blob Detection**|Jie Ren et.al.|[2305.00435](http://arxiv.org/abs/2305.00435)|null|
|**2023-04-28**|**SFD2: Semantic-guided Feature Detection and Description**|Fei Xue et.al.|[2304.14845](http://arxiv.org/abs/2304.14845)|**[link](https://github.com/feixue94/sfd2)**|
|**2023-04-28**|**Quantum enhanced non-interferometric quantitative phase imaging**|Giuseppe Ortolano et.al.|[2304.14727](http://arxiv.org/abs/2304.14727)|null|
|**2023-04-26**|**Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams**|Yun Chang et.al.|[2304.13487](http://arxiv.org/abs/2304.13487)|null|
|**2023-04-27**|**STIR: Siamese Transformer for Image Retrieval Postprocessing**|Aleksei Shabanov et.al.|[2304.13393](http://arxiv.org/abs/2304.13393)|null|
|**2023-04-25**|**DualSlide: Global-to-Local Sketching Interface for Slide Content and Layout Design**|Jiahao Weng et.al.|[2304.12506](http://arxiv.org/abs/2304.12506)|null|
|**2023-04-24**|**Rank Flow Embedding for Unsupervised and Semi-Supervised Manifold Learning**|Lucas Pascotti Valem et.al.|[2304.12448](http://arxiv.org/abs/2304.12448)|**[link](https://github.com/UDLF/UDLF)**|
|**2023-04-23**|**IDLL: Inverse Depth Line based Visual Localization in Challenging Environments**|Wanting Li et.al.|[2304.11748](http://arxiv.org/abs/2304.11748)|null|
|**2023-04-23**|**Class-Specific Variational Auto-Encoder for Content-Based Image Retrieval**|Mehdi Rafiei et.al.|[2304.11734](http://arxiv.org/abs/2304.11734)|null|
|**2023-04-17**|**Features-over-the-Air: Contrastive Learning Enabled Cooperative Edge Inference**|Haotian Wu et.al.|[2304.08221](http://arxiv.org/abs/2304.08221)|null|
|**2023-04-17**|**NeRF-Loc: Visual Localization with Conditional Neural Radiance Field**|Jianlin Liu et.al.|[2304.07979](http://arxiv.org/abs/2304.07979)|**[link](https://github.com/jenningsl/nerf-loc)**|
|**2023-04-16**|**Bent & Broken Bicycles: Leveraging synthetic data for damaged object re-identification**|Luca Piano et.al.|[2304.07883](http://arxiv.org/abs/2304.07883)|null|
|**2023-04-16**|**Language Guided Local Infiltration for Interactive Image Retrieval**|Fuxiang Huang et.al.|[2304.07747](http://arxiv.org/abs/2304.07747)|null|
|**2023-04-16**|**Long-term Visual Localization with Mobile Sensors**|Shen Yan et.al.|[2304.07691](http://arxiv.org/abs/2304.07691)|null|
|**2023-04-16**|**Multimodal Representation Learning of Cardiovascular Magnetic Resonance Imaging**|Jielin Qiu et.al.|[2304.07675](http://arxiv.org/abs/2304.07675)|null|
|**2023-04-14**|**CoPR: Towards Accurate Visual Localization With Continuous Place-descriptor Regression**|Mubariz Zaffar et.al.|[2304.07426](http://arxiv.org/abs/2304.07426)|null|
|**2023-04-14**|**FM-Loc: Using Foundation Models for Improved Vision-based Localization**|Reihaneh Mirjalili et.al.|[2304.07058](http://arxiv.org/abs/2304.07058)|null|
|**2023-04-17**|**Toward Real-Time Image Annotation Using Marginalized Coupled Dictionary Learning**|Seyed Mahdi Roostaiyan et.al.|[2304.06907](http://arxiv.org/abs/2304.06907)|**[link](https://github.com/hamid-amiri/mcdl-image-annotation)**|
|**2023-04-17**|**You are here! Finding position and orientation on a 2D map from a single image: The Flatlandia localization problem and dataset**|Matteo Toso et.al.|[2304.06373](http://arxiv.org/abs/2304.06373)|**[link](https://github.com/IIT-PAVIS/Flatlandia)**|
|**2023-04-12**|**Open-TransMind: A New Baseline and Benchmark for 1st Foundation Model Challenge of Intelligent Transportation**|Yifeng Shi et.al.|[2304.06051](http://arxiv.org/abs/2304.06051)|**[link](https://github.com/Traffic-X/Open-TransMind)**|
|**2023-04-12**|**Visual Localization using Imperfect 3D Models from the Internet**|Vojtech Panek et.al.|[2304.05947](http://arxiv.org/abs/2304.05947)|**[link](https://github.com/v-pnk/cadloc)**|
|**2023-04-12**|**Are Local Features All You Need for Cross-Domain Visual Place Recognition?**|Giovanni Barbarani et.al.|[2304.05887](http://arxiv.org/abs/2304.05887)|**[link](https://github.com/gbarbarani/re-ranking-for-vpr)**|
|**2023-04-12**|**Unicom: Universal and Compact Representation Learning for Image Retrieval**|Xiang An et.al.|[2304.05884](http://arxiv.org/abs/2304.05884)|**[link](https://github.com/deepglint/unicom)**|
|**2023-04-12**|**SGL: Structure Guidance Learning for Camera Localization**|Xudong Zhang et.al.|[2304.05571](http://arxiv.org/abs/2304.05571)|null|
|**2023-04-14**|**Loop Closure Detection Based on Object-level Spatial Layout and Semantic Consistency**|Xingwu Ji et.al.|[2304.05146](http://arxiv.org/abs/2304.05146)|**[link](https://github.com/jixingwu/ss-lcd)**|
|**2023-04-10**|**CAVL: Learning Contrastive and Adaptive Representations of Vision and Language**|Shentong Mo et.al.|[2304.04399](http://arxiv.org/abs/2304.04399)|null|
|**2023-04-09**|**Unsupervised Multi-Criteria Adversarial Detection in Deep Image Retrieval**|Yanru Xiao et.al.|[2304.04228](http://arxiv.org/abs/2304.04228)|null|
|**2023-04-08**|**SGIDN-LCD: An Appearance-based Loop Closure Detection Algorithm using Superpixel Grids and Incremental Dynamic Nodes**|Baosheng Zhang et.al.|[2304.03872](http://arxiv.org/abs/2304.03872)|null|
|**2023-04-06**|**$R^{2}$Former: Unified $R$etrieval and $R$ eranking Transformer for Place Recognition**|Sijie Zhu et.al.|[2304.03410](http://arxiv.org/abs/2304.03410)|null|
|**2023-04-06**|**Distributed formation-enforcing control for UAVs robust to observation noise in relative pose measurements**|Viktor Walter et.al.|[2304.03057](http://arxiv.org/abs/2304.03057)|**[link](https://github.com/ctu-mrs/difec-ron)**|
|**2023-04-05**|**Efficient OCR for Building a Diverse Digital History**|Jacob Carlson et.al.|[2304.02737](http://arxiv.org/abs/2304.02737)|**[link](https://github.com/dell-research-harvard/effocr)**|
|**2023-04-05**|**LogoNet: a fine-grained network for instance-level logo sketch retrieval**|Binbin Feng et.al.|[2304.02214](http://arxiv.org/abs/2304.02214)|**[link](https://github.com/abin333/logonet)**|
|**2023-04-04**|**OrienterNet: Visual Localization in 2D Public Maps with Neural Matching**|Paul-Edouard Sarlin et.al.|[2304.02009](http://arxiv.org/abs/2304.02009)|**[link](https://github.com/facebookresearch/OrienterNet)**|
|**2023-04-04**|**Cross-Domain Image Captioning with Discriminative Finetuning**|Roberto Dessì et.al.|[2304.01662](http://arxiv.org/abs/2304.01662)|**[link](https://github.com/facebookresearch/EGG)**|
|**2023-04-02**|**Learning Similarity between Scene Graphs and Images with Transformers**|Yuren Cong et.al.|[2304.00590](http://arxiv.org/abs/2304.00590)|**[link](https://github.com/yrcong/learning_similarity_between_graphs_images)**|
|**2023-04-01**|**NPR: Nocturnal Place Recognition in Street**|Bingxi Liu et.al.|[2304.00276](http://arxiv.org/abs/2304.00276)|null|
|**2023-03-31**|**Unsupervised crack detection on complex stone masonry surfaces**|Panagiotis Agrafiotis et.al.|[2303.17989](http://arxiv.org/abs/2303.17989)|null|
|**2023-03-30**|**If At First You Don't Succeed: Test Time Re-ranking for Zero-shot, Cross-domain Retrieval**|Finlay G. C. Hudson et.al.|[2303.17703](http://arxiv.org/abs/2303.17703)|null|
|**2023-03-30**|**Vision-Language Modelling For Radiological Imaging and Reports In The Low Data Regime**|Rhydian Windsor et.al.|[2303.17644](http://arxiv.org/abs/2303.17644)|null|
|**2023-03-30**|**3D Line Mapping Revisited**|Shaohui Liu et.al.|[2303.17504](http://arxiv.org/abs/2303.17504)|**[link](https://github.com/cvg/limap)**|
|**2023-03-30**|**Methods and advancement of content-based fashion image retrieval: A Review**|Amin Muhammad Shoib et.al.|[2303.17371](http://arxiv.org/abs/2303.17371)|null|
|**2023-03-30**|**Adaptive Cross Batch Normalization for Metric Learning**|Thalaiyasingam Ajanthan et.al.|[2303.17127](http://arxiv.org/abs/2303.17127)|null|
|**2023-03-30**|**MaMMUT: A Simple Architecture for Joint Learning for MultiModal Tasks**|Weicheng Kuo et.al.|[2303.16839](http://arxiv.org/abs/2303.16839)|null|
|**2023-03-29**|**Sketch-an-Anchor: Sub-epoch Fast Model Adaptation for Zero-shot Sketch-based Image Retrieval**|Leo Sampaio Ferraz Ribeiro et.al.|[2303.16769](http://arxiv.org/abs/2303.16769)|null|
|**2023-03-29**|**Bi-directional Training for Composed Image Retrieval via Text Prompt Learning**|Zheyuan Liu et.al.|[2303.16604](http://arxiv.org/abs/2303.16604)|**[link](https://github.com/Cuberick-Orion/Bi-Blip4CIR)**|
|**2023-03-27**|**Model Cascades for Efficient Image Search**|Robert Hönig et.al.|[2303.15595](http://arxiv.org/abs/2303.15595)|null|
|**2023-03-27**|**Zero-Shot Composed Image Retrieval with Textual Inversion**|Alberto Baldrati et.al.|[2303.15247](http://arxiv.org/abs/2303.15247)|**[link](https://github.com/miccunifi/circo)**|
|**2023-03-27**|**What Can Human Sketches Do for Object Detection?**|Pinaki Nath Chowdhury et.al.|[2303.15149](http://arxiv.org/abs/2303.15149)|null|
|**2023-03-25**|**Zero-Shot Everything Sketch-Based Image Retrieval, and in Explainable Style**|Fengyin Lin et.al.|[2303.14348](http://arxiv.org/abs/2303.14348)|**[link](https://github.com/buptlinfy/zse-sbir)**|
|**2023-03-24**|**A-MuSIC: An Adaptive Ensemble System For Visual Place Recognition In Changing Environments**|Bruno Arcanjo et.al.|[2303.14247](http://arxiv.org/abs/2303.14247)|null|
|**2023-03-24**|**PanoVPR: Towards Unified Perspective-to-Equirectangular Visual Place Recognition via Sliding Windows across the Panoramic View**|Ze Shi et.al.|[2303.14095](http://arxiv.org/abs/2303.14095)|**[link](https://github.com/zafirshi/panovpr)**|
|**2023-03-24**|**Exploiting Unlabelled Photos for Stronger Fine-Grained SBIR**|Aneeshan Sain et.al.|[2303.13779](http://arxiv.org/abs/2303.13779)|null|
|**2023-03-28**|**CLIP for All Things Zero-Shot Sketch-Based Image Retrieval, Fine-Grained or Not**|Aneeshan Sain et.al.|[2303.13440](http://arxiv.org/abs/2303.13440)|null|
|**2023-03-22**|**Reliable and Efficient Evaluation of Adversarial Robustness for Deep Hashing-Based Retrieval**|Xunguang Wang et.al.|[2303.12658](http://arxiv.org/abs/2303.12658)|null|
|**2023-03-21**|**CompoDiff: Versatile Composed Image Retrieval With Latent Diffusion**|Geonmo Gu et.al.|[2303.11916](http://arxiv.org/abs/2303.11916)|**[link](https://github.com/navervision/compodiff)**|
|**2023-03-21**|**LIMITR: Leveraging Local Information for Medical Image-Text Representation**|Gefen Dawidowicz et.al.|[2303.11755](http://arxiv.org/abs/2303.11755)|null|
|**2023-03-25**|**Data-efficient Large Scale Place Recognition with Graded Similarity Supervision**|Maria Leyva-Vallina et.al.|[2303.11739](http://arxiv.org/abs/2303.11739)|**[link](https://github.com/marialeyvallina/generalized_contrastive_loss)**|
|**2023-03-20**|**Picture that Sketch: Photorealistic Image Generation from Abstract Sketches**|Subhadeep Koley et.al.|[2303.11162](http://arxiv.org/abs/2303.11162)|null|
|**2023-03-19**|**Deep Declarative Dynamic Time Warping for End-to-End Learning of Alignment Paths**|Ming Xu et.al.|[2303.10778](http://arxiv.org/abs/2303.10778)|**[link](https://github.com/mingu6/declarativedtw)**|
|**2023-03-17**|**MRIS: A Multi-modal Retrieval Approach for Image Synthesis on Diverse Modalities**|Boqi Chen et.al.|[2303.10249](http://arxiv.org/abs/2303.10249)|null|
|**2023-03-17**|**IRGen: Generative Modeling for Image Retrieval**|Yidan Zhang et.al.|[2303.10126](http://arxiv.org/abs/2303.10126)|**[link](https://github.com/yakt00/IRGen)**|
|**2023-03-16**|**Data Roaming and Early Fusion for Composed Image Retrieval**|Matan Levy et.al.|[2303.09429](http://arxiv.org/abs/2303.09429)|**[link](https://github.com/levymsn/LaSCo)**|
|**2023-03-16**|**Towards a Smaller Student: Capacity Dynamic Distillation for Efficient Image Retrieval**|Yi Xie et.al.|[2303.09230](http://arxiv.org/abs/2303.09230)|null|
|**2023-03-16**|**Metric-Free Exploration for Topological Mapping by Task and Motion Imitation in Feature Space**|Yuhang He et.al.|[2303.09192](http://arxiv.org/abs/2303.09192)|null|
|**2023-03-16**|**Unsupervised Facial Expression Representation Learning with Contrastive Local Warping**|Fanglei Xue et.al.|[2303.09034](http://arxiv.org/abs/2303.09034)|null|
|**2023-03-15**|**A Triplet-loss Dilated Residual Network for High-Resolution Representation Learning in Image Retrieval**|Saeideh Yousefzadeh et.al.|[2303.08398](http://arxiv.org/abs/2303.08398)|null|
|**2023-03-14**|**Data-Free Sketch-Based Image Retrieval**|Abhra Chaudhuri et.al.|[2303.07775](http://arxiv.org/abs/2303.07775)|**[link](https://github.com/abhrac/data-free-sbir)**|
|**2023-03-14**|**PATS: Patch Area Transportation with Subdivision for Local Feature Matching**|Junjie Ni et.al.|[2303.07700](http://arxiv.org/abs/2303.07700)|null|
|**2023-03-10**|**Robotic Applications of Pre-Trained Vision-Language Models to Various Recognition Behaviors**|Kento Kawaharazuka et.al.|[2303.05674](http://arxiv.org/abs/2303.05674)|null|
|**2023-03-09**|**Dominating Set Database Selection for Visual Place Recognition**|Anastasiia Kornilova et.al.|[2303.05123](http://arxiv.org/abs/2303.05123)|null|
|**2023-03-07**|**Graph Neural Networks in Vision-Language Image Understanding: A Survey**|Henry Senior et.al.|[2303.03761](http://arxiv.org/abs/2303.03761)|null|
|**2023-03-07**|**Sketch-based Medical Image Retrieval**|Kazuma Kobayashi et.al.|[2303.03633](http://arxiv.org/abs/2303.03633)|**[link](https://github.com/kaz-k/sketch-based-medical-image-retrieval)**|
|**2023-03-06**|**Visual Place Recognition: A Tutorial**|Stefan Schubert et.al.|[2303.03281](http://arxiv.org/abs/2303.03281)|**[link](https://github.com/stschubert/vpr_tutorial)**|
|**2023-03-06**|**MABNet: Master Assistant Buddy Network with Hybrid Learning for Image Retrieval**|Rohit Agarwal et.al.|[2303.03050](http://arxiv.org/abs/2303.03050)|**[link](https://github.com/rohit102497/mabnet)**|
|**2023-03-06**|**Improving Transformer-based Image Matching by Cascaded Capturing Spatially Informative Keypoints**|Chenjie Cao et.al.|[2303.02885](http://arxiv.org/abs/2303.02885)|**[link](https://github.com/ewrfcas/casmtr)**|
|**2023-03-05**|**Composing Mood Board with User Feedback in Concept Space**|Shin Sano et.al.|[2303.02547](http://arxiv.org/abs/2303.02547)|null|
|**2023-03-04**|**FAME-ViL: Multi-Tasking Vision-Language Model for Heterogeneous Fashion Tasks**|Xiao Han et.al.|[2303.02483](http://arxiv.org/abs/2303.02483)|**[link](https://github.com/brandonhanx/fame-vil)**|
|**2023-03-09**|**Self-Supervised Learning for Place Representation Generalization across Appearance Changes**|Mohamed Adel Musallam et.al.|[2303.02370](http://arxiv.org/abs/2303.02370)|null|
|**2023-03-03**|**MixVPR: Feature Mixing for Visual Place Recognition**|Amar Ali-bey et.al.|[2303.02190](http://arxiv.org/abs/2303.02190)|**[link](https://github.com/amaralibey/mixvpr)**|
|**2023-03-01**|**A Complementarity-Based Switch-Fuse System for Improved Visual Place Recognition**|Maria Waheed et.al.|[2303.00714](http://arxiv.org/abs/2303.00714)|null|
|**2023-03-01**|**ORCHNet: A Robust Global Feature Aggregation approach for 3D LiDAR-based Place recognition in Orchards**|T. Barros et.al.|[2303.00477](http://arxiv.org/abs/2303.00477)|**[link](https://github.com/cybonic/orchnet)**|
|**2023-03-03**|**Renderable Neural Radiance Map for Visual Navigation**|Obin Kwon et.al.|[2303.00304](http://arxiv.org/abs/2303.00304)|null|
|**2023-03-01**|**Region Prediction for Efficient Robot Localization on Large Maps**|Matteo Scucchia et.al.|[2303.00295](http://arxiv.org/abs/2303.00295)|**[link](https://github.com/mi-biolab/region-learner)**|
|**2023-02-28**|**OEKG: The Open Event Knowledge Graph**|Simon Gottschalk et.al.|[2302.14688](http://arxiv.org/abs/2302.14688)|null|
|**2023-02-28**|**Global Proxy-based Hard Mining for Visual Place Recognition**|Amar Ali-bey et.al.|[2302.14217](http://arxiv.org/abs/2302.14217)|**[link](https://github.com/amaralibey/gpm)**|
|**2023-02-27**|**Efficient Informed Proposals for Discrete Distributions via Newton's Series Approximation**|Yue Xiang et.al.|[2302.13929](http://arxiv.org/abs/2302.13929)|**[link](https://github.com/dongyaozhu/newton-proposal-for-discrete-sampling)**|
|**2023-02-26**|**Data-Efficient Sequence-Based Visual Place Recognition with Highly Compressed JPEG Images**|Mihnea-Alexandru Tomita et.al.|[2302.13314](http://arxiv.org/abs/2302.13314)|null|
|**2023-02-26**|**Learning cross space mapping via DNN using large scale click-through logs**|Wei Yu et.al.|[2302.13275](http://arxiv.org/abs/2302.13275)|null|
|**2023-02-25**|**DeepBrainPrint: A Novel Contrastive Framework for Brain MRI Re-Identification**|Lemuel Puglisi et.al.|[2302.13057](http://arxiv.org/abs/2302.13057)|null|
|**2023-02-23**|**Teaching CLIP to Count to Ten**|Roni Paiss et.al.|[2302.12066](http://arxiv.org/abs/2302.12066)|null|
|**2023-02-22**|**Steerable Equivariant Representation Learning**|Sangnie Bhardwaj et.al.|[2302.11349](http://arxiv.org/abs/2302.11349)|null|
|**2023-02-21**|**iQPP: A Benchmark for Image Query Performance Prediction**|Eduard Poesina et.al.|[2302.10126](http://arxiv.org/abs/2302.10126)|**[link](https://github.com/eduard6421/iqpp)**|
|**2023-02-20**|**Ontology-aware Network for Zero-shot Sketch-based Image Retrieval**|Haoxiang Zhang et.al.|[2302.10040](http://arxiv.org/abs/2302.10040)|null|
|**2023-02-20**|**TBPos: Dataset for Large-Scale Precision Visual Localization**|Masud Fahim et.al.|[2302.09825](http://arxiv.org/abs/2302.09825)|**[link](https://gitlab.com/jboutell/tbpos)**|
|**2023-02-17**|**Towards Unifying Medical Vision-and-Language Pre-training via Soft Prompts**|Zhihong Chen et.al.|[2302.08958](http://arxiv.org/abs/2302.08958)|**[link](https://github.com/zhjohnchan/ptunifier)**|
|**2023-02-22**|**Fashion Image Retrieval with Multi-Granular Alignment**|Jinkuan Zhu et.al.|[2302.08902](http://arxiv.org/abs/2302.08902)|null|
|**2023-02-15**|**Unsupervised Hashing via Similarity Distribution Calibration**|Kam Woh Ng et.al.|[2302.07669](http://arxiv.org/abs/2302.07669)|**[link](https://github.com/kamwoh/sdc)**|
|**2023-02-13**|**Render-and-Compare: Cross-View 6 DoF Localization from Noisy Prior**|Shen Yan et.al.|[2302.06287](http://arxiv.org/abs/2302.06287)|**[link](https://github.com/choyaa/render2loc)**|
|**2023-02-13**|**Contour Context: Abstract Structural Distribution for 3D LiDAR Loop Detection and Metric Pose Estimation**|Binqian Jiang et.al.|[2302.06149](http://arxiv.org/abs/2302.06149)|**[link](https://github.com/lewisjiang/contour-context)**|
|**2023-02-13**|**Correspondence-Free Domain Alignment for Unsupervised Cross-Domain Image Retrieval**|Xu Wang et.al.|[2302.06081](http://arxiv.org/abs/2302.06081)|**[link](https://github.com/wangxu-scu/CoDA)**|
|**2023-02-11**|**Sketch Less Face Image Retrieval: A New Challenge**|Dawei Dai et.al.|[2302.05576](http://arxiv.org/abs/2302.05576)|**[link](https://github.com/ddw2aigroup2cqupt/slfir)**|
|**2023-02-10**|**Is multi-modal vision supervision beneficial to language?**|Avinash Madasu et.al.|[2302.05016](http://arxiv.org/abs/2302.05016)|**[link](https://github.com/avinashsai/mml)**|
|**2023-02-06**|**Pic2Word: Mapping Pictures to Words for Zero-shot Composed Image Retrieval**|Kuniaki Saito et.al.|[2302.03084](http://arxiv.org/abs/2302.03084)|**[link](https://github.com/google-research/composed_image_retrieval)**|
|**2023-02-06**|**Probabilistic Contrastive Learning Recovers the Correct Aleatoric Uncertainty of Ambiguous Inputs**|Michael Kirchhof et.al.|[2302.02865](http://arxiv.org/abs/2302.02865)|**[link](https://github.com/mkirchhof/probabilistic_contrastive_learning)**|
|**2023-02-03**|**Simple, Effective and General: A New Backbone for Cross-view Image Geo-localization**|Yingying Zhu et.al.|[2302.01572](http://arxiv.org/abs/2302.01572)|**[link](https://github.com/yanghongji2007/saig)**|
|**2023-02-04**|**Bayesian Metric Learning for Uncertainty Quantification in Image Retrieval**|Frederik Warburg et.al.|[2302.01332](http://arxiv.org/abs/2302.01332)|**[link](https://github.com/frederikwarburg/bayesian-metric-learning)**|
|**2023-01-31**|**Grounding Language Models to Images for Multimodal Generation**|Jing Yu Koh et.al.|[2301.13823](http://arxiv.org/abs/2301.13823)|**[link](https://github.com/kohjingyu/fromage)**|
|**2023-01-31**|**UPop: Unified and Progressive Pruning for Compressing Vision-Language Transformers**|Dachuan Shi et.al.|[2301.13741](http://arxiv.org/abs/2301.13741)|**[link](https://github.com/sdc17/upop)**|
|**2023-01-23**|**Lexi: Self-Supervised Learning of the UI Language**|Pratyay Banerjee et.al.|[2301.10165](http://arxiv.org/abs/2301.10165)|**[link](https://github.com/microsoft/uicaption)**|
|**2023-01-17**|**Distribution Aligned Feature Clustering for Zero-Shot Sketch-Based Image Retrieval**|Yuchen Wu et.al.|[2301.06685](http://arxiv.org/abs/2301.06685)|null|
|**2023-01-19**|**High-bandwidth Close-Range Information Transport through Light Pipes**|Joowon Lim et.al.|[2301.06496](http://arxiv.org/abs/2301.06496)|null|
|**2023-01-13**|**A LiDAR-Inertial-Visual SLAM System with Loop Detection**|Kangcheng Liu et.al.|[2301.05604](http://arxiv.org/abs/2301.05604)|null|
|**2023-01-12**|**GH-Feat: Learning Versatile Generative Hierarchical Features from GANs**|Yinghao Xu et.al.|[2301.05315](http://arxiv.org/abs/2301.05315)|null|
|**2023-01-10**|**Pix2Map: Cross-modal Retrieval for Inferring Street Maps from Images**|Xindi Wu et.al.|[2301.04224](http://arxiv.org/abs/2301.04224)|null|
|**2023-01-10**|**Collaborative Semantic Communication at the Edge**|Wing Fei Lo et.al.|[2301.03996](http://arxiv.org/abs/2301.03996)|null|
|**2023-01-10**|**Online Backfilling with No Regret for Large-Scale Image Retrieval**|Seonguk Seo et.al.|[2301.03767](http://arxiv.org/abs/2301.03767)|null|
|**2023-01-06**|**CyberLoc: Towards Accurate Long-term Visual Localization**|Liu Liu et.al.|[2301.02403](http://arxiv.org/abs/2301.02403)|null|
|**2023-01-05**|**A Probabilistic Framework for Visual Localization in Ambiguous Scenes**|Fereidoon Zangeneh et.al.|[2301.02086](http://arxiv.org/abs/2301.02086)|**[link](https://github.com/efreidun/vapor)**|
|**2022-12-31**|**4Seasons: Benchmarking Visual SLAM and Long-Term Localization for Autonomous Driving in Challenging Conditions**|Patrick Wenzel et.al.|[2301.01147](http://arxiv.org/abs/2301.01147)|null|
|**2022-12-30**|**HPointLoc: Point-based Indoor Place Recognition using Synthetic RGB-D Images**|Dmitry Yudin et.al.|[2212.14649](http://arxiv.org/abs/2212.14649)|**[link](https://github.com/metra4ok/hpointloc)**|
|**2022-12-27**|**Noise-aware Learning from Web-crawled Image-Text Data for Image Captioning**|Wooyoung Kang et.al.|[2212.13563](http://arxiv.org/abs/2212.13563)|**[link](https://github.com/kakaobrain/noc)**|
|**2022-12-23**|**SuperGF: Unifying Local and Global Features for Visual Localization**|Wenzheng Song et.al.|[2212.13105](http://arxiv.org/abs/2212.13105)|null|
|**2022-12-24**|**GraffMatch: Global Matching of 3D Lines and Planes for Wide Baseline LiDAR Registration**|Parker C. Lusk et.al.|[2212.12745](http://arxiv.org/abs/2212.12745)|null|
|**2022-12-19**|**From a Bird's Eye View to See: Joint Camera and Subject Registration without the Camera Calibration**|Zekun Qian et.al.|[2212.09298](http://arxiv.org/abs/2212.09298)|**[link](https://github.com/zekunqian/bevsee)**|
|**2022-12-14**|**The Infinite Index: Information Retrieval on Generative Text-To-Image Models**|Niklas Deckers et.al.|[2212.07476](http://arxiv.org/abs/2212.07476)|null|
|**2022-12-14**|**Shared Coupling-bridge for Weakly Supervised Local Feature Learning**|Jiayuan Sun et.al.|[2212.07047](http://arxiv.org/abs/2212.07047)|**[link](https://github.com/sunjiayuanro/scfeat)**|
|**2022-12-08**|**Group Generalized Mean Pooling for Vision Transformer**|Byungsoo Ko et.al.|[2212.04114](http://arxiv.org/abs/2212.04114)|null|
|**2022-12-12**|**Diffusion Art or Digital Forgery? Investigating Data Replication in Diffusion Models**|Gowthami Somepalli et.al.|[2212.03860](http://arxiv.org/abs/2212.03860)|null|
|**2022-12-07**|**LSVL: Large-scale season-invariant visual localization for UAVs**|Jouko Kinnari et.al.|[2212.03581](http://arxiv.org/abs/2212.03581)|null|
|**2022-12-06**|**ADIR: Adaptive Diffusion for Image Reconstruction**|Shady Abu-Hussein et.al.|[2212.03221](http://arxiv.org/abs/2212.03221)|null|
|**2022-12-08**|**Privacy-Preserving Visual Localization with Event Cameras**|Junho Kim et.al.|[2212.03177](http://arxiv.org/abs/2212.03177)|**[link](https://github.com/82magnolia/event_localization)**|
|**2022-12-06**|**Semantic Communication for Internet of Vehicles: A Multi-User Cooperative Approach**|Wenjun Xu et.al.|[2212.03037](http://arxiv.org/abs/2212.03037)|null|
|**2022-12-06**|**Attention-Enhanced Cross-modal Localization Between 360 Images and Point Clouds**|Zhipeng Zhao et.al.|[2212.02757](http://arxiv.org/abs/2212.02757)|null|
|**2022-12-04**|**Fast and Lightweight Scene Regressor for Camera Relocalization**|Thuan B. Bui et.al.|[2212.01830](http://arxiv.org/abs/2212.01830)|**[link](https://github.com/ais-lab/feat2map)**|
|**2022-12-02**|**Information Retrieval from the Digitized Books**|Riya Gupta et.al.|[2212.00999](http://arxiv.org/abs/2212.00999)|null|
|**2022-12-09**|**StructVPR: Distill Structural Knowledge with Weighting Samples for Visual Place Recognition**|Yanqing Shen et.al.|[2212.00937](http://arxiv.org/abs/2212.00937)|null|
|**2022-11-30**|**Self-Supervised Feature Learning for Long-Term Metric Visual Localization**|Yuxuan Chen et.al.|[2212.00122](http://arxiv.org/abs/2212.00122)|null|
|**2022-11-30**|**SGDraw: Scene Graph Drawing Interface Using Object-Oriented Representation**|Tianyu Zhang et.al.|[2211.16697](http://arxiv.org/abs/2211.16697)|**[link](https://github.com/zty0304/sgdraw)**|
|**2022-11-28**|**SLAN: Self-Locator Aided Network for Cross-Modal Understanding**|Jiang-Tian Zhai et.al.|[2211.16208](http://arxiv.org/abs/2211.16208)|null|
|**2022-11-29**|**RankDNN: Learning to Rank for Few-shot Learning**|Qianyu Guo et.al.|[2211.15320](http://arxiv.org/abs/2211.15320)|**[link](https://github.com/guoqianyu-alberta/rankdnn)**|
|**2022-11-28**|**Safety-quantifiable Line Feature-based Monocular Visual Localization with 3D Prior Map**|Xi Zheng et.al.|[2211.15127](http://arxiv.org/abs/2211.15127)|null|
|**2022-11-28**|**FeatureBooster: Boosting Feature Descriptors with a Lightweight Neural Network**|Xinjiang Wang et.al.|[2211.15069](http://arxiv.org/abs/2211.15069)|**[link](https://github.com/sjtu-visys/featurebooster)**|
|**2022-11-27**|**BEV-Locator: An End-to-end Visual Semantic Localization Network Using Multi-View Images**|Zhihuang Zhang et.al.|[2211.14927](http://arxiv.org/abs/2211.14927)|null|
|**2022-11-27**|**A Faster, Lighter and Stronger Deep Learning-Based Approach for Place Recognition**|Rui Huang et.al.|[2211.14864](http://arxiv.org/abs/2211.14864)|null|
|**2022-11-26**|**Visual Place Recognition**|Bailu Guo et.al.|[2211.14533](http://arxiv.org/abs/2211.14533)|null|
|**2022-11-26**|**Instance-level Heterogeneous Domain Adaptation for Limited-labeled Sketch-to-Photo Retrieval**|Fan Yang et.al.|[2211.14515](http://arxiv.org/abs/2211.14515)|**[link](https://github.com/fandulu/IHDA)**|
|**2022-11-30**|**Roboflow 100: A Rich, Multi-Domain Object Detection Benchmark**|Floriana Ciaglia et.al.|[2211.13523](http://arxiv.org/abs/2211.13523)|**[link](https://github.com/roboflow-ai/roboflow-100-benchmark)**|
|**2022-11-23**|**InDiReCT: Language-Guided Zero-Shot Deep Metric Learning for Images**|Konstantin Kobs et.al.|[2211.12760](http://arxiv.org/abs/2211.12760)|**[link](https://github.com/lsx-uniwue/indirect)**|
|**2022-11-29**|**Wild-Places: A Large-Scale Dataset for Lidar Place Recognition in Unstructured Natural Environments**|Joshua Knights et.al.|[2211.12732](http://arxiv.org/abs/2211.12732)|**[link](https://github.com/csiro-robotics/Wild-Places)**|
|**2022-11-23**|**FE-Fusion-VPR: Attention-based Multi-Scale Network Architecture for Visual Place Recognition by Fusing Frames and Events**|Kuanxu Hou et.al.|[2211.12244](http://arxiv.org/abs/2211.12244)|null|
|**2022-11-22**|**Multimorbidity Content-Based Medical Image Retrieval Using Proxies**|Yunyan Xing et.al.|[2211.12185](http://arxiv.org/abs/2211.12185)|null|
|**2022-11-22**|**Vision-based localization methods under GPS-denied conditions**|Zihao Lu et.al.|[2211.11988](http://arxiv.org/abs/2211.11988)|null|
|**2022-11-21**|**ESLAM: Efficient Dense SLAM System Based on Hybrid Representation of Signed Distance Fields**|Mohammad Mahdi Johari et.al.|[2211.11704](http://arxiv.org/abs/2211.11704)|null|
|**2022-11-21**|**LISA: Localized Image Stylization with Audio via Implicit Neural Representation**|Seung Hyun Lee et.al.|[2211.11381](http://arxiv.org/abs/2211.11381)|null|
|**2022-11-21**|**NeuMap: Neural Coordinate Mapping by Auto-Transdecoder for Camera Localization**|Shitao Tang et.al.|[2211.11177](http://arxiv.org/abs/2211.11177)|**[link](https://github.com/tangshitao/neumap)**|
|**2022-11-16**|**Improving Feature-based Visual Localization by Geometry-Aided Matching**|Hailin Yu et.al.|[2211.08712](http://arxiv.org/abs/2211.08712)|**[link](https://github.com/openxrlab/xrlocalization)**|
|**2022-11-15**|**LiePoseNet: Heterogeneous Loss Function Based on Lie Group for Significant Speed-up of PoseNet Training Process**|Mikhail Kurenkov et.al.|[2211.08480](http://arxiv.org/abs/2211.08480)|null|
|**2022-11-14**|**Degeneracy removal of spin bands in antiferromagnets with non-interconvertible spin motif pair**|Lin-Ding Yuan et.al.|[2211.07803](http://arxiv.org/abs/2211.07803)|null|
|**2022-11-14**|**Supervised Fine-tuning Evaluation for Long-term Visual Place Recognition**|Farid Alijani et.al.|[2211.07696](http://arxiv.org/abs/2211.07696)|null|
|**2022-11-14**|**Composed Image Retrieval with Text Feedback via Multi-grained Uncertainty Regularization**|Yiyang Chen et.al.|[2211.07394](http://arxiv.org/abs/2211.07394)|**[link](https://github.com/Monoxide-Chen/uncertainty_retrieval)**|
|**2022-11-14**|**Zero-shot Image Captioning by Anchor-augmented Vision-Language Space Alignment**|Junyang Wang et.al.|[2211.07275](http://arxiv.org/abs/2211.07275)|null|
|**2022-11-14**|**ContextCLIP: Contextual Alignment of Image-Text pairs on CLIP visual representations**|Chanda Grover et.al.|[2211.07122](http://arxiv.org/abs/2211.07122)|null|
|**2022-11-14**|**Few-shot Metric Learning: Online Adaptation of Embedding for Retrieval**|Deunsol Jung et.al.|[2211.07116](http://arxiv.org/abs/2211.07116)|null|
|**2022-11-12**|**Partial Visual-Semantic Embedding: Fashion Intelligence System with Sensitive Part-by-Part Learning**|Ryotaro Shimizu et.al.|[2211.06688](http://arxiv.org/abs/2211.06688)|null|
|**2022-11-09**|**Visual Named Entity Linking: A New Dataset and A Baseline**|Wenxiang Sun et.al.|[2211.04872](http://arxiv.org/abs/2211.04872)|**[link](https://github.com/ict-bigdatalab/vnel)**|
|**2022-11-07**|**Ultrafast Image Retrieval from a Holographic Memory Disc for High-Speed Operation of a Shift, Scale, and Rotation Invariant Target Recognition System**|Julian Gamboa et.al.|[2211.03881](http://arxiv.org/abs/2211.03881)|null|
|**2022-11-06**|**A Geometrically Constrained Point Matching based on View-invariant Cross-ratios, and Homography**|Yueh-Cheng Huang et.al.|[2211.03007](http://arxiv.org/abs/2211.03007)|null|
|**2022-11-02**|**Optimizing Fiducial Marker Placement for Improved Visual Localization**|Qiangqiang Huang et.al.|[2211.01513](http://arxiv.org/abs/2211.01513)|**[link](https://github.com/doublestrong/omp)**|
|**2022-11-02**|**A comparison of uncertainty estimation approaches for DNN-based camera localization**|Matteo Vaghi et.al.|[2211.01234](http://arxiv.org/abs/2211.01234)|null|
|**2022-11-02**|**M-SpeechCLIP: Leveraging Large-Scale, Pre-Trained Models for Multilingual Speech to Image Retrieval**|Layne Berry et.al.|[2211.01180](http://arxiv.org/abs/2211.01180)|null|
|**2022-11-11**|**Why is Winoground Hard? Investigating Failures in Visuolinguistic Compositionality**|Anuj Diwan et.al.|[2211.00768](http://arxiv.org/abs/2211.00768)|**[link](https://github.com/ajd12342/why-winoground-hard)**|
|**2022-11-07**|**Fashion-Specific Attributes Interpretation via Dual Gaussian Visual-Semantic Embedding**|Ryotaro Shimizu et.al.|[2210.17417](http://arxiv.org/abs/2210.17417)|null|
|**2022-10-27**|**Structuring User-Generated Content on Social Media with Multimodal Aspect-Based Sentiment Analysis**|Miriam Anschütz et.al.|[2210.15377](http://arxiv.org/abs/2210.15377)|**[link](https://github.com/miriull/multimodal_absa_elbphilharmonie)**|
|**2022-10-27**|**Leveraging Computer Vision Application in Visual Arts: A Case Study on the Use of Residual Neural Network to Classify and Analyze Baroque Paintings**|Daniel Kvak et.al.|[2210.15300](http://arxiv.org/abs/2210.15300)|null|
|**2022-10-27**|**Towards Practicality of Sketch-Based Visual Understanding**|Ayan Kumar Bhunia et.al.|[2210.15146](http://arxiv.org/abs/2210.15146)|null|
|**2022-10-27**|**MMFL-Net: Multi-scale and Multi-granularity Feature Learning for Cross-domain Fashion Retrieval**|Chen Bao et.al.|[2210.15128](http://arxiv.org/abs/2210.15128)|null|
|**2022-10-26**|**FaD-VLP: Fashion Vision-and-Language Pre-training towards Unified Retrieval and Captioning**|Suvir Mirchandani et.al.|[2210.15028](http://arxiv.org/abs/2210.15028)|null|
|**2022-10-26**|**FairCLIP: Social Bias Elimination based on Attribute Prototype Learning and Representation Neutralization**|Junyang Wang et.al.|[2210.14562](http://arxiv.org/abs/2210.14562)|null|
|**2022-11-02**|**A Framework for Collaborative Multi-Robot Mapping using Spectral Graph Wavelets**|Lukas Bernreiter et.al.|[2210.13856](http://arxiv.org/abs/2210.13856)|null|
|**2022-10-27**|**Learning by Hallucinating: Vision-Language Pre-training with Weak Supervision**|Tzu-Jui Julius Wang et.al.|[2210.13591](http://arxiv.org/abs/2210.13591)|null|
|**2022-10-24**|**Reliability-Aware Prediction via Uncertainty Learning for Person Image Retrieval**|Zhaopeng Dou et.al.|[2210.13440](http://arxiv.org/abs/2210.13440)|**[link](https://github.com/dcp15/ual)**|
|**2022-10-23**|**Neural Eigenfunctions Are Structured Representation Learners**|Zhijie Deng et.al.|[2210.12637](http://arxiv.org/abs/2210.12637)|**[link](https://github.com/thudzj/NEigenmaps)**|
|**2022-10-21**|**Boosting vision transformers for image retrieval**|Chull Hwan Song et.al.|[2210.11909](http://arxiv.org/abs/2210.11909)|**[link](https://github.com/dealicious-inc/dtop)**|
|**2022-10-20**|**Communication breakdown: On the low mutual intelligibility between human and neural captioning**|Roberto Dessì et.al.|[2210.11512](http://arxiv.org/abs/2210.11512)|**[link](https://github.com/franfranz/emecomm_context)**|
|**2022-10-19**|**Image Semantic Relation Generation**|Mingzhe Du et.al.|[2210.11253](http://arxiv.org/abs/2210.11253)|null|
|**2022-10-20**|**General Image Descriptors for Open World Image Retrieval using ViT CLIP**|Marcos V. Conde et.al.|[2210.11141](http://arxiv.org/abs/2210.11141)|**[link](https://github.com/ivanaer/g-universal-clip)**|
|**2022-10-20**|**DeepRING: Learning Roto-translation Invariant Representation for LiDAR based Place Recognition**|Sha Lu et.al.|[2210.11029](http://arxiv.org/abs/2210.11029)|null|
|**2022-10-19**|**Cross-Modal Fusion Distillation for Fine-Grained Sketch-Based Image Retrieval**|Abhra Chaudhuri et.al.|[2210.10486](http://arxiv.org/abs/2210.10486)|**[link](https://github.com/abhrac/xmodal-vit)**|
|**2022-10-19**|**GSV-Cities: Toward Appropriate Supervised Visual Place Recognition**|Amar Ali-bey et.al.|[2210.10239](http://arxiv.org/abs/2210.10239)|**[link](https://github.com/amaralibey/gsv-cities)**|
|**2022-10-18**|**A Real-Time Fusion Framework for Long-term Visual Localization**|Yuchen Yang et.al.|[2210.09757](http://arxiv.org/abs/2210.09757)|null|
|**2022-10-17**|**Bridging the Gap between Local Semantic Concepts and Bag of Visual Words for Natural Scene Image Retrieval**|Yousef Alqasrawi et.al.|[2210.08875](http://arxiv.org/abs/2210.08875)|null|
|**2022-10-17**|**SGRAM: Improving Scene Graph Parsing via Abstract Meaning Representation**|Woo Suk Choi et.al.|[2210.08675](http://arxiv.org/abs/2210.08675)|null|
|**2022-10-16**|**Learning Self-Regularized Adversarial Views for Self-Supervised Vision Transformers**|Tao Tang et.al.|[2210.08458](http://arxiv.org/abs/2210.08458)|**[link](https://github.com/trent-tangtao/autoview)**|
|**2022-10-14**|**Cross-Scale Context Extracted Hashing for Fine-Grained Image Binary Encoding**|Xuetong Xue et.al.|[2210.07572](http://arxiv.org/abs/2210.07572)|**[link](https://github.com/netease-media/csce-net)**|
|**2022-10-14**|**Boosting Performance of a Baseline Visual Place Recognition Technique by Predicting the Maximally Complementary Technique**|Connor Malone et.al.|[2210.07509](http://arxiv.org/abs/2210.07509)|null|
|**2022-10-11**|**Large-to-small Image Resolution Asymmetry in Deep Metric Learning**|Pavel Suma et.al.|[2210.05463](http://arxiv.org/abs/2210.05463)|**[link](https://github.com/pavelsuma/raml)**|
|**2022-10-09**|**Fusing Event-based Camera and Radar for SLAM Using Spiking Neural Networks with Continual STDP Learning**|Ali Safa et.al.|[2210.04236](http://arxiv.org/abs/2210.04236)|null|
|**2022-10-05**|**Medical Image Retrieval via Nearest Neighbor Search on Pre-trained Image Features**|Deepak Gupta et.al.|[2210.02401](http://arxiv.org/abs/2210.02401)|**[link](https://github.com/deepaknlp/dls)**|
|**2022-10-05**|**Granularity-aware Adaptation for Image Retrieval over Multiple Tasks**|Jon Almazán et.al.|[2210.02254](http://arxiv.org/abs/2210.02254)|null|
|**2022-10-05**|**Improving Visual-Semantic Embedding with Adaptive Pooling and Optimization Objective**|Zijian Zhang et.al.|[2210.02206](http://arxiv.org/abs/2210.02206)|**[link](https://github.com/96-zachary/vse_2ad)**|
|**2022-10-04**|**Supervised Metric Learning for Retrieval via Contextual Similarity Optimization**|Christopher Liao et.al.|[2210.01908](http://arxiv.org/abs/2210.01908)|**[link](https://github.com/chris210634/metric-learning-using-contextual-similarity)**|
|**2022-10-04**|**Wi-Closure: Reliable and Efficient Search of Inter-robot Loop Closures Using Wireless Sensing**|Weiying Wang et.al.|[2210.01320](http://arxiv.org/abs/2210.01320)|null|
|**2022-10-03**|**Merging Classification Predictions with Sequential Information for Lightweight Visual Place Recognition in Changing Environments**|Bruno Arcanjo et.al.|[2210.00834](http://arxiv.org/abs/2210.00834)|null|
|**2022-10-02**|**Loc-VAE: Learning Structurally Localized Representation from 3D Brain MR Images for Content-Based Image Retrieval**|Kei Nishimaki et.al.|[2210.00506](http://arxiv.org/abs/2210.00506)|null|
|**2022-09-29**|**Guided Unsupervised Learning by Subaperture Decomposition for Ocean SAR Image Retrieval**|Nicolae-Cătălin Ristea et.al.|[2209.15034](http://arxiv.org/abs/2209.15034)|null|
|**2022-09-28**|**TVLT: Textless Vision-Language Transformer**|Zineng Tang et.al.|[2209.14156](http://arxiv.org/abs/2209.14156)|**[link](https://github.com/zinengtang/tvlt)**|
|**2022-09-28**|**SEMICON: A Learning-to-hash Solution for Large-scale Fine-grained Image Retrieval**|Yang Shen et.al.|[2209.13833](http://arxiv.org/abs/2209.13833)|**[link](https://github.com/njust-vipgroup/semicon)**|
|**2022-09-28**|**Learning Deep Representations via Contrastive Learning for Instance Retrieval**|Tao Wu et.al.|[2209.13832](http://arxiv.org/abs/2209.13832)|null|
|**2022-09-28**|**Mr. Right: Multimodal Retrieval on Representation of ImaGe witH Text**|Cheng-An Hsieh et.al.|[2209.13764](http://arxiv.org/abs/2209.13764)|**[link](https://github.com/hsiehjackson/mr.right)**|
|**2022-09-27**|**Learning-Based Dimensionality Reduction for Computing Compact and Effective Local Feature Descriptors**|Hao Dong et.al.|[2209.13586](http://arxiv.org/abs/2209.13586)|**[link](https://github.com/prbonn/descriptor-dr)**|
|**2022-09-27**|**Exploring the Algorithm-Dependent Generalization of AUPRC Optimization with List Stability**|Peisong Wen et.al.|[2209.13262](http://arxiv.org/abs/2209.13262)|**[link](https://github.com/kid-7391/soprc)**|
|**2022-09-26**|**NDD: A 3D Point Cloud Descriptor Based on Normal Distribution for Loop Closure Detection**|Ruihao Zhou et.al.|[2209.12513](http://arxiv.org/abs/2209.12513)|**[link](https://github.com/zhouruihao1001/ndd)**|
|**2022-09-25**|**Personalized Saliency in Task-Oriented Semantic Communications: Image Transmission and Performance Analysis**|Jiawen Kang et.al.|[2209.12274](http://arxiv.org/abs/2209.12274)|**[link](https://github.com/Lizonghang/PerSF-SemCom)**|
|**2022-09-24**|**Closing the Loop: Graph Networks to Unify Semantic Objects and Visual Features for Multi-object Scenes**|Jonathan J. Y. Kim et.al.|[2209.11894](http://arxiv.org/abs/2209.11894)|null|
|**2022-09-23**|**Image-to-Image Translation for Autonomous Driving from Coarsely-Aligned Image Pairs**|Youya Xia et.al.|[2209.11673](http://arxiv.org/abs/2209.11673)|null|
|**2022-09-23**|**Query-based Hard-Image Retrieval for Object Detection at Test Time**|Edward Ayers et.al.|[2209.11559](http://arxiv.org/abs/2209.11559)|**[link](https://github.com/fiveai/hardest)**|
|**2022-09-23**|**Unsupervised Hashing with Semantic Concept Mining**|Rong-Cheng Tu et.al.|[2209.11475](http://arxiv.org/abs/2209.11475)|**[link](https://github.com/rongchengtu1/uhscm)**|
|**2022-09-22**|**UNav: An Infrastructure-Independent Vision-Based Navigation System for People with Blindness and Low vision**|Anbang Yang et.al.|[2209.11336](http://arxiv.org/abs/2209.11336)|null|
|**2022-09-21**|**Visual Localization and Mapping in Dynamic and Changing Environments**|João Carlos Virgolino Soares et.al.|[2209.10710](http://arxiv.org/abs/2209.10710)|null|
|**2022-09-20**|**PADLoC: LiDAR-Based Deep Loop Closure Detection and Registration using Panoptic Attention**|José Arce et.al.|[2209.09699](http://arxiv.org/abs/2209.09699)|**[link](https://github.com/robot-learning-freiburg/PADLoC)**|
|**2022-09-19**|**Deep Metric Learning with Chance Constraints**|Yeti Z. Gurbuz et.al.|[2209.09060](http://arxiv.org/abs/2209.09060)|**[link](https://github.com/yetigurbuz/ccp-dml)**|
|**2022-09-18**|**HGI-SLAM: Loop Closure With Human and Geometric Importance Features**|Shuhul Mujoo et.al.|[2209.08608](http://arxiv.org/abs/2209.08608)|null|
|**2022-09-18**|**Data-driven Loop Closure Detection in Bathymetric Point Clouds for Underwater SLAM**|Jiarui Tan et.al.|[2209.08578](http://arxiv.org/abs/2209.08578)|**[link](https://github.com/tjr16/bathy_nn_learning)**|
|**2022-09-17**|**Data Efficient Visual Place Recognition Using Extremely JPEG-Compressed Images**|Mihnea-Alexandru Tomita et.al.|[2209.08343](http://arxiv.org/abs/2209.08343)|null|
|**2022-09-15**|**Efficient Planar Pose Estimation via UWB Measurements**|Haodong Jiang et.al.|[2209.06779](http://arxiv.org/abs/2209.06779)|**[link](https://github.com/SLAMLab-CUHKSZ/Efficient-Pose-Estimation-via-UWB-measurements)**|
|**2022-09-14**|**Transformers and CNNs both Beat Humans on SBIR**|Omar Seddati et.al.|[2209.06629](http://arxiv.org/abs/2209.06629)|null|
|**2022-09-14**|**Tac2Structure: Object Surface Reconstruction Only through Multi Times Touch**|J. Lu et.al.|[2209.06545](http://arxiv.org/abs/2209.06545)|**[link](https://github.com/ljy-zju/tac2structure)**|
|**2022-09-14**|**iSimLoc: Visual Global Localization for Previously Unseen Environments with Simulated Images**|Peng Yin et.al.|[2209.06376](http://arxiv.org/abs/2209.06376)|null|
|**2022-09-09**|**General Place Recognition Survey: Towards the Real-world Autonomy Age**|Peng Yin et.al.|[2209.04497](http://arxiv.org/abs/2209.04497)|**[link](https://github.com/MetaSLAM/GPRS)**|
|**2022-09-09**|**Retinal Image Restoration and Vessel Segmentation using Modified Cycle-CBAM and CBAM-UNet**|Alnur Alimanov et.al.|[2209.04234](http://arxiv.org/abs/2209.04234)|**[link](https://github.com/AAleka/Cycle-CBAM-and-CBAM-UNet/tree/main/UNet)**|
|**2022-09-13**|**Segment Augmentation and Differentiable Ranking for Logo Retrieval**|Feyza Yavuz et.al.|[2209.02482](http://arxiv.org/abs/2209.02482)|null|
|**2022-09-12**|**ScaleFace: Uncertainty-aware Deep Metric Learning**|Roman Kail et.al.|[2209.01880](http://arxiv.org/abs/2209.01880)|**[link](https://github.com/stat-ml/face-evaluation)**|
|**2022-09-04**|**CloudVision: DNN-based Visual Localization of Autonomous Robots using Prebuilt LiDAR Point Cloud**|Evgeny Yudin et.al.|[2209.01605](http://arxiv.org/abs/2209.01605)|null|
|**2022-08-31**|**EViT: Privacy-Preserving Image Retrieval via Encrypted Vision Transformer in Cloud Computing**|Qihua Feng et.al.|[2208.14657](http://arxiv.org/abs/2208.14657)|**[link](https://github.com/onlinehuazai/evit)**|
|**2022-08-25**|**A Deep Perceptual Measure for Lens and Camera Calibration**|Yannick Hold-Geoffroy et.al.|[2208.12300](http://arxiv.org/abs/2208.12300)|null|
|**2022-08-25**|**A Privacy-Preserving and End-to-End-Based Encrypted Image Retrieval Scheme**|Zhixun Lu et.al.|[2208.11876](http://arxiv.org/abs/2208.11876)|null|
|**2022-08-23**|**Satellite Image Search in AgoraEO**|Ahmet Kerem Aksoy et.al.|[2208.10830](http://arxiv.org/abs/2208.10830)|null|
|**2022-08-20**|**Fuse and Attend: Generalized Embedding Learning for Art and Sketches**|Ujjal Kr Dutta et.al.|[2208.09698](http://arxiv.org/abs/2208.09698)|null|
|**2022-08-19**|**Self-Supervised Visual Place Recognition by Mining Temporal and Feature Neighborhoods**|Chao Chen et.al.|[2208.09315](http://arxiv.org/abs/2208.09315)|**[link](https://github.com/ai4ce/TF-VPR)**|
|**2022-08-19**|**TTT-UCDR: Test-time Training for Universal Cross-Domain Retrieval**|Soumava Paul et.al.|[2208.09198](http://arxiv.org/abs/2208.09198)|**[link](https://github.com/mvp18/ttt-ucdr)**|
|**2022-08-17**|**Visual Cross-View Metric Localization with Dense Uncertainty Estimates**|Zimin Xia et.al.|[2208.08519](http://arxiv.org/abs/2208.08519)|**[link](https://github.com/tudelft-iv/crossviewmetriclocalization)**|
|**2022-08-17**|**Understanding Attention for Vision-and-Language Tasks**|Feiqi Cao et.al.|[2208.08104](http://arxiv.org/abs/2208.08104)|**[link](https://github.com/adlnlp/attention_vl)**|
|**2022-08-14**|**Visual Localization via Few-Shot Scene Region Classification**|Siyan Dong et.al.|[2208.06933](http://arxiv.org/abs/2208.06933)|**[link](https://github.com/siyandong/src)**|
|**2022-08-14**|**HyP $^2$ Loss: Beyond Hypersphere Metric Space for Multi-label Image Retrieval**|Chengyin Xu et.al.|[2208.06866](http://arxiv.org/abs/2208.06866)|**[link](https://github.com/jerryxu0129/hyp2-loss)**|
|**2022-08-13**|**Finding Point with Image: An End-to-End Benchmark for Vision-based UAV Localization**|Ming Dai et.al.|[2208.06561](http://arxiv.org/abs/2208.06561)|**[link](https://github.com/dmmm1997/drl)**|
|**2022-08-16**|**Category-Level Pose Retrieval with Contrastive Features Learnt with Occlusion Augmentation**|Georgios Kouros et.al.|[2208.06195](http://arxiv.org/abs/2208.06195)|**[link](https://github.com/gkouros/contrastive-pose-retrieval)**|
|**2022-08-12**|**Instance Image Retrieval by Learning Purely From Within the Dataset**|Zhongyan Zhang et.al.|[2208.06119](http://arxiv.org/abs/2208.06119)|null|
|**2022-08-07**|**CVLNet: Cross-View Semantic Correspondence Learning for Video-based Camera Localization**|Yujiao Shi et.al.|[2208.03660](http://arxiv.org/abs/2208.03660)|null|
|**2022-08-05**|**A Sketch Is Worth a Thousand Words: Image Retrieval with Text and Sketch**|Patsorn Sangkloy et.al.|[2208.03354](http://arxiv.org/abs/2208.03354)|null|
|**2022-08-05**|**ChiQA: A Large Scale Image-based Real-World Question Answering Dataset for Multi-Modal Understanding**|Bingning Wang et.al.|[2208.03030](http://arxiv.org/abs/2208.03030)|**[link](https://github.com/benywon/ChiQA)**|
|**2022-08-04**|**Pattern Spotting and Image Retrieval in Historical Documents using Deep Hashing**|Caio da S. Dias et.al.|[2208.02397](http://arxiv.org/abs/2208.02397)|null|
|**2022-07-27**|**On the robustness of self-supervised representations for multi-view object classification**|David Torpey et.al.|[2208.00787](http://arxiv.org/abs/2208.00787)|null|
|**2022-07-26**|**Multimodal Neural Machine Translation with Search Engine Based Image Retrieval**|ZhenHao Tang et.al.|[2208.00767](http://arxiv.org/abs/2208.00767)|null|
|**2022-07-30**|**Towards Privacy-Preserving, Real-Time and Lossless Feature Matching**|Qiang Meng et.al.|[2208.00214](http://arxiv.org/abs/2208.00214)|**[link](https://github.com/irvingmeng/securevector)**|
|**2022-07-30**|**DAS: Densely-Anchored Sampling for Deep Metric Learning**|Lizhao Liu et.al.|[2208.00119](http://arxiv.org/abs/2208.00119)|**[link](https://github.com/lizhaoliu-Lec/DAS)**|
|**2022-07-29**|**Curriculum Learning for Data-Efficient Vision-Language Alignment**|Tejas Srinivasan et.al.|[2207.14525](http://arxiv.org/abs/2207.14525)|null|
|**2022-07-29**|**Neural Density-Distance Fields**|Itsuki Ueda et.al.|[2207.14455](http://arxiv.org/abs/2207.14455)|**[link](https://github.com/ueda0319/neddf)**|
|**2022-07-27**|**Abstracting Sketches through Simple Primitives**|Stephan Alaniz et.al.|[2207.13543](http://arxiv.org/abs/2207.13543)|**[link](https://github.com/explainableml/sketch-primitives)**|
|**2022-07-27**|**Satellite Image Based Cross-view Localization for Autonomous Vehicle**|Shan Wang et.al.|[2207.13506](http://arxiv.org/abs/2207.13506)|null|
|**2022-07-26**|**RenderNet: Visual Relocalization Using Virtual Viewpoints in Large-Scale Indoor Environments**|Jiahui Zhang et.al.|[2207.12579](http://arxiv.org/abs/2207.12579)|null|
|**2022-07-25**|**A hybrid-qudit representation of digital RGB images**|Sreetama Das et.al.|[2207.12550](http://arxiv.org/abs/2207.12550)|null|
|**2022-07-19**|**ALTO: A Large-Scale Dataset for UAV Visual Place Recognition and Localization**|Ivan Cisneros et.al.|[2207.12317](http://arxiv.org/abs/2207.12317)|**[link](https://github.com/metaslam/alto)**|
|**2022-07-22**|**PLD-SLAM: A Real-Time Visual SLAM Using Points and Line Segments in Dynamic Scenes**|BaoSheng Zhang et.al.|[2207.10916](http://arxiv.org/abs/2207.10916)|null|
|**2022-07-25**|**MeshLoc: Mesh-Based Visual Localization**|Vojtech Panek et.al.|[2207.10762](http://arxiv.org/abs/2207.10762)|**[link](https://github.com/tsattler/meshloc_release)**|
|**2022-07-20**|**Revisiting Hotels-50K and Hotel-ID**|Aarash Feizi et.al.|[2207.10200](http://arxiv.org/abs/2207.10200)|**[link](https://github.com/aarashfeizi/revisited-hotels)**|
|**2022-07-20**|**Feature Representation Learning for Unsupervised Cross-domain Image Retrieval**|Conghui Hu et.al.|[2207.09721](http://arxiv.org/abs/2207.09721)|**[link](https://github.com/conghuihu/ucdir)**|
|**2022-07-19**|**SeasoNet: A Seasonal Scene Classification, segmentation and Retrieval dataset for satellite Imagery over Germany**|Dominik Koßmann et.al.|[2207.09507](http://arxiv.org/abs/2207.09507)|null|
|**2022-07-19**|**Context Unaware Knowledge Distillation for Image Retrieval**|Bytasandram Yaswanth Reddy et.al.|[2207.09070](http://arxiv.org/abs/2207.09070)|**[link](https://github.com/satoru2001/cukdfir)**|
|**2022-07-17**|**FashionViL: Fashion-Focused Vision-and-Language Representation Learning**|Xiao Han et.al.|[2207.08150](http://arxiv.org/abs/2207.08150)|**[link](https://github.com/brandonhanx/mmf)**|
|**2022-07-14**|**AutoMerge: A Framework for Map Assembling and Smoothing in City-scale Environments**|Peng Yin et.al.|[2207.06965](http://arxiv.org/abs/2207.06965)|null|
|**2022-07-14**|**Semi-supervised Vector-Quantization in Visual SLAM using HGCN**|Amir Zarringhalam et.al.|[2207.06738](http://arxiv.org/abs/2207.06738)|null|
|**2022-07-14**|**Self-supervised Vector-Quantization in Visual SLAM using Deep Convolutional Autoencoders**|Amir Zarringhalam et.al.|[2207.06732](http://arxiv.org/abs/2207.06732)|null|
|**2022-07-19**|**Structure PLP-SLAM: Efficient Sparse Mapping and Localization using Point, Line and Plane for Monocular, RGB-D and Stereo Cameras**|Fangwen Shu et.al.|[2207.06058](http://arxiv.org/abs/2207.06058)|**[link](https://github.com/peterfws/structure-plp-slam)**|
|**2022-07-12**|**CPO: Change Robust Panorama to Point Cloud Localization**|Junho Kim et.al.|[2207.05317](http://arxiv.org/abs/2207.05317)|**[link](https://github.com/82magnolia/panoramic-localization)**|
|**2022-07-05**|**Hierarchical Average Precision Training for Pertinent Image Retrieval**|Elias Ramzi et.al.|[2207.04873](http://arxiv.org/abs/2207.04873)|**[link](https://github.com/elias-ramzi/happier)**|
|**2022-07-11**|**A clinically motivated self-supervised approach for content-based image retrieval of CT liver images**|Kristoffer Knutsen Wickstrøm et.al.|[2207.04812](http://arxiv.org/abs/2207.04812)|**[link](https://github.com/wickstrom/clinical-self-supervised-cbir-ct-liver)**|
|**2022-07-09**|**BOSS: Bottom-up Cross-modal Semantic Composition with Hybrid Counterfactual Training for Robust Content-based Image Retrieval**|Wenqiao Zhang et.al.|[2207.04211](http://arxiv.org/abs/2207.04211)|null|
|**2022-07-08**|**Learning Sequential Descriptors for Sequence-based Visual Place Recognition**|Riccardo Mereu et.al.|[2207.03868](http://arxiv.org/abs/2207.03868)|**[link](https://github.com/vandal-vpr/vg-transformers)**|
|**2022-07-08**|**GEMS: Scene Expansion using Generative Models of Graphs**|Rishi Agarwal et.al.|[2207.03729](http://arxiv.org/abs/2207.03729)|null|
|**2022-07-05**|**Object-Level Targeted Selection via Deep Template Matching**|Suraj Kothawade et.al.|[2207.01778](http://arxiv.org/abs/2207.01778)|null|
|**2022-07-06**|**Adaptive Fine-Grained Sketch-Based Image Retrieval**|Ayan Kumar Bhunia et.al.|[2207.01723](http://arxiv.org/abs/2207.01723)|**[link](https://github.com/ayankumarbhunia/adaptive-fgsbir)**|
|**2022-07-04**|**Embedding contrastive unsupervised features to cluster in- and out-of-distribution noise in corrupted image datasets**|Paul Albert et.al.|[2207.01573](http://arxiv.org/abs/2207.01573)|**[link](https://github.com/paulalbert31/sncf)**|
|**2022-07-08**|**Contrastive Cross-Modal Knowledge Sharing Pre-training for Vision-Language Representation Learning and Retrieval**|Keyu Wen et.al.|[2207.00733](http://arxiv.org/abs/2207.00733)|null|
|**2022-07-01**|**DALG: Deep Attentive Local and Global Modeling for Image Retrieval**|Yuxin Song et.al.|[2207.00287](http://arxiv.org/abs/2207.00287)|null|
|**2022-07-04**|**BadHash: Invisible Backdoor Attacks against Deep Hashing with Clean Label**|Shengshan Hu et.al.|[2207.00278](http://arxiv.org/abs/2207.00278)|**[link](https://github.com/cgcl-codes/badhash)**|
|**2022-06-28**|**Improving Worst Case Visual Localization Coverage via Place-specific Sub-selection in Multi-camera Systems**|Stephen Hausler et.al.|[2206.13883](http://arxiv.org/abs/2206.13883)|null|
|**2022-07-08**|**How Many Events do You Need? Event-based Visual Place Recognition Using Sparse But Varying Pixels**|Tobias Fischer et.al.|[2206.13673](http://arxiv.org/abs/2206.13673)|**[link](https://github.com/tobias-fischer/sparse-event-vpr)**|
|**2022-06-25**|**FreSCo: Frequency-Domain Scan Context for LiDAR-based Place Recognition with Translation and Rotation Invariance**|Yongzhi Fan et.al.|[2206.12628](http://arxiv.org/abs/2206.12628)|**[link](https://github.com/soytony/fresco)**|
|**2022-06-25**|**Inverted Semantic-Index for Image Retrieval**|Ying Wang et.al.|[2206.12623](http://arxiv.org/abs/2206.12623)|null|
|**2022-06-17**|**RetrievalGuard: Provably Robust 1-Nearest Neighbor Image Retrieval**|Yihan Wu et.al.|[2206.11225](http://arxiv.org/abs/2206.11225)|null|
|**2022-06-22**|**ICC++: Explainable Image Retrieval for Art Historical Corpora using Image Composition Canvas**|Prathmesh Madhu et.al.|[2206.11115](http://arxiv.org/abs/2206.11115)|null|
|**2022-06-20**|**Self-Supervised Consistent Quantization for Fully Unsupervised Image Retrieval**|Guile Wu et.al.|[2206.09806](http://arxiv.org/abs/2206.09806)|null|
|**2022-06-18**|**Attention-based Dynamic Subspace Learners for Medical Image Analysis**|Sukesh Adiga V et.al.|[2206.09068](http://arxiv.org/abs/2206.09068)|null|
|**2022-06-17**|**Efficient WiFi LiDAR SLAM for Autonomous Robots in Large Environments**|Khairuldanial Ismail et.al.|[2206.08733](http://arxiv.org/abs/2206.08733)|null|
|**2022-06-06**|**Learning Treatment Plan Representations for Content Based Image Retrieval**|Charles Huang et.al.|[2206.02912](http://arxiv.org/abs/2206.02912)|null|
|**2022-06-19**|**NORPPA: NOvel Ringed seal re-identification by Pelage Pattern Aggregation**|Ekaterina Nepovinnykh et.al.|[2206.02498](http://arxiv.org/abs/2206.02498)|**[link](https://github.com/kwadraterry/norppa)**|
|**2022-06-05**|**Autoregressive Model for Multi-Pass SAR Change Detection Based on Image Stacks**|B. G. Palm et.al.|[2206.02278](http://arxiv.org/abs/2206.02278)|null|
|**2022-05-28**|**FaIRCoP: Facial Image Retrieval using Contrastive Personalization**|Devansh Gupta et.al.|[2205.15870](http://arxiv.org/abs/2205.15870)|null|
|**2022-05-31**|**Investigating the Role of Image Retrieval for Visual Localization -- An exhaustive benchmark**|Martin Humenberger et.al.|[2205.15761](http://arxiv.org/abs/2205.15761)|**[link](https://github.com/naver/kapture-localization)**|
|**2022-05-27**|**Improving Road Segmentation in Challenging Domains Using Similar Place Priors**|Connor Malone et.al.|[2205.14112](http://arxiv.org/abs/2205.14112)|null|
|**2022-05-31**|**LAMP 2.0: A Robust Multi-Robot SLAM System for Operation in Challenging Large-Scale Underground Environments**|Yun Chang et.al.|[2205.13135](http://arxiv.org/abs/2205.13135)|**[link](https://github.com/nebula-autonomy/nebula-multirobot-dataset)**|
|**2022-05-26**|**Fine-grained Image Captioning with CLIP Reward**|Jaemin Cho et.al.|[2205.13115](http://arxiv.org/abs/2205.13115)|**[link](https://github.com/j-min/clip-caption-reward)**|
|**2022-05-25**|**Deep Dense Local Feature Matching and Vehicle Removal for Indoor Visual Localization**|Kyung Ho Park et.al.|[2205.12544](http://arxiv.org/abs/2205.12544)|null|
|**2022-05-24**|**OnePose: One-Shot Object Pose Estimation without CAD Models**|Jiaming Sun et.al.|[2205.12257](http://arxiv.org/abs/2205.12257)|**[link](https://github.com/zju3dv/OnePose)**|
|**2022-05-23**|**VPAIR -- Aerial Visual Place Recognition and Localization in Large-scale Outdoor Environments**|Michael Schleiss et.al.|[2205.11567](http://arxiv.org/abs/2205.11567)|**[link](https://github.com/aervisloc/vpair)**|
|**2022-05-23**|**VQA-GNN: Reasoning with Multimodal Semantic Graph for Visual Question Answering**|Yanan Wang et.al.|[2205.11501](http://arxiv.org/abs/2205.11501)|null|
|**2022-05-23**|**Deep Image Retrieval is not Robust to Label Noise**|Stanislav Dereka et.al.|[2205.11195](http://arxiv.org/abs/2205.11195)|null|
|**2022-05-22**|**Geo-Localization via Ground-to-Satellite Cross-View Image Retrieval**|Zelong Zeng et.al.|[2205.10878](http://arxiv.org/abs/2205.10878)|**[link](https://github.com/ZelongZeng/PLCD)**|
|**2022-05-20**|**Visually-Augmented Language Modeling**|Weizhi Wang et.al.|[2205.10178](http://arxiv.org/abs/2205.10178)|**[link](https://github.com/victorwz/valm)**|
|**2022-05-18**|**Deep Features for CBIR with Scarce Data using Hebbian Learning**|Gabriele Lagani et.al.|[2205.08935](http://arxiv.org/abs/2205.08935)|null|
|**2022-05-19**|**Text Detection & Recognition in the Wild for Robot Localization**|Zobeir Raisi et.al.|[2205.08565](http://arxiv.org/abs/2205.08565)|null|
|**2022-05-12**|**One Model, Multiple Modalities: A Sparsely Activated Approach for Text, Sound, Image, Video and Code**|Yong Dai et.al.|[2205.06126](http://arxiv.org/abs/2205.06126)|null|
|**2022-05-11**|**Review on Panoramic Imaging and Its Applications in Scene Understanding**|Shaohua Gao et.al.|[2205.05570](http://arxiv.org/abs/2205.05570)|null|
|**2022-05-18**|**Identical Image Retrieval using Deep Learning**|Sayan Nath et.al.|[2205.04883](http://arxiv.org/abs/2205.04883)|**[link](https://github.com/sayannath/identical-image-retrieval)**|
|**2022-05-09**|**Introspective Deep Metric Learning**|Chengkun Wang et.al.|[2205.04449](http://arxiv.org/abs/2205.04449)|**[link](https://github.com/wangck20/idml)**|
|**2022-05-11**|**Improved Evaluation and Generation of Grid Layouts using Distance Preservation Quality and Linear Assignment Sorting**|Kai Uwe Barthel et.al.|[2205.04255](http://arxiv.org/abs/2205.04255)|**[link](https://github.com/visual-computing/las_flas)**|
|**2022-05-08**|**Adversarial Learning of Hard Positives for Place Recognition**|Wenxuan Fang et.al.|[2205.03871](http://arxiv.org/abs/2205.03871)|null|
|**2022-05-10**|**AdaTriplet: Adaptive Gradient Triplet Loss with Automatic Margin Learning for Forensic Medical Image Matching**|Khanh Nguyen et.al.|[2205.02849](http://arxiv.org/abs/2205.02849)|**[link](https://github.com/oulu-imeds/adatriplet)**|
|**2022-04-29**|**Privacy-Preserving Model Upgrades with Bidirectional Compatible Training in Image Retrieval**|Shupeng Su et.al.|[2204.13919](http://arxiv.org/abs/2204.13919)|null|
|**2022-04-29**|**Leaner and Faster: Two-Stage Model Compression for Lightweight Text-Image Retrieval**|Siyu Ren et.al.|[2204.13913](http://arxiv.org/abs/2204.13913)|**[link](https://github.com/drsy/motis)**|
|**2022-04-28**|**Spatio-Temporal Graph Localization Networks for Image-based Navigation**|Takahiro Niwa et.al.|[2204.13237](http://arxiv.org/abs/2204.13237)|null|
|**2022-04-27**|**The Revisiting Problem in Simultaneous Localization and Mapping: A Survey on Visual Loop Closure Detection**|Konstantinos A. Tsintotas et.al.|[2204.12831](http://arxiv.org/abs/2204.12831)|null|
|**2022-04-25**|**SceneTrilogy: On Scene Sketches and its Relationship with Text and Photo**|Pinaki Nath Chowdhury et.al.|[2204.11964](http://arxiv.org/abs/2204.11964)|null|
|**2022-04-23**|**On Leveraging Variational Graph Embeddings for Open World Compositional Zero-Shot Learning**|Muhammad Umer Anwaar et.al.|[2204.11848](http://arxiv.org/abs/2204.11848)|null|
|**2022-04-24**|**Progressive Learning for Image Retrieval with Hybrid-Modality Queries**|Yida Zhao et.al.|[2204.11212](http://arxiv.org/abs/2204.11212)|null|
|**2022-04-23**|**Training and challenging models for text-guided fashion image retrieval**|Eric Dodds et.al.|[2204.11004](http://arxiv.org/abs/2204.11004)|**[link](https://github.com/yahoo/maaf)**|
|**2022-04-18**|**Centralized Adversarial Learning for Robust Deep Hashing**|Xunguang Wang et.al.|[2204.10779](http://arxiv.org/abs/2204.10779)|**[link](https://github.com/xunguangwang/cgat)**|
|**2022-04-22**|**Transferring ConvNet Features from Passive to Active Robot Self-Localization: The Use of Ego-Centric and World-Centric Views**|Kanya Kurauchi et.al.|[2204.10497](http://arxiv.org/abs/2204.10497)|null|
|**2022-04-21**|**Exploring a Fine-Grained Multiscale Method for Cross-Modal Remote Sensing Image Retrieval**|Zhiqiang Yuan et.al.|[2204.09868](http://arxiv.org/abs/2204.09868)|**[link](https://github.com/xiaoyuan1996/AMFMN)**|
|**2022-04-21**|**Remote Sensing Cross-Modal Text-Image Retrieval Based on Global and Local Information**|Zhiqiang Yuan et.al.|[2204.09860](http://arxiv.org/abs/2204.09860)|**[link](https://github.com/xiaoyuan1996/galr)**|
|**2022-04-20**|**Uncertainty-based Cross-Modal Retrieval with Probabilistic Representations**|Leila Pishdad et.al.|[2204.09268](http://arxiv.org/abs/2204.09268)|null|
|**2022-04-19**|**Unsupervised Contrastive Hashing for Cross-Modal Retrieval in Remote Sensing**|Georgii Mikriukov et.al.|[2204.08707](http://arxiv.org/abs/2204.08707)|null|
|**2022-04-18**|**Multiple-environment Self-adaptive Network for Aerial-view Geo-localization**|Tingyu Wang et.al.|[2204.08381](http://arxiv.org/abs/2204.08381)|**[link](https://github.com/layumi/University1652-Baseline)**|
|**2022-04-15**|**Condition-Invariant and Compact Visual Place Description by Convolutional Autoencoder**|Hanjing Ye et.al.|[2204.07350](http://arxiv.org/abs/2204.07350)|**[link](https://github.com/medlartea/cae-vpr)**|
|**2022-04-14**|**Composite Code Sparse Autoencoders for first stage retrieval**|Carlos Lassance et.al.|[2204.07023](http://arxiv.org/abs/2204.07023)|null|
|**2022-04-13**|**Reuse your features: unifying retrieval and feature-metric alignment**|Javier Morlana et.al.|[2204.06292](http://arxiv.org/abs/2204.06292)|**[link](https://github.com/jmorlana/dran)**|
|**2022-04-12**|**Probabilistic Compositional Embeddings for Multimodal Image Retrieval**|Andrei Neculai et.al.|[2204.05845](http://arxiv.org/abs/2204.05845)|**[link](https://github.com/andreineculai/mpc)**|
|**2022-04-12**|**Three-Stream Joint Network for Zero-Shot Sketch-Based Image Retrieval**|Yu-Wei Zhan et.al.|[2204.05666](http://arxiv.org/abs/2204.05666)|null|
|**2022-04-12**|**HiTPR: Hierarchical Transformer for Place Recognition in Point Cloud**|Zhixing Hou et.al.|[2204.05481](http://arxiv.org/abs/2204.05481)|null|
|**2022-04-11**|**Optimized SC-F-LOAM: Optimized Fast LiDAR Odometry and Mapping Using Scan Context**|Lizhou Liao et.al.|[2204.04932](http://arxiv.org/abs/2204.04932)|**[link](https://github.com/SlamCabbage/Optimized-SC-F-LOAM)**|
|**2022-04-10**|**Beyond Cross-view Image Retrieval: Highly Accurate Vehicle Localization Using Satellite Image**|Yujiao Shi et.al.|[2204.04752](http://arxiv.org/abs/2204.04752)|**[link](https://github.com/shiyujiao/highlyaccurate)**|
|**2022-04-08**|**A Generic Image Retrieval Method for Date Estimation of Historical Document Collections**|Adrià Molina et.al.|[2204.04028](http://arxiv.org/abs/2204.04028)|null|
|**2022-04-08**|**SnapMode: An Intelligent and Distributed Large-Scale Fashion Image Retrieval Platform Based On Big Data and Deep Generative Adversarial Network Technologies**|Narges Norouzi et.al.|[2204.03998](http://arxiv.org/abs/2204.03998)|null|
|**2022-04-05**|**Leveraging Equivariant Features for Absolute Pose Regression**|Mohamed Adel Musallam et.al.|[2204.02163](http://arxiv.org/abs/2204.02163)|null|
|**2022-04-04**|**"This is my unicorn, Fluffy": Personalizing frozen vision-language representations**|Niv Cohen et.al.|[2204.01694](http://arxiv.org/abs/2204.01694)|**[link](https://github.com/nvlabs/pervlbenchmark)**|
|**2022-04-01**|**Bi-directional Loop Closure for Visual SLAM**|Ihtisham Ali et.al.|[2204.01524](http://arxiv.org/abs/2204.01524)|null|
|**2022-04-01**|**LASER: LAtent SpacE Rendering for 2D Visual Localization**|Zhixiang Min et.al.|[2204.00157](http://arxiv.org/abs/2204.00157)|**[link](https://github.com/zillow/laser)**|
|**2022-03-31**|**Semantic Pose Verification for Outdoor Visual Localization with Self-supervised Contrastive Learning**|Semih Orhan et.al.|[2203.16945](http://arxiv.org/abs/2203.16945)|null|
|**2022-03-30**|**AmsterTime: A Visual Place Recognition Benchmark Dataset for Severe Domain Shift**|Burak Yildiz et.al.|[2203.16291](http://arxiv.org/abs/2203.16291)|**[link](https://github.com/seyrankhademi/AmsterTime)**|
|**2022-03-29**|**Long-term Visual Map Sparsification with Heterogeneous GNN**|Ming-Fang Chang et.al.|[2203.15182](http://arxiv.org/abs/2203.15182)|null|
|**2022-04-01**|**A Simulation Benchmark for Vision-based Autonomous Navigation**|Lauri Suomela et.al.|[2203.13048](http://arxiv.org/abs/2203.13048)|**[link](https://github.com/lasuomela/carla_vloc_benchmark)**|
|**2022-03-24**|**Is Geometry Enough for Matching in Visual Localization?**|Qunjie Zhou et.al.|[2203.12979](http://arxiv.org/abs/2203.12979)|**[link](https://github.com/dvl-tum/gomatch)**|
|**2022-03-21**|**MatchFormer: Interleaving Attention in Transformers for Feature Matching**|Qing Wang et.al.|[2203.09645](http://arxiv.org/abs/2203.09645)|**[link](https://github.com/jamycheung/matchformer)**|
|**2022-03-10**|**ReF -- Rotation Equivariant Features for Local Feature Matching**|Abhishek Peri et.al.|[2203.05206](http://arxiv.org/abs/2203.05206)|null|
|**2022-03-09**|**Object-Based Visual Camera Pose Estimation From Ellipsoidal Model and 3D-Aware Ellipse Prediction**|Matthieu Zins et.al.|[2203.04613](http://arxiv.org/abs/2203.04613)|null|
|**2022-03-08**|**Tune your Place Recognition: Self-Supervised Domain Calibration via Robust SLAM**|Pierre-Yves Lajoie et.al.|[2203.04446](http://arxiv.org/abs/2203.04446)|**[link](https://github.com/mistlab/vpr-calibration-and-uncertainty)**|
|**2022-03-07**|**ZippyPoint: Fast Interest Point Detection, Description, and Matching through Mixed Precision Discretization**|Simon Maurer et.al.|[2203.03610](http://arxiv.org/abs/2203.03610)|**[link](https://github.com/menelaoskanakis/zippypoint)**|
|**2022-03-07**|**Multi-Modal Lidar Dataset for Benchmarking General-Purpose Localization and Mapping Algorithms**|Qingqing Li et.al.|[2203.03454](http://arxiv.org/abs/2203.03454)|**[link](https://github.com/tiers/tiers-lidars-dataset)**|
|**2022-03-01**|**SwitchHit: A Probabilistic, Complementarity-Based Switching System for Improved Visual Place Recognition in Changing Environments**|Maria Waheed et.al.|[2203.00591](http://arxiv.org/abs/2203.00591)|null|
|**2022-02-28**|**Deep Camera Pose Regression Using Pseudo-LiDAR**|Ali Raza et.al.|[2203.00080](http://arxiv.org/abs/2203.00080)|null|
|**2022-02-25**|**RELMOBNET: A Robust Two-Stage End-To-End Training Approach For MOBILENETV3 Based Relative Camera Pose Estimation**|Praveen Kumar Rajendran et.al.|[2202.12838](http://arxiv.org/abs/2202.12838)|null|
|**2022-02-24**|**Highly-Efficient Binary Neural Networks for Visual Place Recognition**|Bruno Ferrarini et.al.|[2202.12375](http://arxiv.org/abs/2202.12375)|null|
|**2022-02-18**|**MultiRes-NetVLAD: Augmenting Place Recognition Training with Low-Resolution Imagery**|Ahmad Khaliq et.al.|[2202.09146](http://arxiv.org/abs/2202.09146)|**[link](https://github.com/ahmedest61/multires-netvlad)**|
|**2022-02-14**|**Tightly Coupled Learning Strategy for Weakly Supervised Hierarchical Place Recognition**|Y. Shen et.al.|[2202.06470](http://arxiv.org/abs/2202.06470)|null|
|**2022-02-11**|**Patch-NetVLAD+: Learned patch descriptor and weighted matching strategy for place recognition**|Yingfeng Cai et.al.|[2202.05738](http://arxiv.org/abs/2202.05738)|null|
|**2022-02-09**|**Object-Guided Day-Night Visual Localization in Urban Scenes**|Assia Benbihi et.al.|[2202.04445](http://arxiv.org/abs/2202.04445)|null|
|**2022-02-08**|**A Novel Image Descriptor with Aggregated Semantic Skeleton Representation for Long-term Visual Place Recognition**|Nie Jiwei et.al.|[2202.03677](http://arxiv.org/abs/2202.03677)|null|
|**2022-02-25**|**CFP-SLAM: A Real-time Visual SLAM Based on Coarse-to-Fine Probability in Dynamic Environments**|Xinggang Hu et.al.|[2202.01938](http://arxiv.org/abs/2202.01938)|null|
|**2022-02-03**|**Danish Airs and Grounds: A Dataset for Aerial-to-Street-Level Place Recognition and Localization**|Andrea Vallone et.al.|[2202.01821](http://arxiv.org/abs/2202.01821)|null|
|**2022-02-02**|**Training Semantic Descriptors for Image-Based Localization**|Ibrahim Cinaroglu et.al.|[2202.01212](http://arxiv.org/abs/2202.01212)|null|
|**2022-01-31**|**Hydra: A Real-time Spatial Perception Engine for 3D Scene Graph Construction and Optimization**|Nathan Hughes et.al.|[2201.13360](http://arxiv.org/abs/2201.13360)|null|
|**2022-01-31**|**Rigidity Preserving Image Transformations and Equivariance in Perspective**|Lucas Brynte et.al.|[2201.13065](http://arxiv.org/abs/2201.13065)|null|
|**2022-01-25**|**Learning Semantics for Visual Place Recognition through Multi-Scale Attention**|Valerio Paolicelli et.al.|[2201.09701](http://arxiv.org/abs/2201.09701)|**[link](https://github.com/valeriopaolicelli/SegVPR)**|
|**2022-01-22**|**Phase-SLAM: Phase Based Simultaneous Localization and Mapping for Mobile Structured Light Illumination Systems**|Xi Zheng et.al.|[2201.09048](http://arxiv.org/abs/2201.09048)|**[link](https://github.com/zhengxi-git/phase-slam)**|
|**2022-01-15**|**A Critical Analysis of Image-based Camera Pose Estimation Techniques**|Meng Xu et.al.|[2201.05816](http://arxiv.org/abs/2201.05816)|null|
|**2022-01-14**|**SRVIO: Super Robust Visual Inertial Odometry for dynamic environments and challenging Loop-closure conditions**|Ali Samadzadeh et.al.|[2201.05386](http://arxiv.org/abs/2201.05386)|**[link](https://github.com/aa-samad/srvio)**|
|**2021-12-23**|**NinjaDesc: Content-Concealing Visual Descriptors via Adversarial Learning**|Tony Ng et.al.|[2112.12785](http://arxiv.org/abs/2112.12785)|null|
|**2021-12-16**|**CrossLoc: Scalable Aerial Localization Assisted by Multimodal Synthetic Data**|Qi Yan et.al.|[2112.09081](http://arxiv.org/abs/2112.09081)|**[link](https://github.com/topo-epfl/crossloc)**|
|**2021-12-05**|**RADA: Robust Adversarial Data Augmentation for Camera Localization in Challenging Weather**|Jialu Wang et.al.|[2112.02469](http://arxiv.org/abs/2112.02469)|null|
|**2021-11-25**|**MegLoc: A Robust and Accurate Visual Localization Pipeline**|Shuxue Peng et.al.|[2111.13063](http://arxiv.org/abs/2111.13063)|null|
|**2021-10-08**|**Semantic Image Alignment for Vehicle Localization**|Markus Herb et.al.|[2110.04162](http://arxiv.org/abs/2110.04162)|null|
|**2021-10-05**|**Season-invariant GNSS-denied visual localization for UAVs**|Jouko Kinnari et.al.|[2110.01967](http://arxiv.org/abs/2110.01967)|**[link](https://github.com/aalto-intelligent-robotics/sivl)**|
|**2021-09-30**|**Forming a sparse representation for visual place recognition using a neurorobotic approach**|Sylvain Colomer et.al.|[2109.14916](http://arxiv.org/abs/2109.14916)|null|
|**2021-09-22**|**Audio-Visual Grounding Referring Expression for Robotic Manipulation**|Yefei Wang et.al.|[2109.10571](http://arxiv.org/abs/2109.10571)|null|
|**2021-09-20**|**Efficient shape mapping through dense touch and vision**|Sudharshan Suresh et.al.|[2109.09884](http://arxiv.org/abs/2109.09884)|**[link](https://github.com/cmurobotouch/ycb-sight)**|
|**2021-09-15**|**S3LAM: Structured Scene SLAM**|Mathieu Gonzalez et.al.|[2109.07339](http://arxiv.org/abs/2109.07339)|null|
|**2021-09-13**|**Monocular Camera Localization for Automated Vehicles Using Image Retrieval**|Eunhyek Joa et.al.|[2109.06296](http://arxiv.org/abs/2109.06296)|null|
|**2021-09-10**|**Line as a Visual Sentence: Context-aware Line Descriptor for Visual Localization**|Sungho Yoon et.al.|[2109.04753](http://arxiv.org/abs/2109.04753)|**[link](https://github.com/yosungho/LineTR)**|
|**2021-09-09**|**CrowdDriven: A New Challenging Dataset for Outdoor Visual Localization**|Ara Jafarzadeh et.al.|[2109.04527](http://arxiv.org/abs/2109.04527)|null|
|**2021-09-09**|**Keeping an Eye on Things: Deep Learned Features for Long-Term Visual Localization**|Mona Gridseth et.al.|[2109.04041](http://arxiv.org/abs/2109.04041)|**[link](https://github.com/utiasasrl/deep_learned_visual_features)**|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## Keypoint Detection

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2023-06-12**|**Topology Repairing of Disconnected Pulmonary Airways and Vessels: Baselines and a Dataset**|Ziqiao Weng et.al.|[2306.07089](http://arxiv.org/abs/2306.07089)|**[link](https://github.com/m3dv/pulmonary-tree-repairing)**|
|**2023-06-07**|**Learning Probabilistic Coordinate Fields for Robust Correspondences**|Weiyue Zhao et.al.|[2306.04231](http://arxiv.org/abs/2306.04231)|null|
|**2023-06-03**|**LDEB -- Label Digitization with Emotion Binarization and Machine Learning for Emotion Recognition in Conversational Dialogues**|Amitabha Dey et.al.|[2306.02193](http://arxiv.org/abs/2306.02193)|null|
|**2023-06-02**|**Self-supervised Interest Point Detection and Description for Fisheye and Perspective Images**|Marcela Mera-Trujillo et.al.|[2306.01938](http://arxiv.org/abs/2306.01938)|null|
|**2023-06-01**|**A Probabilistic Relaxation of the Two-Stage Object Pose Estimation Paradigm**|Onur Beker et.al.|[2306.00892](http://arxiv.org/abs/2306.00892)|null|
|**2023-05-30**|**Align, Perturb and Decouple: Toward Better Leverage of Difference Information for RSI Change Detection**|Supeng Wang et.al.|[2305.18714](http://arxiv.org/abs/2305.18714)|**[link](https://github.com/wangsp1999/cd-research)**|
|**2023-05-23**|**Diffusion Hyperfeatures: Searching Through Time and Space for Semantic Correspondence**|Grace Luo et.al.|[2305.14334](http://arxiv.org/abs/2305.14334)|null|
|**2023-05-15**|**Non-Separable Multi-Dimensional Network Flows for Visual Computing**|Viktoria Ehm et.al.|[2305.08628](http://arxiv.org/abs/2305.08628)|null|
|**2023-05-13**|**Illumination-insensitive Binary Descriptor for Visual Measurement Based on Local Inter-patch Invariance**|Xinyu Lin et.al.|[2305.07943](http://arxiv.org/abs/2305.07943)|**[link](https://github.com/roylin1229/IIB_descriptor)**|
|**2023-05-05**|**HD2Reg: Hierarchical Descriptors and Detectors for Point Cloud Registration**|Canhui Tang et.al.|[2305.03487](http://arxiv.org/abs/2305.03487)|**[link](https://github.com/hui-design/hd2reg)**|
|**2023-04-17**|**Human Pose Estimation in Monocular Omnidirectional Top-View Images**|Jingrui Yu et.al.|[2304.08186](http://arxiv.org/abs/2304.08186)|null|
|**2023-04-14**|**CoPR: Towards Accurate Visual Localization With Continuous Place-descriptor Regression**|Mubariz Zaffar et.al.|[2304.07426](http://arxiv.org/abs/2304.07426)|null|
|**2023-04-12**|**SiLK -- Simple Learned Keypoints**|Pierre Gleize et.al.|[2304.06194](http://arxiv.org/abs/2304.06194)|**[link](https://github.com/facebookresearch/silk)**|
|**2023-04-06**|**From Saliency to DINO: Saliency-guided Vision Transformer for Few-shot Keypoint Detection**|Changsheng Lu et.al.|[2304.03140](http://arxiv.org/abs/2304.03140)|null|
|**2023-03-29**|**NerVE: Neural Volumetric Edges for Parametric Curve Extraction from Point Cloud**|Xiangyu Zhu et.al.|[2303.16465](http://arxiv.org/abs/2303.16465)|**[link](https://github.com/uhzoaix/NerVE)**|
|**2023-03-24**|**PanoVPR: Towards Unified Perspective-to-Equirectangular Visual Place Recognition via Sliding Windows across the Panoramic View**|Ze Shi et.al.|[2303.14095](http://arxiv.org/abs/2303.14095)|**[link](https://github.com/zafirshi/panovpr)**|
|**2023-03-23**|**Semantic Image Attack for Visual Model Diagnosis**|Jinqi Luo et.al.|[2303.13010](http://arxiv.org/abs/2303.13010)|null|
|**2023-03-22**|**Object Pose Estimation with Statistical Guarantees: Conformal Keypoint Detection and Geometric Uncertainty Propagation**|Heng Yang et.al.|[2303.12246](http://arxiv.org/abs/2303.12246)|**[link](https://github.com/nvlabs/conformalkeypoint)**|
|**2023-03-21**|**RN-Net: Reservoir Nodes-Enabled Neuromorphic Vision Sensing Network**|Sangmin Yoo et.al.|[2303.10770](http://arxiv.org/abs/2303.10770)|null|
|**2023-03-17**|**ShaRPy: Shape Reconstruction and Hand Pose Estimation from RGB-D with Uncertainty**|Vanessa Wirth et.al.|[2303.10042](http://arxiv.org/abs/2303.10042)|null|
|**2023-03-15**|**Descriptor Distillation for Efficient Multi-Robot SLAM**|Xiyue Guo et.al.|[2303.08420](http://arxiv.org/abs/2303.08420)|null|
|**2023-03-15**|**From Local Binary Patterns to Pixel Difference Networks for Efficient Visual Representation Learning**|Zhuo Su et.al.|[2303.08414](http://arxiv.org/abs/2303.08414)|null|
|**2023-03-16**|**KGNv2: Separating Scale and Pose Prediction for Keypoint-based 6-DoF Grasp Synthesis on RGB-D input**|Yiye Chen et.al.|[2303.05617](http://arxiv.org/abs/2303.05617)|**[link](https://github.com/ivalab/kgn)**|
|**2023-03-07**|**External Camera-based Mobile Robot Pose Estimation for Collaborative Perception with Smart Edge Sensors**|Simon Bultmann et.al.|[2303.03797](http://arxiv.org/abs/2303.03797)|null|
|**2023-02-26**|**PaRK-Detect: Towards Efficient Multi-Task Satellite Imagery Road Extraction via Patch-Wise Keypoints Detection**|Shenwei Xie et.al.|[2302.13263](http://arxiv.org/abs/2302.13263)|null|
|**2023-02-24**|**Hybrid machine-learned homogenization: Bayesian data mining and convolutional neural networks**|Julian Lißner et.al.|[2302.12545](http://arxiv.org/abs/2302.12545)|null|
|**2023-02-21**|**Deep Reinforcement Learning Based on Local GNN for Goal-conditioned Deformable Object Rearranging**|Yuhong Deng et.al.|[2302.10446](http://arxiv.org/abs/2302.10446)|null|
|**2023-02-12**|**A Correct-and-Certify Approach to Self-Supervise Object Pose Estimators via Ensemble Self-Training**|Jingnan Shi et.al.|[2302.06019](http://arxiv.org/abs/2302.06019)|null|
|**2023-02-11**|**Rethinking Vision Transformer and Masked Autoencoder in Multimodal Face Anti-Spoofing**|Zitong Yu et.al.|[2302.05744](http://arxiv.org/abs/2302.05744)|null|
|**2023-02-09**|**MAPS: A Noise-Robust Progressive Learning Approach for Source-Free Domain Adaptive Keypoint Detection**|Yuhe Ding et.al.|[2302.04589](http://arxiv.org/abs/2302.04589)|**[link](https://github.com/yuhed/maps)**|
|**2023-02-03**|**Explicit Box Detection Unifies End-to-End Multi-Person Pose Estimation**|Jie Yang et.al.|[2302.01593](http://arxiv.org/abs/2302.01593)|**[link](https://github.com/idea-research/ed-pose)**|
|**2023-02-03**|**Simple, Effective and General: A New Backbone for Cross-view Image Geo-localization**|Yingying Zhu et.al.|[2302.01572](http://arxiv.org/abs/2302.01572)|**[link](https://github.com/yanghongji2007/saig)**|
|**2023-01-21**|**Vision Aided Environment Semantics Extraction and Its Application in mmWave Beam Selection**|Feiyang Wen et.al.|[2301.08973](http://arxiv.org/abs/2301.08973)|null|
|**2023-01-18**|**OnePose++: Keypoint-Free One-Shot Object Pose Estimation without CAD Models**|Xingyi He et.al.|[2301.07673](http://arxiv.org/abs/2301.07673)|null|
|**2023-01-12**|**Towards High Performance One-Stage Human Pose Estimation**|Ling Li et.al.|[2301.04842](http://arxiv.org/abs/2301.04842)|null|
|**2022-12-31**|**Rethinking Rotation Invariance with Point Cloud Registration**|Jianhui Yu et.al.|[2301.00149](http://arxiv.org/abs/2301.00149)|null|
|**2023-02-06**|**Fruit Ripeness Classification: a Survey**|Matteo Rizzo et.al.|[2212.14441](http://arxiv.org/abs/2212.14441)|null|
|**2022-12-28**|**NeMo: 3D Neural Motion Fields from Multiple Video Instances of the Same Action**|Kuan-Chieh Wang et.al.|[2212.13660](http://arxiv.org/abs/2212.13660)|**[link](https://github.com/wangkua1/nemo-cvpr2023)**|
|**2022-12-24**|**HandsOff: Labeled Dataset Generation With No Additional Human Annotations**|Austin Xu et.al.|[2212.12645](http://arxiv.org/abs/2212.12645)|null|
|**2022-12-13**|**Learning to Detect Good Keypoints to Match Non-Rigid Objects in RGB Images**|Welerson Melo et.al.|[2212.09589](http://arxiv.org/abs/2212.09589)|**[link](https://github.com/verlab/learningtodetect_sibgrapi_2022)**|
|**2022-12-15**|**Learning Markerless Robot-Depth Camera Calibration and End-Effector Pose Estimation**|Bugra C. Sefercik et.al.|[2212.07567](http://arxiv.org/abs/2212.07567)|null|
|**2023-02-01**|**DDM-NET: End-to-end learning of keypoint feature Detection, Description and Matching for 3D localization**|Xiangyu Xu et.al.|[2212.04575](http://arxiv.org/abs/2212.04575)|null|
|**2022-12-07**|**ViTPose+: Vision Transformer Foundation Model for Generic Body Pose Estimation**|Yufei Xu et.al.|[2212.04246](http://arxiv.org/abs/2212.04246)|**[link](https://github.com/vitae-transformer/vitpose)**|
|**2022-12-15**|**Designing Feature Vector Representations: A case study from Chemistry**|Signe Sidwall Thygesen et.al.|[2212.03731](http://arxiv.org/abs/2212.03731)|null|
|**2022-12-09**|**DiffuPose: Monocular 3D Human Pose Estimation via Denoising Diffusion Probabilistic Model**|Jeongjun Choi et.al.|[2212.02796](http://arxiv.org/abs/2212.02796)|**[link](https://github.com/lojol2327/DiffuPose)**|
|**2022-12-05**|**Images Speak in Images: A Generalist Painter for In-Context Visual Learning**|Xinlong Wang et.al.|[2212.02499](http://arxiv.org/abs/2212.02499)|**[link](https://github.com/baaivision/painter)**|
|**2022-12-06**|**R2FD2: Fast and Robust Matching of Multimodal Remote Sensing Image via Repeatable Feature Detector and Rotation-invariant Feature Descriptor**|Bai Zhu et.al.|[2212.02277](http://arxiv.org/abs/2212.02277)|null|
|**2022-11-28**|**FeatureBooster: Boosting Feature Descriptors with a Lightweight Neural Network**|Xinjiang Wang et.al.|[2211.15069](http://arxiv.org/abs/2211.15069)|**[link](https://github.com/sjtu-visys/featurebooster)**|
|**2022-11-29**|**BALF: Simple and Efficient Blur Aware Local Feature Detector**|Zhenjun Zhao et.al.|[2211.14731](http://arxiv.org/abs/2211.14731)|null|
|**2022-11-21**|**Conjugate Product Graphs for Globally Optimal 2D-3D Shape Matching**|Paul Roetzer et.al.|[2211.11589](http://arxiv.org/abs/2211.11589)|**[link](https://github.com/paul0noah/sm-2d3d)**|
|**2022-11-07**|**Learning Feature Descriptors for Pre- and Intra-operative Point Cloud Matching for Laparoscopic Liver Registration**|Zixin Yang et.al.|[2211.03688](http://arxiv.org/abs/2211.03688)|null|
|**2022-10-31**|**Tree Detection and Diameter Estimation Based on Deep Learning**|Vincent Grondin et.al.|[2210.17424](http://arxiv.org/abs/2210.17424)|**[link](https://github.com/norlab-ulaval/perceptreev1)**|
|**2022-10-26**|**Learning a Task-specific Descriptor for Robust Matching of 3D Point Clouds**|Zhiyuan Zhang et.al.|[2210.14899](http://arxiv.org/abs/2210.14899)|null|
|**2022-10-23**|**Few-Shot Meta Learning for Recognizing Facial Phenotypes of Genetic Disorders**|Ömer Sümer et.al.|[2210.12705](http://arxiv.org/abs/2210.12705)|null|
|**2022-10-21**|**Real-time Detection of 2D Tool Landmarks with Synthetic Training Data**|Bram Vanherle et.al.|[2210.11991](http://arxiv.org/abs/2210.11991)|null|
|**2022-10-09**|**Fusing Event-based Camera and Radar for SLAM Using Spiking Neural Networks with Continual STDP Learning**|Ali Safa et.al.|[2210.04236](http://arxiv.org/abs/2210.04236)|null|
|**2022-10-04**|**Centroid Distance Keypoint Detector for Colored Point Clouds**|Hanzhe Teng et.al.|[2210.01298](http://arxiv.org/abs/2210.01298)|**[link](https://github.com/ucr-robotics/ced_detector)**|
|**2022-09-28**|**Category-Level Global Camera Pose Estimation with Multi-Hypothesis Point Cloud Correspondences**|Jun-Jee Chao et.al.|[2209.14419](http://arxiv.org/abs/2209.14419)|null|
|**2022-09-28**|**USEEK: Unsupervised SE(3)-Equivariant 3D Keypoints for Generalizable Manipulation**|Zhengrong Xue et.al.|[2209.13864](http://arxiv.org/abs/2209.13864)|null|
|**2022-10-16**|**Suture Thread Spline Reconstruction from Endoscopic Images for Robotic Surgery with Reliability-driven Keypoint Detection**|Neelay Joglekar et.al.|[2209.13657](http://arxiv.org/abs/2209.13657)|**[link](https://github.com/ucsdarclab/thread-reconstruction)**|
|**2022-09-27**|**Learning-Based Dimensionality Reduction for Computing Compact and Effective Local Feature Descriptors**|Hao Dong et.al.|[2209.13586](http://arxiv.org/abs/2209.13586)|**[link](https://github.com/prbonn/descriptor-dr)**|
|**2022-09-26**|**Performance Evaluation of 3D Keypoint Detectors and Descriptors on Coloured Point Clouds in Subsea Environments**|Kyungmin Jung et.al.|[2209.12881](http://arxiv.org/abs/2209.12881)|null|
|**2022-10-07**|**Long-Lived Accurate Keypoints in Event Streams**|Philippe Chiberre et.al.|[2209.10385](http://arxiv.org/abs/2209.10385)|null|
|**2022-09-20**|**Integrative Feature and Cost Aggregation with Transformers for Dense Correspondence**|Sunghwan Hong et.al.|[2209.08742](http://arxiv.org/abs/2209.08742)|null|
|**2022-09-15**|**Online Marker-free Extrinsic Camera Calibration using Person Keypoint Detections**|Bastian Pätzold et.al.|[2209.07393](http://arxiv.org/abs/2209.07393)|**[link](https://github.com/ais-bonn/extrcamcalib_personkeypoints)**|
|**2022-09-07**|**Deep Learning-Based Automatic Diagnosis System for Developmental Dysplasia of the Hip**|Yang Li et.al.|[2209.03440](http://arxiv.org/abs/2209.03440)|null|
|**2022-08-27**|**Learning to SLAM on the Fly in Unknown Environments: A Continual Learning Approach for Drones in Visually Ambiguous Scenes**|Ali Safa et.al.|[2208.12997](http://arxiv.org/abs/2208.12997)|null|
|**2022-08-24**|**Self-Supervised Endoscopic Image Key-Points Matching**|Manel Farhat et.al.|[2208.11424](http://arxiv.org/abs/2208.11424)|**[link](https://github.com/abenhamadou/Self-Supervised-Endoscopic-Image-Key-Points-Matching)**|
|**2022-08-19**|**Blind-Spot Collision Detection System for Commercial Vehicles Using Multi Deep CNN Architecture**|Muhammad Muzammel et.al.|[2208.08224](http://arxiv.org/abs/2208.08224)|null|
|**2022-08-08**|**MetaGraspNet: A Large-Scale Benchmark Dataset for Scene-Aware Ambidextrous Bin Picking via Physics-based Metaverse Synthesis**|Maximilian Gilles et.al.|[2208.03963](http://arxiv.org/abs/2208.03963)|null|
|**2022-08-07**|**CVLNet: Cross-View Semantic Correspondence Learning for Video-based Camera Localization**|Yujiao Shi et.al.|[2208.03660](http://arxiv.org/abs/2208.03660)|null|
|**2022-07-29**|**Explicit Occlusion Reasoning for Multi-person 3D Human Pose Estimation**|Qihao Liu et.al.|[2208.00090](http://arxiv.org/abs/2208.00090)|null|
|**2022-07-25**|**Translating a Visual LEGO Manual to a Machine-Executable Plan**|Ruocheng Wang et.al.|[2207.12572](http://arxiv.org/abs/2207.12572)|null|
|**2022-07-21**|**Multi-modal Retinal Image Registration Using a Keypoint-Based Vessel Structure Aligning Network**|Aline Sindel et.al.|[2207.10506](http://arxiv.org/abs/2207.10506)|null|
|**2022-07-15**|**Human keypoint detection for close proximity human-robot interaction**|Jan Docekal et.al.|[2207.07742](http://arxiv.org/abs/2207.07742)|null|
|**2022-07-15**|**Adversarial Focal Loss: Asking Your Discriminator for Hard Examples**|Chen Liu et.al.|[2207.07739](http://arxiv.org/abs/2207.07739)|null|
|**2022-07-13**|**Rapid Person Re-Identification via Sub-space Consistency Regularization**|Qingze Yin et.al.|[2207.05933](http://arxiv.org/abs/2207.05933)|null|
|**2022-07-07**|**RWT-SLAM: Robust Visual SLAM for Highly Weak-textured Environments**|Qihao Peng et.al.|[2207.03539](http://arxiv.org/abs/2207.03539)|null|
|**2022-08-15**|**Semi-supervised Human Pose Estimation in Art-historical Images**|Matthias Springstein et.al.|[2207.02976](http://arxiv.org/abs/2207.02976)|**[link](https://github.com/tibhannover/iart-semi-pose)**|
|**2022-07-01**|**Weakly-supervised High-fidelity Ultrasound Video Synthesis with Feature Decoupling**|Jiamin Liang et.al.|[2207.00474](http://arxiv.org/abs/2207.00474)|null|
|**2022-06-24**|**Motion Estimation for Large Displacements and Deformations**|Qiao Chen et.al.|[2206.12464](http://arxiv.org/abs/2206.12464)|null|
|**2022-06-24**|**Deep embedded clustering algorithm for clustering PACS repositories**|Teo Manojlović et.al.|[2206.12417](http://arxiv.org/abs/2206.12417)|null|
|**2022-06-21**|**KTN: Knowledge Transfer Network for Learning Multi-person 2D-3D Correspondences**|Xuanhan Wang et.al.|[2206.10090](http://arxiv.org/abs/2206.10090)|**[link](https://github.com/stoa-xh91/humandensepose)**|
|**2022-06-20**|**Self-Supervised Consistent Quantization for Fully Unsupervised Image Retrieval**|Guile Wu et.al.|[2206.09806](http://arxiv.org/abs/2206.09806)|null|
|**2022-06-15**|**A Unified Sequence Interface for Vision Tasks**|Ting Chen et.al.|[2206.07669](http://arxiv.org/abs/2206.07669)|**[link](https://github.com/google-research/pix2seq)**|
|**2022-06-09**|**Beyond RGB: Scene-Property Synthesis with Neural Radiance Fields**|Mingtong Zhang et.al.|[2206.04669](http://arxiv.org/abs/2206.04669)|null|
|**2022-06-03**|**SNAKE: Shape-aware Neural 3D Keypoint Field**|Chengliang Zhong et.al.|[2206.01724](http://arxiv.org/abs/2206.01724)|**[link](https://github.com/zhongcl-thu/snake)**|
|**2022-05-17**|**MulT: An End-to-End Multitask Learning Transformer**|Deblina Bhattacharjee et.al.|[2205.08303](http://arxiv.org/abs/2205.08303)|null|
|**2022-05-10**|**ConfLab: A Rich Multimodal Multisensor Dataset of Free-Standing Social Interactions In-the-Wild**|Chirag Raman et.al.|[2205.05177](http://arxiv.org/abs/2205.05177)|**[link](https://github.com/tudelft-spc-lab/conflab)**|
|**2022-04-28**|**Polarimetric imaging for the detection of synthetic models of SARS-CoV-2: a proof of concept**|Emilio Gomez-Gonzalez et.al.|[2204.14050](http://arxiv.org/abs/2204.14050)|null|
|**2022-05-02**|**GRIT: General Robust Image Task Benchmark**|Tanmay Gupta et.al.|[2204.13653](http://arxiv.org/abs/2204.13653)|**[link](https://github.com/allenai/grit_official)**|
|**2022-05-24**|**ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation**|Yufei Xu et.al.|[2204.12484](http://arxiv.org/abs/2204.12484)|**[link](https://github.com/vitae-transformer/vitpose)**|
|**2022-04-26**|**Unified GCNs: Towards Connecting GCNs with CNNs**|Ziyan Zhang et.al.|[2204.12300](http://arxiv.org/abs/2204.12300)|null|
|**2022-04-19**|**Self-Supervised Equivariant Learning for Oriented Keypoint Detection**|Jongmin Lee et.al.|[2204.08613](http://arxiv.org/abs/2204.08613)|**[link](https://github.com/bluedream1121/REKD)**|
|**2022-04-17**|**The Z-axis, X-axis, Weight and Disambiguation Methods for Constructing Local Reference Frame in 3D Registration: An Evaluation**|Bao Zhao et.al.|[2204.08024](http://arxiv.org/abs/2204.08024)|null|
|**2022-04-15**|**2D Human Pose Estimation: A Survey**|Haoming Chen et.al.|[2204.07370](http://arxiv.org/abs/2204.07370)|null|
|**2022-04-11**|**Towards Homogeneous Modality Learning and Multi-Granularity Information Exploration for Visible-Infrared Person Re-Identification**|Haojie Liu et.al.|[2204.04842](http://arxiv.org/abs/2204.04842)|null|
|**2022-04-07**|**Cloning Outfits from Real-World Images to 3D Characters for Generalizable Person Re-Identification**|Yanan Wang et.al.|[2204.02611](http://arxiv.org/abs/2204.02611)|**[link](https://github.com/yanan-wang-cs/clonedperson)**|
|**2022-04-02**|**SkeleVision: Towards Adversarial Resiliency of Person Tracking with Multi-Task Learning**|Nilaksh Das et.al.|[2204.00734](http://arxiv.org/abs/2204.00734)|**[link](https://github.com/nilakshdas/skelevision)**|
|**2022-04-01**|**MS-HLMO: Multi-scale Histogram of Local Main Orientation for Remote Sensing Image Registration**|Chenzhong Gao et.al.|[2204.00260](http://arxiv.org/abs/2204.00260)|null|
|**2022-03-29**|**Assessing Evolutionary Terrain Generation Methods for Curriculum Reinforcement Learning**|David Howard et.al.|[2203.15172](http://arxiv.org/abs/2203.15172)|null|
|**2022-03-28**|**REGTR: End-to-end Point Cloud Correspondences with Transformers**|Zi Jian Yew et.al.|[2203.14517](http://arxiv.org/abs/2203.14517)|**[link](https://github.com/yewzijian/regtr)**|
|**2022-03-27**|**UMT: Unified Multi-modal Transformers for Joint Video Moment Retrieval and Highlight Detection**|Ye Liu et.al.|[2203.12745](http://arxiv.org/abs/2203.12745)|**[link](https://github.com/tencentarc/umt)**|
|**2022-03-21**|**MatchFormer: Interleaving Attention in Transformers for Feature Matching**|Qing Wang et.al.|[2203.09645](http://arxiv.org/abs/2203.09645)|**[link](https://github.com/jamycheung/matchformer)**|
|**2022-03-16**|**PosePipe: Open-Source Human Pose Estimation Pipeline for Clinical Research**|R. James Cotton et.al.|[2203.08792](http://arxiv.org/abs/2203.08792)|**[link](https://github.com/peabody124/posepipeline)**|
|**2022-03-11**|**DRTAM: Dual Rank-1 Tensor Attention Module**|Hanxing Chi et.al.|[2203.05893](http://arxiv.org/abs/2203.05893)|null|
|**2022-03-07**|**Weakly Supervised Learning of Keypoints for 6D Object Pose Estimation**|Meng Tian et.al.|[2203.03498](http://arxiv.org/abs/2203.03498)|null|
|**2022-02-10**|**Motion-Aware Transformer For Occluded Person Re-identification**|Mi Zhou et.al.|[2202.04243](http://arxiv.org/abs/2202.04243)|null|
|**2022-02-03**|**Sim2Real Object-Centric Keypoint Detection and Description**|Chengliang Zhong et.al.|[2202.00448](http://arxiv.org/abs/2202.00448)|null|
|**2022-01-16**|**Cross-Centroid Ripple Pattern for Facial Expression Recognition**|Monu Verma et.al.|[2201.05958](http://arxiv.org/abs/2201.05958)|null|
|**2022-01-14**|**Reproducing BowNet: Learning Representations by Predicting Bags of Visual Words**|Harry Nguyen et.al.|[2201.03556](http://arxiv.org/abs/2201.03556)|**[link](https://github.com/StoneY1/Reproducing-BowNet)**|
|**2022-01-10**|**TFS Recognition: Investigating MPH]{Thai Finger Spelling Recognition: Investigating MediaPipe Hands Potentials**|Jinnavat Sanalohit et.al.|[2201.03170](http://arxiv.org/abs/2201.03170)|null|
|**2022-01-06**|**A Keypoint Detection and Description Network Based on the Vessel Structure for Multi-Modal Retinal Image Registration**|Aline Sindel et.al.|[2201.02242](http://arxiv.org/abs/2201.02242)|null|
|**2021-12-28**|**Skin feature point tracking using deep feature encodings**|Jose Ramon Chang et.al.|[2112.14159](http://arxiv.org/abs/2112.14159)|null|
|**2021-12-23**|**Data-efficient learning for 3D mirror symmetry detection**|Yancong Lin et.al.|[2112.12579](http://arxiv.org/abs/2112.12579)|null|
|**2021-12-22**|**Improved 2D Keypoint Detection in Out-of-Balance and Fall Situations -- combining input rotations and a kinematic model**|Michael Zwölfer et.al.|[2112.12193](http://arxiv.org/abs/2112.12193)|null|
|**2021-12-22**|**Looking Beyond Corners: Contrastive Learning of Visual Representations for Keypoint Detection and Description Extraction**|Henrique Siqueira et.al.|[2112.12002](http://arxiv.org/abs/2112.12002)|**[link](https://github.com/siqueira-hc/corrnet)**|
|**2021-12-19**|**Parallel Multi-Scale Networks with Deep Supervision for Hand Keypoint Detection**|Renjie Li et.al.|[2112.10275](http://arxiv.org/abs/2112.10275)|null|
|**2021-12-19**|**GPU optimization of the 3D Scale-invariant Feature Transform Algorithm and a Novel BRIEF-inspired 3D Fast Descriptor**|Jean-Baptiste Carluer et.al.|[2112.10258](http://arxiv.org/abs/2112.10258)|**[link](https://github.com/carluerjb/3d_sift_cuda)**|
|**2021-12-16**|**Masked Feature Prediction for Self-Supervised Visual Pre-Training**|Chen Wei et.al.|[2112.09133](http://arxiv.org/abs/2112.09133)|**[link](https://github.com/facebookresearch/SlowFast)**|
|**2021-12-13**|**DenseGAP: Graph-Structured Dense Correspondence Learning with Anchor Points**|Zhengfei Kuang et.al.|[2112.06910](http://arxiv.org/abs/2112.06910)|null|
|**2021-12-12**|**Few-shot Keypoint Detection with Uncertainty Learning for Unseen Species**|Changsheng Lu et.al.|[2112.06183](http://arxiv.org/abs/2112.06183)|**[link](https://github.com/alanlusun/few-shot-keypoint-detection)**|
|**2021-12-13**|**Few-Shot Keypoint Detection as Task Adaptation via Latent Embeddings**|Mel Vecerik et.al.|[2112.04910](http://arxiv.org/abs/2112.04910)|null|
|**2021-12-06**|**ALIKE: Accurate and Lightweight Keypoint Detection and Descriptor Extraction**|Xiaoming Zhao et.al.|[2112.02906](http://arxiv.org/abs/2112.02906)|**[link](https://github.com/Shiaoming/ALIKE)**|
|**2021-11-25**|**Attend to Who You Are: Supervising Self-Attention for Keypoint Detection and Instance-Aware Association**|Sen Yang et.al.|[2111.12892](http://arxiv.org/abs/2111.12892)|**[link](https://github.com/yangsenius/ssa)**|
|**2021-11-08**|**Template NeRF: Towards Modeling Dense Shape Correspondences from Category-Specific Object Images**|Jianfei Guo et.al.|[2111.04237](http://arxiv.org/abs/2111.04237)|null|
|**2021-11-04**|**Voxel-based 3D Detection and Reconstruction of Multiple Objects from a Single Image**|Feng Liu et.al.|[2111.03098](http://arxiv.org/abs/2111.03098)|null|
|**2021-11-01**|**Learning Event-based Spatio-Temporal Feature Descriptors via Local Synaptic Plasticity: A Biologically-realistic Perspective of Computer Vision**|Ali Safa et.al.|[2111.00791](http://arxiv.org/abs/2111.00791)|null|
|**2021-10-30**|**Geometry-Aware Hierarchical Bayesian Learning on Manifolds**|Yonghui Fan et.al.|[2111.00184](http://arxiv.org/abs/2111.00184)|null|
|**2021-10-26**|**CoFiNet: Reliable Coarse-to-fine Correspondences for Robust Point Cloud Registration**|Hao Yu et.al.|[2110.14076](http://arxiv.org/abs/2110.14076)|**[link](https://github.com/haoyu94/coarse-to-fine-correspondences)**|
|**2021-10-23**|**HWTool: Fully Automatic Mapping of an Extensible C++ Image Processing Language to Hardware**|James Hegarty et.al.|[2110.12106](http://arxiv.org/abs/2110.12106)|null|
|**2021-10-18**|**Keypoint-Based Bimanual Shaping of Deformable Linear Objects under Environmental Constraints using Hierarchical Action Planning**|Shengzeng Huo et.al.|[2110.08962](http://arxiv.org/abs/2110.08962)|null|
|**2021-10-11**|**High-order Tensor Pooling with Attention for Action Recognition**|Piotr Koniusz et.al.|[2110.05216](http://arxiv.org/abs/2110.05216)|null|
|**2021-10-10**|**Digging Into Self-Supervised Learning of Feature Descriptors**|Iaroslav Melekhov et.al.|[2110.04773](http://arxiv.org/abs/2110.04773)|null|
|**2021-10-04**|**BPFNet: A Unified Framework for Bimodal Palmprint Alignment and Fusion**|Zhaoqun Li et.al.|[2110.01179](http://arxiv.org/abs/2110.01179)|**[link](https://github.com/dxbdxx/bpfnet)**|
|**2021-10-01**|**Machine learning aided noise filtration and signal classification for CREDO experiment**|Łukasz Bibrzycki et.al.|[2110.00297](http://arxiv.org/abs/2110.00297)|null|
|**2021-09-28**|**PDC-Net+: Enhanced Probabilistic Dense Correspondence Network**|Prune Truong et.al.|[2109.13912](http://arxiv.org/abs/2109.13912)|**[link](https://github.com/PruneTruong/DenseMatching)**|
|**2021-09-27**|**HarrisZ $^+$ : Harris Corner Selection for Next-Gen Image Matching Pipelines**|Fabio Bellavia et.al.|[2109.12925](http://arxiv.org/abs/2109.12925)|null|
|**2021-09-24**|**Catadioptric Stereo on a Smartphone**|Kristijan Bartol et.al.|[2109.11872](http://arxiv.org/abs/2109.11872)|null|
|**2021-09-20**|**Semi-supervised Dense Keypointsusing Unlabeled Multiview Images**|Zhixuan Yu et.al.|[2109.09299](http://arxiv.org/abs/2109.09299)|null|
|**2021-08-31**|**A Novel Dataset for Keypoint Detection of quadruped Animals from Images**|Prianka Banik et.al.|[2108.13958](http://arxiv.org/abs/2108.13958)|**[link](https://github.com/prinik/awa-pose)**|
|**2021-08-27**|**A Matching Algorithm based on Image Attribute Transfer and Local Features for Underwater Acoustic and Optical Images**|Xiaoteng Zhou et.al.|[2108.12151](http://arxiv.org/abs/2108.12151)|null|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## Image Matching

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2023-06-09**|**Leaving the Lines Behind: Vision-Based Crop Row Exit for Agricultural Robot Navigation**|Rajitha de Silva et.al.|[2306.05869](http://arxiv.org/abs/2306.05869)|null|
|**2023-06-07**|**A2B: Anchor to Barycentric Coordinate for Robust Correspondence**|Weiyue Zhao et.al.|[2306.02760](http://arxiv.org/abs/2306.02760)|null|
|**2023-05-27**|**Pentagon-Match (PMatch): Identification of View-Invariant Planar Feature for Local Feature Matching-Based Homography Estimation**|Yueh-Cheng Huang et.al.|[2305.17463](http://arxiv.org/abs/2305.17463)|null|
|**2023-05-19**|**SIDAR: Synthetic Image Dataset for Alignment & Restoration**|Monika Kwiatkowski et.al.|[2305.12036](http://arxiv.org/abs/2305.12036)|**[link](https://github.com/niika/SIDAR)**|
|**2023-05-18**|**LLMScore: Unveiling the Power of Large Language Models in Text-to-Image Synthesis Evaluation**|Yujie Lu et.al.|[2305.11116](http://arxiv.org/abs/2305.11116)|**[link](https://github.com/yujielu10/llmscore)**|
|**2023-05-16**|**A Method for Training-free Person Image Picture Generation**|Tianyu Chen et.al.|[2305.09817](http://arxiv.org/abs/2305.09817)|null|
|**2023-05-15**|**Image Matching by Bare Homography**|Fabio Bellavia et.al.|[2305.08946](http://arxiv.org/abs/2305.08946)|null|
|**2023-05-12**|**CLIP-Count: Towards Text-Guided Zero-Shot Object Counting**|Ruixiang Jiang et.al.|[2305.07304](http://arxiv.org/abs/2305.07304)|**[link](https://github.com/songrise/clip-count)**|
|**2023-05-10**|**SENDD: Sparse Efficient Neural Depth and Deformation for Tissue Tracking**|Adam Schmidt et.al.|[2305.06477](http://arxiv.org/abs/2305.06477)|null|
|**2023-05-10**|**Level-line Guided Edge Drawing for Robust Line Segment Detection**|Xinyu Lin et.al.|[2305.05883](http://arxiv.org/abs/2305.05883)|**[link](https://github.com/roylin1229/gedrlsd)**|
|**2023-05-09**|**ColonMapper: topological mapping and localization for colonoscopy**|Javier Morlana et.al.|[2305.05546](http://arxiv.org/abs/2305.05546)|null|
|**2023-04-29**|**A Comprehensive Review of Image Line Segment Detection and Description: Taxonomies, Comparisons, and Challenges**|Xinyu Lin et.al.|[2305.00264](http://arxiv.org/abs/2305.00264)|**[link](https://github.com/roylin1229/line_segment_review)**|
|**2023-04-28**|**SFD2: Semantic-guided Feature Detection and Description**|Fei Xue et.al.|[2304.14845](http://arxiv.org/abs/2304.14845)|**[link](https://github.com/feixue94/sfd2)**|
|**2023-04-17**|**DeepSim-Nets: Deep Similarity Networks for Stereo Image Matching**|Mohamed Ali Chebbi et.al.|[2304.08056](http://arxiv.org/abs/2304.08056)|**[link](https://github.com/dalichebbi/deepsimnets)**|
|**2023-04-16**|**Long-term Visual Localization with Mobile Sensors**|Shen Yan et.al.|[2304.07691](http://arxiv.org/abs/2304.07691)|null|
|**2023-04-12**|**SiLK -- Simple Learned Keypoints**|Pierre Gleize et.al.|[2304.06194](http://arxiv.org/abs/2304.06194)|**[link](https://github.com/facebookresearch/silk)**|
|**2023-04-16**|**ALIKED: A Lighter Keypoint and Descriptor Extraction Network via Deformable Transformation**|Xiaoming Zhao et.al.|[2304.03608](http://arxiv.org/abs/2304.03608)|**[link](https://github.com/Shiaoming/ALIKED)**|
|**2023-04-04**|**GlueStick: Robust Image Matching by Sticking Points and Lines Together**|Rémi Pautrat et.al.|[2304.02008](http://arxiv.org/abs/2304.02008)|**[link](https://github.com/cvg/gluestick)**|
|**2023-04-03**|**PoseMatcher: One-shot 6D Object Pose Estimation by Deep Feature Matching**|Pedro Castro et.al.|[2304.01382](http://arxiv.org/abs/2304.01382)|null|
|**2023-04-02**|**Enhancing Deformable Local Features by Jointly Learning to Detect and Describe Keypoints**|Guilherme Potje et.al.|[2304.00583](http://arxiv.org/abs/2304.00583)|**[link](https://github.com/verlab/DALF_CVPR_2023)**|
|**2023-04-13**|**Structured Epipolar Matcher for Local Feature Matching**|Jiahao Chang et.al.|[2303.16646](http://arxiv.org/abs/2303.16646)|null|
|**2023-03-29**|**Adaptive Spot-Guided Transformer for Consistent Local Feature Matching**|Jiahuan Yu et.al.|[2303.16624](http://arxiv.org/abs/2303.16624)|null|
|**2023-03-28**|**ASIC: Aligning Sparse in-the-wild Image Collections**|Kamal Gupta et.al.|[2303.16201](http://arxiv.org/abs/2303.16201)|null|
|**2023-03-25**|**Learning Rotation-Equivariant Features for Visual Correspondence**|Jongmin Lee et.al.|[2303.15472](http://arxiv.org/abs/2303.15472)|null|
|**2023-03-27**|**Learnable Graph Matching: A Practical Paradigm for Data Association**|Jiawei He et.al.|[2303.15414](http://arxiv.org/abs/2303.15414)|**[link](https://github.com/jiaweihe1996/GMTracker)**|
|**2023-03-24**|**Efficient and Accurate Co-Visible Region Localization with Matching Key-Points Crop (MKPC): A Two-Stage Pipeline for Enhancing Image Matching Performance**|Hongjian Song et.al.|[2303.13794](http://arxiv.org/abs/2303.13794)|null|
|**2023-03-15**|**Rethinking Optical Flow from Geometric Matching Consistent Perspective**|Qiaole Dong et.al.|[2303.08384](http://arxiv.org/abs/2303.08384)|**[link](https://github.com/dqiaole/matchflow)**|
|**2023-04-04**|**PATS: Patch Area Transportation with Subdivision for Local Feature Matching**|Junjie Ni et.al.|[2303.07700](http://arxiv.org/abs/2303.07700)|null|
|**2023-03-07**|**Parsing Line Segments of Floor Plan Images Using Graph Neural Networks**|Mingxiang Chen et.al.|[2303.03851](http://arxiv.org/abs/2303.03851)|null|
|**2023-03-06**|**Improving Transformer-based Image Matching by Cascaded Capturing Spatially Informative Keypoints**|Chenjie Cao et.al.|[2303.02885](http://arxiv.org/abs/2303.02885)|**[link](https://github.com/ewrfcas/casmtr)**|
|**2023-03-10**|**ParaFormer: Parallel Attention Transformer for Efficient Feature Matching**|Xiaoyong Lu et.al.|[2303.00941](http://arxiv.org/abs/2303.00941)|null|
|**2023-03-01**|**RIFT2: Speeding-up RIFT with A New Rotation-Invariance Technique**|Jiayuan Li et.al.|[2303.00319](http://arxiv.org/abs/2303.00319)|**[link](https://github.com/ljy-rs/rift2-multimodal-matching-rotation)**|
|**2023-02-28**|**Nonlinear Intensity, Scale and Rotation Invariant Matching for Multimodal Images**|Zhongli Fan et.al.|[2302.14239](http://arxiv.org/abs/2302.14239)|**[link](https://github.com/zhongli-fan/nisr)**|
|**2023-02-25**|**BrainCLIP: Bridging Brain and Visual-Linguistic Representation via CLIP for Generic Natural Visual Stimulus Decoding from fMRI**|Yulong Liu et.al.|[2302.12971](http://arxiv.org/abs/2302.12971)|**[link](https://github.com/YulongBonjour/BrainCLIP)**|
|**2023-02-24**|**Classification of structural building damage grades from multi-temporal photogrammetric point clouds using a machine learning model trained on virtual laser scanning data**|Vivien Zahs et.al.|[2302.12591](http://arxiv.org/abs/2302.12591)|null|
|**2023-02-20**|**A Large Scale Homography Benchmark**|Daniel Barath et.al.|[2302.09997](http://arxiv.org/abs/2302.09997)|**[link](https://github.com/danini/homography-benchmark)**|
|**2023-02-12**|**OAMatcher: An Overlapping Areas-based Network for Accurate Local Feature Matching**|Kun Dai et.al.|[2302.05846](http://arxiv.org/abs/2302.05846)|**[link](https://github.com/dk-hu/oamatcher)**|
|**2023-02-10**|**General, Single-shot, Target-less, and Automatic LiDAR-Camera Extrinsic Calibration Toolbox**|Kenji Koide et.al.|[2302.05094](http://arxiv.org/abs/2302.05094)|**[link](https://github.com/koide3/direct_visual_lidar_calibration)**|
|**2023-02-03**|**Simple, Effective and General: A New Backbone for Cross-view Image Geo-localization**|Yingying Zhu et.al.|[2302.01572](http://arxiv.org/abs/2302.01572)|**[link](https://github.com/yanghongji2007/saig)**|
|**2023-01-27**|**Harmonizing Flows: Unsupervised MR harmonization based on normalizing flows**|Farzad Beizaee et.al.|[2301.11551](http://arxiv.org/abs/2301.11551)|**[link](https://github.com/farzad-bz/harmonizing-flows)**|
|**2023-01-25**|**Local Feature Extraction from Salient Regions by Feature Map Transformation**|Yerim Jung et.al.|[2301.10413](http://arxiv.org/abs/2301.10413)|null|
|**2023-01-24**|**Feature-based Image Matching for Identifying Individual Kākā**|Fintan O'Sullivan et.al.|[2301.06678](http://arxiv.org/abs/2301.06678)|null|
|**2023-01-18**|**Instance Segmentation Based Graph Extraction for Handwritten Circuit Diagram Images**|Johannes Bayer et.al.|[2301.03155](http://arxiv.org/abs/2301.03155)|null|
|**2023-01-08**|**DeepMatcher: A Deep Transformer-based Network for Robust and Accurate Local Feature Matching**|Tao Xie et.al.|[2301.02993](http://arxiv.org/abs/2301.02993)|**[link](https://github.com/XT-1997/DeepMatcher)**|
|**2023-01-07**|**Deep Learning-Based UAV Aerial Triangulation without Image Control Points**|Jiageng Zhong et.al.|[2301.02869](http://arxiv.org/abs/2301.02869)|null|
|**2023-01-06**|**The UNCOVER Survey: A first-look HST+JWST catalog of 50,000 galaxies near Abell 2744 and beyond**|John R. Weaver et.al.|[2301.02671](http://arxiv.org/abs/2301.02671)|**[link](https://github.com/astrowhit/aperpy)**|
|**2023-02-13**|**Translating Text Synopses to Video Storyboards**|Xu Gu et.al.|[2301.00135](http://arxiv.org/abs/2301.00135)|**[link](https://github.com/guxu313/TeViS)**|
|**2022-12-23**|**SuperGF: Unifying Local and Global Features for Visual Localization**|Wenzheng Song et.al.|[2212.13105](http://arxiv.org/abs/2212.13105)|null|
|**2022-12-26**|**Transformer and GAN Based Super-Resolution Reconstruction Network for Medical Images**|Weizhi Du et.al.|[2212.13068](http://arxiv.org/abs/2212.13068)|null|
|**2022-12-20**|**Seafloor-Invariant Caustics Removal from Underwater Imagery**|Panagiotis Agrafiotis et.al.|[2212.10167](http://arxiv.org/abs/2212.10167)|null|
|**2022-12-15**|**DeepLSD: Line Segment Detection and Refinement with Deep Image Gradients**|Rémi Pautrat et.al.|[2212.07766](http://arxiv.org/abs/2212.07766)|**[link](https://github.com/cvg/deeplsd)**|
|**2022-12-14**|**Shared Coupling-bridge for Weakly Supervised Local Feature Learning**|Jiayuan Sun et.al.|[2212.07047](http://arxiv.org/abs/2212.07047)|**[link](https://github.com/sunjiayuanro/scfeat)**|
|**2022-12-05**|**Real Time Incremental Image Mosaicking Without Use of Any Camera Parameter**|Suleyman Melih Portakal et.al.|[2212.02302](http://arxiv.org/abs/2212.02302)|null|
|**2022-12-05**|**ObjectMatch: Robust Registration using Canonical Object Correspondences**|Can Gümeli et.al.|[2212.01985](http://arxiv.org/abs/2212.01985)|null|
|**2022-12-07**|**Universe Points Representation Learning for Partial Multi-Graph Matching**|Zhakshylyk Nurlanov et.al.|[2212.00780](http://arxiv.org/abs/2212.00780)|null|
|**2022-11-30**|**Self-Supervised Feature Learning for Long-Term Metric Visual Localization**|Yuxuan Chen et.al.|[2212.00122](http://arxiv.org/abs/2212.00122)|null|
|**2022-11-28**|**FeatureBooster: Boosting Feature Descriptors with a Lightweight Neural Network**|Xinjiang Wang et.al.|[2211.15069](http://arxiv.org/abs/2211.15069)|**[link](https://github.com/sjtu-visys/featurebooster)**|
|**2022-11-19**|**Person Text-Image Matching via Text-Feature Interpretability Embedding and External Attack Node Implantation**|Fan Li et.al.|[2211.08657](http://arxiv.org/abs/2211.08657)|**[link](https://github.com/lhf12278/saa)**|
|**2022-11-20**|**Detecting Line Segments in Motion-blurred Images with Events**|Huai Yu et.al.|[2211.07365](http://arxiv.org/abs/2211.07365)|**[link](https://github.com/lh9171338/FE-LSD)**|
|**2022-11-15**|**Fast Key Points Detection and Matching for Tree-Structured Images**|Hao Wang et.al.|[2211.03242](http://arxiv.org/abs/2211.03242)|null|
|**2022-10-25**|**A Comparative Study on Deep-Learning Methods for Dense Image Matching of Multi-angle and Multi-date Remote Sensing Stereo Images**|Hessah Albanwan et.al.|[2210.14031](http://arxiv.org/abs/2210.14031)|null|
|**2022-10-11**|**DeepMLE: A Robust Deep Maximum Likelihood Estimator for Two-view Structure from Motion**|Yuxi Xiao et.al.|[2210.05517](http://arxiv.org/abs/2210.05517)|null|
|**2022-10-07**|**Mars Rover Localization Based on A2G Obstacle Distribution Pattern Matching**|Lang Zhou et.al.|[2210.03398](http://arxiv.org/abs/2210.03398)|**[link](https://github.com/Mars-Rover-Localization/A2G-Localization)**|
|**2022-09-27**|**Learning-Based Dimensionality Reduction for Computing Compact and Effective Local Feature Descriptors**|Hao Dong et.al.|[2209.13586](http://arxiv.org/abs/2209.13586)|**[link](https://github.com/prbonn/descriptor-dr)**|
|**2022-09-25**|**ECO-TR: Efficient Correspondences Finding Via Coarse-to-Fine Refinement**|Dongli Tan et.al.|[2209.12213](http://arxiv.org/abs/2209.12213)|null|
|**2022-09-22**|**DRKF: Distilled Rotated Kernel Fusion for Efficiently Boosting Rotation Invariance in Image Matching**|Chao Li et.al.|[2209.10907](http://arxiv.org/abs/2209.10907)|null|
|**2022-11-15**|**Uncertainty-aware Efficient Subgraph Isomorphism using Graph Topology**|Arpan Kusari et.al.|[2209.09090](http://arxiv.org/abs/2209.09090)|null|
|**2022-09-16**|**SRFeat: Learning Locally Accurate and Globally Consistent Non-Rigid Shape Correspondence**|Lei Li et.al.|[2209.07806](http://arxiv.org/abs/2209.07806)|**[link](https://github.com/craigleili/srfeat)**|
|**2022-08-30**|**ASpanFormer: Detector-Free Image Matching with Adaptive Span Transformer**|Hongkai Chen et.al.|[2208.14201](http://arxiv.org/abs/2208.14201)|**[link](https://github.com/apple/ml-aspanformer)**|
|**2022-08-25**|**A Gis Aided Approach for Geolocalizing an Unmanned Aerial System Using Deep Learning**|Jianli Wei et.al.|[2208.12251](http://arxiv.org/abs/2208.12251)|**[link](https://github.com/osupcvlab/ubiheredrone2021)**|
|**2022-08-25**|**UAS Navigation in the Real World Using Visual Observation**|Yuci Han et.al.|[2208.12125](http://arxiv.org/abs/2208.12125)|null|
|**2022-08-24**|**Self-Supervised Endoscopic Image Key-Points Matching**|Manel Farhat et.al.|[2208.11424](http://arxiv.org/abs/2208.11424)|**[link](https://github.com/abenhamadou/Self-Supervised-Endoscopic-Image-Key-Points-Matching)**|
|**2022-08-22**|**Equivariant Hypergraph Neural Networks**|Jinwoo Kim et.al.|[2208.10428](http://arxiv.org/abs/2208.10428)|**[link](https://github.com/jw9730/ehnn)**|
|**2022-09-22**|**Understanding Attention for Vision-and-Language Tasks**|Feiqi Cao et.al.|[2208.08104](http://arxiv.org/abs/2208.08104)|**[link](https://github.com/adlnlp/attention_vl)**|
|**2022-08-16**|**Hierarchical Attention Network for Few-Shot Object Detection via Meta-Contrastive Learning**|Dongwoo Park et.al.|[2208.07039](http://arxiv.org/abs/2208.07039)|**[link](https://github.com/infinity7428/hANMCL)**|
|**2022-08-04**|**Learning Modal-Invariant and Temporal-Memory for Video-based Visible-Infrared Person Re-Identification**|Xinyu Lin et.al.|[2208.02450](http://arxiv.org/abs/2208.02450)|**[link](https://github.com/vcm-project233/mitml)**|
|**2022-08-04**|**OmniCity: Omnipotent City Understanding with Multi-level and Multi-view Images**|Weijia Li et.al.|[2208.00928](http://arxiv.org/abs/2208.00928)|null|
|**2022-07-29**|**Testing Relational Understanding in Text-Guided Image Generation**|Colin Conwell et.al.|[2208.00005](http://arxiv.org/abs/2208.00005)|null|
|**2022-07-21**|**Pose for Everything: Towards Category-Agnostic Pose Estimation**|Lumin Xu et.al.|[2207.10387](http://arxiv.org/abs/2207.10387)|**[link](https://github.com/luminxu/pose-for-everything)**|
|**2022-07-20**|**Explaining Deepfake Detection by Analysing Image Matching**|Shichao Dong et.al.|[2207.09679](http://arxiv.org/abs/2207.09679)|**[link](https://github.com/megvii-research/fst-matching)**|
|**2022-07-18**|**Adaptive Assignment for Geometry Aware Local Feature Matching**|Dihe Huang et.al.|[2207.08427](http://arxiv.org/abs/2207.08427)|**[link](https://github.com/abyssgaze/adamatcher)**|
|**2022-07-16**|**Semi-Supervised Keypoint Detector and Descriptor for Retinal Image Matching**|Jiazhen Liu et.al.|[2207.07932](http://arxiv.org/abs/2207.07932)|**[link](https://github.com/ruc-aimc-lab/superretina)**|
|**2022-07-06**|**Virtual staining of defocused autofluorescence images of unlabeled tissue using deep neural networks**|Yijie Zhang et.al.|[2207.02946](http://arxiv.org/abs/2207.02946)|null|
|**2022-07-01**|**TopicFM: Robust and Interpretable Feature Matching with Topic-assisted**|Khang Truong Giang et.al.|[2207.00328](http://arxiv.org/abs/2207.00328)|**[link](https://github.com/truongkhang/topicfm)**|
|**2022-06-16**|**Virtual Correspondence: Humans as a Cue for Extreme-View Geometry**|Wei-Chiu Ma et.al.|[2206.08365](http://arxiv.org/abs/2206.08365)|null|
|**2022-06-15**|**Self-Supervised Learning of Image Scale and Orientation**|Jongmin Lee et.al.|[2206.07259](http://arxiv.org/abs/2206.07259)|**[link](https://github.com/bluedream1121/self-sca-ori)**|
|**2022-05-27**|**Image Keypoint Matching using Graph Neural Networks**|Nancy Xu et.al.|[2205.14275](http://arxiv.org/abs/2205.14275)|null|
|**2022-05-27**|**Fine-tuning deep learning models for stereo matching using results from semi-global matching**|Hessah Albanwan et.al.|[2205.14051](http://arxiv.org/abs/2205.14051)|null|
|**2022-05-23**|**TransforMatcher: Match-to-Match Attention for Semantic Correspondence**|Seungwook Kim et.al.|[2205.11634](http://arxiv.org/abs/2205.11634)|**[link](https://github.com/wookiekim/transformatcher)**|
|**2022-05-16**|**ReDFeat: Recoupling Detection and Description for Multimodal Feature Learning**|Yuxin Deng et.al.|[2205.07439](http://arxiv.org/abs/2205.07439)|null|
|**2022-05-06**|**BDIS: Bayesian Dense Inverse Searching Method for Real-Time Stereo Surgical Image Matching**|Jingwei Song et.al.|[2205.03133](http://arxiv.org/abs/2205.03133)|**[link](https://github.com/jingweisong/bdis-v2)**|
|**2022-05-10**|**AdaTriplet: Adaptive Gradient Triplet Loss with Automatic Margin Learning for Forensic Medical Image Matching**|Khanh Nguyen et.al.|[2205.02849](http://arxiv.org/abs/2205.02849)|**[link](https://github.com/oulu-imeds/adatriplet)**|
|**2022-04-27**|**Gleo-Det: Deep Convolution Feature-Guided Detector with Local Entropy Optimization for Salient Points**|Chao Li et.al.|[2204.12884](http://arxiv.org/abs/2204.12884)|null|
|**2022-04-22**|**SUES-200: A Multi-height Multi-scene Cross-view Image Benchmark Across Drone and Satellite**|Runzhe Zhu et.al.|[2204.10704](http://arxiv.org/abs/2204.10704)|**[link](https://github.com/Reza-Zhu/SUES-200-Benchmark)**|
|**2022-04-20**|**Uncertainty-based Cross-Modal Retrieval with Probabilistic Representations**|Leila Pishdad et.al.|[2204.09268](http://arxiv.org/abs/2204.09268)|null|
|**2022-04-19**|**OpenGlue: Open Source Graph Neural Net Based Pipeline for Image Matching**|Ostap Viniavskyi et.al.|[2204.08870](http://arxiv.org/abs/2204.08870)|**[link](https://github.com/ucuapps/openglue)**|
|**2022-04-19**|**Self-Supervised Equivariant Learning for Oriented Keypoint Detection**|Jongmin Lee et.al.|[2204.08613](http://arxiv.org/abs/2204.08613)|**[link](https://github.com/bluedream1121/REKD)**|
|**2022-04-22**|**Efficient Linear Attention for Fast and Accurate Keypoint Matching**|Suwichaya Suwanwimolkul et.al.|[2204.07731](http://arxiv.org/abs/2204.07731)|null|
|**2022-04-08**|**Lightweight starshade position sensing with convolutional neural networks and simulation-based inference**|Andrew Chen et.al.|[2204.03853](http://arxiv.org/abs/2204.03853)|**[link](https://github.com/astro-data-lab/starshade-xy)**|
|**2022-03-30**|**AmsterTime: A Visual Place Recognition Benchmark Dataset for Severe Domain Shift**|Burak Yildiz et.al.|[2203.16291](http://arxiv.org/abs/2203.16291)|**[link](https://github.com/seyrankhademi/AmsterTime)**|
|**2022-03-29**|**Photographic Visualization of Weather Forecasts with Generative Adversarial Networks**|Christian Sigg et.al.|[2203.15601](http://arxiv.org/abs/2203.15601)|**[link](https://github.com/meteoswiss/photocast)**|
|**2022-03-29**|**Sparse Image based Navigation Architecture to Mitigate the need of precise Localization in Mobile Robots**|Pranay Mathur et.al.|[2203.15272](http://arxiv.org/abs/2203.15272)|null|
|**2022-03-28**|**Optimizing Elimination Templates by Greedy Parameter Search**|Evgeniy Martyushev et.al.|[2203.14901](http://arxiv.org/abs/2203.14901)|**[link](https://github.com/martyushev/eliminationtemplates)**|
|**2022-03-28**|**S2-Net: Self-supervision Guided Feature Representation Learning for Cross-Modality Images**|Shasha Mei et.al.|[2203.14581](http://arxiv.org/abs/2203.14581)|null|
|**2022-03-26**|**Accurate 3-DoF Camera Geo-Localization via Ground-to-Satellite Image Matching**|Yujiao Shi et.al.|[2203.14148](http://arxiv.org/abs/2203.14148)|**[link](https://github.com/shiyujiao/ibl)**|
|**2022-03-24**|**Keypoints Tracking via Transformer Networks**|Oleksii Nasypanyi et.al.|[2203.12848](http://arxiv.org/abs/2203.12848)|**[link](https://github.com/lexanagibator228/keypoints-tracking-via-transformer-networks)**|
|**2022-03-21**|**MatchFormer: Interleaving Attention in Transformers for Feature Matching**|Qing Wang et.al.|[2203.09645](http://arxiv.org/abs/2203.09645)|**[link](https://github.com/jamycheung/matchformer)**|
|**2022-03-14**|**There's no difference: Convolutional Neural Networks for transient detection without template subtraction**|Tatiana Acero-Cuellar et.al.|[2203.07390](http://arxiv.org/abs/2203.07390)|**[link](https://github.com/taceroc/dia_nodia)**|
|**2022-03-25**|**Cross Language Image Matching for Weakly Supervised Semantic Segmentation**|Jinheng Xie et.al.|[2203.02668](http://arxiv.org/abs/2203.02668)|**[link](https://github.com/cvi-szu/clims)**|
|**2022-03-01**|**CLIP-GEN: Language-Free Training of a Text-to-Image Generator with CLIP**|Zihao Wang et.al.|[2203.00386](http://arxiv.org/abs/2203.00386)|null|
|**2022-03-09**|**Time-resolved Imaging of Stochastic Cascade Reactions over a Submillisecond to Second Time Range at the Angstrom Level**|Toshiki Shimizu et.al.|[2202.13332](http://arxiv.org/abs/2202.13332)|null|
|**2022-02-16**|**Cross-view and Cross-domain Underwater Localization based on Optical Aerial and Acoustic Underwater Images**|Matheus M. Dos Santos et.al.|[2202.07817](http://arxiv.org/abs/2202.07817)|null|
|**2022-02-14**|**CATs++: Boosting Cost Aggregation with Convolutions and Transformers**|Seokju Cho et.al.|[2202.06817](http://arxiv.org/abs/2202.06817)|**[link](https://github.com/SunghwanHong/Cost-Aggregation-transformers)**|
|**2022-02-11**|**Improving Image-recognition Edge Caches with a Generative Adversarial Network**|Guilherme B. Souza et.al.|[2202.05929](http://arxiv.org/abs/2202.05929)|null|
|**2022-02-08**|**Learning Optical Flow with Adaptive Graph Reasoning**|Ao Luo et.al.|[2202.03857](http://arxiv.org/abs/2202.03857)|**[link](https://github.com/la30/agflow)**|
|**2022-02-03**|**Sim2Real Object-Centric Keypoint Detection and Description**|Chengliang Zhong et.al.|[2202.00448](http://arxiv.org/abs/2202.00448)|null|
|**2022-01-27**|**Efficient divide-and-conquer registration of UAV and ground LiDAR point clouds through canopy shape context**|Jie Shao et.al.|[2201.11296](http://arxiv.org/abs/2201.11296)|null|
|**2021-12-24**|**Multi-initialization Optimization Network for Accurate 3D Human Pose and Shape Estimation**|Zhiwei Liu et.al.|[2112.12917](http://arxiv.org/abs/2112.12917)|null|
|**2021-12-20**|**Scale-Net: Learning to Reduce Scale Differences for Large-Scale Invariant Image Matching**|Yujie Fu et.al.|[2112.10485](http://arxiv.org/abs/2112.10485)|null|
|**2021-12-19**|**GPU optimization of the 3D Scale-invariant Feature Transform Algorithm and a Novel BRIEF-inspired 3D Fast Descriptor**|Jean-Baptiste Carluer et.al.|[2112.10258](http://arxiv.org/abs/2112.10258)|**[link](https://github.com/carluerjb/3d_sift_cuda)**|
|**2021-12-14**|**More Control for Free! Image Synthesis with Semantic Diffusion Guidance**|Xihui Liu et.al.|[2112.05744](http://arxiv.org/abs/2112.05744)|null|
|**2021-12-08**|**Label-free virtual HER2 immunohistochemical staining of breast tissue using deep learning**|Bijie Bai et.al.|[2112.05240](http://arxiv.org/abs/2112.05240)|null|
|**2021-12-01**|**FaSS-MVS -- Fast Multi-View Stereo with Surface-Aware Semi-Global Matching from UAV-borne Monocular Imagery**|Boitumelo Ruf et.al.|[2112.00821](http://arxiv.org/abs/2112.00821)|null|
|**2021-12-01**|**CLIPstyler: Image Style Transfer with a Single Text Condition**|Gihyun Kwon et.al.|[2112.00374](http://arxiv.org/abs/2112.00374)|**[link](https://github.com/paper11667/clipstyler)**|
|**2021-11-29**|**Nonlinear Intensity Underwater Sonar Image Matching Method Based on Phase Information and Deep Convolution Features**|Xiaoteng Zhou et.al.|[2111.15514](http://arxiv.org/abs/2111.15514)|null|
|**2021-11-29**|**Zero-Shot Image-to-Text Generation for Visual-Semantic Arithmetic**|Yoad Tewel et.al.|[2111.14447](http://arxiv.org/abs/2111.14447)|**[link](https://github.com/yoadtew/zero-shot-image-to-text)**|
|**2021-11-29**|**Heterogeneous Visible-Thermal and Visible-Infrared Face Recognition using Unit-Class Loss and Cross-Modality Discriminator**|Usman Cheema et.al.|[2111.14339](http://arxiv.org/abs/2111.14339)|null|
|**2021-11-17**|**Probabilistic Spatial Distribution Prior Based Attentional Keypoints Matching Network**|Xiaoming Zhao et.al.|[2111.09006](http://arxiv.org/abs/2111.09006)|null|
|**2021-11-17**|**Nonlinear Intensity Sonar Image Matching based on Deep Convolution Features**|Xiaoteng Zhou et.al.|[2111.08994](http://arxiv.org/abs/2111.08994)|null|
|**2021-10-30**|**A Deep Search for Faint Chandra X-ray Sources, Radio Sources, and Optical Counterparts in NGC 6752**|Haldan N. Cohn et.al.|[2111.00357](http://arxiv.org/abs/2111.00357)|null|
|**2021-10-01**|**Robustly Removing Deep Sea Lighting Effects for Visual Mapping of Abyssal Plains**|Kevin Köser et.al.|[2110.00480](http://arxiv.org/abs/2110.00480)|null|
|**2021-09-29**|**Visually Grounded Concept Composition**|Bowen Zhang et.al.|[2109.14115](http://arxiv.org/abs/2109.14115)|null|
|**2021-09-27**|**HarrisZ $^+$ : Harris Corner Selection for Next-Gen Image Matching Pipelines**|Fabio Bellavia et.al.|[2109.12925](http://arxiv.org/abs/2109.12925)|null|
|**2021-09-20**|**Viewpoint Invariant Dense Matching for Visual Geolocalization**|Gabriele Berton et.al.|[2109.09827](http://arxiv.org/abs/2109.09827)|**[link](https://github.com/gmberton/geo_warp)**|
|**2021-09-20**|**Image Subtraction in Fourier Space**|Lei Hu et.al.|[2109.09334](http://arxiv.org/abs/2109.09334)|**[link](https://github.com/thomasvrussell/sfft)**|
|**2021-09-10**|**Line as a Visual Sentence: Context-aware Line Descriptor for Visual Localization**|Sungho Yoon et.al.|[2109.04753](http://arxiv.org/abs/2109.04753)|**[link](https://github.com/yosungho/LineTR)**|
|**2021-09-08**|**Matching in the Dark: A Dataset for Matching Image Pairs of Low-light Scenes**|Wenzheng Song et.al.|[2109.03585](http://arxiv.org/abs/2109.03585)|null|
|**2021-08-27**|**A Matching Algorithm based on Image Attribute Transfer and Local Features for Underwater Acoustic and Optical Images**|Xiaoteng Zhou et.al.|[2108.12151](http://arxiv.org/abs/2108.12151)|null|
|**2021-08-27**|**Matching Underwater Sonar Images by the Learned Descriptor Based on Style Transfer Method**|Xiaoteng Zhou et.al.|[2108.12072](http://arxiv.org/abs/2108.12072)|null|
|**2021-08-26**|**Efficient Joint Object Matching via Linear Programming**|Antonio De Rosa et.al.|[2108.11911](http://arxiv.org/abs/2108.11911)|null|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## NeRF

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2023-06-13**|**Binary Radiance Fields**|Seungjoo Shin et.al.|[2306.07581](http://arxiv.org/abs/2306.07581)|null|
|**2023-06-10**|**From NeRFLiX to NeRFLiX++: A General NeRF-Agnostic Restorer Paradigm**|Kun Zhou et.al.|[2306.06388](http://arxiv.org/abs/2306.06388)|null|
|**2023-06-09**|**NERFBK: A High-Quality Benchmark for NERF-Based 3D Reconstruction**|Ali Karami et.al.|[2306.06300](http://arxiv.org/abs/2306.06300)|**[link](https://github.com/3dom-fbk/nerfbk)**|
|**2023-06-09**|**HyP-NeRF: Learning Improved NeRF Priors using a HyperNetwork**|Bipasha Sen et.al.|[2306.06093](http://arxiv.org/abs/2306.06093)|null|
|**2023-06-09**|**GANeRF: Leveraging Discriminators to Optimize Neural Radiance Fields**|Barbara Roessle et.al.|[2306.06044](http://arxiv.org/abs/2306.06044)|null|
|**2023-06-09**|**RePaint-NeRF: NeRF Editting via Semantic Masks and Diffusion Models**|Xingchen Zhou et.al.|[2306.05668](http://arxiv.org/abs/2306.05668)|null|
|**2023-06-08**|**LU-NeRF: Scene and Pose Estimation by Synchronizing Local Unposed NeRFs**|Zezhou Cheng et.al.|[2306.05410](http://arxiv.org/abs/2306.05410)|null|
|**2023-06-08**|**Enhance-NeRF: Multiple Performance Evaluation for Neural Radiance Fields**|Qianqiu Tan et.al.|[2306.05303](http://arxiv.org/abs/2306.05303)|**[link](https://github.com/tanqianq/enhance-nerf)**|
|**2023-06-06**|**Towards Visual Foundational Models of Physical Scenes**|Chethan Parameshwara et.al.|[2306.03727](http://arxiv.org/abs/2306.03727)|null|
|**2023-06-06**|**Human 3D Avatar Modeling with Implicit Neural Representation: A Brief Survey**|Mingyang Sun et.al.|[2306.03576](http://arxiv.org/abs/2306.03576)|null|
|**2023-06-05**|**H2-Mapping: Real-time Dense Mapping Using Hierarchical Hybrid Representation**|Chenxing Jiang et.al.|[2306.03207](http://arxiv.org/abs/2306.03207)|**[link](https://github.com/sysu-star/h2-mapping)**|
|**2023-06-05**|**BeyondPixels: A Comprehensive Review of the Evolution of Neural Radiance Fields**|AKM Shahariar Azad Rabby et.al.|[2306.03000](http://arxiv.org/abs/2306.03000)|null|
|**2023-06-05**|**ZIGNeRF: Zero-shot 3D Scene Representation with Invertible Generative Neural Radiance Fields**|Kanghyeok Ko et.al.|[2306.02741](http://arxiv.org/abs/2306.02741)|null|
|**2023-06-01**|**FDNeRF: Semantics-Driven Face Reconstruction, Prompt Editing and Relighting with Diffusion Models**|Hao Zhang et.al.|[2306.00783](http://arxiv.org/abs/2306.00783)|**[link](https://github.com/billyxyb/fdnerf)**|
|**2023-06-01**|**Analyzing the Internals of Neural Radiance Fields**|Lukas Radl et.al.|[2306.00696](http://arxiv.org/abs/2306.00696)|**[link](https://github.com/r4dl/nerfinternals)**|
|**2023-06-02**|**AvatarStudio: Text-driven Editing of 3D Dynamic Human Head Avatars**|Mohit Mendiratta et.al.|[2306.00547](http://arxiv.org/abs/2306.00547)|null|
|**2023-05-30**|**DäRF: Boosting Radiance Fields from Sparse Inputs with Monocular Depth Adaptation**|Jiuhn Song et.al.|[2305.19201](http://arxiv.org/abs/2305.19201)|**[link](https://github.com/KU-CVLAB/DaRF)**|
|**2023-05-30**|**Template-free Articulated Neural Point Clouds for Reposable View Synthesis**|Lukas Uzolas et.al.|[2305.19065](http://arxiv.org/abs/2305.19065)|**[link](https://github.com/lukasuz/articulated-point-nerf)**|
|**2023-05-31**|**HiFA: High-fidelity Text-to-3D with Advanced Diffusion Guidance**|Junzhe Zhu et.al.|[2305.18766](http://arxiv.org/abs/2305.18766)|**[link](https://github.com/JunzheJosephZhu/HiFA)**|
|**2023-05-31**|**Towards a Robust Framework for NeRF Evaluation**|Adrian Azzarelli et.al.|[2305.18079](http://arxiv.org/abs/2305.18079)|**[link](https://github.com/azzarelli/wape)**|
|**2023-05-31**|**Volume Feature Rendering for Fast Neural Radiance Field Reconstruction**|Kang Han et.al.|[2305.17916](http://arxiv.org/abs/2305.17916)|null|
|**2023-05-30**|**PlaNeRF: SVD Unsupervised 3D Plane Regularization for NeRF Large-Scale Scene Reconstruction**|Fusang Wang et.al.|[2305.16914](http://arxiv.org/abs/2305.16914)|null|
|**2023-05-25**|**ZeroAvatar: Zero-shot 3D Avatar Generation from a Single Image**|Zhenzhen Weng et.al.|[2305.16411](http://arxiv.org/abs/2305.16411)|null|
|**2023-05-25**|**Interactive Segment Anything NeRF with Feature Imitation**|Xiaokang Chen et.al.|[2305.16233](http://arxiv.org/abs/2305.16233)|null|
|**2023-05-25**|**ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation**|Zhengyi Wang et.al.|[2305.16213](http://arxiv.org/abs/2305.16213)|**[link](https://github.com/thu-ml/prolificdreamer)**|
|**2023-05-31**|**Deceptive-NeRF: Enhancing NeRF Reconstruction using Pseudo-Observations from Diffusion Models**|Xinhang Liu et.al.|[2305.15171](http://arxiv.org/abs/2305.15171)|null|
|**2023-05-24**|**InpaintNeRF360: Text-Guided 3D Inpainting on Unbounded Neural Radiance Fields**|Dongqing Wang et.al.|[2305.15094](http://arxiv.org/abs/2305.15094)|null|
|**2023-05-24**|**OD-NeRF: Efficient Training of On-the-Fly Dynamic Neural Radiance Fields**|Zhiwen Yan et.al.|[2305.14831](http://arxiv.org/abs/2305.14831)|null|
|**2023-05-24**|**3D Open-vocabulary Segmentation with Foundation Models**|Kunhao Liu et.al.|[2305.14093](http://arxiv.org/abs/2305.14093)|**[link](https://github.com/kunhao-liu/3d-ovs)**|
|**2023-05-22**|**NeRFuser: Large-Scale Scene Representation by NeRF Fusion**|Jiading Fang et.al.|[2305.13307](http://arxiv.org/abs/2305.13307)|**[link](https://github.com/ripl/nerfuser)**|
|**2023-05-22**|**Registering Neural Radiance Fields as 3D Density Images**|Han Jiang et.al.|[2305.12843](http://arxiv.org/abs/2305.12843)|null|
|**2023-05-19**|**Text2NeRF: Text-Driven 3D Scene Generation with Neural Radiance Fields**|Jingbo Zhang et.al.|[2305.11588](http://arxiv.org/abs/2305.11588)|**[link](https://github.com/eckertzhang/text2nerf)**|
|**2023-05-18**|**MVPSNet: Fast Generalizable Multi-view Photometric Stereo**|Dongxu Zhao et.al.|[2305.11167](http://arxiv.org/abs/2305.11167)|null|
|**2023-05-18**|**ConsistentNeRF: Enhancing Neural Radiance Fields with 3D Consistency for Sparse View Synthesis**|Shoukang Hu et.al.|[2305.11031](http://arxiv.org/abs/2305.11031)|**[link](https://github.com/skhu101/consistentnerf)**|
|**2023-05-17**|**MultiPlaneNeRF: Neural Radiance Field with Non-Trainable Representation**|Dominik Zimny et.al.|[2305.10579](http://arxiv.org/abs/2305.10579)|**[link](https://github.com/gmum/multiplanenerf)**|
|**2023-05-24**|**OR-NeRF: Object Removing from 3D Scenes Guided by Multiview Segmentation with Neural Radiance Fields**|Youtan Yin et.al.|[2305.10503](http://arxiv.org/abs/2305.10503)|**[link](https://github.com/cuteyyt/or-nerf)**|
|**2023-05-16**|**NerfBridge: Bringing Real-time, Online Neural Radiance Field Training to Robotics**|Javier Yu et.al.|[2305.09761](http://arxiv.org/abs/2305.09761)|**[link](https://github.com/javieryu/nerf_bridge)**|
|**2023-05-15**|**MV-Map: Offboard HD-Map Generation with Multi-view Consistency**|Ziyang Xie et.al.|[2305.08851](http://arxiv.org/abs/2305.08851)|**[link](https://github.com/ziyang-xie/mv-map)**|
|**2023-05-12**|**BundleRecon: Ray Bundle-Based 3D Neural Reconstruction**|Weikun Zhang et.al.|[2305.07342](http://arxiv.org/abs/2305.07342)|null|
|**2023-05-10**|**Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era**|Chenghao Li et.al.|[2305.06131](http://arxiv.org/abs/2305.06131)|null|
|**2023-05-10**|**NeRF $^\textbf{2}$ : Neural Radio-Frequency Radiance Fields**|Xiaopeng Zhao et.al.|[2305.06118](http://arxiv.org/abs/2305.06118)|null|
|**2023-05-09**|**Instant-NeRF: Instant On-Device Neural Radiance Field Training via Algorithm-Accelerator Co-Designed Near-Memory Processing**|Yang Zhao et.al.|[2305.05766](http://arxiv.org/abs/2305.05766)|null|
|**2023-05-09**|**PET-NeuS: Positional Encoding Tri-Planes for Neural Surfaces**|Yiqun Wang et.al.|[2305.05594](http://arxiv.org/abs/2305.05594)|**[link](https://github.com/yiqun-wang/pet-neus)**|
|**2023-05-08**|**NerfAcc: Efficient Sampling Accelerates NeRFs**|Ruilong Li et.al.|[2305.04966](http://arxiv.org/abs/2305.04966)|null|
|**2023-05-08**|**AvatarReX: Real-time Expressive Full-body Avatars**|Zerong Zheng et.al.|[2305.04789](http://arxiv.org/abs/2305.04789)|null|
|**2023-05-07**|**HashCC: Lightweight Method to Improve the Quality of the Camera-less NeRF Scene Generation**|Jan Olszewski et.al.|[2305.04296](http://arxiv.org/abs/2305.04296)|null|
|**2023-05-07**|**Multi-Space Neural Radiance Fields**|Ze-Xin Yin et.al.|[2305.04268](http://arxiv.org/abs/2305.04268)|null|
|**2023-05-04**|**NeRF-QA: Neural Radiance Fields Quality Assessment Database**|Pedro Martin et.al.|[2305.03176](http://arxiv.org/abs/2305.03176)|null|
|**2023-05-04**|**NeuralEditor: Editing Neural Radiance Fields via Manipulating Point Clouds**|Jun-Kun Chen et.al.|[2305.03049](http://arxiv.org/abs/2305.03049)|null|
|**2023-05-04**|**Radiance Field Gradient Scaling for Unbiased Near-Camera Training**|Julien Philip et.al.|[2305.02756](http://arxiv.org/abs/2305.02756)|**[link](https://github.com/gradient-scaling/gradient-scaling.github.io)**|
|**2023-05-04**|**Semantic-aware Generation of Multi-view Portrait Drawings**|Biao Ma et.al.|[2305.02618](http://arxiv.org/abs/2305.02618)|**[link](https://github.com/aiart-hdu/sage)**|
|**2023-05-02**|**Neural LiDAR Fields for Novel View Synthesis**|Shengyu Huang et.al.|[2305.01643](http://arxiv.org/abs/2305.01643)|null|
|**2023-05-03**|**LatentAvatar: Learning Latent Expression Code for Expressive Neural Head Avatar**|Yuelang Xu et.al.|[2305.01190](http://arxiv.org/abs/2305.01190)|null|
|**2023-05-02**|**Federated Neural Radiance Fields**|Lachlan Holden et.al.|[2305.01163](http://arxiv.org/abs/2305.01163)|**[link](https://github.com/lachholden/fednerf-pytorch)**|
|**2023-05-01**|**GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation**|Zhenhui Ye et.al.|[2305.00787](http://arxiv.org/abs/2305.00787)|null|
|**2023-04-30**|**Neural Radiance Fields (NeRFs): A Review and Some Recent Developments**|Mohamed Debbagh et.al.|[2305.00375](http://arxiv.org/abs/2305.00375)|null|
|**2023-04-28**|**ViP-NeRF: Visibility Prior for Sparse Input Neural Radiance Fields**|Nagabhushan Somraj et.al.|[2305.00041](http://arxiv.org/abs/2305.00041)|**[link](https://github.com/NagabhushanSN95/ViP-NeRF)**|
|**2023-04-28**|**NeRF-LiDAR: Generating Realistic LiDAR Point Clouds with Neural Radiance Fields**|Junge Zhang et.al.|[2304.14811](http://arxiv.org/abs/2304.14811)|**[link](https://github.com/fudan-zvg/nerf-lidar)**|
|**2023-04-27**|**Learning a Diffusion Prior for NeRFs**|Guandao Yang et.al.|[2304.14473](http://arxiv.org/abs/2304.14473)|null|
|**2023-04-27**|**ActorsNeRF: Animatable Few-shot Human Rendering with Generalizable NeRFs**|Jiteng Mu et.al.|[2304.14401](http://arxiv.org/abs/2304.14401)|null|
|**2023-05-03**|**Combining HoloLens with Instant-NeRFs: Advanced Real-Time 3D Mobile Mapping**|Dennis Haitz et.al.|[2304.14301](http://arxiv.org/abs/2304.14301)|null|
|**2023-04-27**|**Compositional 3D Human-Object Neural Animation**|Zhi Hou et.al.|[2304.14070](http://arxiv.org/abs/2304.14070)|null|
|**2023-04-26**|**Super-NeRF: View-consistent Detail Generation for NeRF super-resolution**|Yuqi Han et.al.|[2304.13518](http://arxiv.org/abs/2304.13518)|null|
|**2023-04-26**|**VGOS: Voxel Grid Optimization for View Synthesis from Sparse Inputs**|Jiakai Sun et.al.|[2304.13386](http://arxiv.org/abs/2304.13386)|**[link](https://github.com/sjojok/vgos)**|
|**2023-04-25**|**Local Implicit Ray Function for Generalizable Radiance Field Representation**|Xin Huang et.al.|[2304.12746](http://arxiv.org/abs/2304.12746)|null|
|**2023-04-27**|**MF-NeRF: Memory Efficient NeRF with Mixed-Feature Hash Table**|Yongjae Lee et.al.|[2304.12587](http://arxiv.org/abs/2304.12587)|**[link](https://github.com/nfyfamr/mf-nerf)**|
|**2023-04-24**|**Instant-3D: Instant Neural Radiance Field Training Towards On-Device AR/VR 3D Reconstruction**|Sixu Li et.al.|[2304.12467](http://arxiv.org/abs/2304.12467)|null|
|**2023-04-24**|**TextMesh: Generation of Realistic 3D Meshes From Text Prompts**|Christina Tsalicoglou et.al.|[2304.12439](http://arxiv.org/abs/2304.12439)|null|
|**2023-04-26**|**Segment Anything in 3D with NeRFs**|Jiazhong Cen et.al.|[2304.12308](http://arxiv.org/abs/2304.12308)|**[link](https://github.com/jumpat/segmentanythingin3d)**|
|**2023-04-24**|**Explicit Correspondence Matching for Generalizable Neural Radiance Fields**|Yuedong Chen et.al.|[2304.12294](http://arxiv.org/abs/2304.12294)|**[link](https://github.com/donydchen/matchnerf)**|
|**2023-04-25**|**Gen-NeRF: Efficient and Generalizable Neural Radiance Fields via Algorithm-Hardware Co-Design**|Yonggan Fu et.al.|[2304.11842](http://arxiv.org/abs/2304.11842)|null|
|**2023-04-22**|**3D-IntPhys: Towards More Generalized 3D-grounded Visual Intuitive Physics under Challenging Scenes**|Haotian Xue et.al.|[2304.11470](http://arxiv.org/abs/2304.11470)|null|
|**2023-04-22**|**Dehazing-NeRF: Neural Radiance Fields from Hazy Images**|Tian Li et.al.|[2304.11448](http://arxiv.org/abs/2304.11448)|null|
|**2023-04-22**|**NaviNeRF: NeRF-based 3D Representation Disentanglement by Latent Semantic Navigation**|Baao Xie et.al.|[2304.11342](http://arxiv.org/abs/2304.11342)|**[link](https://github.com/arlo0o/navinerf)**|
|**2023-04-21**|**AutoNeRF: Training Implicit Scene Representations with Autonomous Agents**|Pierre Marza et.al.|[2304.11241](http://arxiv.org/abs/2304.11241)|**[link](https://github.com/PierreMarza/autonerf)**|
|**2023-04-21**|**Omni-Line-of-Sight Imaging for Holistic Shape Reconstruction**|Binbin Huang et.al.|[2304.10780](http://arxiv.org/abs/2304.10780)|null|
|**2023-04-20**|**A Comparative Neural Radiance Field (NeRF) 3D Analysis of Camera Poses from HoloLens Trajectories and Structure from Motion**|Miriam Jäger et.al.|[2304.10664](http://arxiv.org/abs/2304.10664)|null|
|**2023-04-20**|**Learning Neural Duplex Radiance Fields for Real-Time View Synthesis**|Ziyu Wan et.al.|[2304.10537](http://arxiv.org/abs/2304.10537)|null|
|**2023-04-21**|**Nerfbusters: Removing Ghostly Artifacts from Casually Captured NeRFs**|Frederik Warburg et.al.|[2304.10532](http://arxiv.org/abs/2304.10532)|**[link](https://github.com/ethanweber/nerfbusters)**|
|**2023-04-20**|**ReLight My NeRF: A Dataset for Novel View Synthesis and Relighting of Real World Objects**|Marco Toschi et.al.|[2304.10448](http://arxiv.org/abs/2304.10448)|null|
|**2023-04-20**|**LiDAR-NeRF: Novel LiDAR View Synthesis via Neural Radiance Fields**|Tang Tao et.al.|[2304.10406](http://arxiv.org/abs/2304.10406)|**[link](https://github.com/tangtaogo/lidar-nerf)**|
|**2023-04-20**|**Revisiting Implicit Neural Representations in Low-Level Vision**|Wentian Xu et.al.|[2304.10250](http://arxiv.org/abs/2304.10250)|**[link](https://github.com/wentxul/linr)**|
|**2023-04-20**|**Multiscale Representation for Real-Time Anti-Aliasing Neural Rendering**|Dongting Hu et.al.|[2304.10075](http://arxiv.org/abs/2304.10075)|null|
|**2023-04-20**|**Neural Radiance Fields: Past, Present, and Future**|Ansh Mittal et.al.|[2304.10050](http://arxiv.org/abs/2304.10050)|**[link](https://github.com/vlar-group/nvfi)**|
|**2023-04-19**|**Tetra-NeRF: Representing Neural Radiance Fields Using Tetrahedra**|Jonas Kulhanek et.al.|[2304.09987](http://arxiv.org/abs/2304.09987)|**[link](https://github.com/jkulhanek/tetra-nerf)**|
|**2023-04-20**|**Reference-guided Controllable Inpainting of Neural Radiance Fields**|Ashkan Mirzaei et.al.|[2304.09677](http://arxiv.org/abs/2304.09677)|null|
|**2023-04-18**|**SurfelNeRF: Neural Surfel Radiance Fields for Online Photorealistic Reconstruction of Indoor Scenes**|Yiming Gao et.al.|[2304.08971](http://arxiv.org/abs/2304.08971)|null|
|**2023-04-18**|**NeAI: A Pre-convoluted Representation for Plug-and-Play Neural Ambient Illumination**|Yiyu Zhuang et.al.|[2304.08757](http://arxiv.org/abs/2304.08757)|null|
|**2023-04-17**|**MoDA: Modeling Deformable 3D Objects from Casual Videos**|Chaoyue Song et.al.|[2304.08279](http://arxiv.org/abs/2304.08279)|**[link](https://github.com/chaoyuesong/moda)**|
|**2023-04-17**|**NeRF-Loc: Visual Localization with Conditional Neural Radiance Field**|Jianlin Liu et.al.|[2304.07979](http://arxiv.org/abs/2304.07979)|**[link](https://github.com/jenningsl/nerf-loc)**|
|**2023-04-16**|**Likelihood-Based Generative Radiance Field with Latent Space Energy-Based Model for 3D-Aware Disentangled Image Representation**|Yaxuan Zhu et.al.|[2304.07918](http://arxiv.org/abs/2304.07918)|null|
|**2023-04-16**|**CAT-NeRF: Constancy-Aware Tx $^2$ Former for Dynamic Body Modeling**|Haidong Zhu et.al.|[2304.07915](http://arxiv.org/abs/2304.07915)|**[link](https://github.com/haidongz-usc/CAT-NeRF)**|
|**2023-04-16**|**SeaThru-NeRF: Neural Radiance Fields in Scattering Media**|Deborah Levy et.al.|[2304.07743](http://arxiv.org/abs/2304.07743)|**[link](https://github.com/deborahLevy130/seathru_NeRF)**|
|**2023-04-14**|**UVA: Towards Unified Volumetric Avatar for View Synthesis, Pose rendering, Geometry and Texture Editing**|Jinlong Fan et.al.|[2304.06969](http://arxiv.org/abs/2304.06969)|null|
|**2023-04-17**|**Single-Stage Diffusion NeRF: A Unified Approach to 3D Generation and Reconstruction**|Hansheng Chen et.al.|[2304.06714](http://arxiv.org/abs/2304.06714)|**[link](https://github.com/Lakonik/SSDNeRF)**|
|**2023-04-13**|**Zip-NeRF: Anti-Aliased Grid-Based Neural Radiance Fields**|Jonathan T. Barron et.al.|[2304.06706](http://arxiv.org/abs/2304.06706)|null|
|**2023-04-13**|**NeRFVS: Neural Radiance Fields for Free View Synthesis via Geometry Scaffolds**|Chen Yang et.al.|[2304.06287](http://arxiv.org/abs/2304.06287)|null|
|**2023-04-12**|**NutritionVerse-Thin: An Optimized Strategy for Enabling Improved Rendering of 3D Thin Food Models**|Chi-en Amy Tai et.al.|[2304.05620](http://arxiv.org/abs/2304.05620)|null|
|**2023-04-11**|**Improving Neural Radiance Fields with Depth-aware Optimization for Novel View Synthesis**|Shu Chen et.al.|[2304.05218](http://arxiv.org/abs/2304.05218)|**[link](https://github.com/xtu-pr-lab/sfmnerf)**|
|**2023-04-11**|**One-Shot High-Fidelity Talking-Head Synthesis with Deformable Neural Radiance Field**|Weichuang Li et.al.|[2304.05097](http://arxiv.org/abs/2304.05097)|null|
|**2023-04-11**|**MRVM-NeRF: Mask-Based Pretraining for Neural Radiance Fields**|Ganlin Yang et.al.|[2304.04962](http://arxiv.org/abs/2304.04962)|**[link](https://github.com/ganlin-yang/mrvm-nerf)**|
|**2023-04-10**|**Neural Image-based Avatars: Generalizable Radiance Fields for Human Avatar Modeling**|Youngjoong Kwon et.al.|[2304.04897](http://arxiv.org/abs/2304.04897)|null|
|**2023-04-07**|**Event-based Camera Tracker by $\nabla$ t NeRF**|Mana Masuda et.al.|[2304.04559](http://arxiv.org/abs/2304.04559)|null|
|**2023-04-10**|**Neural Residual Radiance Fields for Streamably Free-Viewpoint Videos**|Liao Wang et.al.|[2304.04452](http://arxiv.org/abs/2304.04452)|null|
|**2023-04-10**|**Inferring Fluid Dynamics via Inverse Rendering**|Jinxian Liu et.al.|[2304.04446](http://arxiv.org/abs/2304.04446)|null|
|**2023-04-10**|**Instance Neural Radiance Field**|Benran Hu et.al.|[2304.04395](http://arxiv.org/abs/2304.04395)|**[link](https://github.com/lyclyc52/instance_nerf)**|
|**2023-04-12**|**NeRF applied to satellite imagery for surface reconstruction**|Federico Semeraro et.al.|[2304.04133](http://arxiv.org/abs/2304.04133)|**[link](https://github.com/fsemerar/satnerf)**|
|**2023-04-08**|**PVD-AL: Progressive Volume Distillation with Active Learning for Efficient Conversion Between Different NeRF Architectures**|Shuangkang Fang et.al.|[2304.04012](http://arxiv.org/abs/2304.04012)|**[link](https://github.com/megvii-research/AAAI2023-PVD)**|
|**2023-04-07**|**Lift3D: Synthesize 3D Training Data by Lifting 2D GAN to 3D Generative Radiance Field**|Leheng Li et.al.|[2304.03526](http://arxiv.org/abs/2304.03526)|null|
|**2023-04-06**|**Beyond NeRF Underwater: Learning Neural Reflectance Fields for True Color Correction of Marine Imagery**|Tianyi Zhang et.al.|[2304.03384](http://arxiv.org/abs/2304.03384)|**[link](https://github.com/tyz1030/neuralsea)**|
|**2023-04-06**|**LANe: Lighting-Aware Neural Fields for Compositional Scene Synthesis**|Akshay Krishnan et.al.|[2304.03280](http://arxiv.org/abs/2304.03280)|null|
|**2023-04-06**|**Neural Fields meet Explicit Geometric Representation for Inverse Rendering of Urban Scenes**|Zian Wang et.al.|[2304.03266](http://arxiv.org/abs/2304.03266)|null|
|**2023-04-06**|**DITTO-NeRF: Diffusion-based Iterative Text To Omni-directional 3D Model**|Hoigi Seo et.al.|[2304.02827](http://arxiv.org/abs/2304.02827)|null|
|**2023-04-05**|**Image Stabilization for Hololens Camera in Remote Collaboration**|Gowtham Senthil et.al.|[2304.02736](http://arxiv.org/abs/2304.02736)|null|
|**2023-04-04**|**Generating Continual Human Motion in Diverse 3D Scenes**|Aymen Mir et.al.|[2304.02061](http://arxiv.org/abs/2304.02061)|null|
|**2023-04-04**|**MonoHuman: Animatable Human Neural Field from Monocular Video**|Zhengming Yu et.al.|[2304.02001](http://arxiv.org/abs/2304.02001)|null|
|**2023-04-06**|**DreamAvatar: Text-and-Shape Guided 3D Human Avatar Generation via Diffusion Models**|Yukang Cao et.al.|[2304.00916](http://arxiv.org/abs/2304.00916)|**[link](https://github.com/threestudio-project/threestudio)**|
|**2023-04-01**|**JacobiNeRF: NeRF Shaping with Mutual Information Gradients**|Xiaomeng Xu et.al.|[2304.00341](http://arxiv.org/abs/2304.00341)|**[link](https://github.com/xxm19/jacobinerf)**|
|**2023-03-31**|**VDN-NeRF: Resolving Shape-Radiance Ambiguity via View-Dependence Normalization**|Bingfan Zhu et.al.|[2303.17968](http://arxiv.org/abs/2303.17968)|**[link](https://github.com/boifz/vdn-nerf)**|
|**2023-03-30**|**NeRF-Supervised Deep Stereo**|Fabio Tosi et.al.|[2303.17603](http://arxiv.org/abs/2303.17603)|**[link](https://github.com/fabiotosi92/nerf-supervised-deep-stereo)**|
|**2023-03-30**|**SynBody: Synthetic Dataset with Layered Human Models for 3D Human Perception and Modeling**|Zhitao Yang et.al.|[2303.17368](http://arxiv.org/abs/2303.17368)|**[link](https://github.com/openxrlab/xrfeitoria)**|
|**2023-03-30**|**NeILF++: Inter-Reflectable Light Fields for Geometry and Material Estimation**|Jingyang Zhang et.al.|[2303.17147](http://arxiv.org/abs/2303.17147)|null|
|**2023-03-30**|**Enhanced Stable View Synthesis**|Nishant Jain et.al.|[2303.17094](http://arxiv.org/abs/2303.17094)|null|
|**2023-03-29**|**TriVol: Point Cloud Rendering via Triple Volumes**|Tao Hu et.al.|[2303.16485](http://arxiv.org/abs/2303.16485)|**[link](https://github.com/dvlab-research/trivol)**|
|**2023-03-29**|**Point2Pix: Photo-Realistic Point Cloud Rendering via Neural Radiance Fields**|Tao Hu et.al.|[2303.16482](http://arxiv.org/abs/2303.16482)|null|
|**2023-03-28**|**Flow supervision for Deformable NeRF**|Chaoyang Wang et.al.|[2303.16333](http://arxiv.org/abs/2303.16333)|null|
|**2023-03-28**|**SparseNeRF: Distilling Depth Ranking for Few-shot Novel View Synthesis**|Guangcong Wang et.al.|[2303.16196](http://arxiv.org/abs/2303.16196)|**[link](https://github.com/Wanggcong/SparseNeRF)**|
|**2023-03-28**|**VMesh: Hybrid Volume-Mesh Representation for Efficient View Synthesis**|Yuan-Chen Guo et.al.|[2303.16184](http://arxiv.org/abs/2303.16184)|null|
|**2023-03-30**|**Adaptive Voronoi NeRFs**|Tim Elsner et.al.|[2303.16001](http://arxiv.org/abs/2303.16001)|null|
|**2023-03-28**|**F $^{2}$ -NeRF: Fast Neural Radiance Field Training with Free Camera Trajectories**|Peng Wang et.al.|[2303.15951](http://arxiv.org/abs/2303.15951)|**[link](https://github.com/Totoro97/f2-nerf)**|
|**2023-03-27**|**JAWS: Just A Wild Shot for Cinematic Transfer in Neural Radiance Fields**|Xi Wang et.al.|[2303.15427](http://arxiv.org/abs/2303.15427)|**[link](https://github.com/robincourant/jaws)**|
|**2023-03-27**|**Generalizable Neural Voxels for Fast Human Radiance Fields**|Taoran Yi et.al.|[2303.15387](http://arxiv.org/abs/2303.15387)|null|
|**2023-03-27**|**NeUDF: Learning Unsigned Distance Fields from Multi-view Images for Reconstructing Non-watertight Models**|Fei Hou et.al.|[2303.15368](http://arxiv.org/abs/2303.15368)|**[link](https://bitbucket.org/jkdeng/2sudf)**|
|**2023-03-24**|**Perceptual Quality Assessment of NeRF and Neural View Synthesis Methods for Front-Facing Views**|Hanxue Liang et.al.|[2303.15206](http://arxiv.org/abs/2303.15206)|null|
|**2023-03-27**|**3D-Aware Multi-Class Image-to-Image Translation with NeRFs**|Senmao Li et.al.|[2303.15012](http://arxiv.org/abs/2303.15012)|**[link](https://github.com/sen-mao/3di2i-translation)**|
|**2023-03-26**|**Clean-NeRF: Reformulating NeRF to account for View-Dependent Observations**|Xinhang Liu et.al.|[2303.14707](http://arxiv.org/abs/2303.14707)|null|
|**2023-03-25**|**SUDS: Scalable Urban Dynamic Scenes**|Haithem Turki et.al.|[2303.14536](http://arxiv.org/abs/2303.14536)|null|
|**2023-03-25**|**DBARF: Deep Bundle-Adjusting Generalizable Neural Radiance Fields**|Yu Chen et.al.|[2303.14478](http://arxiv.org/abs/2303.14478)|null|
|**2023-03-25**|**NeRF-DS: Neural Radiance Fields for Dynamic Specular Objects**|Zhiwen Yan et.al.|[2303.14435](http://arxiv.org/abs/2303.14435)|**[link](https://github.com/jokeryan/nerf-ds)**|
|**2023-03-24**|**Grid-guided Neural Radiance Fields for Large Urban Scenes**|Linning Xu et.al.|[2303.14001](http://arxiv.org/abs/2303.14001)|null|
|**2023-03-24**|**CompoNeRF: Text-guided Multi-object Compositional NeRF with Editable 3D Scene Layout**|Yiqi Lin et.al.|[2303.13843](http://arxiv.org/abs/2303.13843)|null|
|**2023-03-24**|**HandNeRF: Neural Radiance Fields for Animatable Interacting Hands**|Zhiyang Guo et.al.|[2303.13825](http://arxiv.org/abs/2303.13825)|null|
|**2023-03-24**|**ABLE-NeRF: Attention-Based Rendering with Learnable Embeddings for Neural Radiance Field**|Zhe Jun Tang et.al.|[2303.13817](http://arxiv.org/abs/2303.13817)|**[link](https://github.com/tangzj/able-nerf)**|
|**2023-03-24**|**GM-NeRF: Learning Generalizable Model-based Neural Radiance Fields from Multi-view Images**|Jianchuan Chen et.al.|[2303.13777](http://arxiv.org/abs/2303.13777)|null|
|**2023-03-24**|**TEGLO: High Fidelity Canonical Texture Mapping from Single-View Images**|Vishal Vinod et.al.|[2303.13743](http://arxiv.org/abs/2303.13743)|null|
|**2023-03-23**|**SCADE: NeRFs from Space Carving with Ambiguity-Aware Depth Estimates**|Mikaela Angelina Uy et.al.|[2303.13582](http://arxiv.org/abs/2303.13582)|null|
|**2023-03-23**|**TriPlaneNet: An Encoder for EG3D Inversion**|Ananta R. Bhattarai et.al.|[2303.13497](http://arxiv.org/abs/2303.13497)|null|
|**2023-03-23**|**Plotting Behind the Scenes: Towards Learnable Game Engines**|Willi Menapace et.al.|[2303.13472](http://arxiv.org/abs/2303.13472)|null|
|**2023-03-23**|**Set-the-Scene: Global-Local Training for Generating Controllable NeRF Scenes**|Dana Cohen-Bar et.al.|[2303.13450](http://arxiv.org/abs/2303.13450)|**[link](https://github.com/DanaCohen95/Set-the-Scene)**|
|**2023-03-23**|**SINE: Semantic-driven Image-based NeRF Editing with Prior-guided Editing Field**|Chong Bao et.al.|[2303.13277](http://arxiv.org/abs/2303.13277)|**[link](https://github.com/zju3dv/SINE)**|
|**2023-03-23**|**Transforming Radiance Field with Lipschitz Network for Photorealistic 3D Scene Stylization**|Zicheng Zhang et.al.|[2303.13232](http://arxiv.org/abs/2303.13232)|null|
|**2023-03-23**|**Semantic Ray: Learning a Generalizable Semantic Field with Cross-Reprojection Attention**|Fangfu Liu et.al.|[2303.13014](http://arxiv.org/abs/2303.13014)|**[link](https://github.com/liuff19/Semantic-Ray)**|
|**2023-03-22**|**NeRF-GAN Distillation for Efficient 3D-Aware Generation with Convolutions**|Mohamad Shahbazi et.al.|[2303.12865](http://arxiv.org/abs/2303.12865)|**[link](https://github.com/mshahbazi72/nerf-gan-distillation)**|
|**2023-03-22**|**SHERF: Generalizable Human NeRF from a Single Image**|Shoukang Hu et.al.|[2303.12791](http://arxiv.org/abs/2303.12791)|**[link](https://github.com/skhu101/sherf)**|
|**2023-03-22**|**Instruct-NeRF2NeRF: Editing 3D Scenes with Instructions**|Ayaan Haque et.al.|[2303.12789](http://arxiv.org/abs/2303.12789)|null|
|**2023-03-22**|**FeatureNeRF: Learning Generalizable NeRFs by Distilling Foundation Models**|Jianglong Ye et.al.|[2303.12786](http://arxiv.org/abs/2303.12786)|**[link](https://github.com/jianglongye/featurenerf)**|
|**2023-03-22**|**Balanced Spherical Grid for Egocentric View Synthesis**|Changwoon Choi et.al.|[2303.12408](http://arxiv.org/abs/2303.12408)|**[link](https://github.com/changwoonchoi/EgoNeRF)**|
|**2023-03-21**|**Pre-NeRF 360: Enriching Unbounded Appearances for Neural Radiance Fields**|Ahmad AlMughrabi et.al.|[2303.12234](http://arxiv.org/abs/2303.12234)|**[link](https://github.com/amughrabi/pre-nerf)**|
|**2023-03-21**|**3D-CLFusion: Fast Text-to-3D Rendering with Contrastive Latent Diffusion**|Yu-Jhe Li et.al.|[2303.11938](http://arxiv.org/abs/2303.11938)|null|
|**2023-03-22**|**ExtremeNeRF: Few-shot Neural Radiance Fields Under Unconstrained Illumination**|SeokYeong Lee et.al.|[2303.11728](http://arxiv.org/abs/2303.11728)|null|
|**2023-03-20**|**DehazeNeRF: Multiple Image Haze Removal and 3D Shape Reconstruction using Neural Radiance Fields**|Wei-Ting Chen et.al.|[2303.11364](http://arxiv.org/abs/2303.11364)|null|
|**2023-03-20**|**ContraNeRF: Generalizable Neural Radiance Fields for Synthetic-to-real Novel View Synthesis via Contrastive Learning**|Hao Yang et.al.|[2303.11052](http://arxiv.org/abs/2303.11052)|null|
|**2023-03-19**|**SKED: Sketch-guided Text-based 3D Editing**|Aryan Mikaeili et.al.|[2303.10735](http://arxiv.org/abs/2303.10735)|null|
|**2023-03-19**|**NeRF-LOAM: Neural Implicit Representation for Large-Scale Incremental LiDAR Odometry and Mapping**|Junyuan Deng et.al.|[2303.10709](http://arxiv.org/abs/2303.10709)|**[link](https://github.com/junyuandeng/nerf-loam)**|
|**2023-03-18**|**3D Data Augmentation for Driving Scenes on Camera**|Wenwen Tong et.al.|[2303.10340](http://arxiv.org/abs/2303.10340)|null|
|**2023-03-17**|**$α$ Surf: Implicit Surface Reconstruction for Semi-Transparent and Thin Objects with Decoupled Geometry and Opacity**|Tianhao Wu et.al.|[2303.10083](http://arxiv.org/abs/2303.10083)|null|
|**2023-03-17**|**Single-view Neural Radiance Fields with Depth Teacher**|Yurui Chen et.al.|[2303.09952](http://arxiv.org/abs/2303.09952)|null|
|**2023-03-21**|**PartNeRF: Generating Part-Aware Editable 3D Shapes without 3D Supervision**|Konstantinos Tertikas et.al.|[2303.09554](http://arxiv.org/abs/2303.09554)|null|
|**2023-03-16**|**LERF: Language Embedded Radiance Fields**|Justin Kerr et.al.|[2303.09553](http://arxiv.org/abs/2303.09553)|null|
|**2023-03-16**|**NeRFMeshing: Distilling Neural Radiance Fields into Geometrically-Accurate 3D Meshes**|Marie-Julie Rakotosaona et.al.|[2303.09431](http://arxiv.org/abs/2303.09431)|null|
|**2023-03-17**|**NeRFtrinsic Four: An End-To-End Trainable NeRF Jointly Optimizing Diverse Intrinsic and Extrinsic Camera Parameters**|Hannah Schieber et.al.|[2303.09412](http://arxiv.org/abs/2303.09412)|**[link](https://github.com/hannahhaensen/nerftrinsic_four)**|
|**2023-03-16**|**Reliable Image Dehazing by NeRF**|Zheyan Jin et.al.|[2303.09153](http://arxiv.org/abs/2303.09153)|null|
|**2023-03-15**|**Mesh Strikes Back: Fast and Efficient Human Reconstruction from RGB videos**|Rohit Jena et.al.|[2303.08808](http://arxiv.org/abs/2303.08808)|null|
|**2023-03-15**|**Re-ReND: Real-time Rendering of NeRFs across Devices**|Sara Rojas et.al.|[2303.08717](http://arxiv.org/abs/2303.08717)|**[link](https://github.com/sararoma95/Re-ReND)**|
|**2023-03-15**|**RefiNeRF: Modelling dynamic neural radiance fields with inconsistent or missing camera parameters**|Shuja Khalid et.al.|[2303.08695](http://arxiv.org/abs/2303.08695)|null|
|**2023-03-15**|**Harnessing Low-Frequency Neural Fields for Few-Shot View Synthesis**|Liangchen Song et.al.|[2303.08370](http://arxiv.org/abs/2303.08370)|**[link](https://github.com/lsongx/halo)**|
|**2023-03-14**|**MELON: NeRF with Unposed Images Using Equivalence Class Estimation**|Axel Levy et.al.|[2303.08096](http://arxiv.org/abs/2303.08096)|null|
|**2023-03-16**|**Let 2D Diffusion Model Know 3D-Consistency for Robust Text-to-3D Generation**|Junyoung Seo et.al.|[2303.07937](http://arxiv.org/abs/2303.07937)|**[link](https://github.com/KU-CVLAB/3DFuse)**|
|**2023-03-16**|**NEF: Neural Edge Fields for 3D Parametric Curve Reconstruction from Multi-view Images**|Yunfan Ye et.al.|[2303.07653](http://arxiv.org/abs/2303.07653)|**[link](https://github.com/yunfan1202/NEF_code)**|
|**2023-03-14**|**Frequency-Modulated Point Cloud Rendering with Easy Editing**|Yi Zhang et.al.|[2303.07596](http://arxiv.org/abs/2303.07596)|**[link](https://github.com/yizhangphd/freqpcr)**|
|**2023-03-13**|**FreeNeRF: Improving Few-shot Neural Rendering with Free Frequency Regularization**|Jiawei Yang et.al.|[2303.07418](http://arxiv.org/abs/2303.07418)|**[link](https://github.com/jiawei-yang/freenerf)**|
|**2023-03-13**|**NeRFLiX: High-Quality Neural View Synthesis by Learning a Degradation-Driven Inter-viewpoint MiXer**|Kun Zhou et.al.|[2303.06919](http://arxiv.org/abs/2303.06919)|**[link](https://github.com/redrock303/NeRFLiX_CPVR2023)**|
|**2023-03-11**|**Just Flip: Flipped Observation Generation and Optimization for Neural Radiance Fields to Cover Unobserved View**|Minjae Lee et.al.|[2303.06335](http://arxiv.org/abs/2303.06335)|**[link](https://github.com/minjae-lulu/just-flip)**|
|**2023-03-10**|**NeRFlame: FLAME-based conditioning of NeRF for 3D face rendering**|Wojciech Zając et.al.|[2303.06226](http://arxiv.org/abs/2303.06226)|**[link](https://github.com/wojtekz4/nerflame)**|
|**2023-03-10**|**You Only Train Once: Multi-Identity Free-Viewpoint Neural Human Rendering from Monocular Videos**|Jaehyeok Kim et.al.|[2303.05835](http://arxiv.org/abs/2303.05835)|null|
|**2023-03-10**|**Aleth-NeRF: Low-light Condition View Synthesis with Concealing Fields**|Ziteng Cui et.al.|[2303.05807](http://arxiv.org/abs/2303.05807)|null|
|**2023-03-10**|**Self-NeRF: A Self-Training Pipeline for Few-Shot Neural Radiance Fields**|Jiayang Bai et.al.|[2303.05775](http://arxiv.org/abs/2303.05775)|null|
|**2023-03-14**|**Hardware Acceleration of Neural Graphics**|Muhammad Husnain Mubarik et.al.|[2303.05735](http://arxiv.org/abs/2303.05735)|null|
|**2023-03-10**|**MovingParts: Motion-based 3D Part Discovery in Dynamic Radiance Field**|Kaizhi Yang et.al.|[2303.05703](http://arxiv.org/abs/2303.05703)|null|
|**2023-03-09**|**PAC-NeRF: Physics Augmented Continuum Neural Radiance Fields for Geometry-Agnostic System Identification**|Xuan Li et.al.|[2303.05512](http://arxiv.org/abs/2303.05512)|null|
|**2023-03-08**|**FastSurf: Fast Neural RGB-D Surface Reconstruction using Per-Frame Intrinsic Refinement and TSDF Fusion Prior Learning**|Seunghwan Lee et.al.|[2303.04508](http://arxiv.org/abs/2303.04508)|**[link](https://github.com/ROKIT-Healthcare/FastSurf)**|
|**2023-03-08**|**DroNeRF: Real-time Multi-agent Drone Pose Optimization for Computing Neural Radiance Fields**|Dipam Patel et.al.|[2303.04322](http://arxiv.org/abs/2303.04322)|null|
|**2023-03-07**|**NEPHELE: A Neural Platform for Highly Realistic Cloud Radiance Rendering**|Haimin Luo et.al.|[2303.04086](http://arxiv.org/abs/2303.04086)|null|
|**2023-03-05**|**Semantic-aware Occlusion Filtering Neural Radiance Fields in the Wild**|Jaewon Lee et.al.|[2303.03966](http://arxiv.org/abs/2303.03966)|null|
|**2023-03-07**|**Multiscale Tensor Decomposition and Rendering Equation Encoding for View Synthesis**|Kang Han et.al.|[2303.03808](http://arxiv.org/abs/2303.03808)|**[link](https://github.com/imkanghan/nrff)**|
|**2023-03-10**|**Nerflets: Local Radiance Fields for Efficient Structure-Aware 3D Scene Representation from 2D Supervision**|Xiaoshuai Zhang et.al.|[2303.03361](http://arxiv.org/abs/2303.03361)|null|
|**2023-03-07**|**Efficient Large-scale Scene Representation with a Hybrid of High-resolution Grid and Plane Features**|Yuqi Zhang et.al.|[2303.03003](http://arxiv.org/abs/2303.03003)|**[link](https://github.com/zyqz97/gp-nerf)**|
|**2023-03-03**|**Delicate Textured Mesh Recovery from NeRF via Adaptive Surface Refinement**|Jiaxiang Tang et.al.|[2303.02091](http://arxiv.org/abs/2303.02091)|**[link](https://github.com/ashawkey/nerf2mesh)**|
|**2023-03-03**|**Multi-Plane Neural Radiance Fields for Novel View Synthesis**|Youssef Abdelkareem et.al.|[2303.01736](http://arxiv.org/abs/2303.01736)|null|
|**2023-03-01**|**S-NeRF: Neural Radiance Fields for Street Views**|Ziyang Xie et.al.|[2303.00749](http://arxiv.org/abs/2303.00749)|null|
|**2023-02-28**|**IntrinsicNGP: Intrinsic Coordinate based Hash Encoding for Human NeRF**|Bo Peng et.al.|[2302.14683](http://arxiv.org/abs/2302.14683)|null|
|**2023-02-27**|**BaLi-RF: Bandlimited Radiance Fields for Dynamic Scene Modeling**|Sameera Ramasinghe et.al.|[2302.13543](http://arxiv.org/abs/2302.13543)|null|
|**2023-02-26**|**Efficient physics-informed neural networks using hash encoding**|Xinquan Huang et.al.|[2302.13397](http://arxiv.org/abs/2302.13397)|null|
|**2023-02-24**|**CATNIPS: Collision Avoidance Through Neural Implicit Probabilistic Scenes**|Timothy Chen et.al.|[2302.12931](http://arxiv.org/abs/2302.12931)|**[link](https://github.com/chengine/catnips)**|
|**2023-02-24**|**Learning Neural Volumetric Representations of Dynamic Humans in Minutes**|Chen Geng et.al.|[2302.12237](http://arxiv.org/abs/2302.12237)|**[link](https://github.com/zju3dv/instant-nvr)**|
|**2023-02-23**|**DiffusioNeRF: Regularizing Neural Radiance Fields with Denoising Diffusion Models**|Jamie Wynn et.al.|[2302.12231](http://arxiv.org/abs/2302.12231)|**[link](https://github.com/nianticlabs/diffusionerf)**|
|**2023-02-20**|**NerfDiff: Single-image View Synthesis with NeRF-guided Distillation from 3D-aware Diffusion**|Jiatao Gu et.al.|[2302.10109](http://arxiv.org/abs/2302.10109)|null|
|**2023-02-19**|**LC-NeRF: Local Controllable Face Generation in Neural Randiance Field**|Wenyang Zhou et.al.|[2302.09486](http://arxiv.org/abs/2302.09486)|null|
|**2023-02-17**|**MixNeRF: Modeling a Ray with Mixture Density for Novel View Synthesis from Sparse Inputs**|Seunghyeon Seo et.al.|[2302.08788](http://arxiv.org/abs/2302.08788)|**[link](https://github.com/shawn615/MixNeRF)**|
|**2023-02-14**|**VQ3D: Learning a 3D-Aware Generative Model on ImageNet**|Kyle Sargent et.al.|[2302.06833](http://arxiv.org/abs/2302.06833)|null|
|**2023-02-13**|**3D-aware Blending with Generative NeRFs**|Hyunsu Kim et.al.|[2302.06608](http://arxiv.org/abs/2302.06608)|**[link](https://github.com/naver-ai/BlendNeRF)**|
|**2023-02-11**|**3D Colored Shape Reconstruction from a Single RGB Image through Diffusion**|Bo Li et.al.|[2302.05573](http://arxiv.org/abs/2302.05573)|null|
|**2023-02-08**|**Nerfstudio: A Modular Framework for Neural Radiance Field Development**|Matthew Tancik et.al.|[2302.04264](http://arxiv.org/abs/2302.04264)|null|
|**2023-02-07**|**AV-NeRF: Learning Neural Fields for Real-World Audio-Visual Scene Synthesis**|Susan Liang et.al.|[2302.02088](http://arxiv.org/abs/2302.02088)|null|
|**2023-02-03**|**Semantic 3D-aware Portrait Synthesis and Manipulation Based on Compositional Neural Radiance Field**|Tianxiang Ma et.al.|[2302.01579](http://arxiv.org/abs/2302.01579)|**[link](https://github.com/tianxiangma/cnerf)**|
|**2023-02-03**|**Robust Camera Pose Refinement for Multi-Resolution Hash Encoding**|Hwan Heo et.al.|[2302.01571](http://arxiv.org/abs/2302.01571)|null|
|**2023-02-03**|**INV: Towards Streaming Incremental Neural Videos**|Shengze Wang et.al.|[2302.01532](http://arxiv.org/abs/2302.01532)|null|
|**2023-02-02**|**Factor Fields: A Unified Framework for Neural Fields and Beyond**|Anpei Chen et.al.|[2302.01226](http://arxiv.org/abs/2302.01226)|null|
|**2023-02-02**|**RobustNeRF: Ignoring Distractors with Robust Losses**|Sara Sabour et.al.|[2302.00833](http://arxiv.org/abs/2302.00833)|null|
|**2023-01-31**|**GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis**|Zhenhui Ye et.al.|[2301.13430](http://arxiv.org/abs/2301.13430)|null|
|**2023-01-30**|**Equivariant Architectures for Learning in Deep Weight Spaces**|Aviv Navon et.al.|[2301.12780](http://arxiv.org/abs/2301.12780)|**[link](https://github.com/AvivNavon/DWSNets)**|
|**2023-01-27**|**HyperNeRFGAN: Hypernetwork approach to 3D NeRF GAN**|Adam Kania et.al.|[2301.11631](http://arxiv.org/abs/2301.11631)|**[link](https://github.com/gmum/hypernerfgan)**|
|**2023-01-27**|**A Comparison of Tiny-nerf versus Spatial Representations for 3d Reconstruction**|Saulo Abraham Gante et.al.|[2301.11522](http://arxiv.org/abs/2301.11522)|null|
|**2023-01-27**|**SNeRL: Semantic-aware Neural Radiance Fields for Reinforcement Learning**|Dongseok Shim et.al.|[2301.11520](http://arxiv.org/abs/2301.11520)|null|
|**2023-01-26**|**Text-To-4D Dynamic Scene Generation**|Uriel Singer et.al.|[2301.11280](http://arxiv.org/abs/2301.11280)|null|
|**2023-01-26**|**GeCoNeRF: Few-shot Neural Radiance Fields via Geometric Consistency**|Minseop Kwak et.al.|[2301.10941](http://arxiv.org/abs/2301.10941)|**[link](https://github.com/KU-CVLAB/GeCoNeRF)**|
|**2023-01-23**|**HexPlane: A Fast Representation for Dynamic Scenes**|Ang Cao et.al.|[2301.09632](http://arxiv.org/abs/2301.09632)|**[link](https://github.com/Caoang327/HexPlane)**|
|**2023-01-22**|**3D Reconstruction of Non-cooperative Resident Space Objects using Instant NGP-accelerated NeRF and D-NeRF**|Trupti Mahendrakar et.al.|[2301.09060](http://arxiv.org/abs/2301.09060)|null|
|**2023-01-18**|**NeRF in the Palm of Your Hand: Corrective Augmentation for Robotics via Novel-View Synthesis**|Allan Zhou et.al.|[2301.08556](http://arxiv.org/abs/2301.08556)|null|
|**2023-01-19**|**RecolorNeRF: Layer Decomposed Radiance Field for Efficient Color Editing of 3D Scenes**|Bingchen Gong et.al.|[2301.07958](http://arxiv.org/abs/2301.07958)|null|
|**2023-01-18**|**Behind the Scenes: Density Fields for Single View Reconstruction**|Felix Wimbauer et.al.|[2301.07668](http://arxiv.org/abs/2301.07668)|**[link](https://github.com/Brummi/BehindTheScenes)**|
|**2023-01-17**|**A Large-Scale Outdoor Multi-modal Dataset and Benchmark for Novel View Synthesis and Implicit Scene Reconstruction**|Chongshan Lu et.al.|[2301.06782](http://arxiv.org/abs/2301.06782)|null|
|**2023-01-13**|**Laser: Latent Set Representations for 3D Generative Modeling**|Pol Moreno et.al.|[2301.05747](http://arxiv.org/abs/2301.05747)|null|
|**2023-01-10**|**Benchmarking Robustness in Neural Radiance Fields**|Chen Wang et.al.|[2301.04075](http://arxiv.org/abs/2301.04075)|null|
|**2023-01-08**|**Towards Open World NeRF-Based SLAM**|Daniil Lisus et.al.|[2301.03102](http://arxiv.org/abs/2301.03102)|null|
|**2023-01-10**|**Traditional Readability Formulas Compared for English**|Bruce W. Lee et.al.|[2301.02975](http://arxiv.org/abs/2301.02975)|null|
|**2023-01-09**|**Class-Continuous Conditional Generative Neural Radiance Field**|Jiwook Kim et.al.|[2301.00950](http://arxiv.org/abs/2301.00950)|**[link](https://github.com/tom919654/C3G-NeRF)**|
|**2023-01-11**|**Detachable Novel Views Synthesis of Dynamic Scenes Using Distribution-Driven Neural Radiance Fields**|Boyu Zhang et.al.|[2301.00411](http://arxiv.org/abs/2301.00411)|**[link](https://github.com/luciferbobo/d4nerf)**|
|**2022-12-26**|**MonoNeRF: Learning a Generalizable Dynamic Radiance Field from Monocular Videos**|Fengrui Tian et.al.|[2212.13056](http://arxiv.org/abs/2212.13056)|**[link](https://github.com/tianfr/mononerf)**|
|**2022-12-25**|**PaletteNeRF: Palette-based Color Editing for NeRFs**|Qiling Wu et.al.|[2212.12871](http://arxiv.org/abs/2212.12871)|null|
|**2022-12-22**|**Removing Objects From Neural Radiance Fields**|Silvan Weder et.al.|[2212.11966](http://arxiv.org/abs/2212.11966)|null|
|**2022-12-21**|**Incremental Learning for Neural Radiance Field with Uncertainty-Filtered Knowledge Distillation**|Mengqi Guo et.al.|[2212.10950](http://arxiv.org/abs/2212.10950)|**[link](https://github.com/dreamguo/UNIKD)**|
|**2022-12-21**|**PaletteNeRF: Palette-based Appearance Editing of Neural Radiance Fields**|Zhengfei Kuang et.al.|[2212.10699](http://arxiv.org/abs/2212.10699)|null|
|**2022-12-20**|**Correspondence Distillation from NeRF-based GAN**|Yushi Lan et.al.|[2212.09735](http://arxiv.org/abs/2212.09735)|null|
|**2022-12-19**|**StyleTRF: Stylizing Tensorial Radiance Fields**|Rahul Goel et.al.|[2212.09330](http://arxiv.org/abs/2212.09330)|null|
|**2022-12-18**|**SPARF: Large-Scale Learning of 3D Sparse Radiance Fields from Few Input Images**|Abdullah Hamdi et.al.|[2212.09100](http://arxiv.org/abs/2212.09100)|**[link](https://github.com/ajhamdi/sparf_pytorch)**|
|**2022-12-18**|**Masked Wavelet Representation for Compact Neural Radiance Fields**|Daniel Rho et.al.|[2212.09069](http://arxiv.org/abs/2212.09069)|**[link](https://github.com/daniel03c1/masked_wavelet_nerf)**|
|**2022-12-15**|**SteerNeRF: Accelerating NeRF Rendering via Smooth Viewpoint Trajectory**|Sicheng Li et.al.|[2212.08476](http://arxiv.org/abs/2212.08476)|null|
|**2022-12-16**|**MEIL-NeRF: Memory-Efficient Incremental Learning of Neural Radiance Fields**|Jaeyoung Chung et.al.|[2212.08328](http://arxiv.org/abs/2212.08328)|null|
|**2022-12-15**|**NeRF-Art: Text-Driven Neural Radiance Fields Stylization**|Can Wang et.al.|[2212.08070](http://arxiv.org/abs/2212.08070)|**[link](https://github.com/cassiePython/NeRF-Art)**|
|**2022-12-15**|**Real-Time Neural Light Field on Mobile Devices**|Junli Cao et.al.|[2212.08057](http://arxiv.org/abs/2212.08057)|**[link](https://github.com/snap-research/mobiler2l)**|
|**2022-12-14**|**NoPe-NeRF: Optimising Neural Radiance Field with No Pose Prior**|Wenjing Bian et.al.|[2212.07388](http://arxiv.org/abs/2212.07388)|**[link](https://github.com/ActiveVisionLab/nope-nerf)**|
|**2022-12-08**|**GazeNeRF: 3D-Aware Gaze Redirection with Neural Radiance Fields**|Alessandro Ruzzi et.al.|[2212.04823](http://arxiv.org/abs/2212.04823)|**[link](https://github.com/alessandroruzzi/gazenerf)**|
|**2022-12-09**|**4K-NeRF: High Fidelity Neural Radiance Fields at Ultra High Resolutions**|Zhongshu Wang et.al.|[2212.04701](http://arxiv.org/abs/2212.04701)|**[link](https://github.com/frozoul/4k-nerf)**|
|**2022-12-07**|**EditableNeRF: Editing Topologically Varying Neural Radiance Fields by Key Points**|Chengwei Zheng et.al.|[2212.04247](http://arxiv.org/abs/2212.04247)|null|
|**2022-12-08**|**NeRFEditor: Differentiable Style Decomposition for Full 3D Scene Editing**|Chunyi Sun et.al.|[2212.03848](http://arxiv.org/abs/2212.03848)|null|
|**2022-12-07**|**Non-uniform Sampling Strategies for NeRF on 360{\textdegree} images**|Takashi Otonari et.al.|[2212.03635](http://arxiv.org/abs/2212.03635)|null|
|**2022-12-07**|**SSDNeRF: Semantic Soft Decomposition of Neural Radiance Fields**|Siddhant Ranade et.al.|[2212.03406](http://arxiv.org/abs/2212.03406)|null|
|**2022-12-06**|**NeRDi: Single-View NeRF Synthesis with Language-Guided Diffusion as General Image Priors**|Congyue Deng et.al.|[2212.03267](http://arxiv.org/abs/2212.03267)|null|
|**2022-12-05**|**SceneRF: Self-Supervised Monocular 3D Scene Reconstruction with Radiance Fields**|Anh-Quan Cao et.al.|[2212.02501](http://arxiv.org/abs/2212.02501)|**[link](https://github.com/astra-vision/SceneRF)**|
|**2022-12-05**|**Canonical Fields: Self-Supervised Learning of Pose-Canonicalized Neural Fields**|Rohith Agaram et.al.|[2212.02493](http://arxiv.org/abs/2212.02493)|**[link](https://github.com/brown-ivl/Cafi-Net)**|
|**2022-12-06**|**D-TensoRF: Tensorial Radiance Fields for Dynamic Scenes**|Hankyu Jang et.al.|[2212.02375](http://arxiv.org/abs/2212.02375)|null|
|**2022-12-07**|**GARF:Geometry-Aware Generalized Neural Radiance Field**|Yue Shi et.al.|[2212.02280](http://arxiv.org/abs/2212.02280)|null|
|**2022-12-05**|**INGeo: Accelerating Instant Neural Scene Reconstruction with Noisy Geometry Priors**|Chaojian Li et.al.|[2212.01959](http://arxiv.org/abs/2212.01959)|null|
|**2022-12-03**|**MaRF: Representing Mars as Neural Radiance Fields**|Lorenzo Giusti et.al.|[2212.01672](http://arxiv.org/abs/2212.01672)|**[link](https://github.com/lrnzgiusti/marf)**|
|**2022-12-03**|**StegaNeRF: Embedding Invisible Information within Neural Radiance Fields**|Chenxin Li et.al.|[2212.01602](http://arxiv.org/abs/2212.01602)|null|
|**2022-12-02**|**RT-NeRF: Real-Time On-Device Neural Radiance Fields Towards Immersive AR/VR Rendering**|Chaojian Li et.al.|[2212.01120](http://arxiv.org/abs/2212.01120)|null|
|**2022-12-02**|**3D-TOGO: Towards Text-Guided Cross-Category 3D Object Generation**|Zutao Jiang et.al.|[2212.01103](http://arxiv.org/abs/2212.01103)|null|
|**2022-12-02**|**QFF: Quantized Fourier Features for Neural Field Representations**|Jae Yong Lee et.al.|[2212.00914](http://arxiv.org/abs/2212.00914)|null|
|**2022-12-01**|**ViewNeRF: Unsupervised Viewpoint Estimation Using Category-Level Neural Radiance Fields**|Octave Mariotti et.al.|[2212.00436](http://arxiv.org/abs/2212.00436)|null|
|**2022-11-30**|**NeRFInvertor: High Fidelity NeRF-GAN Inversion for Single-shot Real Image Animation**|Yu Yin et.al.|[2211.17235](http://arxiv.org/abs/2211.17235)|null|
|**2022-11-29**|**NeuralLift-360: Lifting An In-the-wild 2D Photo to A 3D Object with 360° Views**|Dejia Xu et.al.|[2211.16431](http://arxiv.org/abs/2211.16431)|**[link](https://github.com/VITA-Group/NeuralLift-360)**|
|**2022-11-29**|**Compressing Volumetric Radiance Fields to 1 MB**|Lingzhi Li et.al.|[2211.16386](http://arxiv.org/abs/2211.16386)|**[link](https://github.com/algohunt/vqrf)**|
|**2022-11-28**|**In-Hand 3D Object Scanning from an RGB Sequence**|Shreyas Hampali et.al.|[2211.16193](http://arxiv.org/abs/2211.16193)|null|
|**2022-11-30**|**One is All: Bridging the Gap Between Neural Radiance Fields Architectures with Progressive Volume Distillation**|Shuangkang Fang et.al.|[2211.15977](http://arxiv.org/abs/2211.15977)|**[link](https://github.com/megvii-research/AAAI2023-PVD)**|
|**2022-11-28**|**High-fidelity Facial Avatar Reconstruction from Monocular Video with Generative Priors**|Yunpeng Bai et.al.|[2211.15064](http://arxiv.org/abs/2211.15064)|null|
|**2022-11-27**|**SuNeRF: Validation of a 3D Global Reconstruction of the Solar Corona Using Simulated EUV Images**|Kyriaki-Margarita Bintsi et.al.|[2211.14879](http://arxiv.org/abs/2211.14879)|null|
|**2022-11-27**|**3D Scene Creation and Rendering via Rough Meshes: A Lighting Transfer Avenue**|Yujie Li et.al.|[2211.14823](http://arxiv.org/abs/2211.14823)|null|
|**2022-11-27**|**Sampling Neural Radiance Fields for Refractive Objects**|Jen-I Pan et.al.|[2211.14799](http://arxiv.org/abs/2211.14799)|**[link](https://github.com/alexkeroro86/samplenerfro)**|
|**2022-11-25**|**3DDesigner: Towards Photorealistic 3D Object Generation and Editing with Text-guided Diffusion Models**|Gang Li et.al.|[2211.14108](http://arxiv.org/abs/2211.14108)|null|
|**2022-11-25**|**ShadowNeuS: Neural SDF Reconstruction by Shadow Ray Supervision**|Jingwang Ling et.al.|[2211.14086](http://arxiv.org/abs/2211.14086)|**[link](https://github.com/gerwang/shadowneus)**|
|**2022-11-25**|**Dynamic Neural Portraits**|Michail Christos Doukas et.al.|[2211.13994](http://arxiv.org/abs/2211.13994)|null|
|**2022-11-25**|**Unsupervised Continual Semantic Adaptation through Neural Rendering**|Zhizheng Liu et.al.|[2211.13969](http://arxiv.org/abs/2211.13969)|**[link](https://github.com/ethz-asl/ucsa_neural_rendering)**|
|**2022-11-25**|**TPA-Net: Generate A Dataset for Text to Physics-based Animation**|Yuxing Qiu et.al.|[2211.13887](http://arxiv.org/abs/2211.13887)|null|
|**2022-11-24**|**ScanNeRF: a Scalable Benchmark for Neural Radiance Fields**|Luca De Luigi et.al.|[2211.13762](http://arxiv.org/abs/2211.13762)|null|
|**2022-11-24**|**Immersive Neural Graphics Primitives**|Ke Li et.al.|[2211.13494](http://arxiv.org/abs/2211.13494)|**[link](https://github.com/uhhhci/immersive-ngp)**|
|**2022-11-23**|**CGOF++: Controllable 3D Face Synthesis with Conditional Generative Occupancy Fields**|Keqiang Sun et.al.|[2211.13251](http://arxiv.org/abs/2211.13251)|null|
|**2022-11-26**|**ClimateNeRF: Physically-based Neural Rendering for Extreme Climate Synthesis**|Yuan Li et.al.|[2211.13226](http://arxiv.org/abs/2211.13226)|null|
|**2022-11-23**|**ManVatar : Fast 3D Head Avatar Reconstruction Using Motion-Aware Neural Voxels**|Yuelang Xu et.al.|[2211.13206](http://arxiv.org/abs/2211.13206)|null|
|**2022-11-23**|**BAD-NeRF: Bundle Adjusted Deblur Neural Radiance Fields**|Peng Wang et.al.|[2211.12853](http://arxiv.org/abs/2211.12853)|**[link](https://github.com/WU-CVGL/BAD-NeRF)**|
|**2022-11-23**|**PANeRF: Pseudo-view Augmentation for Improved Neural Radiance Fields Based on Few-shot Inputs**|Young Chun Ahn et.al.|[2211.12758](http://arxiv.org/abs/2211.12758)|null|
|**2022-11-23**|**ActiveRMAP: Radiance Field for Active Mapping And Planning**|Huangying Zhan et.al.|[2211.12656](http://arxiv.org/abs/2211.12656)|null|
|**2022-11-22**|**Zero NeRF: Registration with Zero Overlap**|Casey Peat et.al.|[2211.12544](http://arxiv.org/abs/2211.12544)|null|
|**2022-11-22**|**Depth-Supervised NeRF for Multi-View RGB-D Operating Room Images**|Beerend G. A. Gerats et.al.|[2211.12436](http://arxiv.org/abs/2211.12436)|null|
|**2022-11-22**|**Real-time Neural Radiance Talking Portrait Synthesis via Audio-spatial Decomposition**|Jiaxiang Tang et.al.|[2211.12368](http://arxiv.org/abs/2211.12368)|null|
|**2022-11-22**|**Exact-NeRF: An Exploration of a Precise Volumetric Parameterization for Neural Radiance Fields**|Brian K. S. Isaac-Medina et.al.|[2211.12285](http://arxiv.org/abs/2211.12285)|**[link](https://github.com/kostadinovshalon/exact-nerf)**|
|**2022-11-22**|**SPIn-NeRF: Multiview Segmentation and Perceptual Inpainting with Neural Radiance Fields**|Ashkan Mirzaei et.al.|[2211.12254](http://arxiv.org/abs/2211.12254)|null|
|**2022-11-22**|**Deblurred Neural Radiance Field with Physical Scene Priors**|Dogyoon Lee et.al.|[2211.12046](http://arxiv.org/abs/2211.12046)|**[link](https://github.com/dogyoonlee/dp-nerf)**|
|**2022-11-22**|**ONeRF: Unsupervised 3D Object Segmentation from Multiple Views**|Shengnan Liang et.al.|[2211.12038](http://arxiv.org/abs/2211.12038)|null|
|**2022-11-21**|**Towards Live 3D Reconstruction from Wearable Video: An Evaluation of V-SLAM, NeRF, and Videogrammetry Techniques**|David Ramirez et.al.|[2211.11836](http://arxiv.org/abs/2211.11836)|null|
|**2022-11-21**|**SPARF: Neural Radiance Fields from Sparse and Noisy Poses**|Prune Truong et.al.|[2211.11738](http://arxiv.org/abs/2211.11738)|**[link](https://github.com/google-research/sparf)**|
|**2022-11-21**|**ESLAM: Efficient Dense SLAM System Based on Hybrid Representation of Signed Distance Fields**|Mohammad Mahdi Johari et.al.|[2211.11704](http://arxiv.org/abs/2211.11704)|null|
|**2022-11-21**|**Shape, Pose, and Appearance from a Single Image via Bootstrapped Radiance Field Inversion**|Dario Pavllo et.al.|[2211.11674](http://arxiv.org/abs/2211.11674)|**[link](https://github.com/google-research/nerf-from-image)**|
|**2022-11-18**|**Magic3D: High-Resolution Text-to-3D Content Creation**|Chen-Hsuan Lin et.al.|[2211.10440](http://arxiv.org/abs/2211.10440)|null|
|**2022-11-17**|**AligNeRF: High-Fidelity Neural Radiance Fields via Alignment-Aware Training**|Yifan Jiang et.al.|[2211.09682](http://arxiv.org/abs/2211.09682)|null|
|**2022-11-16**|**CoNFies: Controllable Neural Face Avatars**|Heng Yu et.al.|[2211.08610](http://arxiv.org/abs/2211.08610)|null|
|**2022-11-14**|**Latent-NeRF for Shape-Guided Generation of 3D Shapes and Textures**|Gal Metzer et.al.|[2211.07600](http://arxiv.org/abs/2211.07600)|**[link](https://github.com/eladrich/latent-nerf)**|
|**2022-11-12**|**3D-Aware Encoding for Style-based Neural Radiance Fields**|Yu-Jhe Li et.al.|[2211.06583](http://arxiv.org/abs/2211.06583)|null|
|**2022-11-11**|**ParticleNeRF: A Particle-Based Encoding for Online Neural Radiance Fields in Dynamic Scenes**|Jad Abou-Chakra et.al.|[2211.04041](http://arxiv.org/abs/2211.04041)|null|
|**2022-11-07**|**Common Pets in 3D: Dynamic New-View Synthesis of Real-Life Deformable Categories**|Samarth Sinha et.al.|[2211.03889](http://arxiv.org/abs/2211.03889)|null|
|**2022-11-03**|**nerf2nerf: Pairwise Registration of Neural Radiance Fields**|Lily Goli et.al.|[2211.01600](http://arxiv.org/abs/2211.01600)|null|
|**2022-10-27**|**ProbNeRF: Uncertainty-Aware Inference of 3D Shapes from 2D Images**|Matthew D. Hoffman et.al.|[2210.17415](http://arxiv.org/abs/2210.17415)|null|
|**2022-10-27**|**Boosting Point Clouds Rendering via Radiance Mapping**|Xiaoyang Huang et.al.|[2210.15107](http://arxiv.org/abs/2210.15107)|**[link](https://github.com/seanywang0408/radiancemapping)**|
|**2022-10-24**|**Learning Neural Radiance Fields from Multi-View Geometry**|Marco Orsingher et.al.|[2210.13041](http://arxiv.org/abs/2210.13041)|null|
|**2022-10-23**|**Compressing Explicit Voxel Grid Representations: fast NeRFs become also small**|Chenxi Lola Deng et.al.|[2210.12782](http://arxiv.org/abs/2210.12782)|null|
|**2022-11-06**|**Joint Rigid Motion Correction and Sparse-View CT via Self-Calibrating Neural Field**|Qing Wu et.al.|[2210.12731](http://arxiv.org/abs/2210.12731)|null|
|**2022-10-21**|**An Exploration of Neural Radiance Field Scene Reconstruction: Synthetic, Real-world and Dynamic Scenes**|Benedict Quartey et.al.|[2210.12268](http://arxiv.org/abs/2210.12268)|null|
|**2022-11-06**|**Neural Fields for Robotic Object Manipulation from a Single Image**|Valts Blukis et.al.|[2210.12126](http://arxiv.org/abs/2210.12126)|null|
|**2022-10-21**|**HDHumans: A Hybrid Approach for High-fidelity Digital Humans**|Marc Habermann et.al.|[2210.12003](http://arxiv.org/abs/2210.12003)|null|
|**2022-10-21**|**RGB-Only Reconstruction of Tabletop Scenes for Collision-Free Manipulator Control**|Zhenggang Tang et.al.|[2210.11668](http://arxiv.org/abs/2210.11668)|null|
|**2022-10-21**|**Coordinates Are NOT Lonely -- Codebook Prior Helps Implicit Neural 3D Representations**|Fukun Yin et.al.|[2210.11170](http://arxiv.org/abs/2210.11170)|**[link](https://github.com/fukunyin/coco-nerf)**|
|**2022-10-18**|**Parallel Inversion of Neural Radiance Fields for Robust Pose Estimation**|Yunzhi Lin et.al.|[2210.10108](http://arxiv.org/abs/2210.10108)|**[link](https://github.com/NVlabs/ParallelInversion)**|
|**2022-10-18**|**ARAH: Animatable Volume Rendering of Articulated Human SDFs**|Shaofei Wang et.al.|[2210.10036](http://arxiv.org/abs/2210.10036)|null|
|**2022-10-20**|**Differentiable Physics Simulation of Dynamics-Augmented Neural Objects**|Simon Le Cleac'h et.al.|[2210.09420](http://arxiv.org/abs/2210.09420)|null|
|**2022-10-15**|**SPIDR: SDF-based Neural Point Fields for Illumination and Deformation**|Ruofan Liang et.al.|[2210.08398](http://arxiv.org/abs/2210.08398)|null|
|**2022-10-15**|**IBL-NeRF: Image-Based Lighting Formulation of Neural Radiance Fields**|Changwoon Choi et.al.|[2210.08202](http://arxiv.org/abs/2210.08202)|**[link](https://github.com/changwoonchoi/IBL-NeRF)**|
|**2022-10-17**|**3D GAN Inversion with Pose Optimization**|Jaehoon Ko et.al.|[2210.07301](http://arxiv.org/abs/2210.07301)|**[link](https://github.com/KU-CVLAB/3DGAN-Inversion)**|
|**2022-10-13**|**Multiplane NeRF-Supervised Disentanglement of Depth and Camera Pose from Videos**|Yang Fu et.al.|[2210.07181](http://arxiv.org/abs/2210.07181)|null|
|**2022-10-12**|**GraspNeRF: Multiview-based 6-DoF Grasp Detection for Transparent and Specular Objects Using Generalizable NeRF**|Qiyu Dai et.al.|[2210.06575](http://arxiv.org/abs/2210.06575)|**[link](https://github.com/PKU-EPIC/GraspNeRF)**|
|**2022-10-12**|**Reconstructing Personalized Semantic Facial NeRF Models From Monocular Video**|Xuan Gao et.al.|[2210.06108](http://arxiv.org/abs/2210.06108)|**[link](https://github.com/USTC3DV/NeRFBlendShape-code)**|
|**2022-10-11**|**X-NeRF: Explicit Neural Radiance Field for Multi-Scene 360 $^{\circ}$ Insufficient RGB-D Views**|Haoyi Zhu et.al.|[2210.05135](http://arxiv.org/abs/2210.05135)|**[link](https://github.com/haoyizhu/xnerf)**|
|**2022-10-10**|**NeRF2Real: Sim2real Transfer of Vision-guided Bipedal Motion Skills using Neural Radiance Fields**|Arunkumar Byravan et.al.|[2210.04932](http://arxiv.org/abs/2210.04932)|null|
|**2022-10-10**|**EVA3D: Compositional 3D Human Generation from 2D Image Collections**|Fangzhou Hong et.al.|[2210.04888](http://arxiv.org/abs/2210.04888)|**[link](https://github.com/hongfz16/EVA3D)**|
|**2022-10-13**|**NerfAcc: A General NeRF Acceleration Toolbox**|Ruilong Li et.al.|[2210.04847](http://arxiv.org/abs/2210.04847)|**[link](https://github.com/kair-bair/nerfacc)**|
|**2022-10-10**|**SiNeRF: Sinusoidal Neural Radiance Fields for Joint Pose Estimation and Scene Reconstruction**|Yitong Xia et.al.|[2210.04553](http://arxiv.org/abs/2210.04553)|**[link](https://github.com/yitongx/sinerf)**|
|**2022-10-09**|**Robustifying the Multi-Scale Representation of Neural Radiance Fields**|Nishant Jain et.al.|[2210.04233](http://arxiv.org/abs/2210.04233)|null|
|**2022-10-09**|**Estimating Neural Reflectance Field from Radiance Field using Tree Structures**|Xiu Li et.al.|[2210.04217](http://arxiv.org/abs/2210.04217)|null|
|**2022-10-09**|**Data augmentation for NeRF: a geometric consistent solution based on view morphing**|Matteo Bortolon et.al.|[2210.04214](http://arxiv.org/abs/2210.04214)|**[link](https://github.com/mbortolon97/vm-nerf)**|
|**2022-10-09**|**Towards Efficient Neural Scene Graphs by Learning Consistency Fields**|Yeji Song et.al.|[2210.04127](http://arxiv.org/abs/2210.04127)|null|
|**2022-10-08**|**ViewFool: Evaluating the Robustness of Visual Recognition to Adversarial Viewpoints**|Yinpeng Dong et.al.|[2210.03895](http://arxiv.org/abs/2210.03895)|**[link](https://github.com/heathcliff-saku/viewfool_)**|
|**2022-10-04**|**SelfNeRF: Fast Training NeRF for Human from Monocular Self-rotating Video**|Bo Peng et.al.|[2210.01651](http://arxiv.org/abs/2210.01651)|null|
|**2022-10-03**|**NARF22: Neural Articulated Radiance Fields for Configuration-Aware Rendering**|Stanley Lewis et.al.|[2210.01166](http://arxiv.org/abs/2210.01166)|null|
|**2022-10-02**|**IntrinsicNeRF: Learning Intrinsic Neural Radiance Fields for Editable Novel View Synthesis**|Weicai Ye et.al.|[2210.00647](http://arxiv.org/abs/2210.00647)|**[link](https://github.com/zju3dv/intrinsicnerf)**|
|**2022-10-02**|**Unsupervised Multi-View Object Segmentation Using Radiance Field Propagation**|Xinhang Liu et.al.|[2210.00489](http://arxiv.org/abs/2210.00489)|null|
|**2022-10-01**|**NeRF: Neural Radiance Field in 3D Vision, A Comprehensive Review**|Kyle Gao et.al.|[2210.00379](http://arxiv.org/abs/2210.00379)|null|
|**2022-10-01**|**Structure-Aware NeRF without Posed Camera via Epipolar Constraint**|Shu Chen et.al.|[2210.00183](http://arxiv.org/abs/2210.00183)|**[link](https://github.com/xtu-pr-lab/sanerf)**|
|**2022-09-30**|**Improving 3D-aware Image Synthesis with A Geometry-aware Discriminator**|Zifan Shi et.al.|[2209.15637](http://arxiv.org/abs/2209.15637)|null|
|**2022-09-30**|**Understanding Pure CLIP Guidance for Voxel Grid NeRF Models**|Han-Hung Lee et.al.|[2209.15172](http://arxiv.org/abs/2209.15172)|null|
|**2022-09-29**|**DreamFusion: Text-to-3D using 2D Diffusion**|Ben Poole et.al.|[2209.14988](http://arxiv.org/abs/2209.14988)|null|
|**2022-09-29**|**SymmNeRF: Learning to Explore Symmetry Prior for Single-View View Synthesis**|Xingyi Li et.al.|[2209.14819](http://arxiv.org/abs/2209.14819)|**[link](https://github.com/xingyi-li/symmnerf)**|
|**2022-10-03**|**360FusionNeRF: Panoramic Neural Radiance Fields with Joint Guidance**|Shreyas Kulkarni et.al.|[2209.14265](http://arxiv.org/abs/2209.14265)|**[link](https://github.com/metaslam/360fusionnerf)**|
|**2022-09-27**|**OmniNeRF: Hybriding Omnidirectional Distance and Radiance fields for Neural Surface Reconstruction**|Jiaming Shen et.al.|[2209.13433](http://arxiv.org/abs/2209.13433)|null|
|**2022-09-27**|**Orbeez-SLAM: A Real-time Monocular Visual SLAM with ORB Features and NeRF-realized Mapping**|Chi-Ming Chung et.al.|[2209.13274](http://arxiv.org/abs/2209.13274)|**[link](https://github.com/MarvinChung/Orbeez-slam)**|
|**2022-09-27**|**WaterNeRF: Neural Radiance Fields for Underwater Scenes**|Advaith Venkatramanan Sethuraman et.al.|[2209.13091](http://arxiv.org/abs/2209.13091)|null|
|**2022-09-26**|**Baking in the Feature: Accelerating Volumetric Segmentation by Rendering Feature Maps**|Kenneth Blomqvist et.al.|[2209.12744](http://arxiv.org/abs/2209.12744)|null|
|**2022-09-25**|**Enforcing safety for vision-based controllers via Control Barrier Functions and Neural Radiance Fields**|Mukun Tong et.al.|[2209.12266](http://arxiv.org/abs/2209.12266)|null|
|**2022-09-24**|**NeRF-Loc: Transformer-Based Object Localization Within Neural Radiance Fields**|Jiankai Sun et.al.|[2209.12068](http://arxiv.org/abs/2209.12068)|null|
|**2022-09-19**|**Loc-NeRF: Monte Carlo Localization using Neural Radiance Fields**|Dominic Maggio et.al.|[2209.09050](http://arxiv.org/abs/2209.09050)|**[link](https://github.com/mit-spark/loc-nerf)**|
|**2022-09-23**|**NeRF-SOS: Any-View Self-supervised Object Segmentation on Complex Scenes**|Zhiwen Fan et.al.|[2209.08776](http://arxiv.org/abs/2209.08776)|**[link](https://github.com/vita-group/nerf-sos)**|
|**2022-09-19**|**Density-aware NeRF Ensembles: Quantifying Predictive Uncertainty in Neural Radiance Fields**|Niko Sünderhauf et.al.|[2209.08718](http://arxiv.org/abs/2209.08718)|null|
|**2022-09-18**|**ActiveNeRF: Learning where to See with Uncertainty Estimation**|Xuran Pan et.al.|[2209.08546](http://arxiv.org/abs/2209.08546)|**[link](https://github.com/leaplabthu/activenerf)**|
|**2022-09-18**|**LATITUDE: Robotic Global Localization with Truncated Dynamic Low-pass Filter in City-scale NeRF**|Zhenxin Zhu et.al.|[2209.08498](http://arxiv.org/abs/2209.08498)|**[link](https://github.com/jike5/LATITUDE)**|
|**2022-09-16**|**iDF-SLAM: End-to-End RGB-D SLAM with Neural Implicit Mapping and Deep Feature Tracking**|Yuhang Ming et.al.|[2209.07919](http://arxiv.org/abs/2209.07919)|null|
|**2022-09-12**|**StructNeRF: Neural Radiance Fields for Indoor Scenes with Structural Hints**|Zheng Chen et.al.|[2209.05277](http://arxiv.org/abs/2209.05277)|null|
|**2022-09-09**|**Generative Deformable Radiance Fields for Disentangled Image Synthesis of Topology-Varying Objects**|Ziyu Wang et.al.|[2209.04183](http://arxiv.org/abs/2209.04183)|null|
|**2022-09-08**|**im2nerf: Image to Neural Radiance Field in the Wild**|Lu Mi et.al.|[2209.04061](http://arxiv.org/abs/2209.04061)|null|
|**2022-09-08**|**PixTrack: Precise 6DoF Object Pose Tracking using NeRF Templates and Feature-metric Alignment**|Prajwal Chidananda et.al.|[2209.03910](http://arxiv.org/abs/2209.03910)|**[link](https://github.com/giantai/pixtrack)**|
|**2022-09-07**|**Neural Feature Fusion Fields: 3D Distillation of Self-Supervised 2D Image Representations**|Vadim Tschernezki et.al.|[2209.03494](http://arxiv.org/abs/2209.03494)|null|
|**2022-08-29**|**Volume Rendering Digest (for NeRF)**|Andrea Tagliasacchi et.al.|[2209.02417](http://arxiv.org/abs/2209.02417)|null|
|**2022-09-06**|**CLONeR: Camera-Lidar Fusion for Occupancy Grid-aided Neural Representations**|Alexandra Carlson et.al.|[2209.01194](http://arxiv.org/abs/2209.01194)|null|
|**2022-09-01**|**On Quantizing Implicit Neural Representations**|Cameron Gordon et.al.|[2209.01019](http://arxiv.org/abs/2209.01019)|null|
|**2022-08-31**|**Dual-Space NeRF: Learning Animatable Avatars and Scene Lighting in Separate Spaces**|Yihao Zhi et.al.|[2208.14851](http://arxiv.org/abs/2208.14851)|**[link](https://github.com/zyhbili/Dual-Space-NeRF)**|
|**2022-08-30**|**A Portable Multiscopic Camera for Novel View and Time Synthesis in Dynamic Scenes**|Tianjia Zhang et.al.|[2208.14433](http://arxiv.org/abs/2208.14433)|null|
|**2022-08-24**|**PeRFception: Perception using Radiance Fields**|Yoonwoo Jeong et.al.|[2208.11537](http://arxiv.org/abs/2208.11537)|**[link](https://github.com/POSTECH-CVLab/PeRFception)**|
|**2022-08-24**|**E-NeRF: Neural Radiance Fields from a Moving Event Camera**|Simon Klenk et.al.|[2208.11300](http://arxiv.org/abs/2208.11300)|**[link](https://github.com/knelk/enerf)**|
|**2022-08-18**|**Neural Capture of Animatable 3D Human from Monocular Video**|Gusi Te et.al.|[2208.08728](http://arxiv.org/abs/2208.08728)|null|
|**2022-08-16**|**Casual Indoor HDR Radiance Capture from Omnidirectional Images**|Pulkit Gera et.al.|[2208.07903](http://arxiv.org/abs/2208.07903)|null|
|**2022-08-15**|**DM-NeRF: 3D Scene Geometry Decomposition and Manipulation from 2D Images**|Bing Wang et.al.|[2208.07227](http://arxiv.org/abs/2208.07227)|**[link](https://github.com/vlar-group/dm-nerf)**|
|**2022-08-11**|**RelPose: Predicting Probabilistic Relative Rotation for Single Objects in the Wild**|Jason Y. Zhang et.al.|[2208.05963](http://arxiv.org/abs/2208.05963)|null|
|**2022-08-11**|**FDNeRF: Few-shot Dynamic Neural Radiance Fields for Face Reconstruction and Expression Editing**|Jingbo Zhang et.al.|[2208.05751](http://arxiv.org/abs/2208.05751)|**[link](https://github.com/fdnerf/fdnerf)**|
|**2022-08-04**|**360Roam: Real-Time Indoor Roaming Using Geometry-Aware ${360^\circ}$ Radiance Fields**|Huajian Huang et.al.|[2208.02705](http://arxiv.org/abs/2208.02705)|null|
|**2022-08-02**|**T4DT: Tensorizing Time for Learning Temporal 3D Visual Data**|Mikhail Usvyatsov et.al.|[2208.01421](http://arxiv.org/abs/2208.01421)|**[link](https://github.com/aelphy/t4dt)**|
|**2022-08-01**|**DoF-NeRF: Depth-of-Field Meets Neural Radiance Fields**|Zijin Wu et.al.|[2208.00945](http://arxiv.org/abs/2208.00945)|**[link](https://github.com/zijinwuzijin/dof-nerf)**|
|**2022-08-06**|**MobileNeRF: Exploiting the Polygon Rasterization Pipeline for Efficient Neural Field Rendering on Mobile Architectures**|Zhiqin Chen et.al.|[2208.00277](http://arxiv.org/abs/2208.00277)|**[link](https://github.com/google-research/jax3d)**|
|**2022-07-30**|**Distilled Low Rank Neural Radiance Field with Quantization for Light Field Compression**|Jinglei Shi et.al.|[2208.00164](http://arxiv.org/abs/2208.00164)|null|
|**2022-08-01**|**End-to-end View Synthesis via NeRF Attention**|Zelin Zhao et.al.|[2207.14741](http://arxiv.org/abs/2207.14741)|null|
|**2022-07-29**|**Neural Density-Distance Fields**|Itsuki Ueda et.al.|[2207.14455](http://arxiv.org/abs/2207.14455)|**[link](https://github.com/ueda0319/neddf)**|
|**2022-07-27**|**Is Attention All NeRF Needs?**|Mukund Varma T et.al.|[2207.13298](http://arxiv.org/abs/2207.13298)|null|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## Inference

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2025-03-20**|**SPIN: Accelerating Large Language Model Inference with Heterogeneous Speculative Models**|Fahao Chen et.al.|[2503.15921](http://arxiv.org/abs/2503.15921)|null|
|**2025-03-17**|**AccelGen: Heterogeneous SLO-Guaranteed High-Throughput LLM Inference Serving for Diverse Applications**|Haiying Shen et.al.|[2503.13737](http://arxiv.org/abs/2503.13737)|null|
|**2025-03-13**|**Collaborative Speculative Inference for Efficient LLM Inference Serving**|Luyao Gao et.al.|[2503.10325](http://arxiv.org/abs/2503.10325)|null|
|**2025-03-07**|**Optimizing LLM Inference Throughput via Memory-aware and SLA-constrained Dynamic Batching**|Bowen Pang et.al.|[2503.05248](http://arxiv.org/abs/2503.05248)|**[link](https://github.com/kevinlee1110/dynamic-batching)**|
|**2025-02-21**|**Towards Swift Serverless LLM Cold Starts with ParaServe**|Chiheng Lou et.al.|[2502.15524](http://arxiv.org/abs/2502.15524)|null|
|**2025-02-03**|**OCTOPINF: Workload-Aware Inference Serving for Edge Video Analytics**|Thanh-Tung Nguyen et.al.|[2502.01277](http://arxiv.org/abs/2502.01277)|**[link](https://github.com/tungngreen/pipelinescheduler)**|
|**2025-01-09**|**Optimizing Distributed Deployment of Mixture-of-Experts Model Inference in Serverless Computing**|Mengfan Liu et.al.|[2501.05313](http://arxiv.org/abs/2501.05313)|null|
|**2025-01-02**|**FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving**|Zihao Ye et.al.|[2501.01005](http://arxiv.org/abs/2501.01005)|**[link](https://github.com/flashinfer-ai/flashinfer)**|
|**2024-12-21**|**SYMPHONY: Improving Memory Management for LLM Inference Workloads**|Saurabh Agarwal et.al.|[2412.16434](http://arxiv.org/abs/2412.16434)|null|
|**2024-11-23**|**Enabling Efficient Serverless Inference Serving for LLM (Large Language Model) in the Cloud**|Himel Ghosh et.al.|[2411.15664](http://arxiv.org/abs/2411.15664)|null|
|**2024-11-19**|**The Effect of Scheduling and Preemption on the Efficiency of LLM Inference Serving**|Kyoungmin Kim et.al.|[2411.07447](http://arxiv.org/abs/2411.07447)|null|
|**2024-10-31**|**ALISE: Accelerating Large Language Model Serving with Speculative Scheduling**|Youpeng Zhao et.al.|[2410.23537](http://arxiv.org/abs/2410.23537)|null|
|**2024-10-29**|**Pushing the Performance Envelope of DNN-based Recommendation Systems Inference on GPUs**|Rishabh Jain et.al.|[2410.22249](http://arxiv.org/abs/2410.22249)|**[link](https://github.com/rishucoding/reproduce_MICRO24_GPU_DLRM_inference)**|
|**2024-12-05**|**SwiftKV: Fast Prefill-Optimized Inference with Knowledge-Preserving Model Transformation**|Aurick Qiao et.al.|[2410.03960](http://arxiv.org/abs/2410.03960)|null|
|**2024-09-24**|**UELLM: A Unified and Efficient Approach for LLM Inference Serving**|Yiyuan He et.al.|[2409.14961](http://arxiv.org/abs/2409.14961)|null|
|**2025-01-07**|**Intelligent Router for LLM Workloads: Improving Performance Through Workload-Aware Load Balancing**|Kunal Jain et.al.|[2408.13510](http://arxiv.org/abs/2408.13510)|null|
|**2024-08-10**|**LLMServingSim: A HW/SW Co-Simulation Infrastructure for LLM Inference Serving at Scale**|Jaehong Cho et.al.|[2408.05499](http://arxiv.org/abs/2408.05499)|**[link](https://github.com/casys-kaist/llmservingsim)**|
|**2024-08-05**|**SLO-aware GPU Frequency Scaling for Energy Efficient LLM Inference Serving**|Andreas Kosmas Kakolyris et.al.|[2408.05235](http://arxiv.org/abs/2408.05235)|null|
|**2024-07-20**|**A Tale of Two Scales: Reconciling Horizontal and Vertical Scaling for Inference Serving Systems**|Kamran Razavi et.al.|[2407.14843](http://arxiv.org/abs/2407.14843)|null|
|**2024-07-17**|**LLM Inference Serving: Survey of Recent Advances and Opportunities**|Baolin Li et.al.|[2407.12391](http://arxiv.org/abs/2407.12391)|null|
|**2024-07-04**|**Loki: A System for Serving ML Inference Pipelines with Hardware and Accuracy Scaling**|Sohaib Ahmad et.al.|[2407.03583](http://arxiv.org/abs/2407.03583)|**[link](https://github.com/UMass-LIDS/Loki)**|
|**2024-06-20**|**CascadeServe: Unlocking Model Cascades for Inference Serving**|Ferdi Kossmann et.al.|[2406.14424](http://arxiv.org/abs/2406.14424)|null|
|**2024-06-11**|**ElasticRec: A Microservice-based Model Serving Architecture Enabling Elastic Resource Scaling for Recommendation Models**|Yujeong Choi et.al.|[2406.06955](http://arxiv.org/abs/2406.06955)|null|
|**2024-06-05**|**Llumnix: Dynamic Scheduling for Large Language Model Serving**|Biao Sun et.al.|[2406.03243](http://arxiv.org/abs/2406.03243)|**[link](https://github.com/alibabapai/llumnix)**|
|**2024-05-25**|**Online Resource Allocation for Edge Intelligence with Colocated Model Retraining and Inference**|Huaiguang Cai et.al.|[2405.16029](http://arxiv.org/abs/2405.16029)|**[link](https://github.com/caihuaiguang/ORRIC)**|
|**2024-05-11**|**Aladdin: Joint Placement and Scaling for SLO-Aware LLM Serving**|Chengyi Nie et.al.|[2405.06856](http://arxiv.org/abs/2405.06856)|null|
|**2024-04-15**|**Prepacking: A Simple Method for Fast Prefilling and Increased Throughput in Large Language Models**|Siyan Zhao et.al.|[2404.09529](http://arxiv.org/abs/2404.09529)|**[link](https://github.com/siyan-zhao/prepacking)**|
|**2024-04-23**|**Sponge: Inference Serving with Dynamic SLOs Using In-Place Vertical Scaling**|Kamran Razavi et.al.|[2404.00704](http://arxiv.org/abs/2404.00704)|**[link](https://github.com/saeid93/sponge)**|
|**2024-03-29**|**Towards Greener LLMs: Bringing Energy-Efficiency to the Forefront of LLM Inference**|Jovan Stojkovic et.al.|[2403.20306](http://arxiv.org/abs/2403.20306)|null|
|**2024-01-20**|**Inference without Interference: Disaggregate LLM Inference for Mixed Downstream Workloads**|Cunchen Hu et.al.|[2401.11181](http://arxiv.org/abs/2401.11181)|null|
|**2023-12-27**|**SuperServe: Fine-Grained Inference Serving for Unpredictable Workloads**|Alind Khare et.al.|[2312.16733](http://arxiv.org/abs/2312.16733)|null|
|**2023-12-17**|**Graft: Efficient Inference Serving for Hybrid Deep Learning with SLO Guarantees via DNN Re-alignment**|Jing Wu et.al.|[2312.10636](http://arxiv.org/abs/2312.10636)|null|
|**2024-02-01**|**ERASER: Machine Unlearning in MLaaS via an Inference Serving-Aware Approach**|Yuke Hu et.al.|[2311.16136](http://arxiv.org/abs/2311.16136)|null|
|**2023-10-27**|**MOSEL: Inference Serving Using Dynamic Modality Selection**|Bodun Hu et.al.|[2310.18481](http://arxiv.org/abs/2310.18481)|null|
|**2023-08-06**|**Pareto-Secure Machine Learning (PSML): Fingerprinting and Securing Inference Serving Systems**|Debopam Sanyal et.al.|[2307.01292](http://arxiv.org/abs/2307.01292)|null|
|**2023-06-21**|**Subgraph Stationary Hardware-Software Inference Co-Design**|Payman Behnam et.al.|[2306.17266](http://arxiv.org/abs/2306.17266)|null|
|**2024-02-01**|**Small Language Models Improve Giants by Rewriting Their Outputs**|Giorgos Vernikos et.al.|[2305.13514](http://arxiv.org/abs/2305.13514)|**[link](https://github.com/georgevern/lmcor)**|
|**2023-05-10**|**Fast Distributed Inference Serving for Large Language Models**|Bingyang Wu et.al.|[2305.05920](http://arxiv.org/abs/2305.05920)|null|
|**2023-04-24**|**Reconciling High Accuracy, Cost-Efficiency, and Low Latency of Inference Serving Systems**|Mehran Salmani et.al.|[2304.10892](http://arxiv.org/abs/2304.10892)|**[link](https://github.com/reconfigurable-ml-pipeline/infadapter)**|
|**2023-08-31**|**Clover: Toward Sustainable AI with Carbon-Aware Machine Learning Inference Service**|Baolin Li et.al.|[2304.09781](http://arxiv.org/abs/2304.09781)|null|
|**2022-10-17**|**A GPU-specialized Inference Parameter Server for Large-Scale Deep Recommendation Models**|Yingcan Wei et.al.|[2210.08804](http://arxiv.org/abs/2210.08804)|**[link](https://github.com/nvidia-merlin/hugectr)**|
|**2022-07-28**|**RIBBON: Cost-Effective and QoS-Aware Deep Learning Model Inference using a Diverse Pool of Cloud Computing Instances**|Baolin Li et.al.|[2207.11434](http://arxiv.org/abs/2207.11434)|null|
|**2022-04-18**|**Dynamic Network Adaptation at Inference**|Daniel Mendoza et.al.|[2204.08400](http://arxiv.org/abs/2204.08400)|null|
|**2022-03-14**|**Hercules: Heterogeneity-Aware Inference Serving for At-Scale Personalized Recommendation**|Liu Ke et.al.|[2203.07424](http://arxiv.org/abs/2203.07424)|null|
|**2022-02-23**|**MLProxy: SLA-Aware Reverse Proxy for Machine Learning Inference Serving on Serverless Computing Platforms**|Nima Mahmoudi et.al.|[2202.11243](http://arxiv.org/abs/2202.11243)|**[link](https://github.com/pacslab/serverless-ml-serving)**|
|**2022-02-18**|**A Survey of Large-Scale Deep Learning Serving System Optimization: Challenges and Opportunities**|Fuxun Yu et.al.|[2111.14247](http://arxiv.org/abs/2111.14247)|null|
|**2021-10-28**|**Characterizing and Taming Resolution in Convolutional Neural Networks**|Eddie Yan et.al.|[2110.14819](http://arxiv.org/abs/2110.14819)|null|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## Distributed Deep Learning

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2025-03-24**|**Mist: Efficient Distributed Training of Large Language Models via Memory-Parallelism Co-Optimization**|Zhanda Zhu et.al.|[2503.19050](http://arxiv.org/abs/2503.19050)|null|
|**2025-03-21**|**OmniLearn: A Framework for Distributed Deep Learning over Heterogeneous Clusters**|Sahil Tyagi et.al.|[2503.17469](http://arxiv.org/abs/2503.17469)|null|
|**2025-03-21**|**DeFT: Mitigating Data Dependencies for Flexible Communication Scheduling in Distributed Training**|Lin Meng et.al.|[2503.16815](http://arxiv.org/abs/2503.16815)|null|
|**2025-03-20**|**Distributed LLMs and Multimodal Large Language Models: A Survey on Advances, Challenges, and Future Directions**|Hadi Amini et.al.|[2503.16585](http://arxiv.org/abs/2503.16585)|null|
|**2025-03-20**|**OffsetOPT: Explicit Surface Reconstruction without Normals**|Huan Lei et.al.|[2503.15763](http://arxiv.org/abs/2503.15763)|null|
|**2025-03-19**|**Global Group Fairness in Federated Learning via Function Tracking**|Yves Rychener et.al.|[2503.15163](http://arxiv.org/abs/2503.15163)|null|
|**2025-03-19**|**pFedFair: Towards Optimal Group Fairness-Accuracy Trade-off in Heterogeneous Federated Learning**|Haoyu Lei et.al.|[2503.14925](http://arxiv.org/abs/2503.14925)|null|
|**2025-03-14**|**Federated Learning for Secure and Efficient Device Activity Detection in mMTC Networks**|Ali Elkeshawy et.al.|[2503.13513](http://arxiv.org/abs/2503.13513)|null|
|**2025-03-12**|**Automatic Operator-level Parallelism Planning for Distributed Deep Learning -- A Mixed-Integer Programming Approach**|Ruifeng She et.al.|[2503.09357](http://arxiv.org/abs/2503.09357)|null|
|**2025-03-11**|**Will LLMs Scaling Hit the Wall? Breaking Barriers via Distributed Resources on Massive Edge Devices**|Tao Shen et.al.|[2503.08223](http://arxiv.org/abs/2503.08223)|null|
|**2025-03-10**|**Distributed Resource Block Allocation for Wideband Cell-free System**|Yang Ma et.al.|[2503.06875](http://arxiv.org/abs/2503.06875)|null|
|**2025-03-07**|**FedMABench: Benchmarking Mobile Agents on Decentralized Heterogeneous User Data**|Wenhao Wang et.al.|[2503.05143](http://arxiv.org/abs/2503.05143)|**[link](https://github.com/wwh0411/fedmabench)**|
|**2025-03-14**|**Thunder: Harnessing Unused GPU Cycles in Large-Scale Training via Opportunistic Execution**|Cunchi Lv et.al.|[2503.02550](http://arxiv.org/abs/2503.02550)|null|
|**2025-03-06**|**Efficient Long Context Fine-tuning with Chunk Flow**|Xiulong Yuan et.al.|[2503.02356](http://arxiv.org/abs/2503.02356)|null|
|**2025-02-28**|**Deep RC: A Scalable Data Engineering and Deep Learning Pipeline**|Arup Kumar Sarker et.al.|[2502.20724](http://arxiv.org/abs/2502.20724)|null|
|**2025-02-26**|**Chemical knowledge-informed framework for privacy-aware retrosynthesis learning**|Guikun Chen et.al.|[2502.19119](http://arxiv.org/abs/2502.19119)|null|
|**2025-02-25**|**Armada: Memory-Efficient Distributed Training of Large-Scale Graph Neural Networks**|Roger Waleffe et.al.|[2502.17846](http://arxiv.org/abs/2502.17846)|null|
|**2025-02-21**|**SpikeRL: A Scalable and Energy-efficient Framework for Deep Spiking Reinforcement Learning**|Tokey Tahmid et.al.|[2502.17496](http://arxiv.org/abs/2502.17496)|null|
|**2025-02-20**|**GiGL: Large-Scale Graph Neural Networks at Snapchat**|Tong Zhao et.al.|[2502.15054](http://arxiv.org/abs/2502.15054)|null|
|**2025-02-18**|**Performance Evaluation of Sentiment Analysis on Text and Emoji Data Using End-to-End, Transfer Learning, Distributed and Explainable AI Models**|Sirisha Velampalli et.al.|[2502.13278](http://arxiv.org/abs/2502.13278)|null|
|**2025-02-16**|**DreamDDP: Accelerating Data Parallel Distributed LLM Training with Layer-wise Scheduled Partial Synchronization**|Zhenheng Tang et.al.|[2502.11058](http://arxiv.org/abs/2502.11058)|null|
|**2025-02-13**|**Adaptive Teaming in Multi-Drone Pursuit: Simulation, Training, and Deployment**|Yang Li et.al.|[2502.09762](http://arxiv.org/abs/2502.09762)|null|
|**2025-02-11**|**Memory Analysis on the Training Course of DeepSeek Models**|Ping Zhang et.al.|[2502.07846](http://arxiv.org/abs/2502.07846)|null|
|**2025-02-11**|**Distributed Value Decomposition Networks with Networked Agents**|Guilherme S. Varela et.al.|[2502.07635](http://arxiv.org/abs/2502.07635)|null|
|**2025-02-10**|**Fine-tuning Multimodal Transformers on Edge: A Parallel Split Learning Approach**|Timo Fudala et.al.|[2502.06355](http://arxiv.org/abs/2502.06355)|null|
|**2025-02-04**|**Scalable Higher Resolution Polar Sea Ice Classification and Freeboard Calculation from ICESat-2 ATL03 Data**|Jurdana Masuma Iqrah et.al.|[2502.02700](http://arxiv.org/abs/2502.02700)|null|
|**2025-02-03**|**Simple Linear Neuron Boosting**|Daniel Munoz et.al.|[2502.01131](http://arxiv.org/abs/2502.01131)|null|
|**2025-01-30**|**Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch**|Arthur Douillard et.al.|[2501.18512](http://arxiv.org/abs/2501.18512)|null|
|**2025-01-25**|**ReInc: Scaling Training of Dynamic Graph Neural Networks**|Mingyu Guan et.al.|[2501.15348](http://arxiv.org/abs/2501.15348)|null|
|**2025-01-24**|**Adaptive Rank Allocation for Federated Parameter-Efficient Fine-Tuning of Language Models**|Fei Wu et.al.|[2501.14406](http://arxiv.org/abs/2501.14406)|null|
|**2025-01-21**|**A Survey on Memory-Efficient Large-Scale Model Training in AI for Science**|Kaiyuan Tian et.al.|[2501.11847](http://arxiv.org/abs/2501.11847)|null|
|**2025-01-18**|**MOFA: Discovering Materials for Carbon Capture with a GenAI- and Simulation-Based Workflow**|Xiaoli Yan et.al.|[2501.10651](http://arxiv.org/abs/2501.10651)|null|
|**2025-01-14**|**Physics-Informed Latent Neural Operator for Real-time Predictions of Complex Physical Systems**|Sharmila Karumuri et.al.|[2501.08428](http://arxiv.org/abs/2501.08428)|null|
|**2025-01-12**|**Differentially Private Gradient-Tracking-Based Distributed Stochastic Optimization over Directed Graphs**|Jialong Chen et.al.|[2501.06793](http://arxiv.org/abs/2501.06793)|null|
|**2025-01-11**|**SafeSplit: A Novel Defense Against Client-Side Backdoor Attacks in Split Learning**|Phillip Rieger et.al.|[2501.06650](http://arxiv.org/abs/2501.06650)|null|
|**2025-01-11**|**ARES: Auxiliary Range Expansion for Outlier Synthesis**|Eui-Soo Jung et.al.|[2501.06442](http://arxiv.org/abs/2501.06442)|null|
|**2025-01-10**|**Regularized Top- $k$ : A Bayesian Framework for Gradient Sparsification**|Ali Bereyhi et.al.|[2501.05633](http://arxiv.org/abs/2501.05633)|null|
|**2025-01-09**|**Prediction-Assisted Online Distributed Deep Learning Workload Scheduling in GPU Clusters**|Ziyue Luo et.al.|[2501.05563](http://arxiv.org/abs/2501.05563)|null|
|**2025-01-08**|**Federated-Continual Dynamic Segmentation of Histopathology guided by Barlow Continuity**|Niklas Babendererde et.al.|[2501.04588](http://arxiv.org/abs/2501.04588)|null|
|**2025-01-07**|**mFabric: An Efficient and Scalable Fabric for Mixture-of-Experts Training**|Xudong Liao et.al.|[2501.03905](http://arxiv.org/abs/2501.03905)|null|
|**2025-01-06**|**A Self-supervised Diffusion Bridge for MRI Reconstruction**|Harry Gao et.al.|[2501.03430](http://arxiv.org/abs/2501.03430)|null|
|**2025-01-06**|**The Robustness of Spiking Neural Networks in Federated Learning with Compression Against Non-omniscient Byzantine Attacks**|Manh V. Nguyen et.al.|[2501.03306](http://arxiv.org/abs/2501.03306)|null|
|**2024-12-30**|**Adaptive Batch Size Schedules for Distributed Training of Language Models with Data and Model Parallelism**|Tim Tsz-Kit Lau et.al.|[2412.21124](http://arxiv.org/abs/2412.21124)|null|
|**2024-12-30**|**UnrealZoo: Enriching Photo-realistic Virtual Worlds for Embodied AI**|Fangwei Zhong et.al.|[2412.20977](http://arxiv.org/abs/2412.20977)|null|
|**2024-12-26**|**Federated Hybrid Training and Self-Adversarial Distillation: Towards Robust Edge Networks**|Yu Qiao et.al.|[2412.19354](http://arxiv.org/abs/2412.19354)|null|
|**2024-12-29**|**Beyond Gradient Averaging in Parallel Optimization: Improved Robustness through Gradient Agreement Filtering**|Francois Chaubard et.al.|[2412.18052](http://arxiv.org/abs/2412.18052)|**[link](https://github.com/Fchaubard/gradient_agreement_filtering)**|
|**2024-12-19**|**MoEtion: Efficient and Reliable Checkpointing for Mixture-of-Experts Models at Scale**|Swapnil Gandhi et.al.|[2412.15411](http://arxiv.org/abs/2412.15411)|null|
|**2024-12-17**|**Echo: Simulating Distributed Training At Scale**|Yicheng Feng et.al.|[2412.12487](http://arxiv.org/abs/2412.12487)|null|
|**2024-12-30**|**SepLLM: Accelerate Large Language Models by Compressing One Segment into One Separator**|Guoxuan Chen et.al.|[2412.12094](http://arxiv.org/abs/2412.12094)|**[link](https://github.com/HKUDS/SepLLM)**|
|**2024-12-10**|**Distributed Gradient Descent with Many Local Steps in Overparameterized Models**|Heng Zhu et.al.|[2412.07971](http://arxiv.org/abs/2412.07971)|null|
|**2024-12-10**|**Evaluating the Potential of Federated Learning for Maize Leaf Disease Prediction**|Thalita Mendonça Antico et.al.|[2412.07872](http://arxiv.org/abs/2412.07872)|null|
|**2024-12-10**|**EDiT: A Local-SGD-Based Efficient Distributed Training Method for Large Language Models**|Jialiang Cheng et.al.|[2412.07210](http://arxiv.org/abs/2412.07210)|**[link](https://github.com/intelligent-machine-learning/atorch)**|
|**2024-12-03**|**Proximal Control of UAVs with Federated Learning for Human-Robot Collaborative Domains**|Lucas Nogueira Nobrega et.al.|[2412.02863](http://arxiv.org/abs/2412.02863)|null|
|**2024-12-03**|**Defending Against Diverse Attacks in Federated Learning Through Consensus-Based Bi-Level Optimization**|Nicolás García Trillos et.al.|[2412.02535](http://arxiv.org/abs/2412.02535)|**[link](https://github.com/SixuLi/FedCB2O)**|
|**2024-12-02**|**INTELLECT-1 Technical Report**|Sami Jaghouar et.al.|[2412.01152](http://arxiv.org/abs/2412.01152)|**[link](https://github.com/PrimeIntellect-ai/prime)**|
|**2024-11-29**|**DeMo: Decoupled Momentum Optimization**|Bowen Peng et.al.|[2411.19870](http://arxiv.org/abs/2411.19870)|**[link](https://github.com/bloc97/demo)**|
|**2024-11-26**|**Distributed Sign Momentum with Local Steps for Training Transformers**|Shuhua Yu et.al.|[2411.17866](http://arxiv.org/abs/2411.17866)|**[link](https://github.com/shuhuayu/dist-sign-momentum)**|
|**2024-11-25**|**Lion Cub: Minimizing Communication Overhead in Distributed Lion**|Satoki Ishikawa et.al.|[2411.16462](http://arxiv.org/abs/2411.16462)|null|
|**2024-11-24**|**eFedLLM: Efficient LLM Inference Based on Federated Learning**|Shengwen Ding et.al.|[2411.16003](http://arxiv.org/abs/2411.16003)|null|
|**2024-11-24**|**Hiding Communication Cost in Distributed LLM Training via Micro-batch Co-execution**|Haiquan Wang et.al.|[2411.15871](http://arxiv.org/abs/2411.15871)|null|
|**2024-11-20**|**Hardware Scaling Trends and Diminishing Returns in Large-Scale Distributed Training**|Jared Fernandez et.al.|[2411.13055](http://arxiv.org/abs/2411.13055)|null|
|**2024-11-18**|**Graph Neural Networks on Graph Databases**|Dmytro Lopushanskyy et.al.|[2411.11375](http://arxiv.org/abs/2411.11375)|null|
|**2024-11-18**|**Syllabus: Portable Curricula for Reinforcement Learning Agents**|Ryan Sullivan et.al.|[2411.11318](http://arxiv.org/abs/2411.11318)|**[link](https://github.com/RyanNavillus/Syllabus)**|
|**2024-11-21**|**Pro-Prophet: A Systematic Load Balancing Method for Efficient Parallel Training of Large-scale MoE Models**|Wei Wang et.al.|[2411.10003](http://arxiv.org/abs/2411.10003)|null|
|**2024-11-06**|**ParaGAN: A Scalable Distributed Training Framework for Generative Adversarial Networks**|Ziji Shi et.al.|[2411.03999](http://arxiv.org/abs/2411.03999)|null|
|**2024-11-06**|**Adaptive Consensus Gradients Aggregation for Scaled Distributed Training**|Yoni Choukroun et.al.|[2411.03742](http://arxiv.org/abs/2411.03742)|**[link](https://github.com/yonilc/adacons)**|
|**2024-11-05**|**Photon: Federated LLM Pre-Training**|Lorenzo Sani et.al.|[2411.02908](http://arxiv.org/abs/2411.02908)|null|
|**2024-11-04**|**Minder: Faulty Machine Detection for Large-scale Distributed Model Training**|Yangtao Deng et.al.|[2411.01791](http://arxiv.org/abs/2411.01791)|null|
|**2024-11-13**|**Data movement limits to frontier model training**|Ege Erdil et.al.|[2411.01137](http://arxiv.org/abs/2411.01137)|null|
|**2024-11-01**|**MoNTA: Accelerating Mixture-of-Experts Training with Network-Traffc-Aware Parallel Optimization**|Jingming Guo et.al.|[2411.00662](http://arxiv.org/abs/2411.00662)|**[link](https://github.com/enflametechnology/deepspeed)**|
|**2024-11-05**|**SimpleFSDP: Simpler Fully Sharded Data Parallel with torch.compile**|Ruisi Zhang et.al.|[2411.00284](http://arxiv.org/abs/2411.00284)|null|
|**2024-10-31**|**Enhancing Brain Source Reconstruction through Physics-Informed 3D Neural Networks**|Marco Morik et.al.|[2411.00143](http://arxiv.org/abs/2411.00143)|null|
|**2024-10-26**|**DQRM: Deep Quantized Recommendation Models**|Yang Zhou et.al.|[2410.20046](http://arxiv.org/abs/2410.20046)|**[link](https://github.com/YangZhou08/Deep_Quantized_Recommendation_Model_DQRM)**|
|**2024-10-25**|**Lightweight, Secure and Stateful Serverless Computing with PSL**|Alexander Thomas et.al.|[2410.20004](http://arxiv.org/abs/2410.20004)|null|
|**2024-10-25**|**BitPipe: Bidirectional Interleaved Pipeline Parallelism for Accelerating Large Models Training**|Houming Wu et.al.|[2410.19367](http://arxiv.org/abs/2410.19367)|**[link](https://github.com/wuhouming/bitpipe)**|
|**2024-10-25**|**COAT: Compressing Optimizer states and Activation for Memory-Efficient FP8 Training**|Haocheng Xi et.al.|[2410.19313](http://arxiv.org/abs/2410.19313)|**[link](https://github.com/nvlabs/coat)**|
|**2024-10-24**|**Why Does the Effective Context Length of LLMs Fall Short?**|Chenxin An et.al.|[2410.18745](http://arxiv.org/abs/2410.18745)|null|
|**2024-10-09**|**OPTIMA: Optimized Policy for Intelligent Multi-Agent Systems Enables Coordination-Aware Autonomous Vehicles**|Rui Du et.al.|[2410.18112](http://arxiv.org/abs/2410.18112)|null|
|**2024-10-20**|**SDP4Bit: Toward 4-bit Communication Quantization in Sharded Data Parallelism for LLM Training**|Jinda Jia et.al.|[2410.15526](http://arxiv.org/abs/2410.15526)|null|
|**2024-10-15**|**Patch-Based Diffusion Models Beat Whole-Image Models for Mismatched Distribution Inverse Problems**|Jason Hu et.al.|[2410.11730](http://arxiv.org/abs/2410.11730)|null|
|**2024-10-24**|**Scalable Multi-Domain Adaptation of Language Models using Modular Experts**|Peter Schafhalter et.al.|[2410.10181](http://arxiv.org/abs/2410.10181)|null|
|**2024-10-09**|**TorchTitan: One-stop PyTorch native solution for production ready LLM pre-training**|Wanchao Liang et.al.|[2410.06511](http://arxiv.org/abs/2410.06511)|**[link](https://github.com/pytorch/torchtitan)**|
|**2024-10-07**|**Collaboration! Towards Robust Neural Methods for Routing Problems**|Jianan Zhou et.al.|[2410.04968](http://arxiv.org/abs/2410.04968)|**[link](https://github.com/RoyalSkye/Routing-CNF)**|
|**2024-10-02**|**Toward a Holistic Evaluation of Robustness in CLIP Models**|Weijie Tu et.al.|[2410.01534](http://arxiv.org/abs/2410.01534)|null|
|**2024-09-20**|**Time Distributed Deep Learning models for Purely Exogenous Forecasting. Application to Water Table Depth Prediction using Weather Image Time Series**|Matteo Salis et.al.|[2409.13284](http://arxiv.org/abs/2409.13284)|null|
|**2024-09-20**|**Convergence of Distributed Adaptive Optimization with Local Updates**|Ziheng Cheng et.al.|[2409.13155](http://arxiv.org/abs/2409.13155)|null|
|**2024-09-15**|**Leiden-Fusion Partitioning Method for Effective Distributed Training of Graph Embeddings**|Yuhe Bai et.al.|[2409.09887](http://arxiv.org/abs/2409.09887)|null|
|**2024-09-14**|**A Dynamic Weighting Strategy to Mitigate Worker Node Failure in Distributed Deep Learning**|Yuesheng Xu et.al.|[2409.09242](http://arxiv.org/abs/2409.09242)|null|
|**2024-09-11**|**Distributed Convolutional Neural Network Training on Mobile and Edge Clusters**|Pranav Rama et.al.|[2409.09083](http://arxiv.org/abs/2409.09083)|null|
|**2024-09-13**|**Gaussian is All You Need: A Unified Framework for Solving Inverse Problems via Diffusion Posterior Sampling**|Nebiyou Yismaw et.al.|[2409.08906](http://arxiv.org/abs/2409.08906)|null|
|**2024-09-13**|**Enhancing Privacy in ControlNet and Stable Diffusion via Split Learning**|Dixi Yao et.al.|[2409.08503](http://arxiv.org/abs/2409.08503)|null|
|**2024-09-18**|**Retrofitting Temporal Graph Neural Networks with Transformer**|Qiang Huang et.al.|[2409.05477](http://arxiv.org/abs/2409.05477)|**[link](https://github.com/qianghuangwhu/tf-tgn)**|
|**2024-09-03**|**On-chain Validation of Tracking Data Messages (TDM) Using Distributed Deep Learning on a Proof of Stake (PoS) Blockchain**|Yasir Latif et.al.|[2409.01614](http://arxiv.org/abs/2409.01614)|null|
|**2024-09-04**|**Unveiling the Vulnerability of Private Fine-Tuning in Split-Based Frameworks for Large Language Models: A Bidirectionally Enhanced Attack**|Guanzhong Chen et.al.|[2409.00960](http://arxiv.org/abs/2409.00960)|**[link](https://github.com/StupidTrees/SplitLLM)**|
|**2024-09-02**|**LuWu: An End-to-End In-Network Out-of-Core Optimizer for 100B-Scale Model-in-Network Data-Parallel Training on Distributed GPUs**|Mo Sun et.al.|[2409.00918](http://arxiv.org/abs/2409.00918)|null|
|**2024-09-08**|**HopGNN: Boosting Distributed GNN Training Efficiency via Feature-Centric Model Migration**|Weijian Chen et.al.|[2409.00657](http://arxiv.org/abs/2409.00657)|null|
|**2024-08-29**|**OpenFGL: A Comprehensive Benchmarks for Federated Graph Learning**|Xunkai Li et.al.|[2408.16288](http://arxiv.org/abs/2408.16288)|**[link](https://github.com/xkli-allen/openfgl)**|
|**2024-08-22**|**Poplar: Efficient Scaling of Distributed DNN Training on Heterogeneous GPU Clusters**|WenZheng Zhang et.al.|[2408.12596](http://arxiv.org/abs/2408.12596)|null|
|**2024-08-20**|**Security Assessment of Hierarchical Federated Deep Learning**|D Alqattan et.al.|[2408.10752](http://arxiv.org/abs/2408.10752)|**[link](https://github.com/dalqattan/sechfl)**|
|**2024-08-20**|**Pluto and Charon: A Time and Memory Efficient Collaborative Edge AI Framework for Personal LLMs Fine-Tuning**|Bei Ouyang et.al.|[2408.10746](http://arxiv.org/abs/2408.10746)|null|
|**2024-08-19**|**Demystifying the Communication Characteristics for Distributed Transformer Models**|Quentin Anthony et.al.|[2408.10197](http://arxiv.org/abs/2408.10197)|null|
|**2024-08-20**|**Heta: Distributed Training of Heterogeneous Graph Neural Networks**|Yuchen Zhong et.al.|[2408.09697](http://arxiv.org/abs/2408.09697)|null|
|**2024-08-15**|**Asteroid: Resource-Efficient Hybrid Pipeline Parallelism for Collaborative DNN Training on Heterogeneous Edge Devices**|Shengyuan Ye et.al.|[2408.08015](http://arxiv.org/abs/2408.08015)|null|
|**2024-08-08**|**Partial Experts Checkpoint: Efficient Fault Tolerance for Sparse Mixture-of-Experts Model Training**|Weilin Cai et.al.|[2408.04307](http://arxiv.org/abs/2408.04307)|null|
|**2024-08-07**|**Image-to-LaTeX Converter for Mathematical Formulas and Text**|Daniil Gurgurov et.al.|[2408.04015](http://arxiv.org/abs/2408.04015)|**[link](https://github.com/d-gurgurov/im2latex)**|
|**2024-08-06**|**Masked Random Noise for Communication Efficient Federaetd Learning**|Shiwei Li et.al.|[2408.03220](http://arxiv.org/abs/2408.03220)|**[link](https://github.com/Leopold1423/fedmrn-mm24)**|
|**2024-07-31**|**Algorithms for Collaborative Machine Learning under Statistical Heterogeneity**|Seok-Ju Hahn et.al.|[2408.00050](http://arxiv.org/abs/2408.00050)|null|
|**2024-08-07**|**FedBChain: A Blockchain-enabled Federated Learning Framework for Improving DeepConvLSTM with Comparative Strategy Insights**|Gaoxuan Li et.al.|[2407.21282](http://arxiv.org/abs/2407.21282)|null|
|**2024-07-30**|**OmniBal: Towards Fast Instruct-tuning for Vision-Language Models via Omniverse Computation Balance**|Yongqiang Yao et.al.|[2407.20761](http://arxiv.org/abs/2407.20761)|**[link](https://github.com/modeltc/omnibal)**|
|**2024-07-29**|**Model Agnostic Hybrid Sharding For Heterogeneous Distributed Inference**|Claudio Angione et.al.|[2407.19775](http://arxiv.org/abs/2407.19775)|null|
|**2024-07-29**|**Rina: Enhancing Ring-AllReduce with In-network Aggregation in Distributed Model Training**|Zixuan Chen et.al.|[2407.19721](http://arxiv.org/abs/2407.19721)|null|
|**2024-08-08**|**Parallel Split Learning with Global Sampling**|Mohammad Kohankhaki et.al.|[2407.15738](http://arxiv.org/abs/2407.15738)|null|
|**2024-07-22**|**GraphScale: A Framework to Enable Machine Learning over Billion-node Graphs**|Vipul Gupta et.al.|[2407.15452](http://arxiv.org/abs/2407.15452)|null|
|**2024-07-23**|**STrack: A Reliable Multipath Transport for AI/ML Clusters**|Yanfang Le et.al.|[2407.15266](http://arxiv.org/abs/2407.15266)|null|
|**2024-07-20**|**Latent Pollution Model: The Hidden Carbon Footprint in 3D Image Synthesis**|Marvin Seyfarth et.al.|[2407.14892](http://arxiv.org/abs/2407.14892)|null|
|**2024-07-19**|**Performance Modeling and Workload Analysis of Distributed Large Language Model Training and Inference**|Joyjit Kundu et.al.|[2407.14645](http://arxiv.org/abs/2407.14645)|null|
|**2024-07-01**|**A Look Into Training Large Language Models on Next Generation Datacenters**|Alexandru M. Gherghescu et.al.|[2407.12819](http://arxiv.org/abs/2407.12819)|null|
|**2024-07-18**|**Characterizing and Understanding HGNN Training on GPUs**|Dengke Han et.al.|[2407.11790](http://arxiv.org/abs/2407.11790)|null|
|**2024-07-14**|**SpreadFGL: Edge-Client Collaborative Federated Graph Learning with Adaptive Neighbor Generation**|Luying Zhong et.al.|[2407.11085](http://arxiv.org/abs/2407.11085)|null|
|**2024-07-08**|**High-Dimensional Distributed Sparse Classification with Scalable Communication-Efficient Global Updates**|Fred Lu et.al.|[2407.06346](http://arxiv.org/abs/2407.06346)|**[link](https://github.com/futurecomputing4ai/proxcsl)**|
|**2024-07-08**|**Hecaton: Training and Finetuning Large Language Models with Scalable Chiplet Systems**|Zongle Huang et.al.|[2407.05784](http://arxiv.org/abs/2407.05784)|null|
|**2024-07-02**|**QSync: Quantization-Minimized Synchronous Distributed Training Across Hybrid Devices**|Juntao Zhao et.al.|[2407.02327](http://arxiv.org/abs/2407.02327)|**[link](https://github.com/bytedance/QSync)**|
|**2024-07-02**|**On the Performance and Memory Footprint of Distributed Training: An Empirical Study on Transformers**|Zhengxian Lu et.al.|[2407.02081](http://arxiv.org/abs/2407.02081)|null|
|**2024-06-28**|**Enhancing Stability for Large Models Training in Constrained Bandwidth Networks**|Yun Dai et.al.|[2407.01614](http://arxiv.org/abs/2407.01614)|null|
|**2024-07-01**|**DistML.js: Installation-free Distributed Deep Learning Framework for Web Browsers**|Masatoshi Hidaka et.al.|[2407.01023](http://arxiv.org/abs/2407.01023)|**[link](https://github.com/mil-tokyo/distmljs)**|
|**2024-06-30**|**Challenging the Need for Packet Spraying in Large-Scale Distributed Training**|Vamsi Addanki et.al.|[2407.00550](http://arxiv.org/abs/2407.00550)|null|
|**2024-06-28**|**FRED: Flexible REduction-Distribution Interconnect and Communication Implementation for Wafer-Scale Distributed Training of DNN Models**|Saeed Rashidi et.al.|[2406.19580](http://arxiv.org/abs/2406.19580)|null|
|**2024-06-26**|**A Quantization-based Technique for Privacy Preserving Distributed Learning**|Maurizio Colombo et.al.|[2406.19418](http://arxiv.org/abs/2406.19418)|null|
|**2024-06-28**|**Universal Checkpointing: Efficient and Flexible Checkpointing for Large Scale Distributed Training**|Xinyu Lian et.al.|[2406.18820](http://arxiv.org/abs/2406.18820)|**[link](https://github.com/microsoft/DeepSpeed)**|
|**2024-06-26**|**Mixture of Experts in a Mixture of RL settings**|Timon Willi et.al.|[2406.18420](http://arxiv.org/abs/2406.18420)|null|
|**2024-06-25**|**Distributed Training of Large Graph Neural Networks with Variable Communication Rates**|Juan Cervino et.al.|[2406.17611](http://arxiv.org/abs/2406.17611)|null|
|**2024-06-21**|**Embracing Federated Learning: Enabling Weak Client Participation via Partial Model Training**|Sunwoo Lee et.al.|[2406.15125](http://arxiv.org/abs/2406.15125)|null|
|**2024-06-20**|**Communication-Efficient Adaptive Batch Size Strategies for Distributed Local Gradient Methods**|Tim Tsz-Kit Lau et.al.|[2406.13936](http://arxiv.org/abs/2406.13936)|null|
|**2024-06-16**|**Predicting Exoplanetary Features with a Residual Model for Uniform and Gaussian Distributions**|Andrew Sweet et.al.|[2406.10771](http://arxiv.org/abs/2406.10771)|null|
|**2024-06-12**|**A deep cut into Split Federated Self-supervised Learning**|Marcin Przewięźlikowski et.al.|[2406.08267](http://arxiv.org/abs/2406.08267)|**[link](https://github.com/gmum/monacosfl)**|
|**2024-06-12**|**Resource Allocation and Workload Scheduling for Large-Scale Distributed Deep Learning: A Survey**|Feng Liang et.al.|[2406.08115](http://arxiv.org/abs/2406.08115)|null|
|**2024-06-06**|**Seq1F1B: Efficient Sequence-Level Pipeline Parallelism for Large Language Model Training**|Ao Sun et.al.|[2406.03488](http://arxiv.org/abs/2406.03488)|**[link](https://github.com/maydomine/seq1f1b)**|
|**2024-06-03**|**ACCO: Accumulate while you Communicate, Hiding Communications in Distributed LLM Training**|Adel Nabli et.al.|[2406.02613](http://arxiv.org/abs/2406.02613)|null|
|**2024-06-03**|**Optimizing the Optimal Weighted Average: Efficient Distributed Sparse Classification**|Fred Lu et.al.|[2406.01753](http://arxiv.org/abs/2406.01753)|null|
|**2024-06-08**|**Graph Neural Network Training Systems: A Performance Comparison of Full-Graph and Mini-Batch**|Saurabh Bajaj et.al.|[2406.00552](http://arxiv.org/abs/2406.00552)|null|
|**2024-06-06**|**Communication-Efficient Distributed Deep Learning via Federated Dynamic Averaging**|Michail Theologitis et.al.|[2405.20988](http://arxiv.org/abs/2405.20988)|**[link](https://github.com/miketheologitis/FedL-Sync-FDA)**|
|**2024-05-27**|**WASH: Train your Ensemble with Communication-Efficient Weight Shuffling, then Average**|Louis Fournier et.al.|[2405.17517](http://arxiv.org/abs/2405.17517)|null|
|**2024-05-25**|**HetHub: A Heterogeneous distributed hybrid training system for large-scale models**|Si Xu et.al.|[2405.16256](http://arxiv.org/abs/2405.16256)|null|
|**2024-05-25**|**Apply Distributed CNN on Genomics to accelerate Transcription-Factor TAL1 Motif Prediction**|Tasnim Assali et.al.|[2405.16097](http://arxiv.org/abs/2405.16097)|null|
|**2024-05-24**|**Federated Behavioural Planes: Explaining the Evolution of Client Behaviour in Federated Learning**|Dario Fenoglio et.al.|[2405.15632](http://arxiv.org/abs/2405.15632)|**[link](https://github.com/dariofenoglio98/cf_fl)**|
|**2024-05-24**|**A Comparative Analysis of Distributed Training Strategies for GPT-2**|Ishan Patwardhan et.al.|[2405.15628](http://arxiv.org/abs/2405.15628)|null|
|**2024-05-22**|**Trajectory Volatility for Out-of-Distribution Detection in Mathematical Reasoning**|Yiming Wang et.al.|[2405.14039](http://arxiv.org/abs/2405.14039)|**[link](https://github.com/alsace08/ood-math-reasoning)**|
|**2024-05-22**|**SlipStream: Adapting Pipelines for Distributed Training of Large DNNs Amid Failures**|Swapnil Gandhi et.al.|[2405.14009](http://arxiv.org/abs/2405.14009)|null|
|**2024-05-18**|**Adjacent Leader Decentralized Stochastic Gradient Descent**|Haoze He et.al.|[2405.11389](http://arxiv.org/abs/2405.11389)|null|
|**2024-05-05**|**Tree-based Ensemble Learning for Out-of-distribution Detection**|Zhaiming Shen et.al.|[2405.03060](http://arxiv.org/abs/2405.03060)|null|
|**2024-04-27**|**Privacy-Preserving, Dropout-Resilient Aggregation in Decentralized Learning**|Ali Reza Ghavamipour et.al.|[2404.17984](http://arxiv.org/abs/2404.17984)|null|
|**2024-04-27**|**Personalized Federated Learning via Sequential Layer Expansion in Representation Learning**|Jaewon Jang et.al.|[2404.17799](http://arxiv.org/abs/2404.17799)|null|
|**2024-04-24**|**NeRF-XL: Scaling NeRFs with Multiple GPUs**|Ruilong Li et.al.|[2404.16221](http://arxiv.org/abs/2404.16221)|null|
|**2024-04-23**|**Workload-Aware Hardware Accelerator Mining for Distributed Deep Learning Training**|Muhammad Adnan et.al.|[2404.14632](http://arxiv.org/abs/2404.14632)|null|
|**2024-04-22**|**Machine Learning Techniques for MRI Data Processing at Expanding Scale**|Taro Langner et.al.|[2404.14326](http://arxiv.org/abs/2404.14326)|null|
|**2024-04-18**|**Context-Aware Orchestration of Energy-Efficient Gossip Learning Schemes**|Mina Aghaei Dinani et.al.|[2404.12023](http://arxiv.org/abs/2404.12023)|null|
|**2024-04-17**|**Accelerating Geo-distributed Machine Learning with Network-Aware Adaptive Tree and Auxiliary Route**|Zonghang Li et.al.|[2404.11352](http://arxiv.org/abs/2404.11352)|**[link](https://github.com/fengwenjiao/netstorm)**|
|**2024-04-17**|**Farthest Point Sampling in Property Designated Chemical Feature Space as a General Strategy for Enhancing the Machine Learning Model Performance for Small Scale Chemical Dataset**|Yuze Liu et.al.|[2404.11348](http://arxiv.org/abs/2404.11348)|null|
|**2024-04-16**|**HLAT: High-quality Large Language Model Pre-trained on AWS Trainium**|Haozheng Fan et.al.|[2404.10630](http://arxiv.org/abs/2404.10630)|**[link](https://github.com/awslabs/hlat)**|
|**2024-04-15**|**Distributed Federated Learning-Based Deep Learning Model for Privacy MRI Brain Tumor Detection**|Lisang Zhou et.al.|[2404.10026](http://arxiv.org/abs/2404.10026)|null|
|**2024-04-15**|**AntDT: A Self-Adaptive Distributed Training Framework for Leader and Straggler Nodes**|Youshao Xiao et.al.|[2404.09679](http://arxiv.org/abs/2404.09679)|null|
|**2024-03-30**|**Going Forward-Forward in Distributed Deep Learning**|Ege Aktemur et.al.|[2404.08573](http://arxiv.org/abs/2404.08573)|null|
|**2024-04-09**|**Communication-Efficient Large-Scale Distributed Deep Learning: A Comprehensive Survey**|Feng Liang et.al.|[2404.06114](http://arxiv.org/abs/2404.06114)|null|
|**2024-04-04**|**SiloFuse: Cross-silo Synthetic Data Generation with Latent Tabular Diffusion Models**|Aditya Shankar et.al.|[2404.03299](http://arxiv.org/abs/2404.03299)|null|
|**2024-04-07**|**MODNO: Multi Operator Learning With Distributed Neural Operators**|Zecheng Zhang et.al.|[2404.02892](http://arxiv.org/abs/2404.02892)|null|
|**2024-04-03**|**Linear Attention Sequence Parallelism**|Weigao Sun et.al.|[2404.02882](http://arxiv.org/abs/2404.02882)|**[link](https://github.com/opennlplab/lasp)**|
|**2024-04-02**|**CATGNN: Cost-Efficient and Scalable Distributed Training for Graph Neural Networks**|Xin Huang et.al.|[2404.02300](http://arxiv.org/abs/2404.02300)|null|
|**2024-04-01**|**Collaborative Learning of Anomalies with Privacy (CLAP) for Unsupervised Video Anomaly Detection: A New Baseline**|Anas Al-lahham et.al.|[2404.00847](http://arxiv.org/abs/2404.00847)|**[link](https://github.com/anasemad11/clap)**|
|**2024-03-30**|**Communication Efficient Distributed Training with Distributed Lion**|Bo Liu et.al.|[2404.00438](http://arxiv.org/abs/2404.00438)|null|
|**2024-03-27**|**Differentially Private Distributed Nonconvex Stochastic Optimization with Quantized Communications**|Jialong Chen et.al.|[2403.18254](http://arxiv.org/abs/2403.18254)|null|
|**2024-04-02**|**FLIGAN: Enhancing Federated Learning with Incomplete Data using GAN**|Paul Joe Maliakel et.al.|[2403.16930](http://arxiv.org/abs/2403.16930)|null|
|**2024-03-19**|**JORA: JAX Tensor-Parallel LoRA Library for Retrieval Augmented Fine-Tuning**|Anique Tahir et.al.|[2403.11366](http://arxiv.org/abs/2403.11366)|**[link](https://github.com/aniquetahir/JORA)**|
|**2024-03-15**|**ATOM: Asynchronous Training of Massive Models for Deep Learning in a Decentralized Environment**|Xiaofeng Wu et.al.|[2403.10504](http://arxiv.org/abs/2403.10504)|null|
|**2024-03-14**|**FedComLoc: Communication-Efficient Distributed Training of Sparse and Quantized Models**|Kai Yi et.al.|[2403.09904](http://arxiv.org/abs/2403.09904)|null|
|**2024-03-13**|**Distributed Deep Learning for Modulation Classification in 6G Cell-Free Wireless Networks**|Dieter Verbruggen et.al.|[2403.08563](http://arxiv.org/abs/2403.08563)|null|
|**2024-03-12**|**Communication Optimization for Distributed Training: Architecture, Advances, and Opportunities**|Yunze Wei et.al.|[2403.07585](http://arxiv.org/abs/2403.07585)|null|
|**2024-03-14**|**DeepVM: Integrating Spot and On-Demand VMs for Cost-Efficient Deep Learning Clusters in the Cloud**|Yoochan Kim et.al.|[2403.05861](http://arxiv.org/abs/2403.05861)|null|
|**2024-03-07**|**GRAWA: Gradient-based Weighted Averaging for Distributed Training of Deep Learning Models**|Tolga Dimlioglu et.al.|[2403.04206](http://arxiv.org/abs/2403.04206)|**[link](https://github.com/tolgadimli/grawa)**|
|**2024-03-03**|**It Takes a Village: A Distributed Training Model for AI-based Chatbots**|Colleen Estes et.al.|[2403.01545](http://arxiv.org/abs/2403.01545)|null|
|**2024-03-07**|**Disaggregated Multi-Tower: Topology-aware Modeling Technique for Efficient Large-Scale Recommendation**|Liang Luo et.al.|[2403.00877](http://arxiv.org/abs/2403.00877)|null|
|**2024-02-29**|**Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models**|Soham De et.al.|[2402.19427](http://arxiv.org/abs/2402.19427)|null|
|**2024-02-23**|**Sampling-based Distributed Training with Message Passing Neural Network**|Priyesh Kakka et.al.|[2402.15106](http://arxiv.org/abs/2402.15106)|null|
|**2024-02-22**|**Practical Insights into Knowledge Distillation for Pre-Trained Models**|Norah Alballa et.al.|[2402.14922](http://arxiv.org/abs/2402.14922)|null|
|**2024-02-22**|**Dependable Distributed Training of Compressed Machine Learning Models**|Francesco Malandrino et.al.|[2402.14346](http://arxiv.org/abs/2402.14346)|null|
|**2024-02-21**|**Preserving Near-Optimal Gradient Sparsification Cost for Scalable Distributed Deep Learning**|Daegun Yoon et.al.|[2402.13781](http://arxiv.org/abs/2402.13781)|**[link](https://github.com/kljp/exdyna)**|
|**2024-02-21**|**FinGPT-HPC: Efficient Pretraining and Finetuning Large Language Models for Financial Applications with High-Performance Computing**|Xiao-Yang Liu et.al.|[2402.13533](http://arxiv.org/abs/2402.13533)|null|
|**2024-02-20**|**Fog enabled distributed training architecture for federated learning**|Aditya Kumar et.al.|[2402.12906](http://arxiv.org/abs/2402.12906)|null|
|**2024-02-17**|**Achieving Linear Speedup in Asynchronous Federated Learning with Heterogeneous Clients**|Xiaolu Wang et.al.|[2402.11198](http://arxiv.org/abs/2402.11198)|null|
|**2024-02-16**|**TernaryVote: Differentially Private, Communication Efficient, and Byzantine Resilient Distributed Optimization on Heterogeneous Data**|Richeng Jin et.al.|[2402.10816](http://arxiv.org/abs/2402.10816)|null|
|**2024-02-16**|**Error Feedback Reloaded: From Quadratic to Arithmetic Mean of Smoothness Constants**|Peter Richtárik et.al.|[2402.10774](http://arxiv.org/abs/2402.10774)|null|
|**2024-02-15**|**A chaotic maps-based privacy-preserving distributed deep learning for incomplete and Non-IID datasets**|Irina Arévalo et.al.|[2402.10145](http://arxiv.org/abs/2402.10145)|null|
|**2024-02-12**|**Accelerating Distributed Deep Learning using Lossless Homomorphic Compression**|Haoyu Li et.al.|[2402.07529](http://arxiv.org/abs/2402.07529)|**[link](https://github.com/lihy0529/lossless_homomorphic_compression)**|
|**2024-02-07**|**Training DNN Models over Heterogeneous Clusters with Optimal Performance**|Chengyi Nie et.al.|[2402.05302](http://arxiv.org/abs/2402.05302)|null|
|**2024-02-06**|**Adaptive Blockwise Task-interleaved Pipeline Parallelism**|Ding Tang et.al.|[2402.03791](http://arxiv.org/abs/2402.03791)|null|
|**2024-02-05**|**Breaking the Curse of Dimensionality with Distributed Neural Computation**|Haitz Sáez de Ocáriz Borde et.al.|[2402.03460](http://arxiv.org/abs/2402.03460)|null|
|**2024-02-04**|**Breaking MLPerf Training: A Case Study on Optimizing BERT**|Yongdeok Kim et.al.|[2402.02447](http://arxiv.org/abs/2402.02447)|null|
|**2024-02-02**|**Improved Quantization Strategies for Managing Heavy-tailed Gradients in Distributed Learning**|Guangfeng Yan et.al.|[2402.01798](http://arxiv.org/abs/2402.01798)|null|
|**2024-02-02**|**Privacy-Preserving Distributed Learning for Residential Short-Term Load Forecasting**|Yi Dong et.al.|[2402.01546](http://arxiv.org/abs/2402.01546)|**[link](https://github.com/yingjiewangtony/fl-dl)**|
|**2024-01-29**|**CO2: Efficient Distributed Training with Full Communication-Computation Overlap**|Weigao Sun et.al.|[2401.16265](http://arxiv.org/abs/2401.16265)|**[link](https://github.com/opennlplab/co2)**|
|**2024-01-18**|**FLex&Chill: Improving Local Federated Learning Training with Logit Chilling**|Kichang Lee et.al.|[2401.09986](http://arxiv.org/abs/2401.09986)|null|
|**2024-01-19**|**A Fast, Performant, Secure Distributed Training Framework For Large Language Model**|Wei Huang et.al.|[2401.09796](http://arxiv.org/abs/2401.09796)|null|
|**2024-01-18**|**Mobility Accelerates Learning: Convergence Analysis on Hierarchical Federated Learning in Vehicular Networks**|Tan Chen et.al.|[2401.09656](http://arxiv.org/abs/2401.09656)|null|
|**2024-01-16**|**GMLake: Efficient and Transparent GPU Memory Defragmentation for Large-scale DNN Training with Virtual Memory Stitching**|Cong Guo et.al.|[2401.08156](http://arxiv.org/abs/2401.08156)|**[link](https://github.com/intelligent-machine-learning/glake)**|
|**2024-01-15**|**Activations and Gradients Compression for Model-Parallel Training**|Mikhail Rudakov et.al.|[2401.07788](http://arxiv.org/abs/2401.07788)|**[link](https://github.com/glemhel/activationsgradientscompressionformp)**|
|**2024-01-11**|**HAP: SPMD DNN Training on Heterogeneous GPU Clusters with Automated Program Synthesis**|Shiwei Zhang et.al.|[2401.05965](http://arxiv.org/abs/2401.05965)|**[link](https://github.com/alibaba/hap)**|
|**2024-01-09**|**G-Meta: Distributed Meta Learning in GPU Clusters for Large-Scale Recommender Systems**|Youshao Xiao et.al.|[2401.04338](http://arxiv.org/abs/2401.04338)|null|
|**2024-01-03**|**An Edge-Cloud Collaboration Framework for Generative AI Service Provision with Synergetic Big Cloud Model and Small Edge Models**|Yuqing Tian et.al.|[2401.01666](http://arxiv.org/abs/2401.01666)|null|
|**2023-12-30**|**On the Burstiness of Distributed Machine Learning Traffic**|Natchanon Luangsomboon et.al.|[2401.00329](http://arxiv.org/abs/2401.00329)|null|
|**2023-12-29**|**RS-DGC: Exploring Neighborhood Statistics for Dynamic Gradient Compression on Remote Sensing Image Interpretation**|Weiying Xie et.al.|[2312.17530](http://arxiv.org/abs/2312.17530)|null|
|**2023-12-29**|**Differentially Private Low-Rank Adaptation of Large Language Model Using Federated Learning**|Xiao-Yang Liu et.al.|[2312.17493](http://arxiv.org/abs/2312.17493)|null|
|**2023-12-21**|**Optimizing Distributed Training on Frontier for Large Language Models**|Sajal Dash et.al.|[2312.12705](http://arxiv.org/abs/2312.12705)|null|
|**2023-12-19**|**Beyond Prototypes: Semantic Anchor Regularization for Better Representation Learning**|Yanqi Ge et.al.|[2312.11872](http://arxiv.org/abs/2312.11872)|**[link](https://github.com/geyanqi/sar)**|
|**2023-12-18**|**ACCL+: an FPGA-Based Collective Engine for Distributed Applications**|Zhenhao He et.al.|[2312.11742](http://arxiv.org/abs/2312.11742)|null|
|**2023-12-11**|**The Limits of Fair Medical Imaging AI In The Wild**|Yuzhe Yang et.al.|[2312.10083](http://arxiv.org/abs/2312.10083)|**[link](https://github.com/yyzharry/shortcut-ood-fairness)**|
|**2023-12-14**|**EAT: Towards Long-Tailed Out-of-Distribution Detection**|Tong Wei et.al.|[2312.08939](http://arxiv.org/abs/2312.08939)|**[link](https://github.com/stomach-ache/long-tailed-ood-detection)**|
|**2023-12-13**|**Contractive error feedback for gradient compression**|Bingcong Li et.al.|[2312.08538](http://arxiv.org/abs/2312.08538)|null|
|**2023-12-13**|**Kimad: Adaptive Gradient Compression with Bandwidth Awareness**|Jihao Xin et.al.|[2312.08053](http://arxiv.org/abs/2312.08053)|null|
|**2023-12-15**|**A Geometry-based Stochastic Wireless Channel Model using Channel Images**|Seongjoon Kang et.al.|[2312.06637](http://arxiv.org/abs/2312.06637)|**[link](https://github.com/sk8053/geostochasticchanmodel)**|
|**2023-12-11**|**Holmes: Towards Distributed Training Across Clusters with Heterogeneous NIC Environment**|Fei Yang et.al.|[2312.03549](http://arxiv.org/abs/2312.03549)|null|
|**2023-12-06**|**Snake Robot with Tactile Perception Navigates on Large-scale Challenging Terrain**|Shuo Jiang et.al.|[2312.03225](http://arxiv.org/abs/2312.03225)|null|
|**2023-12-05**|**FlexModel: A Framework for Interpretability of Distributed Large Language Models**|Matthew Choi et.al.|[2312.03140](http://arxiv.org/abs/2312.03140)|**[link](https://github.com/vectorinstitute/flex_model)**|
|**2023-12-05**|**DanZero+: Dominating the GuanDan Game through Reinforcement Learning**|Youpeng Zhao et.al.|[2312.02561](http://arxiv.org/abs/2312.02561)|**[link](https://github.com/submit-paper/Danzero_plus)**|
|**2023-12-05**|**Flexible Communication for Optimal Distributed Learning over Unpredictable Networks**|Sahil Tyagi et.al.|[2312.02493](http://arxiv.org/abs/2312.02493)|**[link](https://github.com/sahiltyagi4/artopk)**|
|**2023-12-02**|**Can We Learn Communication-Efficient Optimizers?**|Charles-Étienne Joseph et.al.|[2312.02204](http://arxiv.org/abs/2312.02204)|**[link](https://github.com/lefameuxbeding/learned_aggregation)**|
|**2023-11-30**|**GNNFlow: A Distributed Framework for Continuous Temporal GNN Learning on Dynamic Graphs**|Yuchen Zhong et.al.|[2311.17410](http://arxiv.org/abs/2311.17410)|**[link](https://github.com/jasperzhong/GNNFlow)**|
|**2023-11-29**|**The Falcon Series of Open Language Models**|Ebtesam Almazrouei et.al.|[2311.16867](http://arxiv.org/abs/2311.16867)|null|
|**2023-12-04**|**YUAN 2.0: A Large Language Model with Localized Filtering-based Attention**|Shaohua Wu et.al.|[2311.15786](http://arxiv.org/abs/2311.15786)|**[link](https://github.com/ieit-yuan/yuan-2.0)**|
|**2023-11-22**|**Confidant: Customizing Transformer-based LLMs via Collaborative Edge Training**|Yuhao Chen et.al.|[2311.13381](http://arxiv.org/abs/2311.13381)|null|
|**2023-11-21**|**Attacks of fairness in Federated Learning**|Joseph Rance et.al.|[2311.12715](http://arxiv.org/abs/2311.12715)|**[link](https://github.com/slkdfjslkjfd/fl_fairness_attacks)**|
|**2023-11-21**|**Federated Learning via Consensus Mechanism on Heterogeneous Data: A New Perspective on Convergence**|Shu Zheng et.al.|[2311.12358](http://arxiv.org/abs/2311.12358)|**[link](https://github.com/fedcome/fedcome)**|
|**2023-11-15**|**HypOp: Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks**|Nasimeh Heydaribeni et.al.|[2311.09375](http://arxiv.org/abs/2311.09375)|**[link](https://github.com/nasheydari/HypOp)**|
|**2023-11-14**|**Leveraging Foundation Models to Improve Lightweight Clients in Federated Learning**|Xidong Wu et.al.|[2311.08479](http://arxiv.org/abs/2311.08479)|null|
|**2023-11-12**|**GraNNDis: Efficient Unified Distributed Training Framework for Deep GNNs on Large Clusters**|Jaeyong Song et.al.|[2311.06837](http://arxiv.org/abs/2311.06837)|**[link](https://github.com/ais-snu/granndis_artifact)**|
|**2023-11-11**|**Topology-Matching Normalizing Flows for Out-of-Distribution Detection in Robot Learning**|Jianxiang Feng et.al.|[2311.06481](http://arxiv.org/abs/2311.06481)|null|
|**2023-11-06**|**EControl: Fast Distributed Optimization with Compression and Error Control**|Yuan Gao et.al.|[2311.05645](http://arxiv.org/abs/2311.05645)|null|
|**2023-11-08**|**Byzantine-Tolerant Methods for Distributed Variational Inequalities**|Nazarii Tupitsa et.al.|[2311.04611](http://arxiv.org/abs/2311.04611)|null|
|**2023-11-08**|**Ultra-Long Sequence Distributed Transformer**|Xiao Wang et.al.|[2311.02382](http://arxiv.org/abs/2311.02382)|null|
|**2023-11-02**|**RTP: Rethinking Tensor Parallelism with Memory Deduplication**|Cheng Luo et.al.|[2311.01635](http://arxiv.org/abs/2311.01635)|**[link](https://github.com/wdlctc/rtp)**|
|**2023-10-31**|**Network Contention-Aware Cluster Scheduling with Reinforcement Learning**|Junyeol Ryu et.al.|[2310.20209](http://arxiv.org/abs/2310.20209)|**[link](https://github.com/gajagajago/deepshare)**|
|**2023-10-25**|**Redco: A Lightweight Tool to Automate Distributed Training of LLMs on Any GPU/TPUs**|Bowen Tan et.al.|[2310.16355](http://arxiv.org/abs/2310.16355)|**[link](https://github.com/tanyuqian/redco)**|
|**2023-10-23**|**Elemantra: An End-to-End Automated Framework Empowered with AI and IoT for Tackling Human-Elephant Conflict in Elephant-Range Countries**|Nuwan Sriyantha Bandara et.al.|[2310.15012](http://arxiv.org/abs/2310.15012)|**[link](https://github.com/nuwansribandara/elemantra)**|
|**2023-10-22**|**A Quadratic Synchronization Rule for Distributed Deep Learning**|Xinran Gu et.al.|[2310.14423](http://arxiv.org/abs/2310.14423)|**[link](https://github.com/hmgxr128/qsr)**|
|**2023-10-19**|**GARI: Graph Attention for Relative Isomorphism of Arabic Word Embeddings**|Muhammad Asif Ali et.al.|[2310.13068](http://arxiv.org/abs/2310.13068)|**[link](https://github.com/asif6827/gari)**|
|**2023-10-18**|**GRI: Graph-based Relative Isomorphism of Word Embedding Spaces**|Muhammad Asif Ali et.al.|[2310.12360](http://arxiv.org/abs/2310.12360)|**[link](https://github.com/asif6827/gri)**|
|**2023-10-18**|**Differentially Private Distributed Stochastic Optimization with Time-Varying Sample Sizes**|Jimin Wang et.al.|[2310.11892](http://arxiv.org/abs/2310.11892)|null|
|**2023-10-18**|**Unintended Memorization in Large ASR Models, and How to Mitigate It**|Lun Wang et.al.|[2310.11739](http://arxiv.org/abs/2310.11739)|null|
|**2023-10-15**|**The Capacity Region of Information Theoretic Secure Aggregation with Uncoded Groupwise Keys**|Kai Wan et.al.|[2310.09889](http://arxiv.org/abs/2310.09889)|null|
|**2023-10-10**|**Ultima: Robust and Tail-Optimal AllReduce for Distributed Deep Learning in the Cloud**|Ertza Warraich et.al.|[2310.06993](http://arxiv.org/abs/2310.06993)|null|
|**2023-10-10**|**Distributed Transfer Learning with 4th Gen Intel Xeon Processors**|Lakshmi Arunachalam et.al.|[2310.06916](http://arxiv.org/abs/2310.06916)|null|
|**2023-10-23**|**Making Scalable Meta Learning Practical**|Sang Keun Choe et.al.|[2310.05674](http://arxiv.org/abs/2310.05674)|**[link](https://github.com/leopard-ai/betty)**|
|**2023-10-05**|**Solving a Class of Non-Convex Minimax Optimization in Federated Learning**|Xidong Wu et.al.|[2310.03613](http://arxiv.org/abs/2310.03613)|**[link](https://github.com/xidongwu/federated-minimax-and-conditional-stochastic-optimization)**|
|**2023-10-05**|**LightSeq: Sequence Level Parallelism for Distributed Training of Long Context Transformers**|Dacheng Li et.al.|[2310.03294](http://arxiv.org/abs/2310.03294)|**[link](https://github.com/rulinshao/lightseq)**|
|**2023-10-03**|**HPCClusterScape: Increasing Transparency and Efficiency of Shared High-Performance Computing Clusters for Large-scale AI Models**|Heungseok Park et.al.|[2310.02120](http://arxiv.org/abs/2310.02120)|null|
|**2023-09-29**|**AI ensemble for signal detection of higher order gravitational wave modes of quasi-circular, spinning, non-precessing binary black hole mergers**|Minyang Tian et.al.|[2310.00052](http://arxiv.org/abs/2310.00052)|**[link](https://github.com/mtian8/higher_order_gw_spatiotemporal_gnn)**|
|**2023-09-25**|**Exploring the Impact of Serverless Computing on Peer To Peer Training Machine Learning**|Amine Barrak et.al.|[2309.14139](http://arxiv.org/abs/2309.14139)|**[link](https://github.com/aminebarrak/peertopeerserverless)**|
|**2023-09-23**|**Zen: Near-Optimal Sparse Tensor Synchronization for Distributed DNN Training**|Zhuang Wang et.al.|[2309.13254](http://arxiv.org/abs/2309.13254)|null|
|**2023-09-19**|**SPFL: A Self-purified Federated Learning Method Against Poisoning Attacks**|Zizhen Liu et.al.|[2309.10607](http://arxiv.org/abs/2309.10607)|null|
|**2023-09-15**|**Oobleck: Resilient Distributed Training of Large Models Using Pipeline Templates**|Insu Jang et.al.|[2309.08125](http://arxiv.org/abs/2309.08125)|**[link](https://github.com/symbioticlab/oobleck)**|
|**2023-09-13**|**FedDIP: Federated Learning with Extreme Dynamic Pruning and Incremental Regularization**|Qianyu Long et.al.|[2309.06805](http://arxiv.org/abs/2309.06805)|**[link](https://github.com/ericloong/feddip)**|
|**2023-09-08**|**Federated Learning for Early Dropout Prediction on Healthy Ageing Applications**|Christos Chrysanthos Nikolaidis et.al.|[2309.04311](http://arxiv.org/abs/2309.04311)|null|
|**2023-09-04**|**Communication-Efficient Design of Learning System for Energy Demand Forecasting of Electrical Vehicles**|Jiacong Xu et.al.|[2309.01297](http://arxiv.org/abs/2309.01297)|null|
|**2023-08-29**|**CEFHRI: A Communication Efficient Federated Learning Framework for Recognizing Industrial Human-Robot Interaction**|Umar Khalid et.al.|[2308.14965](http://arxiv.org/abs/2308.14965)|**[link](https://github.com/umarkhalidai/cefhri-efficient-federated-learning)**|
|**2023-08-27**|**Generalizable Learning Reconstruction for Accelerating MR Imaging via Federated Neural Architecture Search**|Ruoyou Wu et.al.|[2308.13995](http://arxiv.org/abs/2308.13995)|**[link](https://github.com/ternencewu123/gautomri)**|
|**2023-08-25**|**Staleness-Alleviated Distributed GNN Training via Online Dynamic-Embedding Prediction**|Guangji Bai et.al.|[2308.13466](http://arxiv.org/abs/2308.13466)|null|
|**2023-08-23**|**Aligning Language Models with Offline Reinforcement Learning from Human Feedback**|Jian Hu et.al.|[2308.12050](http://arxiv.org/abs/2308.12050)|**[link](https://github.com/OpenLLMAI/OpenLLaMA2)**|
|**2023-08-17**|**Distributed Extra-gradient with Optimal Complexity and Communication Guarantees**|Ali Ramezani-Kebrya et.al.|[2308.09187](http://arxiv.org/abs/2308.09187)|**[link](https://github.com/lions-epfl/qgenx)**|
|**2023-08-17**|**Towards Lightweight Data Integration using Multi-workflow Provenance and Data Observability**|Renan Souza et.al.|[2308.09004](http://arxiv.org/abs/2308.09004)|**[link](https://github.com/ornl/flowcept)**|
|**2023-08-10**|**Isolated Scheduling for Distributed Training Tasks in GPU Clusters**|Xinchi Han et.al.|[2308.05692](http://arxiv.org/abs/2308.05692)|null|
|**2023-07-25**|**Federated K-Means Clustering via Dual Decomposition-based Distributed Optimization**|Vassilios Yfantis et.al.|[2307.13267](http://arxiv.org/abs/2307.13267)|null|
|**2023-07-21**|**Robust Fully-Asynchronous Methods for Distributed Training over General Architecture**|Zehan Zhu et.al.|[2307.11617](http://arxiv.org/abs/2307.11617)|null|
|**2023-07-16**|**Accelerating Distributed ML Training via Selective Synchronization**|Sahil Tyagi et.al.|[2307.07950](http://arxiv.org/abs/2307.07950)|**[link](https://github.com/sahiltyagi4/selsync)**|
|**2023-07-12**|**Tackling Computational Heterogeneity in FL: A Few Theoretical Insights**|Adnan Ben Mansour et.al.|[2307.06283](http://arxiv.org/abs/2307.06283)|null|
|**2023-07-13**|**Efficient Task Offloading Algorithm for Digital Twin in Edge/Cloud Computing Environment**|Ziru Zhang et.al.|[2307.05888](http://arxiv.org/abs/2307.05888)|null|
|**2023-07-11**|**A Survey From Distributed Machine Learning to Distributed Deep Learning**|Mohammad Dehghani et.al.|[2307.05232](http://arxiv.org/abs/2307.05232)|null|
|**2023-07-13**|**DEFT: Exploiting Gradient Norm Difference between Model Layers for Scalable Gradient Sparsification**|Daegun Yoon et.al.|[2307.03500](http://arxiv.org/abs/2307.03500)|**[link](https://github.com/kljp/deft)**|
|**2023-07-05**|**Improving Automatic Parallel Training via Balanced Memory Workload Optimization**|Yujie Wang et.al.|[2307.02031](http://arxiv.org/abs/2307.02031)|**[link](https://github.com/pku-dair/hetu)**|
|**2023-06-30**|**Hashing-Based Distributed Clustering for Massive High-Dimensional Data**|Yifeng Xiao et.al.|[2306.17417](http://arxiv.org/abs/2306.17417)|null|
|**2023-06-29**|**A Survey on Blockchain-Based Federated Learning and Data Privacy**|Bipin Chhetri et.al.|[2306.17338](http://arxiv.org/abs/2306.17338)|null|
|**2023-07-09**|**OSP: Boosting Distributed Model Training with 2-stage Synchronization**|Zixuan Chen et.al.|[2306.16926](http://arxiv.org/abs/2306.16926)|null|
|**2023-06-28**|**Federated Generative Learning with Foundation Models**|Jie Zhang et.al.|[2306.16064](http://arxiv.org/abs/2306.16064)|**[link](https://github.com/zj-jayzhang/federated_generative_learning)**|
|**2023-06-24**|**Computron: Serving Distributed Deep Learning Models with Model Parallel Swapping**|Daniel Zou et.al.|[2306.13835](http://arxiv.org/abs/2306.13835)|**[link](https://github.com/dlzou/computron)**|
|**2023-06-23**|**Reinforcement Federated Learning Method Based on Adaptive OPTICS Clustering**|Tianyu Zhao et.al.|[2306.12859](http://arxiv.org/abs/2306.12859)|null|
|**2023-06-19**|**Data-Heterogeneous Hierarchical Federated Learning with Mobility**|Tan Chen et.al.|[2306.10692](http://arxiv.org/abs/2306.10692)|null|
|**2023-06-18**|**DropCompute: simple and more robust distributed synchronous training via compute variance reduction**|Niv Giladi et.al.|[2306.10598](http://arxiv.org/abs/2306.10598)|**[link](https://github.com/paper-submissions/dropcompute)**|
|**2023-06-15**|**Evaluation and Optimization of Gradient Compression for Distributed Deep Learning**|Lin Zhang et.al.|[2306.08881](http://arxiv.org/abs/2306.08881)|**[link](https://github.com/lzhangbv/acpsgd)**|
|**2023-06-14**|**DistSim: A performance model of large-scale hybrid distributed DNN training**|Guandong Lu et.al.|[2306.08423](http://arxiv.org/abs/2306.08423)|null|
|**2023-06-14**|**$\textbf{A}^2\textbf{CiD}^2$ : Accelerating Asynchronous Communication in Decentralized Deep Learning**|Adel Nabli et.al.|[2306.08289](http://arxiv.org/abs/2306.08289)|**[link](https://github.com/adelnabli/acid)**|
|**2023-05-31**|**Surrogate Model Extension (SME): A Fast and Accurate Weight Update Attack on Federated Learning**|Junyi Zhu et.al.|[2306.00127](http://arxiv.org/abs/2306.00127)|**[link](https://github.com/junyizhu-ai/surrogate_model_extension)**|
|**2023-05-29**|**Global-QSGD: Practical Floatless Quantization for Distributed Learning with Theoretical Guarantees**|Jihao Xin et.al.|[2305.18627](http://arxiv.org/abs/2305.18627)|null|
|**2023-05-26**|**Channel and Gradient-Importance Aware Device Scheduling for Over-the-Air Federated Learning**|Yuchang Sun et.al.|[2305.16854](http://arxiv.org/abs/2305.16854)|null|
|**2023-05-22**|**Distributed Learning over Networks with Graph-Attention-Based Personalization**|Zhuojun Tian et.al.|[2305.13041](http://arxiv.org/abs/2305.13041)|**[link](https://github.com/ZhuoJTian/GATTA)**|
|**2023-05-21**|**2Direction: Theoretically Faster Distributed Training with Bidirectional Communication Compression**|Alexander Tyurin et.al.|[2305.12379](http://arxiv.org/abs/2305.12379)|null|
|**2023-05-17**|**Curriculum Learning in Job Shop Scheduling using Reinforcement Learning**|Constantin Waubert de Puiseau et.al.|[2305.10192](http://arxiv.org/abs/2305.10192)|null|
|**2023-05-18**|**OSDP: Optimal Sharded Data Parallel for Distributed Deep Learning**|Youhe Jiang et.al.|[2305.09940](http://arxiv.org/abs/2305.09940)|**[link](https://github.com/youhe-jiang/ijcai2023-optimalshardeddataparallel)**|
|**2023-05-17**|**Simplifying Distributed Neural Network Training on Massive Graphs: Randomized Partitions Improve Model Aggregation**|Jiong Zhu et.al.|[2305.09887](http://arxiv.org/abs/2305.09887)|null|
|**2023-05-12**|**Dynamically Conservative Self-Driving Planner for Long-Tail Cases**|Weitao Zhou et.al.|[2305.07497](http://arxiv.org/abs/2305.07497)|null|
|**2023-05-10**|**P4SGD: Programmable Switch Enhanced Model-Parallel Training on Generalized Linear Models on Distributed FPGAs**|Hongjing Huang et.al.|[2305.05885](http://arxiv.org/abs/2305.05885)|null|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

## GNN System

|Publish Date|Title|Authors|PDF|Code|
|---|---|---|---|---|
|**2025-03-26**|**$β$ -GNN: A Robust Ensemble Approach Against Graph Structure Perturbation**|Haci Ismail Aslan et.al.|[2503.20630](http://arxiv.org/abs/2503.20630)|null|
|**2025-03-26**|**Multi-dataset and Transfer Learning Using Gene Expression Knowledge Graphs**|Rita T. Sousa et.al.|[2503.20400](http://arxiv.org/abs/2503.20400)|null|
|**2025-03-26**|**Emergent properties and the multiscale characterization challenge in condensed matter, from crystals to complex materials: a Review**|Elisabetta Nocerino et.al.|[2503.20266](http://arxiv.org/abs/2503.20266)|null|
|**2025-03-26**|**BeLightRec: A lightweight recommender system enhanced with BERT**|Manh Mai Van et.al.|[2503.20206](http://arxiv.org/abs/2503.20206)|null|
|**2025-03-25**|**Peer Disambiguation in Self-Reported Surveys using Graph Attention Networks**|Ajitesh Srivastava et.al.|[2503.20076](http://arxiv.org/abs/2503.20076)|null|
|**2025-03-25**|**Developing a Complete AI-Accelerated Workflow for Superconductor Discovery**|Jason B. Gibson et.al.|[2503.20005](http://arxiv.org/abs/2503.20005)|null|
|**2025-03-26**|**Towards Efficient Training of Graph Neural Networks: A Multiscale Approach**|Eshed Gal et.al.|[2503.19666](http://arxiv.org/abs/2503.19666)|null|
|**2025-03-25**|**Extracting Interpretable Logic Rules from Graph Neural Networks**|Chuqin Geng et.al.|[2503.19476](http://arxiv.org/abs/2503.19476)|null|
|**2025-03-25**|**Causal invariant geographic network representations with feature and structural distribution shifts**|Yuhan Wang et.al.|[2503.19382](http://arxiv.org/abs/2503.19382)|null|
|**2025-03-25**|**Social Network User Profiling for Anomaly Detection Based on Graph Neural Networks**|Yiwei Zhang et.al.|[2503.19380](http://arxiv.org/abs/2503.19380)|null|
|**2025-03-25**|**A Social Dynamical System for Twitter Analysis**|Zhiping Xiao et.al.|[2503.19316](http://arxiv.org/abs/2503.19316)|null|
|**2025-03-25**|**Context-Aware Semantic Segmentation: Enhancing Pixel-Level Understanding with Large Language Models for Advanced Vision Applications**|Ben Rahman et.al.|[2503.19276](http://arxiv.org/abs/2503.19276)|null|
|**2025-03-24**|**Graph neural networks extrapolate out-of-distribution for shortest paths**|Robert R. Nerem et.al.|[2503.19173](http://arxiv.org/abs/2503.19173)|null|
|**2025-03-26**|**Graph-Level Label-Only Membership Inference Attack against Graph Neural Networks**|Jiazhu Dai et.al.|[2503.19070](http://arxiv.org/abs/2503.19070)|null|
|**2025-03-24**|**Multi-Physics Inverse Design of Varifocal Optical Devices using Data-Driven Surrogates and Differential Modeling**|Zeqing Jin et.al.|[2503.18911](http://arxiv.org/abs/2503.18911)|null|
|**2025-03-24**|**Energy-Efficient Dynamic Training and Inference for GNN-Based Network Modeling**|Chetna Singhal et.al.|[2503.18706](http://arxiv.org/abs/2503.18706)|null|
|**2025-03-24**|**Predicting airfoil pressure distribution using boundary graph neural networks**|Sankalp Jena et.al.|[2503.18638](http://arxiv.org/abs/2503.18638)|null|
|**2025-03-24**|**Deterministic Certification of Graph Neural Networks against Graph Poisoning Attacks with Arbitrary Perturbations**|Jiate Li et.al.|[2503.18503](http://arxiv.org/abs/2503.18503)|null|
|**2025-03-24**|**MAGIC-VQA: Multimodal And Grounded Inference with Commonsense Knowledge for Visual Question Answering**|Shuo Yang et.al.|[2503.18491](http://arxiv.org/abs/2503.18491)|null|
|**2025-03-24**|**AES-SpMM: Balancing Accuracy and Speed by Adaptive Edge Sampling Strategy to Accelerate SpMM in GNNs**|Yingchen Song et.al.|[2503.18427](http://arxiv.org/abs/2503.18427)|null|
|**2025-03-24**|**DiffusedWrinkles: A Diffusion-Based Model for Data-Driven Garment Animation**|Raquel Vidaurre et.al.|[2503.18370](http://arxiv.org/abs/2503.18370)|null|
|**2025-03-23**|**Iterative Multi-Agent Reinforcement Learning: A Novel Approach Toward Real-World Multi-Echelon Inventory Optimization**|Georg Ziegner et.al.|[2503.18201](http://arxiv.org/abs/2503.18201)|null|
|**2025-03-23**|**Shapley-Guided Utility Learning for Effective Graph Inference Data Valuation**|Hongliang Chi et.al.|[2503.18195](http://arxiv.org/abs/2503.18195)|null|
|**2025-03-23**|**Equivariant Machine Learning Interatomic Potentials with Global Charge Redistribution**|Moin Uddin Maruf et.al.|[2503.17949](http://arxiv.org/abs/2503.17949)|**[link](https://github.com/ahmad-research-group/nequip-charge)**|
|**2025-03-21**|**Robustness of deep learning classification to adversarial input on GPUs: asynchronous parallel accumulation is a source of vulnerability**|Sanjif Shanmugavelu et.al.|[2503.17173](http://arxiv.org/abs/2503.17173)|null|
|**2025-03-21**|**Enhancing Steering Estimation with Semantic-Aware GNNs**|Fouad Makiyeh et.al.|[2503.17153](http://arxiv.org/abs/2503.17153)|null|
|**2025-03-21**|**TeMP-TraG: Edge-based Temporal Message Passing in Transaction Graphs**|Steve Gounoue et.al.|[2503.16901](http://arxiv.org/abs/2503.16901)|null|
|**2025-03-20**|**Ordered Topological Deep Learning: a Network Modeling Case Study**|Guillermo Bernárdez et.al.|[2503.16746](http://arxiv.org/abs/2503.16746)|null|
|**2025-03-20**|**ATOM: A Framework of Detecting Query-Based Model Extraction Attacks for Graph Neural Networks**|Zhan Cheng et.al.|[2503.16693](http://arxiv.org/abs/2503.16693)|null|
|**2025-03-20**|**ContextGNN goes to Elliot: Towards Benchmarking Relational Deep Learning for Static Link Prediction (aka Personalized Item Recommendation)**|Alejandro Ariza-Casabona et.al.|[2503.16661](http://arxiv.org/abs/2503.16661)|null|
|**2025-03-20**|**Beyond Local Selection: Global Cut Selection for Enhanced Mixed-Integer Programming**|Shuli Zeng et.al.|[2503.15847](http://arxiv.org/abs/2503.15847)|null|
|**2025-03-20**|**GraPLUS: Graph-based Placement Using Semantics for Image Composition**|Mir Mohammad Khaleghi et.al.|[2503.15761](http://arxiv.org/abs/2503.15761)|null|
|**2025-03-19**|**Survey on Generalization Theory for Graph Neural Networks**|Antonis Vasileiou et.al.|[2503.15650](http://arxiv.org/abs/2503.15650)|null|
|**2025-03-19**|**PEnGUiN: Partially Equivariant Graph NeUral Networks for Sample Efficient MARL**|Joshua McClellan et.al.|[2503.15615](http://arxiv.org/abs/2503.15615)|null|
|**2025-03-19**|**Modeling crystal defects using defect-informed neural networks**|Ziduo Yang et.al.|[2503.15391](http://arxiv.org/abs/2503.15391)|**[link](https://github.com/Shen-Group/DefiNet)**|
|**2025-03-19**|**Lyapunov-Based Graph Neural Networks for Adaptive Control of Multi-Agent Systems**|Brandon C. Fallin et.al.|[2503.15360](http://arxiv.org/abs/2503.15360)|null|
|**2025-03-19**|**Learning to quantify graph nodes**|Alessio Micheli et.al.|[2503.15267](http://arxiv.org/abs/2503.15267)|null|
|**2025-03-20**|**Classification of Electron and Muon Neutrino Events for the ESS $ν$ SB Near Water Cherenkov Detector using Graph Neural Networks**|J. Aguilar et.al.|[2503.15247](http://arxiv.org/abs/2503.15247)|null|
|**2025-03-19**|**Learning Topology Actions for Power Grid Control: A Graph-Based Soft-Label Imitation Learning Approach**|Mohamed Hassouna et.al.|[2503.15190](http://arxiv.org/abs/2503.15190)|null|
|**2025-03-19**|**Interpretability of Graph Neural Networks to Assert Effects of Global Change Drivers on Ecological Networks**|Emre Anakok et.al.|[2503.15107](http://arxiv.org/abs/2503.15107)|null|
|**2025-03-19**|**Embedding spatial context in urban traffic forecasting with contrastive pre-training**|Matthew Low et.al.|[2503.14980](http://arxiv.org/abs/2503.14980)|null|
|**2025-03-19**|**Deep Polycuboid Fitting for Compact 3D Representation of Indoor Scenes**|Gahye Lee et.al.|[2503.14912](http://arxiv.org/abs/2503.14912)|null|
|**2025-03-19**|**DVHGNN: Multi-Scale Dilated Vision HGNN for Efficient Vision Recognition**|Caoshuo Li et.al.|[2503.14867](http://arxiv.org/abs/2503.14867)|null|
|**2025-03-19**|**Graph-Based Re-ranking: Emerging Techniques, Limitations, and Opportunities**|Md Shahir Zaoad et.al.|[2503.14802](http://arxiv.org/abs/2503.14802)|null|
|**2025-03-18**|**Unifying Text Semantics and Graph Structures for Temporal Text-attributed Graphs with Large Language Models**|Siwei Zhang et.al.|[2503.14411](http://arxiv.org/abs/2503.14411)|null|
|**2025-03-18**|**Spatio-Temporal Graph Neural Networks for Infant Language Acquisition Prediction**|Andrew Roxburgh et.al.|[2503.14341](http://arxiv.org/abs/2503.14341)|null|
|**2025-03-18**|**Higher-Order Graphon Neural Networks: Approximation and Cut Distance**|Daniel Herbst et.al.|[2503.14338](http://arxiv.org/abs/2503.14338)|null|
|**2025-03-18**|**Application of Geometric Deep Learning for Tracking of Hyperons in a Straw Tube Detector**|Adeel Akram et.al.|[2503.14305](http://arxiv.org/abs/2503.14305)|null|
|**2025-03-19**|**Persistent Homology-induced Graph Ensembles for Time Series Regressions**|Viet The Nguyen et.al.|[2503.14240](http://arxiv.org/abs/2503.14240)|**[link](https://github.com/vietngth/ph-ensemble-gnn)**|
|**2025-03-18**|**Rolling Forward: Enhancing LightGCN with Causal Graph Convolution for Credit Bond Recommendation**|Ashraf Ghiye et.al.|[2503.14213](http://arxiv.org/abs/2503.14213)|null|
|**2025-03-17**|**SMPR: A structure-enhanced multimodal drug-disease prediction model for drug repositioning and cold start**|Xin Dong et.al.|[2503.13322](http://arxiv.org/abs/2503.13322)|null|
|**2025-03-17**|**MIXPINN: Mixed-Material Simulations by Physics-Informed Neural Network**|Xintian Yuan et.al.|[2503.13123](http://arxiv.org/abs/2503.13123)|null|
|**2025-03-17**|**TA-GNN: Physics Inspired Time-Agnostic Graph Neural Network for Finger Motion Prediction**|Tinghui Li et.al.|[2503.13034](http://arxiv.org/abs/2503.13034)|null|
|**2025-03-16**|**GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation**|Tao Feng et.al.|[2503.12600](http://arxiv.org/abs/2503.12600)|null|
|**2025-03-16**|**Diffusion on Graph: Augmentation of Graph Structure for Node Classification**|Yancheng Wang et.al.|[2503.12563](http://arxiv.org/abs/2503.12563)|null|
|**2025-03-16**|**Learning Privacy from Visual Entities**|Alessio Xompero et.al.|[2503.12464](http://arxiv.org/abs/2503.12464)|null|
|**2025-03-16**|**GCBLANE: A graph-enhanced convolutional BiLSTM attention network for improved transcription factor binding site prediction**|Jonas Chris Ferrao et.al.|[2503.12377](http://arxiv.org/abs/2503.12377)|**[link](https://github.com/projectultra/GCBLANE)**|
|**2025-03-15**|**Unsupervised Graph Anomaly Detection via Multi-Hypersphere Heterophilic Graph Learning**|Hang Ni et.al.|[2503.12037](http://arxiv.org/abs/2503.12037)|**[link](https://github.com/kennynh/mhetgl)**|
|**2025-03-15**|**Diffusion Dynamics Models with Generative State Estimation for Cloth Manipulation**|Tongxuan Tian et.al.|[2503.11999](http://arxiv.org/abs/2503.11999)|null|
|**2025-03-14**|**Heterogenous graph neural networks for species distribution modeling**|Lauren Harrell et.al.|[2503.11900](http://arxiv.org/abs/2503.11900)|null|
|**2025-03-14**|**Enhanced Soups for Graph Neural Networks**|Joseph Zuber et.al.|[2503.11612](http://arxiv.org/abs/2503.11612)|**[link](https://github.com/zubes01/enhanced-soups-for-graph-neural-networks)**|
|**2025-03-14**|**GNNs as Predictors of Agentic Workflow Performances**|Yuanshuo Zhang et.al.|[2503.11301](http://arxiv.org/abs/2503.11301)|**[link](https://github.com/youngsoul0731/flora-bench)**|
|**2025-03-14**|**Power-Aware Scheduling for Multi-Center HPC Electricity Cost Optimization**|Abrar Hossain et.al.|[2503.11011](http://arxiv.org/abs/2503.11011)|null|
|**2025-03-13**|**PolyRoof: Precision Roof Polygonization in Urban Residential Building with Graph Neural Networks**|Chaikal Amrullah et.al.|[2503.10913](http://arxiv.org/abs/2503.10913)|null|
|**2025-03-13**|**TacticExpert: Spatial-Temporal Graph Language Model for Basketball Tactics**|Xu Lingrui et.al.|[2503.10722](http://arxiv.org/abs/2503.10722)|null|
|**2025-03-13**|**DP-GPL: Differentially Private Graph Prompt Learning**|Jing Xu et.al.|[2503.10544](http://arxiv.org/abs/2503.10544)|null|
|**2025-03-13**|**AMR-Transformer: Enabling Efficient Long-range Interaction for Complex Neural Fluid Simulation**|Zeyi Xu et.al.|[2503.10257](http://arxiv.org/abs/2503.10257)|null|
|**2025-03-12**|**Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis**|Chenjun Li et.al.|[2503.09808](http://arxiv.org/abs/2503.09808)|null|
|**2025-03-12**|**How Feasible is Augmenting Fake Nodes with Learnable Features as a Counter-strategy against Link Stealing Attacks?**|Mir Imtiaz Mostafiz et.al.|[2503.09726](http://arxiv.org/abs/2503.09726)|null|
|**2025-03-14**|**Graph-based Full Event Interpretation: a graph neural network for event reconstruction in Belle II**|Merna Abumusabh et.al.|[2503.09401](http://arxiv.org/abs/2503.09401)|null|
|**2025-03-12**|**Post-interactive Multimodal Trajectory Prediction for Autonomous Driving**|Ziyi Huang et.al.|[2503.09366](http://arxiv.org/abs/2503.09366)|null|
|**2025-03-12**|**Crowdsourced Homophily Ties Based Graph Annotation Via Large Language Model**|Yu Bu et.al.|[2503.09281](http://arxiv.org/abs/2503.09281)|null|
|**2025-03-12**|**SCOPE-DTI: Semi-Inductive Dataset Construction and Framework Optimization for Practical Usability Enhancement in Deep Learning-Based Drug Target Interaction Prediction**|Yigang Chen et.al.|[2503.09251](http://arxiv.org/abs/2503.09251)|**[link](https://github.com/yigang-chen/scope-dti)**|
|**2025-03-12**|**TreeX: Generating Global Graphical GNN Explanations via Critical Subtree Extraction**|Shengyao Lu et.al.|[2503.09051](http://arxiv.org/abs/2503.09051)|null|
|**2025-03-12**|**Adaptive Backdoor Attacks with Reasonable Constraints on Graph Neural Networks**|Xuewen Dong et.al.|[2503.09049](http://arxiv.org/abs/2503.09049)|null|
|**2025-03-12**|**Towards Quantifying Long-Range Interactions in Graph Machine Learning: a Large Graph Dataset and a Measurement**|Huidong Liang et.al.|[2503.09008](http://arxiv.org/abs/2503.09008)|**[link](https://github.com/leonresearch/city-networks)**|
|**2025-03-11**|**i-WiViG: Interpretable Window Vision GNN**|Ivica Obadic et.al.|[2503.08321](http://arxiv.org/abs/2503.08321)|null|
|**2025-03-11**|**Evidential Uncertainty Probes for Graph Neural Networks**|Linlin Yu et.al.|[2503.08097](http://arxiv.org/abs/2503.08097)|null|
|**2025-03-10**|**CIMAGE: Exploiting the Conditional Independence in Masked Graph Auto-encoders**|Jongwon Park et.al.|[2503.07852](http://arxiv.org/abs/2503.07852)|null|
|**2025-03-10**|**Beyond the Edge of Function: Unraveling the Patterns of Type Recovery in Binary Code**|Gangyang Li et.al.|[2503.07243](http://arxiv.org/abs/2503.07243)|**[link](https://github.com/giles-one/ByteTR)**|
|**2025-03-10**|**An Analytics-Driven Approach to Enhancing Supply Chain Visibility with Graph Neural Networks and Federated Learning**|Ge Zheng et.al.|[2503.07231](http://arxiv.org/abs/2503.07231)|null|
|**2025-03-10**|**Explainable Android Malware Detection and Malicious Code Localization Using Graph Attention**|Merve Cigdem Ipek et.al.|[2503.07109](http://arxiv.org/abs/2503.07109)|null|
|**2025-03-10**|**Graph Neural Network for Location- and Orientation-Assisted mmWave Beam Alignment**|Yuzhu Lei et.al.|[2503.06943](http://arxiv.org/abs/2503.06943)|null|
|**2025-03-09**|**Deep Cut-informed Graph Embedding and Clustering**|Zhiyuan Ning et.al.|[2503.06635](http://arxiv.org/abs/2503.06635)|null|
|**2025-03-09**|**Hardware-Accelerated Event-Graph Neural Networks for Low-Latency Time-Series Classification on SoC FPGA**|Hiroshi Nakano et.al.|[2503.06629](http://arxiv.org/abs/2503.06629)|null|
|**2025-03-09**|**Using Subgraph GNNs for Node Classification:an Overlooked Potential Approach**|Qian Zeng et.al.|[2503.06614](http://arxiv.org/abs/2503.06614)|null|
|**2025-03-09**|**Identifying Evidence Subgraphs for Financial Risk Detection via Graph Counterfactual and Factual Reasoning**|Huaming Du et.al.|[2503.06441](http://arxiv.org/abs/2503.06441)|null|
|**2025-03-09**|**Dynamic Load Balancing for EV Charging Stations Using Reinforcement Learning and Demand Prediction**|Hesam Mosalli et.al.|[2503.06370](http://arxiv.org/abs/2503.06370)|null|
|**2025-03-08**|**GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks**|Xiao Yue et.al.|[2503.06352](http://arxiv.org/abs/2503.06352)|null|
|**2025-03-06**|**Learning Wideband User Scheduling and Hybrid Precoding with Graph Neural Networks**|Shengjie Liu et.al.|[2503.04233](http://arxiv.org/abs/2503.04233)|null|
|**2025-03-06**|**The JARVIS Infrastructure is All You Need for Materials Design**|Kamal Choudhary et.al.|[2503.04133](http://arxiv.org/abs/2503.04133)|null|
|**2025-03-05**|**Trial by FIRE: Probing the dark matter density profile of dwarf galaxies with GraphNPE**|Tri Nguyen et.al.|[2503.03812](http://arxiv.org/abs/2503.03812)|**[link](https://github.com/justinread/gravsphere)**|
|**2025-03-05**|**PacketCLIP: Multi-Modal Embedding of Network Traffic and Language for Cybersecurity Reasoning**|Ryozo Masukawa et.al.|[2503.03747](http://arxiv.org/abs/2503.03747)|null|
|**2025-03-05**|**Opportunistic Routing in Wireless Communications via Learnable State-Augmented Policies**|Sourajit Das et.al.|[2503.03736](http://arxiv.org/abs/2503.03736)|**[link](https://github.com/sourajitdas/State-Augmented-Routing-Wireless-Communication)**|
|**2025-03-05**|**REGRACE: A Robust and Efficient Graph-based Re-localization Algorithm using Consistency Evaluation**|Débora N. P. Oliveira et.al.|[2503.03599](http://arxiv.org/abs/2503.03599)|null|
|**2025-03-05**|**Mineral segmentation using electron microscope images and spectral sampling through multimodal graph neural networks**|Samuel Repka et.al.|[2503.03507](http://arxiv.org/abs/2503.03507)|null|
|**2025-03-05**|**GNNMerge: Merging of GNN Models Without Accessing Training Data**|Vipul Garg et.al.|[2503.03384](http://arxiv.org/abs/2503.03384)|**[link](https://github.com/idea-iitd/gnnmerge)**|
|**2025-03-05**|**Leap: Inductive Link Prediction via Learnable TopologyAugmentation**|Ahmed E. Samy et.al.|[2503.03331](http://arxiv.org/abs/2503.03331)|**[link](https://github.com/ahmedesamy/leap)**|
|**2025-03-05**|**LLM as GNN: Graph Vocabulary Learning for Text-Attributed Graph Foundation Models**|Xi Zhu et.al.|[2503.03313](http://arxiv.org/abs/2503.03313)|null|
|**2025-03-05**|**Exploring the Potential of Large Language Models as Predictors in Dynamic Text-Attributed Graphs**|Runlin Lei et.al.|[2503.03258](http://arxiv.org/abs/2503.03258)|null|
|**2025-03-05**|**Structural Entropy Guided Unsupervised Graph Out-Of-Distribution Detection**|Yue Hou et.al.|[2503.03241](http://arxiv.org/abs/2503.03241)|**[link](https://github.com/name-is-what/sego)**|
|**2025-03-05**|**NodeReg: Mitigating the Imbalance and Distribution Shift Effects in Semi-Supervised Node Classification via Norm Consistency**|Shenzhi Yang et.al.|[2503.03211](http://arxiv.org/abs/2503.03211)|null|
|**2025-03-04**|**NodeNAS: Node-Specific Graph Neural Architecture Search for Out-of-Distribution Generalization**|Qiyi Wang et.al.|[2503.02448](http://arxiv.org/abs/2503.02448)|null|
|**2025-03-04**|**InfoGNN: End-to-end deep learning on mesh via graph neural networks**|Ling Gao et.al.|[2503.02414](http://arxiv.org/abs/2503.02414)|null|
|**2025-03-04**|**A Binary Classification Social Network Dataset for Graph Machine Learning**|Adnan Ali et.al.|[2503.02397](http://arxiv.org/abs/2503.02397)|null|
|**2025-03-04**|**Incorporating graph neural network into route choice model**|Yuxun Ma et.al.|[2503.02315](http://arxiv.org/abs/2503.02315)|null|
|**2025-03-04**|**CrystalFramer: Rethinking the Role of Frames for SE(3)-Invariant Crystal Structure Modeling**|Yusei Ito et.al.|[2503.02209](http://arxiv.org/abs/2503.02209)|null|
|**2025-03-03**|**Fairness and/or Privacy on Social Graphs**|Bartlomiej Surma et.al.|[2503.02114](http://arxiv.org/abs/2503.02114)|**[link](https://github.com/EnderGed/FairGCN)**|
|**2025-03-03**|**Quantifying Point Contributions: A Lightweight Framework for Efficient and Effective Query-Driven Trajectory Simplification**|Yumeng Song et.al.|[2503.02047](http://arxiv.org/abs/2503.02047)|null|
|**2025-03-03**|**Learning Exposure Mapping Functions for Inferring Heterogeneous Peer Effects**|Shishir Adhikari et.al.|[2503.01722](http://arxiv.org/abs/2503.01722)|null|
|**2025-03-03**|**GRNFormer: A Biologically-Guided Framework for Integrating Gene Regulatory Networks into RNA Foundation Models**|Mufan Qiu et.al.|[2503.01682](http://arxiv.org/abs/2503.01682)|null|
|**2025-03-03**|**Effective High-order Graph Representation Learning for Credit Card Fraud Detection**|Yao Zou et.al.|[2503.01556](http://arxiv.org/abs/2503.01556)|null|
|**2025-02-28**|**Assessing zero-shot generalisation behaviour in graph-neural-network interatomic potentials**|Chiheb Ben Mahmoud et.al.|[2502.21317](http://arxiv.org/abs/2502.21317)|null|
|**2025-02-28**|**AMPLE: Event-Driven Accelerator for Mixed-Precision Inference of Graph Neural Networks**|Pedro Gimenes et.al.|[2502.21196](http://arxiv.org/abs/2502.21196)|null|
|**2025-02-28**|**Dynamically Local-Enhancement Planner for Large-Scale Autonomous Driving**|Nanshan Deng et.al.|[2502.21134](http://arxiv.org/abs/2502.21134)|null|
|**2025-02-28**|**Information Bottleneck-Guided Heterogeneous Graph Learning for Interpretable Neurodevelopmental Disorder Diagnosis**|Yueyang Li et.al.|[2502.20769](http://arxiv.org/abs/2502.20769)|null|
|**2025-02-28**|**Generating Clinically Realistic EHR Data via a Hierarchy- and Semantics-Guided Transformer**|Guanglin Zhou et.al.|[2502.20719](http://arxiv.org/abs/2502.20719)|null|
|**2025-02-27**|**A2-GNN: Angle-Annular GNN for Visual Descriptor-free Camera Relocalization**|Yejun Zhang et.al.|[2502.20036](http://arxiv.org/abs/2502.20036)|**[link](https://github.com/yejunzhang/a2-gnn)**|
|**2025-02-27**|**WaveGAS: Waveform Relaxation for Scaling Graph Neural Networks**|Jana Vatter et.al.|[2502.19986](http://arxiv.org/abs/2502.19986)|null|
|**2025-02-27**|**Efficient and Universal Neural-Network Decoder for Stabilizer-Based Quantum Error Correction**|Gengyuan Hu et.al.|[2502.19971](http://arxiv.org/abs/2502.19971)|null|
|**2025-02-27**|**GraphSparseNet: a Novel Method for Large Scale Trafffic Flow Prediction**|Weiyang Kong et.al.|[2502.19823](http://arxiv.org/abs/2502.19823)|null|
|**2025-02-27**|**Accurate and Scalable Graph Neural Networks via Message Invariance**|Zhihao Shi et.al.|[2502.19693](http://arxiv.org/abs/2502.19693)|**[link](https://github.com/MIRALab-USTC/TOP)**|
|**2025-02-27**|**Training Robust Graph Neural Networks by Modeling Noise Dependencies**|Yeonjun In et.al.|[2502.19670](http://arxiv.org/abs/2502.19670)|**[link](https://github.com/yeonjun-in/torch-DA-GNN)**|
|**2025-02-26**|**Preference-Based Gradient Estimation for ML-Based Approximate Combinatorial Optimization**|Arman Mielke et.al.|[2502.19377](http://arxiv.org/abs/2502.19377)|null|
|**2025-02-26**|**GraphBridge: Towards Arbitrary Transfer Learning in GNNs**|Li Ju et.al.|[2502.19252](http://arxiv.org/abs/2502.19252)|**[link](https://github.com/jujulili888/graphbridge)**|
|**2025-02-26**|**Multi-level Attention-guided Graph Neural Network for Image Restoration**|Jiatao Jiang et.al.|[2502.19181](http://arxiv.org/abs/2502.19181)|null|
|**2025-02-26**|**Graph Neural Networks embedded into Margules model for vapor-liquid equilibria prediction**|Edgar Ivan Sanchez Medina et.al.|[2502.18998](http://arxiv.org/abs/2502.18998)|**[link](https://github.com/edgarsmdn/gh_gnn_margules)**|
|**2025-02-26**|**SE(3)-Equivariant Ternary Complex Prediction Towards Target Protein Degradation**|Fanglei Xue et.al.|[2502.18875](http://arxiv.org/abs/2502.18875)|**[link](https://github.com/youqingxiaozhua/deepternary)**|
|**2025-02-26**|**TabGLM: Tabular Graph Language Model for Learning Transferable Representations Through Multi-Modal Consistency Minimization**|Anay Majee et.al.|[2502.18847](http://arxiv.org/abs/2502.18847)|null|
|**2025-02-26**|**Exploring Graph Tasks with Pure LLMs: A Comprehensive Benchmark and Investigation**|Yuxiang Wang et.al.|[2502.18771](http://arxiv.org/abs/2502.18771)|**[link](https://github.com/myflashbarry/LLM-benchmarking)**|
|**2025-02-26**|**Robust Prediction of Frictional Contact Network in Near-Jamming Suspensions Employing Deep Graph Neural Networks**|Armin Aminimajd et.al.|[2502.18743](http://arxiv.org/abs/2502.18743)|null|
|**2025-02-25**|**Graph Augmentation for Cross Graph Domain Generalization**|Guanzi Chen et.al.|[2502.18188](http://arxiv.org/abs/2502.18188)|null|
|**2025-02-25**|**ExPath: Towards Explaining Targeted Pathways for Biological Knowledge Bases**|Rikuto Kotoge et.al.|[2502.18026](http://arxiv.org/abs/2502.18026)|null|
|**2025-02-25**|**GNN-XAR: A Graph Neural Network for Explainable Activity Recognition in Smart Homes**|Michele Fiori et.al.|[2502.17999](http://arxiv.org/abs/2502.17999)|null|
|**2025-02-25**|**A graph neural network-based multispectral-view learning model for diabetic macular ischemia detection from color fundus photographs**|Qinghua He et.al.|[2502.17886](http://arxiv.org/abs/2502.17886)|null|
|**2025-02-25**|**Neural Graph Matching Improves Retrieval Augmented Generation in Molecular Machine Learning**|Runzhong Wang et.al.|[2502.17874](http://arxiv.org/abs/2502.17874)|null|
|**2025-02-25**|**Armada: Memory-Efficient Distributed Training of Large-Scale Graph Neural Networks**|Roger Waleffe et.al.|[2502.17846](http://arxiv.org/abs/2502.17846)|null|
|**2025-02-25**|**Are GNNs doomed by the topology of their input graph?**|Amine Mohamed Aboussalah et.al.|[2502.17739](http://arxiv.org/abs/2502.17739)|null|
|**2025-02-24**|**Learning Decentralized Swarms Using Rotation Equivariant Graph Neural Networks**|Taos Transue et.al.|[2502.17612](http://arxiv.org/abs/2502.17612)|null|
|**2025-02-24**|**Sustainable Greenhouse Management: A Comparative Analysis of Recurrent and Graph Neural Networks**|Emiliano Seri et.al.|[2502.17371](http://arxiv.org/abs/2502.17371)|null|
|**2025-02-24**|**Applications of Large Models in Medicine**|YunHe Su et.al.|[2502.17132](http://arxiv.org/abs/2502.17132)|null|
|**2025-02-24**|**Detecting Code Vulnerabilities with Heterogeneous GNN Training**|Yu Luo et.al.|[2502.16835](http://arxiv.org/abs/2502.16835)|null|
|**2025-02-24**|**VGFL-SA: Vertical Graph Federated Learning Structure Attack Based on Contrastive Learning**|Yang Chen et.al.|[2502.16793](http://arxiv.org/abs/2502.16793)|null|
|**2025-02-23**|**Subsampling Graphs with GNN Performance Guarantees**|Mika Sarkin Jain et.al.|[2502.16703](http://arxiv.org/abs/2502.16703)|null|
|**2025-02-23**|**Interpretable Retinal Disease Prediction Using Biology-Informed Heterogeneous Graph Representations**|Laurin Lux et.al.|[2502.16697](http://arxiv.org/abs/2502.16697)|**[link](https://github.com/luxtu/OCTA-graph)**|
|**2025-02-23**|**A Survey of Graph Transformers: Architectures, Theories and Applications**|Chaohao Yuan et.al.|[2502.16533](http://arxiv.org/abs/2502.16533)|null|
|**2025-02-23**|**GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking**|Yingjian Chen et.al.|[2502.16514](http://arxiv.org/abs/2502.16514)|null|
|**2025-02-23**|**MAPN: Enhancing Heterogeneous Sparse Graph Representation by Mamba-based Asynchronous Aggregation**|Xuqi Mao et.al.|[2502.16454](http://arxiv.org/abs/2502.16454)|null|
|**2025-02-23**|**Network Tomography with Path-Centric Graph Neural Network**|Yuntong Hu et.al.|[2502.16430](http://arxiv.org/abs/2502.16430)|null|
|**2025-02-21**|**Game State and Spatio-temporal Action Detection in Soccer using Graph Neural Networks and 3D Convolutional Networks**|Jeremie Ochin et.al.|[2502.15462](http://arxiv.org/abs/2502.15462)|null|
|**2025-02-21**|**Drug-Target Interaction/Affinity Prediction: Deep Learning Models and Advances Review**|Ali Vefghi et.al.|[2502.15346](http://arxiv.org/abs/2502.15346)|null|
|**2025-02-21**|**Learning Maritime Inventory Routing Optimization**|Rui Chen et.al.|[2502.15244](http://arxiv.org/abs/2502.15244)|null|
|**2025-02-21**|**GNN-Coder: Boosting Semantic Code Retrieval with Combined GNNs and Transformer**|Yufan Ye et.al.|[2502.15202](http://arxiv.org/abs/2502.15202)|null|
|**2025-02-21**|**Graph-Based Deep Learning on Stereo EEG for Predicting Seizure Freedom in Epilepsy Patients**|Artur Agaronyan et.al.|[2502.15198](http://arxiv.org/abs/2502.15198)|null|
|**2025-02-21**|**Decoding lithium's subtle phase stability with a machine learning force field**|Yiheng Shen et.al.|[2502.15190](http://arxiv.org/abs/2502.15190)|null|
|**2025-02-20**|**GiGL: Large-Scale Graph Neural Networks at Snapchat**|Tong Zhao et.al.|[2502.15054](http://arxiv.org/abs/2502.15054)|null|
|**2025-02-20**|**Benchmarking Android Malware Detection: Rethinking the Role of Traditional and Deep Learning Models**|Guojun Liu et.al.|[2502.15041](http://arxiv.org/abs/2502.15041)|null|
|**2025-02-20**|**Graph in the Vault: Protecting Edge GNN Inference with Trusted Execution Environment**|Ruyi Ding et.al.|[2502.15012](http://arxiv.org/abs/2502.15012)|null|
|**2025-02-20**|**Understanding the Design Principles of Link Prediction in Directed Settings**|Jun Zhai et.al.|[2502.15008](http://arxiv.org/abs/2502.15008)|null|
|**2025-02-20**|**Small Graph Is All You Need: DeepStateGNN for Scalable Traffic Forecasting**|Yannick Wölker et.al.|[2502.14525](http://arxiv.org/abs/2502.14525)|null|
|**2025-02-20**|**DAG: Deep Adaptive and Generative $K$ -Free Community Detection on Attributed Graphs**|Chang Liu et.al.|[2502.14294](http://arxiv.org/abs/2502.14294)|null|
|**2025-02-20**|**Adaptive Sparsified Graph Learning Framework for Vessel Behavior Anomalies**|Jeehong Kim et.al.|[2502.14197](http://arxiv.org/abs/2502.14197)|null|
|**2025-02-19**|**Dual-level Mixup for Graph Few-shot Learning with Fewer Tasks**|Yonghao Liu et.al.|[2502.14158](http://arxiv.org/abs/2502.14158)|**[link](https://github.com/KEAML-JLU/SMILE)**|
|**2025-02-19**|**SALTY: Explainable Artificial Intelligence Guided Structural Analysis for Hardware Trojan Detection**|Tanzim Mahfuz et.al.|[2502.14116](http://arxiv.org/abs/2502.14116)|null|
|**2025-02-20**|**Extending the RANGE of Graph Neural Networks: Relaying Attention Nodes for Global Encoding**|Alessandro Caruso et.al.|[2502.13797](http://arxiv.org/abs/2502.13797)|null|
|**2025-02-19**|**Unsupervised Graph Embeddings for Session-based Recommendation with Item Features**|Andreas Peintner et.al.|[2502.13763](http://arxiv.org/abs/2502.13763)|**[link](https://github.com/dbis-uibk/gcnext)**|
|**2025-02-19**|**Homophily Heterogeneity Matters in Graph Federated Learning: A Spectrum Sharing and Complementing Perspective**|Wentao Yu et.al.|[2502.13732](http://arxiv.org/abs/2502.13732)|null|
|**2025-02-19**|**Towards Invariance to Node Identifiers in Graph Neural Networks**|Maya Bechler-Speicher et.al.|[2502.13660](http://arxiv.org/abs/2502.13660)|null|
|**2025-02-19**|**Non-Euclidean Hierarchical Representational Learning using Hyperbolic Graph Neural Networks for Environmental Claim Detection**|Darpan Aswal et.al.|[2502.13628](http://arxiv.org/abs/2502.13628)|null|
|**2025-02-19**|**Are Large Language Models In-Context Graph Learners?**|Jintang Li et.al.|[2502.13562](http://arxiv.org/abs/2502.13562)|null|
|**2025-02-19**|**Some Insights of Construction of Feature Graph to Learn Pairwise Feature Interactions with Graph Neural Networks**|Phaphontee Yamchote et.al.|[2502.13471](http://arxiv.org/abs/2502.13471)|null|
|**2025-02-18**|**K-Paths: Reasoning over Graph Paths for Drug Repurposing and Drug Interaction Prediction**|Tassallah Abdullahi et.al.|[2502.13344](http://arxiv.org/abs/2502.13344)|**[link](https://github.com/rsinghlab/K-Paths)**|
|**2025-02-18**|**Tuning Algorithmic and Architectural Hyperparameters in Graph-Based Semi-Supervised Learning with Provable Guarantees**|Ally Yalei Du et.al.|[2502.12937](http://arxiv.org/abs/2502.12937)|null|
|**2025-02-19**|**Graph Neural Networks for Databases: A Survey**|Ziming Li et.al.|[2502.12908](http://arxiv.org/abs/2502.12908)|null|
|**2025-02-18**|**NTP-INT: Network Traffic Prediction-Driven In-band Network Telemetry for High-load Switches**|Penghui Zhang et.al.|[2502.12834](http://arxiv.org/abs/2502.12834)|null|
|**2025-02-18**|**Circuit Representation Learning with Masked Gate Modeling and Verilog-AIG Alignment**|Haoyuan Wu et.al.|[2502.12732](http://arxiv.org/abs/2502.12732)|null|
|**2025-02-18**|**Uncertainty-Aware Graph Structure Learning**|Shen Han et.al.|[2502.12618](http://arxiv.org/abs/2502.12618)|**[link](https://github.com/UnHans/UnGSL)**|
|**2025-02-18**|**A Graph-Enhanced Deep-Reinforcement Learning Framework for the Aircraft Landing Problem**|Vatsal Maru et.al.|[2502.12617](http://arxiv.org/abs/2502.12617)|null|
|**2025-02-18**|**Unveiling Mode Connectivity in Graph Neural Networks**|Bingheng Li et.al.|[2502.12608](http://arxiv.org/abs/2502.12608)|null|
|**2025-02-18**|**GVTNet: Graph Vision Transformer For Face Super-Resolution**|Chao Yang et.al.|[2502.12570](http://arxiv.org/abs/2502.12570)|null|
|**2025-02-18**|**Improving the Stability of GNN Force Field Models by Reducing Feature Correlation**|Yujie Zeng et.al.|[2502.12548](http://arxiv.org/abs/2502.12548)|null|
|**2025-02-18**|**USPilot: An Embodied Robotic Assistant Ultrasound System with Large Language Model Enhanced Graph Planner**|Mingcong Chen et.al.|[2502.12498](http://arxiv.org/abs/2502.12498)|null|
|**2025-02-17**|**LaM-SLidE: Latent Space Modeling of Spatial Dynamical Systems via Linked Entities**|Florian Sestak et.al.|[2502.12128](http://arxiv.org/abs/2502.12128)|**[link](https://github.com/ml-jku/lam-slide)**|
|**2025-02-17**|**Data assimilation performed with robust shape registration and graph neural networks: application to aortic coarctation**|Francesco Romor et.al.|[2502.12097](http://arxiv.org/abs/2502.12097)|null|
|**2025-02-17**|**UniGO: A Unified Graph Neural Network for Modeling Opinion Dynamics on Graphs**|Hao Li et.al.|[2502.11519](http://arxiv.org/abs/2502.11519)|null|
|**2025-02-17**|**A GNN-based Spectral Filtering Mechanism for Imbalance Classification in Network Digital Twin**|Abubakar Isah et.al.|[2502.11505](http://arxiv.org/abs/2502.11505)|null|
|**2025-02-17**|**Structure based SAT dataset for analysing GNN generalisation**|Yi Fu et.al.|[2502.11410](http://arxiv.org/abs/2502.11410)|null|
|**2025-02-17**|**Oversmoothing as Loss of Sign: Towards Structural Balance in Graph Neural Networks**|Jiaqi Wang et.al.|[2502.11394](http://arxiv.org/abs/2502.11394)|null|
|**2025-02-17**|**Hierarchical Graph Topic Modeling with Topic Tree-based Transformer**|Delvin Ce Zhang et.al.|[2502.11345](http://arxiv.org/abs/2502.11345)|null|
|**2025-02-16**|**Unlocking the Potential of Generative AI through Neuro-Symbolic Architectures: Benefits and Limitations**|Oualid Bougzime et.al.|[2502.11269](http://arxiv.org/abs/2502.11269)|null|
|**2025-02-16**|**Large Language-Geometry Model: When LLM meets Equivariance**|Zongzhao Li et.al.|[2502.11149](http://arxiv.org/abs/2502.11149)|null|
|**2025-02-16**|**G-Safeguard: A Topology-Guided Security Lens and Treatment on LLM-based Multi-agent Systems**|Shilong Wang et.al.|[2502.11127](http://arxiv.org/abs/2502.11127)|**[link](https://github.com/wslong20/g-safeguard)**|
|**2025-02-14**|**SGS-GNN: A Supervised Graph Sparsification method for Graph Neural Networks**|Siddhartha Shankar Das et.al.|[2502.10208](http://arxiv.org/abs/2502.10208)|**[link](https://github.com/anonymousauthors001/SGS-GNN)**|
|**2025-02-14**|**COMBINEX: A Unified Counterfactual Explainer for Graph Neural Networks via Node Feature and Structural Perturbations**|Flavio Giorgi et.al.|[2502.10111](http://arxiv.org/abs/2502.10111)|null|
|**2025-02-14**|**TransGUNet: Transformer Meets Graph-based Skip Connection for Medical Image Segmentation**|Ju-Hyeon Nam et.al.|[2502.09931](http://arxiv.org/abs/2502.09931)|null|
|**2025-02-14**|**Evaluating and Improving Graph-based Explanation Methods for Multi-Agent Coordination**|Siva Kailas et.al.|[2502.09889](http://arxiv.org/abs/2502.09889)|null|
|**2025-02-13**|**Enhancing the Utility of Higher-Order Information in Relational Learning**|Raphael Pellegrin et.al.|[2502.09570](http://arxiv.org/abs/2502.09570)|**[link](https://github.com/weber-geoml/hypergraph_encodings)**|
|**2025-02-13**|**Machine learning for modelling unstructured grid data in computational physics: a review**|Sibo Cheng et.al.|[2502.09346](http://arxiv.org/abs/2502.09346)|null|
|**2025-02-13**|**Revisiting Topological Interference Management: A Learning-to-Code on Graphs Perspective**|Zhiwei Shan et.al.|[2502.09344](http://arxiv.org/abs/2502.09344)|null|
|**2025-02-13**|**Graph Diffusion Network for Drug-Gene Prediction**|Jiayang Wu et.al.|[2502.09335](http://arxiv.org/abs/2502.09335)|**[link](https://github.com/csjywu1/gdndgp)**|
|**2025-02-14**|**LiSA: Leveraging Link Recommender to Attack Graph Neural Networks via Subgraph Injection**|Wenlun Zhang et.al.|[2502.09271](http://arxiv.org/abs/2502.09271)|**[link](https://github.com/wenlun-zhang/lisa)**|
|**2025-02-13**|**Unlocking the Potential of Classic GNNs for Graph-level Tasks: Simple Architectures Meet Excellence**|Yuankai Luo et.al.|[2502.09263](http://arxiv.org/abs/2502.09263)|**[link](https://github.com/LUOyk1999/tunedGNN-G)**|
|**2025-02-13**|**Self-Supervised Graph Contrastive Pretraining for Device-level Integrated Circuits**|Sungyoung Lee et.al.|[2502.08949](http://arxiv.org/abs/2502.08949)|null|
|**2025-02-12**|**Bridging Domain Adaptation and Graph Neural Networks: A Tensor-Based Framework for Effective Label Propagation**|Tao Wen et.al.|[2502.08505](http://arxiv.org/abs/2502.08505)|null|
|**2025-02-12**|**Trustworthy GNNs with LLMs: A Systematic Review and Taxonomy**|Ruizhan Xue et.al.|[2502.08353](http://arxiv.org/abs/2502.08353)|null|
|**2025-02-12**|**Graph Foundation Models for Recommendation: A Comprehensive Survey**|Bin Wu et.al.|[2502.08346](http://arxiv.org/abs/2502.08346)|null|
|**2025-02-12**|**Data Pricing for Graph Neural Networks without Pre-purchased Inspection**|Yiping Liu et.al.|[2502.08284](http://arxiv.org/abs/2502.08284)|null|
|**2025-02-12**|**Equivariant Masked Position Prediction for Efficient Molecular Representation**|Junyi An et.al.|[2502.08209](http://arxiv.org/abs/2502.08209)|null|
|**2025-02-12**|**MixDec Sampling: A Soft Link-based Sampling Method of Graph Neural Network for Recommendation**|Xiangjin Xie et.al.|[2502.08161](http://arxiv.org/abs/2502.08161)|null|
|**2025-02-12**|**Mixture of Decoupled Message Passing Experts with Entropy Constraint for General Node Classification**|Xuanze Chen et.al.|[2502.08083](http://arxiv.org/abs/2502.08083)|null|
|**2025-02-12**|**Collaborative Filtering Meets Spectrum Shift: Connecting User-Item Interaction with Graph-Structured Side Information**|Yunhang He et.al.|[2502.08071](http://arxiv.org/abs/2502.08071)|null|
|**2025-02-11**|**Learning Effective Dynamics across Spatio-Temporal Scales of Complex Flows**|Han Gao et.al.|[2502.07990](http://arxiv.org/abs/2502.07990)|null|
|**2025-02-11**|**Stereograph: Stereoscopic event reconstruction using graph neural networks applied to CTAO**|Hana Ali Messaoud et.al.|[2502.07421](http://arxiv.org/abs/2502.07421)|null|
|**2025-02-11**|**Effects of Random Edge-Dropping on Over-Squashing in Graph Neural Networks**|Jasraj Singh et.al.|[2502.07364](http://arxiv.org/abs/2502.07364)|null|
|**2025-02-10**|**Neighborhood-Order Learning Graph Attention Network for Fake News Detection**|Batool Lakzaei et.al.|[2502.06927](http://arxiv.org/abs/2502.06927)|**[link](https://github.com/blakzaei/NOL-GAT)**|
|**2025-02-10**|**GraNNite: Enabling High-Performance Execution of Graph Neural Networks on Resource-Constrained Neural Processing Units**|Arghadip Das et.al.|[2502.06921](http://arxiv.org/abs/2502.06921)|**[link](https://github.com/arghadippurdue/GraNNite)**|
|**2025-02-10**|**RelGNN: Composite Message Passing for Relational Deep Learning**|Tianlang Chen et.al.|[2502.06784](http://arxiv.org/abs/2502.06784)|null|
|**2025-02-10**|**Prompt-Driven Continual Graph Learning**|Qi Wang et.al.|[2502.06327](http://arxiv.org/abs/2502.06327)|**[link](https://github.com/QiWang98/PromptCGL)**|
|**2025-02-10**|**IceBerg: Debiased Self-Training for Class-Imbalanced Node Classification**|Zhixun Li et.al.|[2502.06280](http://arxiv.org/abs/2502.06280)|null|
|**2025-02-11**|**Graph Neural Networks at a Fraction**|Rucha Bhalchandra Joshi et.al.|[2502.06136](http://arxiv.org/abs/2502.06136)|null|
|**2025-02-09**|**Norm Augmented Graph AutoEncoders for Link Prediction**|Yunhui Liu et.al.|[2502.05868](http://arxiv.org/abs/2502.05868)|null|
|**2025-02-09**|**Learning Accurate, Efficient, and Interpretable MLPs on Multiplex Graphs via Node-wise Multi-View Ensemble Distillation**|Yunhui Liu et.al.|[2502.05864](http://arxiv.org/abs/2502.05864)|null|
|**2025-02-09**|**LegalSeg: Unlocking the Structure of Indian Legal Judgments Through Rhetorical Role Classification**|Shubham Kumar Nigam et.al.|[2502.05836](http://arxiv.org/abs/2502.05836)|null|
|**2025-02-09**|**GOLD: Graph Out-of-Distribution Detection via Implicit Adversarial Latent Generation**|Danny Wang et.al.|[2502.05780](http://arxiv.org/abs/2502.05780)|null|
|**2025-02-08**|**Rethinking Link Prediction for Directed Graphs**|Mingguo He et.al.|[2502.05724](http://arxiv.org/abs/2502.05724)|null|
|**2025-02-08**|**Graph Neural Networks for Efficient AC Power Flow Prediction in Power Grids**|Seyedamirhossein Talebi et.al.|[2502.05702](http://arxiv.org/abs/2502.05702)|**[link](https://github.com/amirtalebi83/gnn-optimalpowerflow)**|
|**2025-02-07**|**Graph Contrastive Learning for Connectome Classification**|Martín Schmidt et.al.|[2502.05109](http://arxiv.org/abs/2502.05109)|**[link](https://github.com/sara-silvaad/connectome_gcl)**|
|**2025-02-07**|**Robust Graph Learning Against Adversarial Evasion Attacks via Prior-Free Diffusion-Based Structure Purification**|Jiayi Luo et.al.|[2502.05000](http://arxiv.org/abs/2502.05000)|**[link](https://github.com/RingBDStack/DiffSP)**|
|**2025-02-07**|**GNNs Getting ComFy: Community and Feature Similarity Guided Rewiring**|Celia Rubio-Madrigal et.al.|[2502.04891](http://arxiv.org/abs/2502.04891)|**[link](https://github.com/RelationalML/ComFy)**|
|**2025-02-07**|**Graph Federated Learning Based Proactive Content Caching in Edge Computing**|Rui Wang et.al.|[2502.04760](http://arxiv.org/abs/2502.04760)|null|
|**2025-02-07**|**Rethinking Oversmoothing in Graph Neural Networks: A Rank-Based Perspective**|Piero Deidda et.al.|[2502.04591](http://arxiv.org/abs/2502.04591)|null|
|**2025-02-06**|**Learning Semantics-aware Search Operators for Genetic Programming**|Piotr Wyrwiński et.al.|[2502.04568](http://arxiv.org/abs/2502.04568)|null|
|**2025-02-06**|**Provably Robust Explainable Graph Neural Networks against Graph Perturbation Attacks**|Jiate Li et.al.|[2502.04224](http://arxiv.org/abs/2502.04224)|**[link](https://github.com/JetRichardLee/XGNNCert)**|
|**2025-02-06**|**ICGNN: Graph Neural Network Enabled Scalable Beamforming for MISO Interference Channels**|Changpeng He et.al.|[2502.03936](http://arxiv.org/abs/2502.03936)|null|
|**2025-02-06**|**SWIPTNet: A Unified Deep Learning Framework for SWIPT based on GNN and Transfer Learning**|Hong Han et.al.|[2502.03928](http://arxiv.org/abs/2502.03928)|null|
|**2025-02-06**|**Graph Neural Network Enabled Fluid Antenna Systems: A Two-Stage Approach**|Changpeng He et.al.|[2502.03922](http://arxiv.org/abs/2502.03922)|null|
|**2025-02-06**|**Graph Neural Network-Driven Hierarchical Mining for Complex Imbalanced Data**|Yijiashun Qi et.al.|[2502.03803](http://arxiv.org/abs/2502.03803)|null|
|**2025-02-06**|**Network-Wide Traffic Flow Estimation Across Multiple Cities with Global Open Multi-Source Data: A Large-Scale Case Study in Europe and North America**|Zijian Hu et.al.|[2502.03798](http://arxiv.org/abs/2502.03798)|null|
|**2025-02-06**|**On the Expressive Power of Subgraph Graph Neural Networks for Graphs with Bounded Cycles**|Ziang Chen et.al.|[2502.03703](http://arxiv.org/abs/2502.03703)|null|
|**2025-02-05**|**Towards characterizing dark matter subhalo perturbations in stellar streams with graph neural networks**|Peter Xiangyuan Ma et.al.|[2502.03522](http://arxiv.org/abs/2502.03522)|null|
|**2025-02-05**|**Prediction of the Most Fire-Sensitive Point in Building Structures with Differentiable Agents for Thermal Simulators**|Yuan Xinjie et.al.|[2502.03424](http://arxiv.org/abs/2502.03424)|null|
|**2025-02-05**|**RiemannGFM: Learning a Graph Foundation Model from Riemannian Geometry**|Li Sun et.al.|[2502.03251](http://arxiv.org/abs/2502.03251)|null|
|**2025-02-05**|**SpaceGNN: Multi-Space Graph Neural Network for Node Anomaly Detection with Extremely Limited Labels**|Xiangyu Dong et.al.|[2502.03201](http://arxiv.org/abs/2502.03201)|null|
|**2025-02-05**|**Efficient Triangular Arbitrage Detection via Graph Neural Networks**|Di Zhang et.al.|[2502.03194](http://arxiv.org/abs/2502.03194)|null|
|**2025-02-05**|**Optimizing Electric Vehicles Charging using Large Language Models and Graph Neural Networks**|Stavros Orfanoudakis et.al.|[2502.03067](http://arxiv.org/abs/2502.03067)|null|
|**2025-02-05**|**TGB-Seq Benchmark: Challenging Temporal GNNs with Complex Sequential Dynamics**|Lu Yi et.al.|[2502.02975](http://arxiv.org/abs/2502.02975)|**[link](https://github.com/TGB-Seq/TGB-Seq)**|
|**2025-02-04**|**Beyond Topological Self-Explainable GNNs: A Formal Explainability Perspective**|Steve Azzolin et.al.|[2502.02719](http://arxiv.org/abs/2502.02719)|null|
|**2025-02-04**|**scBIT: Integrating Single-cell Transcriptomic Data into fMRI-based Prediction for Alzheimer's Disease Diagnosis**|Yu-An Huang et.al.|[2502.02630](http://arxiv.org/abs/2502.02630)|**[link](https://github.com/77yq77/scbit)**|
|**2025-02-04**|**Graph Structure Learning for Tumor Microenvironment with Cell Type Annotation from non-spatial scRNA-seq data**|Yu-An Huang et.al.|[2502.02629](http://arxiv.org/abs/2502.02629)|**[link](https://github.com/liyuechao1998/scgsl)**|
|**2025-02-04**|**Do Graph Diffusion Models Accurately Capture and Generate Substructure Distributions?**|Xiyuan Wang et.al.|[2502.02488](http://arxiv.org/abs/2502.02488)|null|
|**2025-02-04**|**Using Random Noise Equivariantly to Boost Graph Neural Networks Universally**|Xiyuan Wang et.al.|[2502.02479](http://arxiv.org/abs/2502.02479)|null|
|**2025-02-04**|**Towards graph neural networks for provably solving convex optimization problems**|Chendi Qian et.al.|[2502.02446](http://arxiv.org/abs/2502.02446)|**[link](https://github.com/chendiqian/feasmpnn)**|
|**2025-02-04**|**MAGNNET: Multi-Agent Graph Neural Network-based Efficient Task Allocation for Autonomous Vehicles with Deep Reinforcement Learning**|Lavanya Ratnabala et.al.|[2502.02311](http://arxiv.org/abs/2502.02311)|null|
|**2025-02-04**|**Comparative Analysis of FPGA and GPU Performance for Machine Learning-Based Track Reconstruction at LHCb**|Fotis I. Giasemis et.al.|[2502.02304](http://arxiv.org/abs/2502.02304)|null|
|**2025-02-04**|**EdgeGFL: Rethinking Edge Information in Graph Feature Preference Learning**|Shengda Zhuo et.al.|[2502.02302](http://arxiv.org/abs/2502.02302)|null|
|**2025-02-04**|**Combinatorial Optimization Perspective based Framework for Multi-behavior Recommendation**|Chenhao Zhai et.al.|[2502.02232](http://arxiv.org/abs/2502.02232)|**[link](https://github.com/1918190/copf)**|
|**2025-02-04**|**Graph Neural Networks for O-RAN Mobility Management: A Link Prediction Approach**|Ana Gonzalez Bermudez et.al.|[2502.02170](http://arxiv.org/abs/2502.02170)|null|
|**2025-02-04**|**Query-Based and Unnoticeable Graph Injection Attack from Neighborhood Perspective**|Chang Liu et.al.|[2502.01936](http://arxiv.org/abs/2502.01936)|null|
|**2025-02-03**|**Self-supervised Subgraph Neural Network With Deep Reinforcement Walk Exploration**|Jianming Huang et.al.|[2502.01809](http://arxiv.org/abs/2502.01809)|null|
|**2025-02-03**|**E2Former: A Linear-time Efficient and Equivariant Transformer for Scalable Molecular Modeling**|Yunyang Li et.al.|[2501.19216](http://arxiv.org/abs/2501.19216)|null|
|**2025-01-31**|**RIGNO: A Graph-based framework for robust and accurate operator learning for PDEs on arbitrary domains**|Sepehr Mousavi et.al.|[2501.19205](http://arxiv.org/abs/2501.19205)|**[link](https://github.com/camlab-ethz/rigno)**|
|**2025-01-31**|**Learning Non-Local Molecular Interactions via Equivariant Local Representations and Charge Equilibration**|Paul Fuchs et.al.|[2501.19179](http://arxiv.org/abs/2501.19179)|null|
|**2025-01-31**|**Learning the Hamiltonian Matrix of Large Atomic Systems**|Chen Hao Xia et.al.|[2501.19110](http://arxiv.org/abs/2501.19110)|null|
|**2025-01-31**|**Understanding Oversmoothing in GNNs as Consensus in Opinion Dynamics**|Keqin Wang et.al.|[2501.19089](http://arxiv.org/abs/2501.19089)|null|
|**2025-01-31**|**Optimizing Job Allocation using Reinforcement Learning with Graph Neural Networks**|Lars C. P. M. Quaedvlieg et.al.|[2501.19063](http://arxiv.org/abs/2501.19063)|null|
|**2025-01-31**|**Project-and-Fuse: Improving RGB-D Semantic Segmentation via Graph Convolution Networks**|Xiaoyan Jiang et.al.|[2501.18851](http://arxiv.org/abs/2501.18851)|null|
|**2025-01-30**|**Neural Graph Pattern Machine**|Zehong Wang et.al.|[2501.18739](http://arxiv.org/abs/2501.18739)|null|
|**2025-01-31**|**Node Classification and Search on the Rubik's Cube Graph with GNNs**|Alessandro Barro et.al.|[2501.18580](http://arxiv.org/abs/2501.18580)|null|
|**2025-01-30**|**MolGraph-xLSTM: A graph-based dual-level xLSTM framework with multi-head mixture-of-experts for enhanced molecular representation and interpretability**|Yan Sun et.al.|[2501.18439](http://arxiv.org/abs/2501.18439)|null|
|**2025-01-30**|**A Cartesian Encoding Graph Neural Network for Crystal Structures Property Prediction: Application to Thermal Ellipsoid Estimation**|Àlex Solé et.al.|[2501.18369](http://arxiv.org/abs/2501.18369)|**[link](https://github.com/imatge-upc/CartNet)**|
|**2025-01-30**|**Contrastive Learning Meets Pseudo-label-assisted Mixup Augmentation: A Comprehensive Graph Representation Framework from Local to Global**|Jinlu Wang et.al.|[2501.18357](http://arxiv.org/abs/2501.18357)|null|
|**2025-01-30**|**Mixed-Precision Graph Neural Quantization for Low Bit Large Language Models**|Wanlong Liu et.al.|[2501.18154](http://arxiv.org/abs/2501.18154)|null|
|**2025-01-30**|**ACTGNN: Assessment of Clustering Tendency with Synthetically-Trained Graph Neural Networks**|Yiran Luo et.al.|[2501.18112](http://arxiv.org/abs/2501.18112)|null|
|**2025-01-30**|**Graph Neural Network Flavor Tagger and measurement of $\mathrm{sin}2β$ at Belle II**|Petros Stavroulakis et.al.|[2501.17631](http://arxiv.org/abs/2501.17631)|null|
|**2025-01-29**|**RegionGCN: Spatial-Heterogeneity-Aware Graph Convolutional Networks**|Hao Guo et.al.|[2501.17599](http://arxiv.org/abs/2501.17599)|null|
|**2025-01-29**|**Query-Aware Learnable Graph Pooling Tokens as Prompt for Large Language Models**|Wooyoung Kim et.al.|[2501.17549](http://arxiv.org/abs/2501.17549)|null|
|**2025-01-29**|**Reqo: A Robust and Explainable Query Optimization Cost Model**|Baoming Chang et.al.|[2501.17414](http://arxiv.org/abs/2501.17414)|**[link](https://github.com/baomingchang/reqo-on-postgresql)**|
|**2025-01-29**|**A Geometric Perspective for High-Dimensional Multiplex Graphs**|Kamel Abdous et.al.|[2501.17374](http://arxiv.org/abs/2501.17374)|**[link](https://github.com/abdouskamel/hyper-mge)**|
|**2025-01-29**|**Channel Estimation for XL-MIMO Systems with Decentralized Baseband Processing: Integrating Local Reconstruction with Global Refinement**|Anzheng Tang et.al.|[2501.17059](http://arxiv.org/abs/2501.17059)|null|
|**2025-01-28**|**Few Edges Are Enough: Few-Shot Network Attack Detection with Graph Neural Networks**|Tristan Bilot et.al.|[2501.16964](http://arxiv.org/abs/2501.16964)|null|
|**2025-01-28**|**Exact Computation of Any-Order Shapley Interactions for Graph Neural Networks**|Fabian Fumagalli et.al.|[2501.16944](http://arxiv.org/abs/2501.16944)|null|
|**2025-01-28**|**Dynamic Hypergraph Representation for Bone Metastasis Cancer Analysis**|Yuxuan Chen et.al.|[2501.16787](http://arxiv.org/abs/2501.16787)|null|
|**2025-01-28**|**Hypergraph Diffusion for High-Order Recommender Systems**|Darnbi Sakong et.al.|[2501.16722](http://arxiv.org/abs/2501.16722)|null|
|**2025-01-28**|**Data Mining in Transportation Networks with Graph Neural Networks: A Review and Outlook**|Jiawei Xue et.al.|[2501.16656](http://arxiv.org/abs/2501.16656)|null|
|**2025-01-28**|**Applying Ensemble Models based on Graph Neural Network and Reinforcement Learning for Wind Power Forecasting**|Hongjin Song et.al.|[2501.16591](http://arxiv.org/abs/2501.16591)|null|
|**2025-01-27**|**Evaluating the Impact of Detector Design on Jet Flavor Tagging for Future Colliders**|Dimitrios Ntounis et.al.|[2501.16584](http://arxiv.org/abs/2501.16584)|**[link](https://github.com/dntounis/jet-flavor-tagging-ee)**|
|**2025-01-27**|**Graph Neural Network Based Hybrid Beamforming Design in Wideband Terahertz MIMO-OFDM Systems**|Beier Li et.al.|[2501.16306](http://arxiv.org/abs/2501.16306)|null|
|**2025-01-27**|**From Molecules to Mixtures: Learning Representations of Olfactory Mixture Similarity using Inductive Biases**|Gary Tom et.al.|[2501.16271](http://arxiv.org/abs/2501.16271)|null|
|**2025-01-27**|**ReFill: Reinforcement Learning for Fill-In Minimization**|Elfarouk Harb et.al.|[2501.16130](http://arxiv.org/abs/2501.16130)|**[link](https://github.com/FaroukY/FillInMinimization)**|
|**2025-01-27**|**ScaDyG:A New Paradigm for Large-scale Dynamic Graph Learning**|Xiang Wu et.al.|[2501.16002](http://arxiv.org/abs/2501.16002)|null|
|**2025-01-27**|**Multi-View Attention Syntactic Enhanced Graph Convolutional Network for Aspect-based Sentiment Analysis**|Xiang Huang et.al.|[2501.15968](http://arxiv.org/abs/2501.15968)|**[link](https://github.com/selgroup/masgcn)**|
|**2025-01-27**|**Adaptive AI-based Decentralized Resource Management in the Cloud-Edge Continuum**|Lanpei Li et.al.|[2501.15802](http://arxiv.org/abs/2501.15802)|null|
|**2025-01-27**|**GraphICL: Unlocking Graph Learning Potential in LLMs through Structured Prompt Design**|Yuanfu Sun et.al.|[2501.15755](http://arxiv.org/abs/2501.15755)|null|
|**2025-01-26**|**Distributionally Robust Graph Out-of-Distribution Recommendation via Diffusion Model**|Chu Zhao et.al.|[2501.15555](http://arxiv.org/abs/2501.15555)|**[link](https://github.com/user683/DRGO)**|
|**2025-01-26**|**Mamba-Based Graph Convolutional Networks: Tackling Over-smoothing with Selective State Space**|Xin He et.al.|[2501.15461](http://arxiv.org/abs/2501.15461)|null|
|**2025-01-26**|**An Aspect Performance-aware Hypergraph Neural Network for Review-based Recommendation**|Junrui Liu et.al.|[2501.15429](http://arxiv.org/abs/2501.15429)|**[link](https://github.com/dianziliu/aph)**|
|**2025-01-24**|**An Attentive Graph Agent for Topology-Adaptive Cyber Defence**|Ilya Orson Sandoval et.al.|[2501.14700](http://arxiv.org/abs/2501.14700)|**[link](https://github.com/ilyaorson/cyberdreamcatcher)**|
|**2025-01-24**|**On the Homophily of Heterogeneous Graphs: Understanding and Unleashing**|Zhen Tao et.al.|[2501.14600](http://arxiv.org/abs/2501.14600)|null|
|**2025-01-24**|**Convergence of gradient based training for linear Graph Neural Networks**|Dhiraj Patel et.al.|[2501.14440](http://arxiv.org/abs/2501.14440)|null|
|**2025-01-24**|**Efficiently charting the space of mixed vacancy-ordered perovskites by machine-learning encoded atomic-site information**|Fan Zhang et.al.|[2501.14384](http://arxiv.org/abs/2501.14384)|null|
|**2025-01-24**|**Adaptive Progressive Attention Graph Neural Network for EEG Emotion Recognition**|Tianzhi Feng et.al.|[2501.14246](http://arxiv.org/abs/2501.14246)|null|
|**2025-01-24**|**Top Ten Challenges Towards Agentic Neural Graph Databases**|Jiaxin Bai et.al.|[2501.14224](http://arxiv.org/abs/2501.14224)|null|
|**2025-01-24**|**Tensor-Based Binary Graph Encoding for Variational Quantum Classifiers**|Shiwen An et.al.|[2501.14185](http://arxiv.org/abs/2501.14185)|null|
|**2025-01-23**|**Crossfire: An Elastic Defense Framework for Graph Neural Networks Under Bit Flip Attacks**|Lorenz Kummer et.al.|[2501.13776](http://arxiv.org/abs/2501.13776)|**[link](https://github.com/lorenz0890/crossfireaaai2025)**|
|**2025-01-23**|**Sample complexity of data-driven tuning of model hyperparameters in neural networks with structured parameter-dependent dual function**|Maria-Florina Balcan et.al.|[2501.13734](http://arxiv.org/abs/2501.13734)|null|
|**2025-01-23**|**The Road to Learning Explainable Inverse Kinematic Models: Graph Neural Networks as Inductive Bias for Symbolic Regression**|Pravin Pandey et.al.|[2501.13641](http://arxiv.org/abs/2501.13641)|null|
|**2025-01-23**|**VARFVV: View-Adaptive Real-Time Interactive Free-View Video Streaming with Edge Computing**|Qiang Hu et.al.|[2501.13630](http://arxiv.org/abs/2501.13630)|null|
|**2025-01-23**|**GCAD: Anomaly Detection in Multivariate Time Series from the Perspective of Granger Causality**|Zehao Liu et.al.|[2501.13493](http://arxiv.org/abs/2501.13493)|null|
|**2025-01-23**|**KAA: Kolmogorov-Arnold Attention for Enhancing Attentive Graph Neural Networks**|Taoran Fang et.al.|[2501.13456](http://arxiv.org/abs/2501.13456)|**[link](https://github.com/luckytiger123/kaa)**|
|**2025-01-22**|**HierPromptLM: A Pure PLM-based Framework for Representation Learning on Heterogeneous Text-rich Networks**|Qiuyu Zhu et.al.|[2501.12857](http://arxiv.org/abs/2501.12857)|null|
|**2025-01-22**|**GRAMA: Adaptive Graph Autoregressive Moving Average Models**|Moshe Eliasof et.al.|[2501.12732](http://arxiv.org/abs/2501.12732)|null|
|**2025-01-22**|**A Unified Invariant Learning Framework for Graph Classification**|Yongduo Sui et.al.|[2501.12595](http://arxiv.org/abs/2501.12595)|**[link](https://github.com/yongduosui/uil)**|
|**2025-01-23**|**FedGrAINS: Personalized SubGraph Federated Learning with Adaptive Neighbor Sampling**|Emir Ceyani et.al.|[2501.12592](http://arxiv.org/abs/2501.12592)|null|
|**2025-01-21**|**SafePowerGraph-HIL: Real-Time HIL Validation of Heterogeneous GNNs for Bridging Sim-to-Real Gap in Power Grids**|Aoxiang Ma et.al.|[2501.12427](http://arxiv.org/abs/2501.12427)|null|
|**2025-01-21**|**A Hybrid Supervised and Self-Supervised Graph Neural Network for Edge-Centric Applications**|Eugenio Borzone et.al.|[2501.12309](http://arxiv.org/abs/2501.12309)|null|
|**2025-01-21**|**SVGS-DSGAT: An IoT-Enabled Innovation in Underwater Robotic Object Detection Technology**|Dongli Wu et.al.|[2501.12169](http://arxiv.org/abs/2501.12169)|null|
|**2025-01-21**|**Coarse-to-Fine Lightweight Meta-Embedding for ID-Based Recommendation**|Yang Wang et.al.|[2501.11870](http://arxiv.org/abs/2501.11870)|**[link](https://github.com/htyjers/c2f-metaembed)**|
|**2025-01-20**|**Leveraging graph neural networks and mobility data for COVID-19 forecasting**|Fernando H. O. Duarte et.al.|[2501.11711](http://arxiv.org/abs/2501.11711)|**[link](https://github.com/hodfernando/2024_asoc_gnn_covid19_forecast)**|
|**2025-01-20**|**Graph Defense Diffusion Model**|Xin He et.al.|[2501.11568](http://arxiv.org/abs/2501.11568)|null|
|**2025-01-20**|**Advancing Multi-Party Dialogue Systems with Speaker-ware Contrastive Learning**|Zhongtian Hu et.al.|[2501.11292](http://arxiv.org/abs/2501.11292)|null|
|**2025-01-20**|**Spatiotemporal Air Quality Mapping in Urban Areas Using Sparse Sensor Data, Satellite Imagery, Meteorological Factors, and Spatial Features**|Osama Ahmad et.al.|[2501.11270](http://arxiv.org/abs/2501.11270)|null|
|**2025-01-20**|**Fast instance-specific algorithm configuration with graph neural network**|Shingo Aihara et.al.|[2501.11240](http://arxiv.org/abs/2501.11240)|null|
|**2025-01-20**|**Mitigating Spatial Disparity in Urban Prediction Using Residual-Aware Spatiotemporal Graph Neural Networks: A Chicago Case Study**|Dingyi Zhuang et.al.|[2501.11214](http://arxiv.org/abs/2501.11214)|null|
|**2025-01-19**|**Achieving Network Resilience through Graph Neural Network-enabled Deep Reinforcement Learning**|Xuzeng Li et.al.|[2501.11074](http://arxiv.org/abs/2501.11074)|null|
|**2025-01-17**|**Few-shot Structure-Informed Machinery Part Segmentation with Foundation Models and Graph Neural Networks**|Michael Schwingshackl et.al.|[2501.10080](http://arxiv.org/abs/2501.10080)|**[link](https://github.com/ait-assistive-autonomous-systems/hopomop)**|
|**2025-01-17**|**Virtual Nodes Improve Long-term Traffic Prediction**|Xiaoyang Cao et.al.|[2501.10048](http://arxiv.org/abs/2501.10048)|null|
|**2025-01-17**|**Study on a Fast Solver for Combined Field Integral Equations of 3D Conducting Bodies Based on Graph Neural Networks**|Tao Shan et.al.|[2501.09923](http://arxiv.org/abs/2501.09923)|**[link](https://github.com/iemcs-lab/gnnsolver-cfie)**|
|**2025-01-16**|**BN-Pool: a Bayesian Nonparametric Approach to Graph Pooling**|Daniele Castellana et.al.|[2501.09821](http://arxiv.org/abs/2501.09821)|**[link](https://github.com/ngmlgroup/bayesian-nonparametric-graph-pooling)**|
|**2025-01-16**|**Graph Neural Networks for Travel Distance Estimation and Route Recommendation Under Probabilistic Hazards**|Tong Liu et.al.|[2501.09803](http://arxiv.org/abs/2501.09803)|null|
|**2025-01-16**|**Fast Searching of Extreme Operating Conditions for Relay Protection Setting Calculation Based on Graph Neural Network and Reinforcement Learning**|Yan Li et.al.|[2501.09399](http://arxiv.org/abs/2501.09399)|null|
|**2025-01-16**|**First Experiments with Neural cvc5**|Jelle Piepenbrock et.al.|[2501.09379](http://arxiv.org/abs/2501.09379)|**[link](https://github.com/jellepiepenbrock/mlcvc5-lpar)**|
|**2025-01-15**|**Enhancing Graph Representation Learning with Localized Topological Features**|Zuoyu Yan et.al.|[2501.09178](http://arxiv.org/abs/2501.09178)|**[link](https://github.com/pkuyzy/TLC-GNN)**|
|**2025-01-15**|**Multi-Class Traffic Assignment using Multi-View Heterogeneous Graph Attention Networks**|Tong Liu et.al.|[2501.09117](http://arxiv.org/abs/2501.09117)|null|
|**2025-01-15**|**Similarity-Quantized Relative Difference Learning for Improved Molecular Activity Prediction**|Karina Zadorozhny et.al.|[2501.09103](http://arxiv.org/abs/2501.09103)|null|
|**2025-01-15**|**CrystalGRW: Generative Modeling of Crystal Structures with Targeted Properties via Geodesic Random Walks**|Krit Tangsongcharoen et.al.|[2501.08998](http://arxiv.org/abs/2501.08998)|**[link](https://github.com/trachote/crystalgrw)**|
|**2025-01-15**|**Joint Detection and Decoding: A Graph Neural Network Approach**|Jannis Clausius et.al.|[2501.08871](http://arxiv.org/abs/2501.08871)|null|
|**2025-01-15**|**MeshMask: Physics-Based Simulations with Masked Graph Neural Networks**|Paul Garnier et.al.|[2501.08738](http://arxiv.org/abs/2501.08738)|null|
|**2025-01-15**|**GRAPPA -- A Hybrid Graph Neural Network for Predicting Pure Component Vapor Pressures**|Marco Hoffmann et.al.|[2501.08729](http://arxiv.org/abs/2501.08729)|**[link](https://github.com/marco-hoffmann/grappa)**|
|**2025-01-15**|**Normalize Then Propagate: Efficient Homophilous Regularization for Few-shot Semi-Supervised Node Classification**|Baoming Zhang et.al.|[2501.08581](http://arxiv.org/abs/2501.08581)|**[link](https://github.com/pallaksch/normprop)**|
|**2025-01-15**|**OMEGA: A Low-Latency GNN Serving System for Large Graphs**|Geon-Woo Kim et.al.|[2501.08547](http://arxiv.org/abs/2501.08547)|null|
|**2025-01-14**|**Predict Confidently, Predict Right: Abstention in Dynamic Graph Learning**|Jayadratha Gayen et.al.|[2501.08397](http://arxiv.org/abs/2501.08397)|null|
|**2025-01-14**|**Benchmarking Graph Representations and Graph Neural Networks for Multivariate Time Series Classification**|Wennuo Yang et.al.|[2501.08305](http://arxiv.org/abs/2501.08305)|**[link](https://github.com/cvi-yangwn/benchmark-gnn-for-multivariate-time-series-classification)**|
|**2025-01-14**|**Combining imaging and shape features for prediction tasks of Alzheimer's disease classification and brain age regression**|Nairouz Shehata et.al.|[2501.07994](http://arxiv.org/abs/2501.07994)|null|
|**2025-01-14**|**QGHNN: A quantum graph Hamiltonian neural network**|Wenxuan Wang et.al.|[2501.07986](http://arxiv.org/abs/2501.07986)|null|
|**2025-01-13**|**A Heterogeneous Multimodal Graph Learning Framework for Recognizing User Emotions in Social Networks**|Sree Bhattacharyya et.al.|[2501.07746](http://arxiv.org/abs/2501.07746)|null|
|**2025-01-13**|**SafePowerGraph-LLM: Novel Power Grid Graph Embedding and Optimization with Large Language Models**|Fabien Bernier et.al.|[2501.07639](http://arxiv.org/abs/2501.07639)|null|
|**2025-01-13**|**Advancing Higgsino Searches by Integrating ML for Boosted Object Tagging and Event Selection**|Rameswar Sahu et.al.|[2501.07491](http://arxiv.org/abs/2501.07491)|null|
|**2025-01-13**|**Dynami-CAL GraphNet: A Physics-Informed Graph Neural Network Conserving Linear and Angular Momentum for Dynamical Systems**|Vinay Sharma et.al.|[2501.07373](http://arxiv.org/abs/2501.07373)|null|
|**2025-01-13**|**Generalizable Graph Neural Networks for Robust Power Grid Topology Control**|Matthijs de Jong et.al.|[2501.07186](http://arxiv.org/abs/2501.07186)|**[link](https://github.com/matthijsdej/gnn_pn_imitation_learning)**|
|**2025-01-13**|**Duplex: Dual Prototype Learning for Compositional Zero-Shot Learning**|Zhong Peng et.al.|[2501.07114](http://arxiv.org/abs/2501.07114)|null|
|**2025-01-13**|**Graph Contrastive Learning on Multi-label Classification for Recommendations**|Jiayang Wu et.al.|[2501.06985](http://arxiv.org/abs/2501.06985)|null|
|**2025-01-11**|**Dual-Modality Representation Learning for Molecular Property Prediction**|Anyin Zhao et.al.|[2501.06608](http://arxiv.org/abs/2501.06608)|null|
|**2025-01-11**|**On the Computational Capability of Graph Neural Networks: A Circuit Complexity Bound Perspective**|Xiaoyu Li et.al.|[2501.06444](http://arxiv.org/abs/2501.06444)|null|
|**2025-01-10**|**Efficient Transition State Searches by Freezing String Method with Graph Neural Network Potentials**|Jonah Marks et.al.|[2501.06159](http://arxiv.org/abs/2501.06159)|null|
|**2025-01-10**|**DeltaGNN: Graph Neural Network with Information Flow Control**|Kevin Mancini et.al.|[2501.06002](http://arxiv.org/abs/2501.06002)|**[link](https://github.com/basiralab/deltagnn)**|
|**2025-01-10**|**Annealing Machine-assisted Learning of Graph Neural Network for Combinatorial Optimization**|Pablo Loyola et.al.|[2501.05845](http://arxiv.org/abs/2501.05845)|null|
|**2025-01-10**|**Fine-tuning is Not Fine: Mitigating Backdoor Attacks in GNNs with Limited Clean Data**|Jiale Zhang et.al.|[2501.05835](http://arxiv.org/abs/2501.05835)|null|
|**2025-01-10**|**TransPlace: Transferable Circuit Global Placement via Graph Neural Network**|Yunbo Hou et.al.|[2501.05667](http://arxiv.org/abs/2501.05667)|**[link](https://github.com/sorarain/transplace)**|
|**2025-01-10**|**Scaling Safe Multi-Agent Control for Signal Temporal Logic Specifications**|Joe Eappen et.al.|[2501.05639](http://arxiv.org/abs/2501.05639)|**[link](https://github.com/jeappen/mastl-gcbf)**|
|**2025-01-09**|**Watermarking Graph Neural Networks via Explanations for Ownership Protection**|Jane Downer et.al.|[2501.05614](http://arxiv.org/abs/2501.05614)|null|
|**2025-01-09**|**Quantum Simplicial Neural Networks**|Simone Piperno et.al.|[2501.05558](http://arxiv.org/abs/2501.05558)|null|
|**2025-01-09**|**Discovery of Spin-Crossover Candidates with Equivariant Graph Neural Networks**|Angel Albavera-Mata et.al.|[2501.05341](http://arxiv.org/abs/2501.05341)|null|
|**2025-01-09**|**Vision Graph Non-Contrastive Learning for Audio Deepfake Detection with Limited Labels**|Falih Gozi Febrinanto et.al.|[2501.04942](http://arxiv.org/abs/2501.04942)|null|
|**2025-01-08**|**Intelligent experiments through real-time AI: Fast Data Processing and Autonomous Detector Control for sPHENIX and future EIC detectors**|J. Kvapil et.al.|[2501.04845](http://arxiv.org/abs/2501.04845)|null|
|**2025-01-08**|**Large-Scale Spectral Graph Neural Networks via Laplacian Sparsification: Technical Report**|Haipeng Ding et.al.|[2501.04570](http://arxiv.org/abs/2501.04570)|null|
|**2025-01-09**|**Dynamic Localisation of Spatial-Temporal Graph Neural Network**|Wenying Duan et.al.|[2501.04239](http://arxiv.org/abs/2501.04239)|null|
|**2025-01-07**|**GraphNeT 2.0 -- A Deep Learning Library for Neutrino Telescopes**|Rasmus F. Ørsøe et.al.|[2501.03817](http://arxiv.org/abs/2501.03817)|null|
|**2025-01-07**|**Image Segmentation: Inducing graph-based learning**|Aryan Singh et.al.|[2501.03765](http://arxiv.org/abs/2501.03765)|**[link](https://github.com/aryan-at-ul/electronic-imaging-2025-paper-4492)**|
|**2025-01-07**|**Exploring Molecule Generation Using Latent Space Graph Diffusion**|Prashanth Pombala et.al.|[2501.03696](http://arxiv.org/abs/2501.03696)|**[link](https://github.com/prashanth-pombala/molecule-generation-using-latent-space-graph-diffusion)**|
|**2025-01-07**|**MHGNet: Multi-Heterogeneous Graph Neural Network for Traffic Prediction**|Mei Wu et.al.|[2501.03635](http://arxiv.org/abs/2501.03635)|**[link](https://github.com/meiwu5/mhgnet)**|
|**2025-01-07**|**Deep Learning for Pathological Speech: A Survey**|Shakeel A. Sheikh et.al.|[2501.03536](http://arxiv.org/abs/2501.03536)|null|
|**2025-01-07**|**LHGNN: Local-Higher Order Graph Neural Networks For Audio Classification and Tagging**|Shubhr Singh et.al.|[2501.03464](http://arxiv.org/abs/2501.03464)|null|
|**2025-01-07**|**Structure-Preference Enabled Graph Embedding Generation under Differential Privacy**|Sen Zhang et.al.|[2501.03451](http://arxiv.org/abs/2501.03451)|**[link](https://github.com/sunnerzs/seprivgemb)**|
|**2025-01-08**|**Mixture-of-Experts Graph Transformers for Interpretable Particle Collision Detection**|Donatella Genovese et.al.|[2501.03432](http://arxiv.org/abs/2501.03432)|null|
|**2025-01-07**|**LightGNN: Simple Graph Neural Network for Recommendation**|Guoxuan Chen et.al.|[2501.03228](http://arxiv.org/abs/2501.03228)|**[link](https://github.com/hkuds/lightgnn)**|
|**2025-01-06**|**Balancing Efficiency and Expressiveness: Subgraph GNNs with Walk-Based Centrality**|Joshua Southern et.al.|[2501.03113](http://arxiv.org/abs/2501.03113)|**[link](https://github.com/jks17/hymn)**|
|**2025-01-06**|**CONTINUUM: Detecting APT Attacks through Spatial-Temporal Graph Neural Networks**|Atmane Ayoub Mansour Bahara et.al.|[2501.02981](http://arxiv.org/abs/2501.02981)|null|
|**2025-01-06**|**LOHA: Direct Graph Spectral Contrastive Learning Between Low-pass and High-pass Views**|Ziyun Zou et.al.|[2501.02969](http://arxiv.org/abs/2501.02969)|null|
|**2025-01-06**|**DarkFarseer: Inductive Spatio-temporal Kriging via Hidden Style Enhancement and Sparsity-Noise Mitigation**|Zhuoxuan Liang et.al.|[2501.02808](http://arxiv.org/abs/2501.02808)|null|
|**2025-01-06**|**GraphDART: Graph Distillation for Efficient Advanced Persistent Threat Detection**|Saba Fathi Rabooki et.al.|[2501.02796](http://arxiv.org/abs/2501.02796)|null|
|**2025-01-06**|**Enhancing Trustworthiness of Graph Neural Networks with Rank-Based Conformal Training**|Ting Wang et.al.|[2501.02767](http://arxiv.org/abs/2501.02767)|**[link](https://github.com/cityu-t/rcp-gnn)**|
|**2025-01-06**|**Are GNNs Effective for Multimodal Fault Diagnosis in Microservice Systems?**|Fei Gao et.al.|[2501.02766](http://arxiv.org/abs/2501.02766)|null|
|**2025-01-06**|**Enhancing Robot Route Optimization in Smart Logistics with Transformer and GNN Integration**|Hao Luo et.al.|[2501.02749](http://arxiv.org/abs/2501.02749)|null|
|**2025-01-06**|**OpenGU: A Comprehensive Benchmark for Graph Unlearning**|Bowen Fan et.al.|[2501.02728](http://arxiv.org/abs/2501.02728)|**[link](https://github.com/bwfan-bit/opengu)**|
|**2025-01-03**|**A Probabilistic Model for Node Classification in Directed Graphs**|Diego Huerta et.al.|[2501.01630](http://arxiv.org/abs/2501.01630)|**[link](https://github.com/diegohuerta1/a-probabilistic-model-for-node-classification-in-directed-graphs)**|
|**2025-01-02**|**HetGCoT-Rec: Heterogeneous Graph-Enhanced Chain-of-Thought LLM Reasoning for Journal Recommendation**|Runsong Jia et.al.|[2501.01203](http://arxiv.org/abs/2501.01203)|null|
|**2025-01-01**|**Revisiting Graph Neural Networks on Graph-level Tasks: Comprehensive Experiments, Analysis, and Improvements**|Haoyang Li et.al.|[2501.00773](http://arxiv.org/abs/2501.00773)|null|
|**2025-01-01**|**Avoiding Oversmoothing in Deep Graph Neural Networks: A Multiplicative Ergodic Analysis**|Ziang Chen et.al.|[2501.00762](http://arxiv.org/abs/2501.00762)|null|
|**2025-01-01**|**AttriReBoost: A Gradient-Free Propagation Optimization Method for Cold Start Mitigation in Attribute Missing Graphs**|Mengran Li et.al.|[2501.00743](http://arxiv.org/abs/2501.00743)|**[link](https://github.com/limengran98/arb)**|
|**2025-01-01**|**KAN KAN Buff Signed Graph Neural Networks?**|Muhieddine Shebaro et.al.|[2501.00709](http://arxiv.org/abs/2501.00709)|null|
|**2024-12-31**|**Hierarchical equivariant graph neural networks for forecasting collective motion in vortex clusters and microswimmers**|Alec J. Linot et.al.|[2501.00626](http://arxiv.org/abs/2501.00626)|null|
|**2024-12-31**|**Unbiased GNN Learning via Fairness-Aware Subgraph Diffusion**|Abdullah Alchihabi et.al.|[2501.00595](http://arxiv.org/abs/2501.00595)|null|
|**2024-12-30**|**Exploring DHCAL design and performance with Graph Neural Networks**|M. Borysova et.al.|[2501.00128](http://arxiv.org/abs/2501.00128)|null|
|**2025-01-03**|**Conservation-informed Graph Learning for Spatiotemporal Dynamics Prediction**|Yuan Mi et.al.|[2412.20962](http://arxiv.org/abs/2412.20962)|null|
|**2024-12-30**|**FastCHGNet: Training one Universal Interatomic Potential to 1.5 Hours with 32 GPUs**|Yuanchang Zhou et.al.|[2412.20796](http://arxiv.org/abs/2412.20796)|null|
|**2024-12-30**|**Overcoming Class Imbalance: Unified GNN Learning with Structural and Semantic Connectivity Representations**|Abdullah Alchihabi et.al.|[2412.20656](http://arxiv.org/abs/2412.20656)|null|
|**2024-12-30**|**Graph Neural Networks for Next-Generation-IoT: Recent Advances and Open Challenges**|Nguyen Xuan Tung et.al.|[2412.20634](http://arxiv.org/abs/2412.20634)|null|
|**2024-12-29**|**NeutronTP: Load-Balanced Distributed Full-Graph GNN Training with Tensor Parallelism**|Xin Ai et.al.|[2412.20379](http://arxiv.org/abs/2412.20379)|null|
|**2024-12-28**|**Towards Ideal Temporal Graph Neural Networks: Evaluations and Conclusions after 10,000 GPU Hours**|Yuxin Yang et.al.|[2412.20256](http://arxiv.org/abs/2412.20256)|null|
|**2024-12-28**|**Discrete Curvature Graph Information Bottleneck**|Xingcheng Fu et.al.|[2412.19993](http://arxiv.org/abs/2412.19993)|null|
|**2024-12-27**|**ViDTA: Enhanced Drug-Target Affinity Prediction via Virtual Graph Nodes and Attention-based Feature Fusion**|Minghui Li et.al.|[2412.19589](http://arxiv.org/abs/2412.19589)|null|
|**2024-12-27**|**Introduction to Graph Neural Networks: A Starting Point for Machine Learning Engineers**|James H. Tanis et.al.|[2412.19419](http://arxiv.org/abs/2412.19419)|null|
|**2025-01-01**|**RecLM: Recommendation Instruction Tuning**|Yangqin Jiang et.al.|[2412.19302](http://arxiv.org/abs/2412.19302)|**[link](https://github.com/hkuds/reclm)**|
|**2024-12-26**|**Virtual Nodes Can Help: Tackling Distribution Shifts in Federated Graph Learning**|Xingbo Fu et.al.|[2412.19229](http://arxiv.org/abs/2412.19229)|**[link](https://github.com/xbfu/FedVN)**|
|**2024-12-26**|**Large Language Models Meet Graph Neural Networks: A Perspective of Graph Mining**|Yuxin You et.al.|[2412.19211](http://arxiv.org/abs/2412.19211)|null|
|**2024-12-26**|**ERGNN: Spectral Graph Neural Network with Explicitly-optimized Rational Graph Filters**|Guoming Li et.al.|[2412.19106](http://arxiv.org/abs/2412.19106)|null|
|**2024-12-25**|**Adversarial Training for Graph Neural Networks via Graph Subspace Energy Optimization**|Ganlin Liu et.al.|[2412.18886](http://arxiv.org/abs/2412.18886)|null|
|**2024-12-25**|**Enhancing Federated Graph Learning via Adaptive Fusion of Structural and Node Characteristics**|Xianjun Gao et.al.|[2412.18845](http://arxiv.org/abs/2412.18845)|null|
|**2024-12-25**|**Hierarchical Multi-Graphs Learning for Robust Group Re-Identification**|Ruiqi Liu et.al.|[2412.18766](http://arxiv.org/abs/2412.18766)|null|
|**2024-12-25**|**Predicting Time Series of Networked Dynamical Systems without Knowing Topology**|Yanna Ding et.al.|[2412.18734](http://arxiv.org/abs/2412.18734)|**[link](https://github.com/dingyanna/LatentTopoDynamics)**|
|**2024-12-24**|**Unveiling the Threat of Fraud Gangs to Graph Neural Networks: Multi-Target Graph Injection Attacks against GNN-Based Fraud Detectors**|Jinhyeok Choi et.al.|[2412.18370](http://arxiv.org/abs/2412.18370)|**[link](https://github.com/bdi-lab/monti)**|
|**2024-12-24**|**Semi-supervised Credit Card Fraud Detection via Attribute-Driven Graph Representation**|Sheng Xiang et.al.|[2412.18287](http://arxiv.org/abs/2412.18287)|**[link](https://github.com/ai4risk/antifraud)**|
|**2024-12-24**|**NoiseHGNN: Synthesized Similarity Graph-Based Neural Network For Noised Heterogeneous Graph Representation Learning**|Xiong Zhang et.al.|[2412.18267](http://arxiv.org/abs/2412.18267)|**[link](https://github.com/kg-cc/noisehgnn)**|
|**2024-12-24**|**Free the Design Space of Equivariant Graph Neural Networks: High-Rank Irreducible Cartesian Tensor Decomposition and Bases of Equivariant Spaces**|Shihao Shao et.al.|[2412.18263](http://arxiv.org/abs/2412.18263)|**[link](https://github.com/shihaoshao-gh/ict-decomposition-and-equivariant-bases)**|
|**2024-12-24**|**An Automatic Graph Construction Framework based on Large Language Models for Recommendation**|Rong Shan et.al.|[2412.18241](http://arxiv.org/abs/2412.18241)|**[link](https://github.com/lavieenrose365/autograph)**|
|**2024-12-24**|**GIMS: Image Matching System Based on Adaptive Graph Construction and Graph Neural Network**|Xianfeng Song et.al.|[2412.18221](http://arxiv.org/abs/2412.18221)|**[link](https://github.com/songxf1024/gims)**|
|**2024-12-24**|**Exact Acceleration of Subgraph Graph Neural Networks by Eliminating Computation Redundancy**|Qian Tao et.al.|[2412.18125](http://arxiv.org/abs/2412.18125)|null|
|**2024-12-23**|**Extending Graph Condensation to Multi-Label Datasets: A Benchmark Study**|Liangliang Zhang et.al.|[2412.17961](http://arxiv.org/abs/2412.17961)|null|
|**2024-12-23**|**LASE: Learned Adjacency Spectral Embeddings**|Sofía Pérez Casulo et.al.|[2412.17734](http://arxiv.org/abs/2412.17734)|**[link](https://github.com/sofiperez91/lase)**|
|**2024-12-24**|**Graph Neural Networks Are Evolutionary Algorithms**|Kaichen Ouyang et.al.|[2412.17629](http://arxiv.org/abs/2412.17629)|null|
|**2024-12-23**|**Towards Foundation Models on Graphs: An Analysis on Cross-Dataset Transfer of Pretrained GNNs**|Fabrizio Frasca et.al.|[2412.17609](http://arxiv.org/abs/2412.17609)|null|
|**2024-12-23**|**Graph Size-imbalanced Learning with Energy-guided Structural Smoothing**|Jiawen Qin et.al.|[2412.17591](http://arxiv.org/abs/2412.17591)|null|
|**2024-12-23**|**Line Graph Vietoris-Rips Persistence Diagram for Topological Graph Representation Learning**|Jaesun Shin et.al.|[2412.17468](http://arxiv.org/abs/2412.17468)|**[link](https://github.com/samsungsds-research-papers/lgvr)**|
|**2024-12-23**|**BrainMAP: Learning Multiple Activation Pathways in Brain Networks**|Song Wang et.al.|[2412.17404](http://arxiv.org/abs/2412.17404)|**[link](https://github.com/lzyfischer/brainmap)**|
|**2024-12-23**|**ORIGAMI: A generative transformer architecture for predictions from semi-structured data**|Thomas Rückstieß et.al.|[2412.17348](http://arxiv.org/abs/2412.17348)|null|
|**2024-12-23**|**Rethinking Cancer Gene Identification through Graph Anomaly Analysis**|Yilong Zang et.al.|[2412.17240](http://arxiv.org/abs/2412.17240)|**[link](https://github.com/zyl199710/hipgnn)**|
|**2024-12-22**|**Distributed Cooperative Positioning in Dense Wireless Networks: A Neural Network Enhanced Fast Convergent Parametric Message Passing Method**|Yue Cao et.al.|[2412.16996](http://arxiv.org/abs/2412.16996)|null|
|**2024-12-22**|**Graph Learning-based Regional Heavy Rainfall Prediction Using Low-Cost Rain Gauges**|Edwin Salcedo et.al.|[2412.16842](http://arxiv.org/abs/2412.16842)|null|
|**2024-12-20**|**Astrometric constraints on stochastic gravitational wave background with neural networks**|Marienza Caldarola et.al.|[2412.15879](http://arxiv.org/abs/2412.15879)|null|
|**2024-12-20**|**GraphSeqLM: A Unified Graph Language Framework for Omic Graph Learning**|Heming Zhang et.al.|[2412.15790](http://arxiv.org/abs/2412.15790)|**[link](https://github.com/fuhailiailab/graphseqlm)**|
|**2024-12-20**|**Prompt-based Unifying Inference Attack on Graph Neural Networks**|Yuecen Wei et.al.|[2412.15735](http://arxiv.org/abs/2412.15735)|**[link](https://github.com/ringbdstack/proia)**|
|**2024-12-20**|**Pre-training Graph Neural Networks on Molecules by Using Subgraph-Conditioned Graph Information Bottleneck**|Van Thuy Hoang et.al.|[2412.15589](http://arxiv.org/abs/2412.15589)|**[link](https://github.com/NSLab-CUK/S-CGIB)**|
|**2024-12-19**|**Investigating Relational State Abstraction in Collaborative MARL**|Sharlin Utke et.al.|[2412.15388](http://arxiv.org/abs/2412.15388)|**[link](https://github.com/gmontana/collaborativepickandplaceenv)**|
|**2024-12-19**|**Tokenphormer: Structure-aware Multi-token Graph Transformer for Node Classification**|Zijie Zhou et.al.|[2412.15302](http://arxiv.org/abs/2412.15302)|**[link](https://github.com/Dodo-D-Caster/Tokenphormer)**|
|**2024-12-19**|**Graph-neural-network predictions of solid-state NMR parameters from spherical tensor decomposition**|Chiheb Ben Mahmoud et.al.|[2412.15063](http://arxiv.org/abs/2412.15063)|null|
|**2024-12-19**|**Answer Set Networks: Casting Answer Set Programming into Deep Learning**|Arseny Skryagin et.al.|[2412.14814](http://arxiv.org/abs/2412.14814)|**[link](https://github.com/ml-research/answersetnetworks)**|
|**2024-12-19**|**Boosting GNN Performance via Training Sample Selection Based on Adversarial Robustness Evaluation**|Yongyu Wang et.al.|[2412.14738](http://arxiv.org/abs/2412.14738)|null|
|**2024-12-19**|**IOHunter: Graph Foundation Model to Uncover Online Information Operations**|Marco Minici et.al.|[2412.14663](http://arxiv.org/abs/2412.14663)|**[link](https://github.com/mminici/socgfm)**|
|**2024-12-19**|**Trainable Adaptive Activation Function Structure (TAAFS) Enhances Neural Network Force Field Performance with Only Dozens of Additional Parameters**|Enji Li et.al.|[2412.14655](http://arxiv.org/abs/2412.14655)|null|
|**2024-12-19**|**Towards Scalable and Deep Graph Neural Networks via Noise Masking**|Yuxuan Liang et.al.|[2412.14602](http://arxiv.org/abs/2412.14602)|null|
|**2024-12-18**|**Towards Precise Prediction Uncertainty in GNNs: Refining GNNs with Topology-grouping Strategy**|Hyunjin Seo et.al.|[2412.14223](http://arxiv.org/abs/2412.14223)|null|
|**2024-12-18**|**Learning and Reconstructing Conflicts in O-RAN: A Graph Neural Network Approach**|Arshia Zolghadr et.al.|[2412.14119](http://arxiv.org/abs/2412.14119)|null|
|**2024-12-18**|**Modality-Independent Graph Neural Networks with Global Transformers for Multimodal Recommendation**|Jun Hu et.al.|[2412.13994](http://arxiv.org/abs/2412.13994)|**[link](https://github.com/crawlscript/mig-gt)**|
|**2024-12-18**|**GraphAvatar: Compact Head Avatars with GNN-Generated 3D Gaussians**|Xiaobao Wei et.al.|[2412.13983](http://arxiv.org/abs/2412.13983)|**[link](https://github.com/ucwxb/graphavatar)**|
|**2024-12-18**|**Spatio-Temporal Forecasting of PM2.5 via Spatial-Diffusion guided Encoder-Decoder Architecture**|Malay Pandey et.al.|[2412.13935](http://arxiv.org/abs/2412.13935)|**[link](https://github.com/malayp717/pm2.5)**|
|**2024-12-18**|**Graph Coarsening via Supervised Granular-Ball for Scalable Graph Neural Network Training**|Shuyin Xia et.al.|[2412.13842](http://arxiv.org/abs/2412.13842)|null|
|**2024-12-17**|**Enhancing Persona Classification in Dialogue Systems: A Graph Neural Network Approach**|Konstantin Zaitsev et.al.|[2412.13283](http://arxiv.org/abs/2412.13283)|null|
|**2024-12-17**|**Enhancing Internet of Things Security throughSelf-Supervised Graph Neural Networks**|Safa Ben Atitallah et.al.|[2412.13240](http://arxiv.org/abs/2412.13240)|null|
|**2024-12-17**|**Cluster-guided Contrastive Class-imbalanced Graph Classification**|Wei Ju et.al.|[2412.12984](http://arxiv.org/abs/2412.12984)|null|
|**2024-12-17**|**Towards Effective Graph Rationalization via Boosting Environment Diversity**|Yujie Wang et.al.|[2412.12880](http://arxiv.org/abs/2412.12880)|null|
|**2024-12-17**|**A Multigrid Graph U-Net Framework for Simulating Multiphase Flow in Heterogeneous Porous Media**|Jiamin Jiang et.al.|[2412.12757](http://arxiv.org/abs/2412.12757)|null|
|**2024-12-17**|**AutoSGNN: Automatic Propagation Mechanism Discovery for Spectral Graph Neural Networks**|Shibing Mo et.al.|[2412.12483](http://arxiv.org/abs/2412.12483)|**[link](https://github.com/Explorermomo/AAAI2025-AutoSGNN)**|
|**2024-12-17**|**Graph Learning in the Era of LLMs: A Survey from the Perspective of Data, Models, and Tasks**|Xunkai Li et.al.|[2412.12456](http://arxiv.org/abs/2412.12456)|null|
|**2024-12-16**|**DeepSN: A Sheaf Neural Framework for Influence Maximization**|Asela Hevapathige et.al.|[2412.12416](http://arxiv.org/abs/2412.12416)|null|
|**2024-12-16**|**Feasibility Study of Measuring $Λ^0\to nπ^{0}$ Using a High-Granularity Zero-Degree Calorimeter at the Future Electron-Ion Collider**|Sebouh J. Paul et.al.|[2412.12346](http://arxiv.org/abs/2412.12346)|null|
|**2024-12-16**|**Graph-Guided Textual Explanation Generation Framework**|Shuzhou Yuan et.al.|[2412.12318](http://arxiv.org/abs/2412.12318)|null|
|**2024-12-16**|**Thermodynamics-informed graph neural networks for real-time simulation of digital human twins**|Lucas Tesán et.al.|[2412.12034](http://arxiv.org/abs/2412.12034)|null|
|**2024-12-16**|**Learning interactions between Rydberg atoms**|Olivier Simard et.al.|[2412.12019](http://arxiv.org/abs/2412.12019)|null|
|**2024-12-16**|**Cost-Effective Label-free Node Classification with LLMs**|Taiyan Zhang et.al.|[2412.11983](http://arxiv.org/abs/2412.11983)|null|
|**2024-12-16**|**BetaExplainer: A Probabilistic Method to Explain Graph Neural Networks**|Whitney Sloneker et.al.|[2412.11964](http://arxiv.org/abs/2412.11964)|**[link](https://github.com/wsloneker/betaexplainerdemo)**|
|**2024-12-16**|**Prediction of social dilemmas in networked populations via graph neural networks**|Huaiyu Tan et.al.|[2412.11775](http://arxiv.org/abs/2412.11775)|null|
|**2024-12-16**|**Asymmetric Learning for Spectral Graph Neural Networks**|Fangbing Liu et.al.|[2412.11739](http://arxiv.org/abs/2412.11739)|**[link](https://github.com/mia-321/asym-opt)**|
|**2024-12-16**|**Smoothness Really Matters: A Simple yet Effective Approach for Unsupervised Graph Domain Adaptation**|Wei Chen et.al.|[2412.11654](http://arxiv.org/abs/2412.11654)|**[link](https://github.com/cwei01/tdss)**|
|**2024-12-16**|**EvoLlama: Enhancing LLMs' Understanding of Proteins via Multimodal Structure and Sequence Representations**|Nuowei Liu et.al.|[2412.11618](http://arxiv.org/abs/2412.11618)|null|
|**2024-12-15**|**A Comparative Study on Dynamic Graph Embedding based on Mamba and Transformers**|Ashish Parmanand Pandey et.al.|[2412.11293](http://arxiv.org/abs/2412.11293)|null|
|**2024-12-15**|**Point Cloud Deep Learning Methods for Particle Shower Reconstruction in the DHCAL**|Maryna Borysova et.al.|[2412.11208](http://arxiv.org/abs/2412.11208)|null|
|**2024-12-13**|**Shape error prediction in 5-axis machining using graph neural networks**|Julia Huuk et.al.|[2412.10341](http://arxiv.org/abs/2412.10341)|null|
|**2024-12-13**|**A Novel Framework Using Deep Reinforcement Learning for Join Order Selection**|Chang Liu et.al.|[2412.10253](http://arxiv.org/abs/2412.10253)|null|
|**2024-12-13**|**Keep It Simple: Towards Accurate Vulnerability Detection for Large Code Graphs**|Xin Peng et.al.|[2412.10164](http://arxiv.org/abs/2412.10164)|null|
|**2024-12-13**|**Can LLMs Convert Graphs to Text-Attributed Graphs?**|Zehong Wang et.al.|[2412.10136](http://arxiv.org/abs/2412.10136)|**[link](https://github.com/zehong-wang/tans)**|
|**2024-12-13**|**Efficient Large-Scale Traffic Forecasting with Transformers: A Spatial Data Management Perspective**|Yuchen Fang et.al.|[2412.09972](http://arxiv.org/abs/2412.09972)|**[link](https://github.com/lmissher/patchstg)**|
|**2024-12-13**|**GraSP: Simple yet Effective Graph Similarity Predictions**|Haoran Zheng et.al.|[2412.09968](http://arxiv.org/abs/2412.09968)|**[link](https://github.com/HaoranZ99/GraSP)**|
|**2024-12-13**|**Towards Fair Graph Neural Networks via Graph Counterfactual without Sensitive Attributes**|Xuemin Wang et.al.|[2412.09947](http://arxiv.org/abs/2412.09947)|null|
|**2024-12-13**|**Brain-inspired Chaotic Graph Backpropagation for Large-scale Combinatorial Optimization**|Peng Tao et.al.|[2412.09860](http://arxiv.org/abs/2412.09860)|null|
|**2024-12-13**|**Universal Inceptive GNNs by Eliminating the Smoothness-generalization Dilemma**|Ming Gu et.al.|[2412.09805](http://arxiv.org/abs/2412.09805)|null|
|**2024-12-12**|**TransferLight: Zero-Shot Traffic Signal Control on any Road-Network**|Johann Schmidt et.al.|[2412.09719](http://arxiv.org/abs/2412.09719)|null|
|**2024-12-12**|**Search Strategy Generation for Branch and Bound Using Genetic Programming**|Gwen Maudet et.al.|[2412.09444](http://arxiv.org/abs/2412.09444)|null|
|**2024-12-12**|**Opinion de-polarization of social networks with GNNs**|Konstantinos Mylonas et.al.|[2412.09404](http://arxiv.org/abs/2412.09404)|null|
|**2024-12-12**|**Hybrid variable spiking graph neural networks for energy-efficient scientific machine learning**|Isha Jain et.al.|[2412.09379](http://arxiv.org/abs/2412.09379)|null|
|**2024-12-12**|**Multi-Scale Heterogeneous Text-Attributed Graph Datasets From Diverse Domains**|Yunhui Liu et.al.|[2412.08937](http://arxiv.org/abs/2412.08937)|**[link](https://github.com/Cloudy1225/HTAG)**|
|**2024-12-12**|**Grothendieck Graph Neural Networks Framework: An Algebraic Platform for Crafting Topology-Aware GNNs**|Amirreza Shiralinasab Langari et.al.|[2412.08835](http://arxiv.org/abs/2412.08835)|**[link](https://github.com/shiralinasab/Grothendieck-Graph-Neural-Networks-Framework)**|
|**2024-12-11**|**Grimm: A Plug-and-Play Perturbation Rectifier for Graph Neural Networks Defending against Poisoning Attacks**|Ao Liu et.al.|[2412.08555](http://arxiv.org/abs/2412.08555)|null|
|**2024-12-11**|**Robustness of Graph Classification: failure modes, causes, and noise-resistant loss in Graph Neural Networks**|Farooq Ahmad Wani et.al.|[2412.08419](http://arxiv.org/abs/2412.08419)|null|
|**2024-12-12**|**Rumor Detection on Social Media with Temporal Propagation Structure Optimization**|Xingyu Peng et.al.|[2412.08316](http://arxiv.org/abs/2412.08316)|null|
|**2024-12-11**|**GDSG: Graph Diffusion-based Solution Generation for Optimization Problems in MEC Networks**|Ruihuai Liang et.al.|[2412.08296](http://arxiv.org/abs/2412.08296)|**[link](https://github.com/qiyu3816/gdsg)**|
|**2024-12-11**|**DistrictNet: Decision-aware learning for geographical districting**|Cheikh Ahmed et.al.|[2412.08287](http://arxiv.org/abs/2412.08287)|**[link](https://github.com/cheikh025/DistrictNet)**|
|**2024-12-11**|**Mixture of Experts Meets Decoupled Message Passing: Towards General and Adaptive Node Classification**|Xuanze Chen et.al.|[2412.08193](http://arxiv.org/abs/2412.08193)|**[link](https://github.com/GISec-Team/GNNMoE)**|
|**2024-12-11**|**Can Graph Neural Networks Learn Language with Extremely Weak Text Supervision?**|Zihao Li et.al.|[2412.08174](http://arxiv.org/abs/2412.08174)|null|
|**2024-12-11**|**DG-Mamba: Robust and Efficient Dynamic Graph Structure Learning with Selective State Space Models**|Haonan Yuan et.al.|[2412.08160](http://arxiv.org/abs/2412.08160)|**[link](https://github.com/RingBDStack/DG-Mamba)**|
|**2024-12-11**|**Rapid Bayesian Seismic Tomography using Graph Mixture Density Networks**|Xin Zhang et.al.|[2412.08080](http://arxiv.org/abs/2412.08080)|null|
|**2024-12-11**|**Cluster-Enhanced Federated Graph Neural Network for Recommendation**|Haiyan Wang et.al.|[2412.08066](http://arxiv.org/abs/2412.08066)|null|
|**2024-12-10**|**Fast Track to Winning Tickets: Repowering One-Shot Pruning for Graph Neural Networks**|Yanwei Yue et.al.|[2412.07605](http://arxiv.org/abs/2412.07605)|**[link](https://github.com/yanweiyue/FastGLT)**|
|**2024-12-10**|**GSM: A GNN-based Space-MIMO Framework for Direct-to-Cell Communications**|Sai Xu et.al.|[2412.07555](http://arxiv.org/abs/2412.07555)|null|
|**2024-12-10**|**Statistical Precoder Design in Multi-User Systems via Graph Neural Networks and Generative Modeling**|Nurettin Turan et.al.|[2412.07519](http://arxiv.org/abs/2412.07519)|null|
|**2024-12-10**|**AHSG: Adversarial Attacks on High-level Semantics in Graph Neural Networks**|Kai Yuan et.al.|[2412.07468](http://arxiv.org/abs/2412.07468)|null|
|**2024-12-10**|**Towards Graph Foundation Models: A Study on the Generalization of Positional and Structural Encodings**|Billy Joe Franks et.al.|[2412.07407](http://arxiv.org/abs/2412.07407)|null|
|**2024-12-10**|**Temporal-Aware Evaluation and Learning for Temporal Graph Neural Networks**|Junwei Su et.al.|[2412.07273](http://arxiv.org/abs/2412.07273)|null|
|**2024-12-10**|**A Dynamical Systems-Inspired Pruning Strategy for Addressing Oversmoothing in Graph Neural Networks**|Biswadeep Chakraborty et.al.|[2412.07243](http://arxiv.org/abs/2412.07243)|null|
|**2024-12-10**|**Graph Neural Networks Are More Than Filters: Revisiting and Benchmarking from A Spectral Perspective**|Yushun Dong et.al.|[2412.07188](http://arxiv.org/abs/2412.07188)|**[link](https://github.com/yushundong/spectral-benchmark)**|
|**2024-12-10**|**Deep Learning-Enhanced Preconditioning for Efficient Conjugate Gradient Solvers in Large-Scale PDE Systems**|Rui Li et.al.|[2412.07127](http://arxiv.org/abs/2412.07127)|null|
|**2024-12-10**|**Covered Forest: Fine-grained generalization analysis of graph neural networks**|Antonis Vasileiou et.al.|[2412.07106](http://arxiv.org/abs/2412.07106)|**[link](https://github.com/benfinkelshtein/CoveredForests)**|
|**2024-12-09**|**MISFEAT: Feature Selection for Subgroups with Systematic Missing Data**|Bar Genossar et.al.|[2412.06711](http://arxiv.org/abs/2412.06711)|null|
|**2024-12-09**|**Cramér-Rao Bound Analysis and Beamforming Design for 3D Extended Target in ISAC: From Optimization to Learning Approaches**|Yiqiu Wang et.al.|[2412.06353](http://arxiv.org/abs/2412.06353)|null|
|**2024-12-09**|**A Self-guided Multimodal Approach to Enhancing Graph Representation Learning for Alzheimer's Diseases**|Zhepeng Wang et.al.|[2412.06212](http://arxiv.org/abs/2412.06212)|null|
|**2024-12-09**|**Deep Unfolding Beamforming and Power Control Designs for Multi-Port Matching Networks**|Bokai Xu et.al.|[2412.06178](http://arxiv.org/abs/2412.06178)|null|
|**2024-12-09**|**Revisiting the Necessity of Graph Learning and Common Graph Benchmarks**|Isay Katsman et.al.|[2412.06173](http://arxiv.org/abs/2412.06173)|null|
|**2024-12-08**|**Fully Distributed Online Training of Graph Neural Networks in Networked Systems**|Rostyslav Olshevskyi et.al.|[2412.06105](http://arxiv.org/abs/2412.06105)|**[link](https://github.com/RostyslavUA/fdTrainGNN)**|
|**2024-12-08**|**Understanding the Impact of Graph Reduction on Adversarial Robustness in Graph Neural Networks**|Kerui Wu et.al.|[2412.05883](http://arxiv.org/abs/2412.05883)|null|
|**2024-12-08**|**Large Language Models Merging for Enhancing the Link Stealing Attack on Graph Neural Networks**|Faqian Guan et.al.|[2412.05830](http://arxiv.org/abs/2412.05830)|null|
|**2024-12-07**|**Towards Robust Spatio-Temporal Auto-Regressive Prediction: Adams-Bashforth Time Integration with Adaptive Multi-Step Rollout**|Sunwoong Yang et.al.|[2412.05657](http://arxiv.org/abs/2412.05657)|null|
|**2024-12-07**|**RouteNet-Fermi: Network Modeling With GNN (Analysis And Re-implementation)**|Shourya Verma et.al.|[2412.05649](http://arxiv.org/abs/2412.05649)|**[link](https://github.com/shouryaverma/routenet_fermi)**|
|**2024-12-06**|**ROS: A GNN-based Relax-Optimize-and-Sample Framework for Max-k-Cut Problems**|Yeqing Qiu et.al.|[2412.05146](http://arxiv.org/abs/2412.05146)|null|
|**2024-12-06**|**Unifying Dual-Space Embedding for Entity Alignment via Contrastive Learning**|Cunda Wang et.al.|[2412.05028](http://arxiv.org/abs/2412.05028)|**[link](https://github.com/wondercs1213/uniea)**|
|**2024-12-06**|**GABAR: Graph Attention-Based Action Ranking for Relational Policy Learning**|Rajesh Mangannavar et.al.|[2412.04752](http://arxiv.org/abs/2412.04752)|null|
|**2024-12-06**|**Code generation and runtime techniques for enabling data-efficient deep learning training on GPUs**|Kun Wu et.al.|[2412.04747](http://arxiv.org/abs/2412.04747)|null|
|**2024-12-05**|**ProtBoost: protein function prediction with Py-Boost and Graph Neural Networks -- CAFA5 top2 solution**|Alexander Chervov et.al.|[2412.04529](http://arxiv.org/abs/2412.04529)|**[link](https://github.com/btbpanda/cafa5-protein-function-prediction-2nd-place)**|
|**2024-12-05**|**PDMD: Potential-free Data-driven Molecular Dynamics for Variable-sized Water Clusters**|Hongyu Yan et.al.|[2412.04442](http://arxiv.org/abs/2412.04442)|**[link](https://github.com/TACC/PDMD)**|
|**2024-12-05**|**Machine Theory of Mind for Autonomous Cyber-Defence**|Luke Swaby et.al.|[2412.04367](http://arxiv.org/abs/2412.04367)|null|
|**2024-12-05**|**Graph-Sequential Alignment and Uniformity: Toward Enhanced Recommendation Systems**|Yuwei Cao et.al.|[2412.04276](http://arxiv.org/abs/2412.04276)|**[link](https://github.com/yuweicao-uic/gsau)**|
|**2024-12-05**|**Graph Neural Networks Need Cluster-Normalize-Activate Modules**|Arseny Skryagin et.al.|[2412.04064](http://arxiv.org/abs/2412.04064)|**[link](https://github.com/ml-research/cna_modules)**|
|**2024-12-05**|**Graph Disentangle Causal Model: Enhancing Causal Inference in Networked Observational Data**|Binbin Hu et.al.|[2412.03913](http://arxiv.org/abs/2412.03913)|null|
|**2024-12-05**|**Training MLPs on Graphs without Supervision**|Zehong Wang et.al.|[2412.03864](http://arxiv.org/abs/2412.03864)|**[link](https://github.com/zehong-wang/simmlp)**|
|**2024-12-05**|**Expressivity of Representation Learning on Continuous-Time Dynamic Graphs: An Information-Flow Centric Review**|Sofiane Ennadir et.al.|[2412.03783](http://arxiv.org/abs/2412.03783)|null|
|**2024-12-04**|**Language Model Meets Prototypes: Towards Interpretable Text Classification Models through Prototypical Networks**|Ximing Wen et.al.|[2412.03761](http://arxiv.org/abs/2412.03761)|null|
|**2024-12-04**|**Explainable Malware Detection through Integrated Graph Reduction and Learning Techniques**|Hesamodin Mohammadian et.al.|[2412.03634](http://arxiv.org/abs/2412.03634)|null|
|**2024-12-04**|**Dielectric tensor of perovskite oxides at finite temperature using equivariant graph neural network potentials**|Alex Kutana et.al.|[2412.03541](http://arxiv.org/abs/2412.03541)|null|
|**2024-12-04**|**Contextual Data Integration for Bike-sharing Demand Prediction with Graph Neural Networks in Degraded Weather Conditions**|Romain Rochas et.al.|[2412.03307](http://arxiv.org/abs/2412.03307)|null|
|**2024-12-04**|**Node Classification With Integrated Reject Option**|Uday Bhaskar et.al.|[2412.03190](http://arxiv.org/abs/2412.03190)|null|
|**2024-12-04**|**Semi-decentralized Training of Spatio-Temporal Graph Neural Networks for Traffic Prediction**|Ivan Kralj et.al.|[2412.03188](http://arxiv.org/abs/2412.03188)|null|
|**2024-12-04**|**Enhancing Recommendation Systems with GNNs and Addressing Over-Smoothing**|Wenyi Liu et.al.|[2412.03097](http://arxiv.org/abs/2412.03097)|null|
|**2024-12-04**|**A Graph Neural Network Approach to Dispersed Systems**|Aref Hashemi et.al.|[2412.02967](http://arxiv.org/abs/2412.02967)|**[link](https://github.com/rfjd/gns-dispersedsystems)**|
|**2024-12-03**|**CuXASNet: Rapid and Accurate Prediction of Copper L-edge X-Ray Absorption Spectra Using Machine Learning**|Samuel P. Gleason et.al.|[2412.02916](http://arxiv.org/abs/2412.02916)|null|
|**2024-12-03**|**Geographical Information Alignment Boosts Traffic Analysis via Transpose Cross-attention**|Xiangyu Jiang et.al.|[2412.02839](http://arxiv.org/abs/2412.02839)|null|
|**2024-12-03**|**MERGE: Multi-faceted Hierarchical Graph-based GNN for Gene Expression Prediction from Whole Slide Histopathology Images**|Aniruddha Ganguly et.al.|[2412.02601](http://arxiv.org/abs/2412.02601)|null|
|**2024-12-03**|**Mobile Cell-Free Massive MIMO with Multi-Agent Reinforcement Learning: A Scalable Framework**|Ziheng Liu et.al.|[2412.02581](http://arxiv.org/abs/2412.02581)|null|
|**2024-12-03**|**An Automated Data Mining Framework Using Autoencoders for Feature Extraction and Dimensionality Reduction**|Yaxin Liang et.al.|[2412.02211](http://arxiv.org/abs/2412.02211)|null|
|**2024-12-03**|**Generalizing Weisfeiler-Lehman Kernels to Subgraphs**|Dongkwan Kim et.al.|[2412.02181](http://arxiv.org/abs/2412.02181)|**[link](https://github.com/dongkwan-kim/wlks)**|
|**2024-12-03**|**GNN-based Auto-Encoder for Short Linear Block Codes: A DRL Approach**|Kou Tian et.al.|[2412.02053](http://arxiv.org/abs/2412.02053)|null|
|**2024-12-02**|**Structure-Guided Input Graph for GNNs facing Heterophily**|Victor M. Tenorio et.al.|[2412.01757](http://arxiv.org/abs/2412.01757)|**[link](https://github.com/vmtenorio/sg-gnn)**|
|**2024-12-02**|**A Survey on Deep Neural Networks in Collaborative Filtering Recommendation Systems**|Pang Li et.al.|[2412.01378](http://arxiv.org/abs/2412.01378)|null|
|**2024-12-02**|**Morphological-Symmetry-Equivariant Heterogeneous Graph Neural Network for Robotic Dynamics Learning**|Fengze Xie et.al.|[2412.01297](http://arxiv.org/abs/2412.01297)|**[link](https://github.com/lunarlab-gatech/morphsym-hgnn)**|
|**2024-12-02**|**Superhypergraph Neural Networks and Plithogenic Graph Neural Networks: Theoretical Foundations**|Takaaki Fujita et.al.|[2412.01176](http://arxiv.org/abs/2412.01176)|null|
|**2024-12-02**|**Lossless and Privacy-Preserving Graph Convolution Network for Federated Item Recommendation**|Guowei Wu et.al.|[2412.01141](http://arxiv.org/abs/2412.01141)|null|
|**2024-11-29**|**SDR-GNN: Spectral Domain Reconstruction Graph Neural Network for Incomplete Multimodal Learning in Conversational Emotion Recognition**|Fangze Fu et.al.|[2411.19822](http://arxiv.org/abs/2411.19822)|**[link](https://github.com/fufangze/SDR-GNN)**|
|**2024-11-29**|**PerLA: Perceptive 3D Language Assistant**|Guofeng Mei et.al.|[2411.19774](http://arxiv.org/abs/2411.19774)|null|
|**2024-11-29**|**Graph Neural Networks for Heart Failure Prediction on an EHR-Based Patient Similarity Graph**|Heloisa Oss Boll et.al.|[2411.19742](http://arxiv.org/abs/2411.19742)|**[link](https://github.com/hossboll/patient-gnn)**|
|**2024-11-29**|**RL-MILP Solver: A Reinforcement Learning Approach for Solving Mixed-Integer Linear Programs with Graph Neural Networks**|Tae-Hoon Lee et.al.|[2411.19517](http://arxiv.org/abs/2411.19517)|null|
|**2024-11-29**|**ContextGNN: Beyond Two-Tower Recommendation Systems**|Yiwen Yuan et.al.|[2411.19513](http://arxiv.org/abs/2411.19513)|**[link](https://github.com/kumo-ai/ContextGNN)**|
|**2024-11-29**|**Graph-Enhanced EEG Foundation Model**|Limin Wang et.al.|[2411.19507](http://arxiv.org/abs/2411.19507)|null|
|**2024-11-29**|**Gradient Inversion Attack on Graph Neural Networks**|Divya Anand Sinha et.al.|[2411.19440](http://arxiv.org/abs/2411.19440)|null|
|**2024-11-28**|**Scale Invariance of Graph Neural Networks**|Qin Jiang et.al.|[2411.19392](http://arxiv.org/abs/2411.19392)|**[link](https://github.com/qin87/scalenet)**|
|**2024-11-28**|**GRU-PFG: Extract Inter-Stock Correlation from Stock Factors with Graph Neural Network**|Yonggai Zhuang et.al.|[2411.18997](http://arxiv.org/abs/2411.18997)|null|
|**2024-11-28**|**NeuroLifting: Neural Inference on Markov Random Fields at Scale**|Yaomin Wang et.al.|[2411.18954](http://arxiv.org/abs/2411.18954)|null|
|**2024-11-27**|**Perturbation Ontology based Graph Attention Networks**|Yichen Wang et.al.|[2411.18520](http://arxiv.org/abs/2411.18520)|null|
|**2024-11-27**|**Learning optimal objective values for MILP**|Lara Scavuzzo et.al.|[2411.18321](http://arxiv.org/abs/2411.18321)|**[link](https://github.com/lascavana/objvalprediction)**|
|**2024-11-27**|**Causal and Local Correlations Based Network for Multivariate Time Series Classification**|Mingsen Du et.al.|[2411.18008](http://arxiv.org/abs/2411.18008)|**[link](https://github.com/dumingsen/calonet)**|
|**2024-11-27**|**Graph Neural Network for Cerebral Blood Flow Prediction With Clinical Datasets**|Seungyeon Kim et.al.|[2411.17971](http://arxiv.org/abs/2411.17971)|null|
|**2024-11-26**|**Spatio-temporal Causal Learning for Streamflow Forecasting**|Shu Wan et.al.|[2411.17937](http://arxiv.org/abs/2411.17937)|null|
|**2024-11-26**|**GNN 101: Visual Learning of Graph Neural Networks in Your Web Browser**|Yilin Lu et.al.|[2411.17849](http://arxiv.org/abs/2411.17849)|null|
|**2024-11-26**|**Instance-Aware Graph Prompt Learning**|Jiazheng Li et.al.|[2411.17676](http://arxiv.org/abs/2411.17676)|null|
|**2024-11-26**|**A Graph Neural Network deep-dive into successful counterattacks**|Joris Bekkers et.al.|[2411.17450](http://arxiv.org/abs/2411.17450)|null|
|**2024-11-26**|**Rewiring Techniques to Mitigate Oversquashing and Oversmoothing in GNNs: A Survey**|Hugo Attali et.al.|[2411.17429](http://arxiv.org/abs/2411.17429)|null|
|**2024-11-26**|**Epidemiology-informed Graph Neural Network for Heterogeneity-aware Epidemic Forecasting**|Yufan Zheng et.al.|[2411.17372](http://arxiv.org/abs/2411.17372)|null|
|**2024-11-26**|**Knowledge-aware Evolutionary Graph Neural Architecture Search**|Chao Wang et.al.|[2411.17339](http://arxiv.org/abs/2411.17339)|**[link](https://github.com/xiaofangxd/KEGNAS)**|
|**2024-11-26**|**GrokFormer: Graph Fourier Kolmogorov-Arnold Transformers**|Guoguo Ai et.al.|[2411.17296](http://arxiv.org/abs/2411.17296)|**[link](https://github.com/GGA23/GrokFormer)**|
|**2024-11-26**|**DGNN-YOLO: Dynamic Graph Neural Networks with YOLO11 for Small Object Detection and Tracking in Traffic Surveillance**|Shahriar Soudeep et.al.|[2411.17251](http://arxiv.org/abs/2411.17251)|null|
|**2024-11-26**|**GraphSubDetector: Time Series Subsequence Anomaly Detection via Density-Aware Adaptive Graph Neural Network**|Weiqi Chen et.al.|[2411.17218](http://arxiv.org/abs/2411.17218)|null|
|**2024-11-26**|**Depth-PC: A Visual Servo Framework Integrated with Cross-Modality Fusion for Sim2Real Transfer**|Haoyu Zhang et.al.|[2411.17195](http://arxiv.org/abs/2411.17195)|null|
|**2024-11-26**|**X-MeshGraphNet: Scalable Multi-Scale Graph Neural Networks for Physics Simulation**|Mohammad Amin Nabian et.al.|[2411.17164](http://arxiv.org/abs/2411.17164)|**[link](https://github.com/nvidia/modulus)**|
|**2024-11-25**|**Limeade: Let integer molecular encoding aid**|Shiqiang Zhang et.al.|[2411.16623](http://arxiv.org/abs/2411.16623)|**[link](https://github.com/cog-imperial/limeade)**|
|**2024-11-25**|**Application of Graph Networks to a wide-field Water-Cherenkov-based Gamma-Ray Observatory**|Jonas Glombitza et.al.|[2411.16565](http://arxiv.org/abs/2411.16565)|null|
|**2024-11-25**|**Graph Neural Networks-based Parameter Design towards Large-Scale Superconducting Quantum Circuits for Crosstalk Mitigation**|Hao Ai et.al.|[2411.16354](http://arxiv.org/abs/2411.16354)|null|
|**2024-11-25**|**A Data-Driven Approach to Dataflow-Aware Online Scheduling for Graph Neural Network Inference**|Pol Puigdemont et.al.|[2411.16342](http://arxiv.org/abs/2411.16342)|null|
|**2024-11-25**|**Graph Adapter of EEG Foundation Models for Parameter Efficient Fine Tuning**|Toyotaro Suzumura et.al.|[2411.16155](http://arxiv.org/abs/2411.16155)|null|
|**2024-11-25**|**DF-GNN: Dynamic Fusion Framework for Attention Graph Neural Networks on GPUs**|Jiahui Liu et.al.|[2411.16127](http://arxiv.org/abs/2411.16127)|**[link](https://github.com/paoxiaode/DF-GNN)**|
|**2024-11-23**|**TANGNN: a Concise, Scalable and Effective Graph Neural Networks with Top-m Attention Mechanism for Graph Representation Learning**|Jiawei E et.al.|[2411.15458](http://arxiv.org/abs/2411.15458)|**[link](https://github.com/ejwww/tangnn)**|
|**2024-11-22**|**GeoScatt-GNN: A Geometric Scattering Transform-Based Graph Neural Network Model for Ames Mutagenicity Prediction**|Abdeljalil Zoubir et.al.|[2411.15331](http://arxiv.org/abs/2411.15331)|null|
|**2024-11-22**|**Lie-Equivariant Quantum Graph Neural Networks**|Jogi Suda Neto et.al.|[2411.15315](http://arxiv.org/abs/2411.15315)|**[link](https://github.com/ml4sci/qmlhep)**|
|**2024-11-22**|**Can GNNs Learn Link Heuristics? A Concise Review and Evaluation of Link Prediction Methods**|Shuming Liang et.al.|[2411.14711](http://arxiv.org/abs/2411.14711)|**[link](https://github.com/astroming/GNNHE)**|
|**2024-11-21**|**Swift: A Multi-FPGA Framework for Scaling Up Accelerated Graph Analytics**|Oluwole Jaiyeoba et.al.|[2411.14554](http://arxiv.org/abs/2411.14554)|null|
|**2024-11-21**|**Learning Pore-scale Multi-phase Flow from Experimental Data with Graph Neural Network**|Yuxuan Gu et.al.|[2411.14192](http://arxiv.org/abs/2411.14192)|null|
|**2024-11-21**|**Predicting rigidity and connectivity percolation in disordered particulate networks using graph neural networks**|D. A. Head et.al.|[2411.14159](http://arxiv.org/abs/2411.14159)|null|
|**2024-11-21**|**GNN-MultiFix: Addressing the pitfalls for GNNs for multi-label node classification**|Tianqi Zhao et.al.|[2411.14094](http://arxiv.org/abs/2411.14094)|null|
|**2024-11-21**|**Interpretable QSPR Modeling using Recursive Feature Machines and Multi-scale Fingerprints**|Jiaxuan Shen et.al.|[2411.14079](http://arxiv.org/abs/2411.14079)|null|
|**2024-11-21**|**Teaching MLPs to Master Heterogeneous Graph-Structured Knowledge for Efficient and Accurate Inference**|Yunhui Liu et.al.|[2411.14035](http://arxiv.org/abs/2411.14035)|**[link](https://github.com/cloudy1225/hg2m)**|
|**2024-11-21**|**Topology-Aware Popularity Debiasing via Simplicial Complexes**|Yanbiao Ji et.al.|[2411.13892](http://arxiv.org/abs/2411.13892)|null|
|**2024-11-21**|**Heterophilic Graph Neural Networks Optimization with Causal Message-passing**|Botao Wang et.al.|[2411.13821](http://arxiv.org/abs/2411.13821)|null|
|**2024-11-21**|**On Representing Convex Quadratically Constrained Quadratic Programs via Graph Neural Networks**|Chenyang Wu et.al.|[2411.13805](http://arxiv.org/abs/2411.13805)|null|
|**2024-11-20**|**Investigating Graph Neural Networks and Classical Feature-Extraction Techniques in Activity-Cliff and Molecular Property Prediction**|Markus Dablander et.al.|[2411.13688](http://arxiv.org/abs/2411.13688)|null|
|**2024-11-20**|**Graph neural network framework for energy mapping of hybrid monte-carlo molecular dynamics simulations of Medium Entropy Alloys**|Mashaekh Tausif Ehsan et.al.|[2411.13670](http://arxiv.org/abs/2411.13670)|null|
|**2024-11-20**|**Predictive Insights into LGBTQ+ Minority Stress: A Transductive Exploration of Social Media Discourse**|S. Chapagain et.al.|[2411.13534](http://arxiv.org/abs/2411.13534)|**[link](https://github.com/chapagaisa/transductive)**|
|**2024-11-20**|**Advancing Heatwave Forecasting via Distribution Informed-Graph Neural Networks (DI-GNNs): Integrating Extreme Value Theory with GNNs**|Farrukh A. Chishtie et.al.|[2411.13496](http://arxiv.org/abs/2411.13496)|null|
|**2024-11-20**|**Predicting Wall Thickness Changes in Cold Forging Processes: An Integrated FEM and Neural Network approach**|Sasa Ilic et.al.|[2411.13366](http://arxiv.org/abs/2411.13366)|null|
|**2024-11-20**|**Domain Adaptive Unfolded Graph Neural Networks**|Zepeng Zhang et.al.|[2411.13137](http://arxiv.org/abs/2411.13137)|null|
|**2024-11-20**|**ORID: Organ-Regional Information Driven Framework for Radiology Report Generation**|Tiancheng Gu et.al.|[2411.13025](http://arxiv.org/abs/2411.13025)|null|
|**2024-11-20**|**Epidemiology-informed Network for Robust Rumor Detection**|Wei Jiang et.al.|[2411.12949](http://arxiv.org/abs/2411.12949)|null|
|**2024-11-19**|**MLDGG: Meta-Learning for Domain Generalization on Graphs**|Qin Tian et.al.|[2411.12913](http://arxiv.org/abs/2411.12913)|null|
|**2024-11-19**|**Benchmarking Positional Encodings for GNNs and Graph Transformers**|Florian Grötschla et.al.|[2411.12732](http://arxiv.org/abs/2411.12732)|**[link](https://github.com/ETH-DISCO/Benchmarking-PEs)**|
|**2024-11-19**|**Estimating Dark Matter Halo Masses in Simulated Galaxy Clusters with Graph Neural Networks**|Nikhil Garuda et.al.|[2411.12629](http://arxiv.org/abs/2411.12629)|null|
|**2024-11-19**|**GNNAS-Dock: Budget Aware Algorithm Selection with Graph Neural Networks for Molecular Docking**|Yiliang Yuan et.al.|[2411.12597](http://arxiv.org/abs/2411.12597)|null|
|**2024-11-19**|**Bias Free Sentiment Analysis**|Hubert Plisiecki et.al.|[2411.12493](http://arxiv.org/abs/2411.12493)|null|
|**2024-11-19**|**Graph as a feature: improving node classification with non-neural graph-aware logistic regression**|Simon Delarue et.al.|[2411.12330](http://arxiv.org/abs/2411.12330)|**[link](https://github.com/graph-lr/graph-aware-logistic-regression)**|
|**2024-11-18**|**Cartesian Atomic Moment Machine Learning Interatomic Potentials**|Mingjian Wen et.al.|[2411.12096](http://arxiv.org/abs/2411.12096)|**[link](https://github.com/wengroup/camp_run)**|
|**2024-11-18**|**Efficient and Robust Continual Graph Learning for Graph Classification in Biology**|Ding Zhang et.al.|[2411.11668](http://arxiv.org/abs/2411.11668)|null|
|**2024-11-19**|**GNN-Based Code Annotation Logic for Establishing Security Boundaries in C Code**|Varun Gadey et.al.|[2411.11567](http://arxiv.org/abs/2411.11567)|null|
|**2024-11-18**|**Graph Artificial Intelligence for Quantifying Compatibility Mechanisms in Traditional Chinese Medicine**|Jingqi Zeng et.al.|[2411.11474](http://arxiv.org/abs/2411.11474)|**[link](https://github.com/zengjingqi/graphai-for-tcm)**|
|**2024-11-18**|**Physics meets Topology: Physics-informed topological neural networks for learning rigid body dynamics**|Amaury Wei et.al.|[2411.11467](http://arxiv.org/abs/2411.11467)|null|
|**2024-11-18**|**Unveiling the Inflexibility of Adaptive Embedding in Traffic Forecasting**|Hongjun Wang et.al.|[2411.11448](http://arxiv.org/abs/2411.11448)|**[link](https://github.com/Dreamzz5/PCA-Embedding)**|
|**2024-11-18**|**The GECo algorithm for Graph Neural Networks Explanation**|Salvatore Calderaro et.al.|[2411.11391](http://arxiv.org/abs/2411.11391)|**[link](https://github.com/salvatorecalderaro/geco_explainer)**|
|**2024-11-18**|**Graph Neural Networks on Graph Databases**|Dmytro Lopushanskyy et.al.|[2411.11375](http://arxiv.org/abs/2411.11375)|null|
|**2024-11-18**|**Dual-Frequency Filtering Self-aware Graph Neural Networks for Homophilic and Heterophilic Graphs**|Yachao Yang et.al.|[2411.11284](http://arxiv.org/abs/2411.11284)|null|
|**2024-11-17**|**Stealing Training Graphs from Graph Neural Networks**|Minhua Lin et.al.|[2411.11197](http://arxiv.org/abs/2411.11197)|null|
|**2024-11-17**|**Robust Defense Against Extreme Grid Events Using Dual-Policy Reinforcement Learning Agents**|Benjamin M. Peter et.al.|[2411.11180](http://arxiv.org/abs/2411.11180)|null|
|**2024-11-15**|**Bitcoin Research with a Transaction Graph Dataset**|Hugo Schnoering et.al.|[2411.10325](http://arxiv.org/abs/2411.10325)|**[link](https://github.com/hugoschnoering2/BTCGraphLabeling)**|
|**2024-11-15**|**DuSEGO: Dual Second-order Equivariant Graph Ordinary Differential Equation**|Yingxu Wang et.al.|[2411.10000](http://arxiv.org/abs/2411.10000)|null|
|**2024-11-15**|**Graph Neural Networks and Differential Equations: A hybrid approach for data assimilation of fluid flows**|M. Quattromini et.al.|[2411.09476](http://arxiv.org/abs/2411.09476)|null|
|**2024-11-14**|**Less is More: Unseen Domain Fake News Detection via Causal Propagation Substructures**|Shuzhi Gong et.al.|[2411.09389](http://arxiv.org/abs/2411.09389)|null|
|**2024-11-14**|**Cross Space and Time: A Spatio-Temporal Unitized Model for Traffic Flow Forecasting**|Weilin Ruan et.al.|[2411.09251](http://arxiv.org/abs/2411.09251)|null|
|**2024-11-14**|**Neural Graph Simulator for Complex Systems**|Hoyun Choi et.al.|[2411.09120](http://arxiv.org/abs/2411.09120)|null|
|**2024-11-14**|**Deep Learning for Beamforming in Multi-User Continuous Aperture Array (CAPA) Systems**|Jia Guo et.al.|[2411.09104](http://arxiv.org/abs/2411.09104)|null|
|**2024-11-13**|**Continuous GNN-based Anomaly Detection on Edge using Efficient Adaptive Knowledge Graph Learning**|Sanggeon Yun et.al.|[2411.09072](http://arxiv.org/abs/2411.09072)|null|
|**2024-11-13**|**Predictive Visuo-Tactile Interactive Perception Framework for Object Properties Inference**|Anirvan Dutta et.al.|[2411.09020](http://arxiv.org/abs/2411.09020)|null|
|**2024-11-13**|**Flow reconstruction in time-varying geometries using graph neural networks**|Bogdan A. Danciu et.al.|[2411.08764](http://arxiv.org/abs/2411.08764)|null|
|**2024-11-13**|**ScaleNet: Scale Invariance Learning in Directed Graphs**|Qin Jiang et.al.|[2411.08758](http://arxiv.org/abs/2411.08758)|**[link](https://github.com/qin87/scalenet)**|
|**2024-11-13**|**Gaussian Mixture Models Based Augmentation Enhances GNN Generalization**|Yassine Abbahaddou et.al.|[2411.08638](http://arxiv.org/abs/2411.08638)|null|
|**2024-11-13**|**TDGCN-Based Mobile Multiuser Physical-Layer Authentication for EI-Enabled IIoT**|Rui Meng et.al.|[2411.08628](http://arxiv.org/abs/2411.08628)|null|
|**2024-11-13**|**Graph Neural Networks in Supply Chain Analytics and Optimization: Concepts, Perspectives, Dataset and Benchmarks**|Azmine Toushik Wasi et.al.|[2411.08550](http://arxiv.org/abs/2411.08550)|**[link](https://github.com/CIOL-SUST/SCG)**|
|**2024-11-13**|**A Heterogeneous Graph Neural Network Fusing Functional and Structural Connectivity for MCI Diagnosis**|Feiyu Yin et.al.|[2411.08424](http://arxiv.org/abs/2411.08424)|null|
|**2024-11-13**|**Federated Graph Learning with Graphless Clients**|Xingbo Fu et.al.|[2411.08374](http://arxiv.org/abs/2411.08374)|null|
|**2024-11-12**|**Rethinking Structure Learning For Graph Neural Networks**|Yilun Zheng et.al.|[2411.07672](http://arxiv.org/abs/2411.07672)|null|
|**2024-11-12**|**Is Graph Convolution Always Beneficial For Every Feature?**|Yilun Zheng et.al.|[2411.07663](http://arxiv.org/abs/2411.07663)|null|
|**2024-11-12**|**xCG: Explainable Cell Graphs for Survival Prediction in Non-Small Cell Lung Cancer**|Marvin Sextro et.al.|[2411.07643](http://arxiv.org/abs/2411.07643)|**[link](https://github.com/marvinsxtr/explainable-cell-graphs)**|
|**2024-11-12**|**Quantum Information-Empowered Graph Neural Network for Hyperspectral Change Detection**|Chia-Hsiang Lin et.al.|[2411.07608](http://arxiv.org/abs/2411.07608)|null|
|**2024-11-12**|**Enhancing Link Prediction with Fuzzy Graph Attention Networks and Dynamic Negative Sampling**|Jinming Xing et.al.|[2411.07482](http://arxiv.org/abs/2411.07482)|null|
|**2024-11-12**|**Machines and Mathematical Mutations: Using GNNs to Characterize Quiver Mutation Classes**|Jesse He et.al.|[2411.07467](http://arxiv.org/abs/2411.07467)|null|
|**2024-11-11**|**General Geospatial Inference with a Population Dynamics Foundation Model**|Mohit Agarwal et.al.|[2411.07207](http://arxiv.org/abs/2411.07207)|**[link](https://github.com/google-research/population-dynamics)**|
|**2024-11-11**|**Efficient Unsupervised Domain Adaptation Regression for Spatial-Temporal Air Quality Sensor Fusion**|Keivan Faghih Niresi et.al.|[2411.06917](http://arxiv.org/abs/2411.06917)|null|
|**2024-11-11**|**Predicting ionic conductivity in solids from the machine-learned potential energy landscape**|Artem Maevskiy et.al.|[2411.06804](http://arxiv.org/abs/2411.06804)|**[link](https://github.com/SiLiKhon/pes_fingerprint)**|
|**2024-11-11**|**Shedding Light on Problems with Hyperbolic Graph Learning**|Isay Katsman et.al.|[2411.06688](http://arxiv.org/abs/2411.06688)|null|
|**2024-11-11**|**Inductive Graph Few-shot Class Incremental Learning**|Yayong Li et.al.|[2411.06634](http://arxiv.org/abs/2411.06634)|null|
|**2024-11-10**|**Graph Neural Networks for modelling breast biomechanical compression**|Hadeel Awwad et.al.|[2411.06596](http://arxiv.org/abs/2411.06596)|**[link](https://github.com/hadiiiil/gnns-breastcompression)**|
|**2024-11-10**|**Towards Graph Neural Network Surrogates Leveraging Mechanistic Expert Knowledge for Pandemic Response**|Agatha Schmidt et.al.|[2411.06500](http://arxiv.org/abs/2411.06500)|null|
|**2024-11-10**|**Deep Learning Approaches for BSM Physics: Evaluating DNN and GNN Performance in Particle Collision Event Classification**|Ali Çelik et.al.|[2411.06487](http://arxiv.org/abs/2411.06487)|null|
|**2024-11-09**|**Constraints and Variables Reduction for Optimal Power Flow Using Hierarchical Graph Neural Networks with Virtual Node-Splitting**|Thuan Phamh et.al.|[2411.06268](http://arxiv.org/abs/2411.06268)|null|
|**2024-11-09**|**Generalizing Hyperedge Expansion for Hyper-relational Knowledge Graph Modeling**|Yu Liu et.al.|[2411.06191](http://arxiv.org/abs/2411.06191)|null|
|**2024-11-08**|**Topology-aware Reinforcement Feature Space Reconstruction for Graph Data**|Wangyang Ying et.al.|[2411.05742](http://arxiv.org/abs/2411.05742)|null|
|**2024-11-08**|**YOSO: You-Only-Sample-Once via Compressed Sensing for Graph Neural Network Training**|Yi Li et.al.|[2411.05693](http://arxiv.org/abs/2411.05693)|null|
|**2024-11-08**|**Streaming Network for Continual Learning of Object Relocations under Household Context Drifts**|Ermanno Bartoli et.al.|[2411.05549](http://arxiv.org/abs/2411.05549)|null|
|**2024-11-08**|**EUREKHA: Enhancing User Representation for Key Hackers Identification in Underground Forums**|Abdoul Nasser Hassane Amadou et.al.|[2411.05479](http://arxiv.org/abs/2411.05479)|**[link](https://github.com/jumbo110/eurekha)**|
|**2024-11-08**|**Generalization, Expressivity, and Universality of Graph Neural Networks on Attributed Graphs**|Levi Rauchwerger et.al.|[2411.05464](http://arxiv.org/abs/2411.05464)|null|
|**2024-11-08**|**Post-Hoc Robustness Enhancement in Graph Neural Networks with Conditional Random Fields**|Yassine Abbahaddou et.al.|[2411.05399](http://arxiv.org/abs/2411.05399)|null|
|**2024-11-08**|**Distributed-Order Fractional Graph Operating Network**|Kai Zhao et.al.|[2411.05274](http://arxiv.org/abs/2411.05274)|**[link](https://github.com/zknus/neurips-2024-dragon)**|
|**2024-11-07**|**Exploiting the Structure of Two Graphs with Graph Neural Networks**|Victor M. Tenorio et.al.|[2411.05119](http://arxiv.org/abs/2411.05119)|**[link](https://github.com/vmtenorio/io-gnn)**|
|**2024-11-07**|**Enhancing Missing Data Imputation through Combined Bipartite Graph and Complete Directed Graph**|Zhaoyang Zhang et.al.|[2411.04907](http://arxiv.org/abs/2411.04907)|null|
|**2024-11-07**|**Sampling-guided Heterogeneous Graph Neural Network with Temporal Smoothing for Scalable Longitudinal Data Imputation**|Zhaoyang Zhang et.al.|[2411.04899](http://arxiv.org/abs/2411.04899)|null|
|**2024-11-07**|**Centrality Graph Shift Operators for Graph Neural Networks**|Yassine Abbahaddou et.al.|[2411.04655](http://arxiv.org/abs/2411.04655)|**[link](https://github.com/abbahaddou/CGSO)**|
|**2024-11-07**|**Cybercrime Prediction via Geographically Weighted Learning**|Muhammad Al-Zafar Khan et.al.|[2411.04635](http://arxiv.org/abs/2411.04635)|null|
|**2024-11-07**|**Higher-Order GNNs Meet Efficiency: Sparse Sobolev Graph Neural Networks**|Jhony H. Giraldo et.al.|[2411.04570](http://arxiv.org/abs/2411.04570)|**[link](https://github.com/jhonygiraldo/S2-GNN)**|
|**2024-11-07**|**ComFairGNN: Community Fair Graph Neural Network**|Yonas Sium et.al.|[2411.04371](http://arxiv.org/abs/2411.04371)|null|
|**2024-11-07**|**GaGSL: Global-augmented Graph Structure Learning via Graph Information Bottleneck**|Shuangjie Li et.al.|[2411.04356](http://arxiv.org/abs/2411.04356)|null|
|**2024-11-06**|**Graph neural networks and non-commuting operators**|Mauricio Velasco et.al.|[2411.04265](http://arxiv.org/abs/2411.04265)|**[link](https://github.com/kkylie/gtnn_weighted_circulant_graphs)**|
|**2024-11-06**|**Multi-branch Spatio-Temporal Graph Neural Network For Efficient Ice Layer Thickness Prediction**|Zesheng Liu et.al.|[2411.04055](http://arxiv.org/abs/2411.04055)|null|
|**2024-11-06**|**Reconsidering the Performance of GAE in Link Prediction**|Weishuo Ma et.al.|[2411.03845](http://arxiv.org/abs/2411.03845)|**[link](https://github.com/graphpku/refined-gae)**|
|**2024-11-06**|**Graph Neural Networks with Coarse- and Fine-Grained Division for Mitigating Label Sparsity and Noise**|Shuangjie Li et.al.|[2411.03744](http://arxiv.org/abs/2411.03744)|null|
|**2024-11-06**|**Can Graph Neural Networks Expose Training Data Properties? An Efficient Risk Assessment Approach**|Hanyang Yuan et.al.|[2411.03663](http://arxiv.org/abs/2411.03663)|**[link](https://github.com/zjunet/GPIA_NIPS)**|
|**2024-11-06**|**SEGMN: A Structure-Enhanced Graph Matching Network for Graph Similarity Learning**|Wenjun Wang et.al.|[2411.03624](http://arxiv.org/abs/2411.03624)|null|
|**2024-11-06**|**Advanced RAG Models with Graph Structures: Optimizing Complex Knowledge Reasoning and Text Generation**|Yuxin Dong et.al.|[2411.03572](http://arxiv.org/abs/2411.03572)|null|
|**2024-11-06**|**Beyond Grid Data: Exploring Graph Neural Networks for Earth Observation**|Shan Zhao et.al.|[2411.03223](http://arxiv.org/abs/2411.03223)|null|
|**2024-11-05**|**DA-MoE: Addressing Depth-Sensitivity in Graph-Level Analysis through Mixture of Experts**|Zelin Yao et.al.|[2411.03025](http://arxiv.org/abs/2411.03025)|**[link](https://github.com/celin-yao/da-moe)**|
|**2024-11-05**|**Privacy-Preserving Graph-Based Machine Learning with Fully Homomorphic Encryption for Collaborative Anti-Money Laundering**|Fabrianne Effendi et.al.|[2411.02926](http://arxiv.org/abs/2411.02926)|**[link](https://github.com/fabecode/GraphML-FHE)**|
|**2024-11-05**|**Distributed Graph Neural Network Design for Sum Ergodic Spectral Efficiency Maximization in Cell-Free Massive MIMO**|Nguyen Xuan Tung et.al.|[2411.02900](http://arxiv.org/abs/2411.02900)|null|
|**2024-11-05**|**Query-Efficient Adversarial Attack Against Vertical Federated Graph Learning**|Jinyin Chen et.al.|[2411.02809](http://arxiv.org/abs/2411.02809)|**[link](https://github.com/hgh0545/NA2)**|
|**2024-11-05**|**JPEC: A Novel Graph Neural Network for Competitor Retrieval in Financial Knowledge Graphs**|Wanying Ding et.al.|[2411.02692](http://arxiv.org/abs/2411.02692)|null|
|**2024-11-04**|**Fine Grained Insider Risk Detection**|Birkett Huber et.al.|[2411.02645](http://arxiv.org/abs/2411.02645)|null|
|**2024-11-04**|**EOSnet: Embedded Overlap Structures for Graph Neural Networks in Predicting Material Properties**|Shuo Tao et.al.|[2411.02579](http://arxiv.org/abs/2411.02579)|null|
|**2024-11-04**|**Enhancing Graph Neural Networks in Large-scale Traffic Incident Analysis with Concurrency Hypothesis**|Xiwen Chen et.al.|[2411.02542](http://arxiv.org/abs/2411.02542)|**[link](https://github.com/xiwenc1/incident-gnn-cp)**|
|**2024-11-04**|**GraphXAIN: Narratives to Explain Graph Neural Networks**|Mateusz Cedro et.al.|[2411.02540](http://arxiv.org/abs/2411.02540)|**[link](https://github.com/ADMAntwerp/GraphXAIN)**|
|**2024-11-04**|**Graph Neural Networks Based Deep Learning for Predicting Structural and Electronic Properties**|Selva Chandrasekaran Selvaraj et.al.|[2411.02331](http://arxiv.org/abs/2411.02331)|**[link](https://github.com/selvachandrasekaranselvaraj/GNN_prediction)**|
|**2024-11-04**|**Federated GNNs for EEG-Based Stroke Assessment**|Andrea Protani et.al.|[2411.02286](http://arxiv.org/abs/2411.02286)|null|
|**2024-11-04**|**On the Utilization of Unique Node Identifiers in Graph Neural Networks**|Maya Bechler-Speicher et.al.|[2411.02271](http://arxiv.org/abs/2411.02271)|null|
|**2024-11-04**|**Advancing Cyber-Attack Detection in Power Systems: A Comparative Study of Machine Learning and Graph Neural Network Approaches**|Tianzhixi Yin et.al.|[2411.02248](http://arxiv.org/abs/2411.02248)|null|
|**2024-11-04**|**Predicting the Temperature-Dependent CMC of Surfactant Mixtures with Graph Neural Networks**|Christoforos Brozos et.al.|[2411.02224](http://arxiv.org/abs/2411.02224)|**[link](https://github.com/brozosc/Predicting-the-Temperature-Dependent-CMC-of-Surfactant-Mixtures-with-Graph-Neural-Networks)**|
|**2024-11-04**|**Do graph neural network states contain graph properties?**|Tom Pelletreau-Duris et.al.|[2411.02168](http://arxiv.org/abs/2411.02168)|null|
|**2024-11-04**|**Physics-Constrained Graph Neural Networks for Spatio-Temporal Prediction of Drop Impact on OLED Display Panels**|Jiyong Kim et.al.|[2411.01848](http://arxiv.org/abs/2411.01848)|null|
|**2024-11-04**|**High-Pass Graph Convolutional Network for Enhanced Anomaly Detection: A Novel Approach**|Shelei Li et.al.|[2411.01817](http://arxiv.org/abs/2411.01817)|**[link](https://github.com/meteor0033/high-pass_gad)**|
|**2024-11-04**|**A General Recipe for Contractive Graph Neural Networks -- Technical Report**|Maya Bechler-Speicher et.al.|[2411.01717](http://arxiv.org/abs/2411.01717)|null|
|**2024-11-03**|**Lorentz-Equivariant Quantum Graph Neural Network for High-Energy Physics**|Md Abrar Jahin et.al.|[2411.01641](http://arxiv.org/abs/2411.01641)|null|
|**2024-10-31**|**The Importance of Being Scalable: Improving the Speed and Accuracy of Neural Network Interatomic Potentials Across Chemical Domains**|Eric Qu et.al.|[2410.24169](http://arxiv.org/abs/2410.24169)|**[link](https://github.com/ASK-Berkeley/EScAIP)**|
|**2024-10-31**|**Graph Learning for Numeric Planning**|Dillon Z. Chen et.al.|[2410.24080](http://arxiv.org/abs/2410.24080)|**[link](https://github.com/DillonZChen/goose)**|
|**2024-10-31**|**Detecting text level intellectual influence with knowledge graph embeddings**|Lucian Li et.al.|[2410.24021](http://arxiv.org/abs/2410.24021)|null|
|**2024-10-31**|**RAGraph: A General Retrieval-Augmented Graph Learning Framework**|Xinke Jiang et.al.|[2410.23855](http://arxiv.org/abs/2410.23855)|**[link](https://github.com/artessay/ragraph)**|
|**2024-10-31**|**Reducing Oversmoothing through Informed Weight Initialization in Graph Neural Networks**|Dimitrios Kelesis et.al.|[2410.23830](http://arxiv.org/abs/2410.23830)|null|
|**2024-10-31**|**Graph Neural Networks Uncover Geometric Neural Representations in Reinforcement-Based Motor Learning**|Federico Nardi et.al.|[2410.23812](http://arxiv.org/abs/2410.23812)|null|
|**2024-10-31**|**Enhancing Chess Reinforcement Learning with Graph Representation**|Tomas Rigaux et.al.|[2410.23753](http://arxiv.org/abs/2410.23753)|**[link](https://github.com/akulen/alphagateau)**|
|**2024-10-31**|**Exploring Consistency in Graph Representations:from Graph Kernels to Graph Neural Networks**|Xuyuan Liu et.al.|[2410.23748](http://arxiv.org/abs/2410.23748)|**[link](https://github.com/graphminddartmouth/graph-consistency)**|
|**2024-10-31**|**Towards Dynamic Message Passing on Graphs**|Junshu Sun et.al.|[2410.23686](http://arxiv.org/abs/2410.23686)|**[link](https://github.com/sunjss/N2)**|
|**2024-10-30**|**Multi-fidelity Machine Learning for Uncertainty Quantification and Optimization**|Ruda Zhang et.al.|[2410.23482](http://arxiv.org/abs/2410.23482)|null|
|**2024-10-30**|**Conditional Forecasting of Margin Calls using Dynamic Graph Neural Networks**|Matteo Citterio et.al.|[2410.23275](http://arxiv.org/abs/2410.23275)|null|
|**2024-10-30**|**NASM: Neural Anisotropic Surface Meshing**|Hongbo Li et.al.|[2410.23109](http://arxiv.org/abs/2410.23109)|null|
|**2024-10-30**|**Dual-Optimized Adaptive Graph Reconstruction for Multi-View Graph Clustering**|Zichen Wen et.al.|[2410.22983](http://arxiv.org/abs/2410.22983)|null|
|**2024-10-30**|**MassiveGNN: Efficient Training via Prefetching for Massively Connected Distributed Graphs**|Aishwarya Sarkar et.al.|[2410.22697](http://arxiv.org/abs/2410.22697)|**[link](https://github.com/pnnl/MassiveGNN)**|
|**2024-10-30**|**PV-VTT: A Privacy-Centric Dataset for Mission-Specific Anomaly Detection and Natural Language Interpretation**|Ryozo Masukawa et.al.|[2410.22623](http://arxiv.org/abs/2410.22623)|null|
|**2024-10-29**|**A Systematic Literature Review of Spatio-Temporal Graph Neural Network Models for Time Series Forecasting and Classification**|Flavio Corradini et.al.|[2410.22377](http://arxiv.org/abs/2410.22377)|**[link](https://github.com/VeritasYin/STGCN_IJCAI-18)**|
|**2024-10-29**|**Subgraph Aggregation for Out-of-Distribution Generalization on Graphs**|Bowen Liu et.al.|[2410.22228](http://arxiv.org/abs/2410.22228)|null|
|**2024-10-29**|**Vision Paper: Designing Graph Neural Networks in Compliance with the European Artificial Intelligence Act**|Barbara Hoffmann et.al.|[2410.22120](http://arxiv.org/abs/2410.22120)|null|
|**2024-10-29**|**LogSHIELD: A Graph-based Real-time Anomaly Detection Framework using Frequency Analysis**|Krishna Chandra Roy et.al.|[2410.21936](http://arxiv.org/abs/2410.21936)|null|
|**2024-10-29**|**Pushing the Limits of All-Atom Geometric Graph Neural Networks: Pre-Training, Scaling and Zero-Shot Transfer**|Zihan Pengmei et.al.|[2410.21683](http://arxiv.org/abs/2410.21683)|null|
|**2024-10-28**|**Graph Sparsification for Enhanced Conformal Prediction in Graph Neural Networks**|Yuntian He et.al.|[2410.21618](http://arxiv.org/abs/2410.21618)|null|
|**2024-10-28**|**Graph Based Traffic Analysis and Delay Prediction**|Gabriele Borg et.al.|[2410.21028](http://arxiv.org/abs/2410.21028)|null|
|**2024-10-28**|**A Review of Graph-Powered Data Quality Applications for IoT Monitoring Sensor Networks**|Pau Ferrer-Cid et.al.|[2410.21006](http://arxiv.org/abs/2410.21006)|null|
|**2024-10-28**|**SEG:Seeds-Enhanced Iterative Refinement Graph Neural Network for Entity Alignment**|Wei Ai et.al.|[2410.20733](http://arxiv.org/abs/2410.20733)|null|
|**2024-10-27**|**A Cosmic-Scale Benchmark for Symmetry-Preserving Data Processing**|Julia Balla et.al.|[2410.20516](http://arxiv.org/abs/2410.20516)|**[link](https://github.com/smsharma/eqnn-jax)**|
|**2024-10-27**|**Graph Neural Networks on Discriminative Graphs of Words**|Yassine Abbahaddou et.al.|[2410.20469](http://arxiv.org/abs/2410.20469)|**[link](https://github.com/abbahaddou/DGOW)**|
|**2024-10-27**|**Uncovering Capabilities of Model Pruning in Graph Contrastive Learning**|Wu Junran et.al.|[2410.20356](http://arxiv.org/abs/2410.20356)|null|
|**2024-10-27**|**DeCaf: A Causal Decoupling Framework for OOD Generalization on Node Classification**|Xiaoxue Han et.al.|[2410.20295](http://arxiv.org/abs/2410.20295)|null|
|**2024-10-26**|**Age of Information-Oriented Probabilistic Link Scheduling for Device-to-Device Networks**|Lixin Wang et.al.|[2410.20196](http://arxiv.org/abs/2410.20196)|null|
|**2024-10-26**|**FedSSP: Federated Graph Learning with Spectral Knowledge and Personalized Preference**|Zihan Tan et.al.|[2410.20105](http://arxiv.org/abs/2410.20105)|**[link](https://github.com/oakleytan/fedssp)**|
|**2024-10-25**|**Global Graph Counterfactual Explanation: A Subgraph Mapping Approach**|Yinhan He et.al.|[2410.19978](http://arxiv.org/abs/2410.19978)|null|
|**2024-10-25**|**Sparse Decomposition of Graph Neural Networks**|Yaochen Hu et.al.|[2410.19723](http://arxiv.org/abs/2410.19723)|null|
|**2024-10-25**|**DeMuVGN: Effective Software Defect Prediction Model by Learning Multi-view Software Dependency via Graph Neural Networks**|Yu Qiao et.al.|[2410.19550](http://arxiv.org/abs/2410.19550)|null|
|**2024-10-25**|**An Enhanced Hierarchical Planning Framework for Multi-Robot Autonomous Exploration**|Gengyuan Cai et.al.|[2410.19373](http://arxiv.org/abs/2410.19373)|null|
|**2024-10-25**|**Double Difference Earthquake Location with Graph Neural Networks**|Ian W. McBrearty et.al.|[2410.19323](http://arxiv.org/abs/2410.19323)|null|
|**2024-10-25**|**A Survey of Deep Graph Learning under Distribution Shifts: from Graph Out-of-Distribution Generalization to Adaptation**|Kexin Zhang et.al.|[2410.19265](http://arxiv.org/abs/2410.19265)|**[link](https://github.com/kaize0409/awesome-graph-ood)**|
|**2024-10-24**|**Enriching GNNs with Text Contextual Representations for Detecting Disinformation Campaigns on Social Media**|Bruno Croso Cunha da Silva et.al.|[2410.19193](http://arxiv.org/abs/2410.19193)|**[link](https://github.com/brunocroso/contextualgnns-fakenews)**|
|**2024-10-24**|**Dynamic 3D Gaussian Tracking for Graph-Based Neural Dynamics Modeling**|Mingtong Zhang et.al.|[2410.18912](http://arxiv.org/abs/2410.18912)|null|
|**2024-10-24**|**Leveraging Graph Neural Networks and Multi-Agent Reinforcement Learning for Inventory Control in Supply Chains**|Niki Kotecha et.al.|[2410.18631](http://arxiv.org/abs/2410.18631)|null|
|**2024-10-24**|**Binary Code Similarity Detection via Graph Contrastive Learning on Intermediate Representations**|Xiuwei Shang et.al.|[2410.18561](http://arxiv.org/abs/2410.18561)|null|
|**2024-10-24**|**Graph Pre-Training Models Are Strong Anomaly Detectors**|Jiashun Cheng et.al.|[2410.18487](http://arxiv.org/abs/2410.18487)|null|
|**2024-10-23**|**GraphTeam: Facilitating Large Language Model-based Graph Analysis via Multi-Agent Collaboration**|Xin Li et.al.|[2410.18032](http://arxiv.org/abs/2410.18032)|**[link](https://github.com/bupt-gamma/graphteam)**|
|**2024-10-23**|**Spiking Graph Neural Network on Riemannian Manifolds**|Li Sun et.al.|[2410.17941](http://arxiv.org/abs/2410.17941)|**[link](https://github.com/ZhenhHuang/MSG)**|
|**2024-10-23**|**TopoQA: a topological deep learning-based approach for protein complex structure interface quality assessment**|Bingqing Han et.al.|[2410.17815](http://arxiv.org/abs/2410.17815)|null|
|**2024-10-23**|**Proteome-wide prediction of mode of inheritance and molecular mechanism underlying genetic diseases using structural interactomics**|Ali Saadat et.al.|[2410.17708](http://arxiv.org/abs/2410.17708)|**[link](https://github.com/alisaadatv/structural-interactomics)**|
|**2024-10-23**|**Exploring structure diversity in atomic resolution microscopy with graph neural networks**|Zheng Luo et.al.|[2410.17631](http://arxiv.org/abs/2410.17631)|null|
|**2024-10-23**|**Self-Supervised Graph Neural Networks for Enhanced Feature Extraction in Heterogeneous Information Networks**|Jianjun Wei et.al.|[2410.17617](http://arxiv.org/abs/2410.17617)|null|
|**2024-10-23**|**GDDA: Semantic OOD Detection on Graphs under Covariate Shift via Score-Based Diffusion Models**|Zhixia He et.al.|[2410.17526](http://arxiv.org/abs/2410.17526)|null|
|**2024-10-22**|**Scalable Implicit Graphon Learning**|Ali Azizpour et.al.|[2410.17464](http://arxiv.org/abs/2410.17464)|**[link](https://github.com/aliaaz99/SIGL)**|
|**2024-10-22**|**Graph Neural Network-Accelerated Network-Reconfigured Optimal Power Flow**|Thuan Pham et.al.|[2410.17460](http://arxiv.org/abs/2410.17460)|null|
|**2024-10-22**|**Geometric Graph Neural Network Modeling of Human Interactions in Crowded Environments**|Sara Honarvar et.al.|[2410.17409](http://arxiv.org/abs/2410.17409)|null|
|**2024-10-22**|**Learning Load Balancing with GNN in MPTCP-Enabled Heterogeneous Networks**|Han Ji et.al.|[2410.17118](http://arxiv.org/abs/2410.17118)|**[link](https://github.com/hanji-ucd/gnn-hetnet)**|
|**2024-10-22**|**Graph Neural Networks for Edge Signals: Orientation Equivariance and Invariance**|Dominik Fuchsgruber et.al.|[2410.16935](http://arxiv.org/abs/2410.16935)|null|
|**2024-10-22**|**Dynamic graph neural networks for enhanced volatility prediction in financial markets**|Pulikandala Nithish Kumar et.al.|[2410.16858](http://arxiv.org/abs/2410.16858)|null|
|**2024-10-22**|**Fast Graph Sharpness-Aware Minimization for Enhancing and Accelerating Few-Shot Node Classification**|Yihong Luo et.al.|[2410.16845](http://arxiv.org/abs/2410.16845)|**[link](https://github.com/draym28/fgsam_neurips24)**|
|**2024-10-22**|**Can Large Language Models Act as Ensembler for Multi-GNNs?**|Hanqi Duan et.al.|[2410.16822](http://arxiv.org/abs/2410.16822)|null|
|**2024-10-22**|**GALA: Graph Diffusion-based Alignment with Jigsaw for Source-free Domain Adaptation**|Junyu Luo et.al.|[2410.16606](http://arxiv.org/abs/2410.16606)|**[link](https://github.com/luo-junyu/gala)**|
|**2024-10-22**|**Graph Sampling for Scalable and Expressive Graph Neural Networks on Homophilic Graphs**|Haolin Li et.al.|[2410.16593](http://arxiv.org/abs/2410.16593)|null|
|**2024-10-21**|**Theoretical Insights into Line Graph Transformation on Graph Learning**|Fan Yang et.al.|[2410.16138](http://arxiv.org/abs/2410.16138)|**[link](https://github.com/lukeyf/graphs-and-lines)**|
|**2024-10-21**|**Accelerating Discovery of Extreme Lattice Thermal Conductivity by Crystal Attention Graph Neural Network (CATGNN) Using Chemical Bonding Intuitive Descriptors**|Mohammed Al-Fahdi et.al.|[2410.16066](http://arxiv.org/abs/2410.16066)|null|
|**2024-10-21**|**Resilient Temporal GCN for Smart Grid State Estimation Under Topology Inaccuracies**|Seyed Hamed Haghshenas et.al.|[2410.16008](http://arxiv.org/abs/2410.16008)|null|
|**2024-10-21**|**Focus Where It Matters: Graph Selective State Focused Attention Networks**|Shikhar Vashistha et.al.|[2410.15849](http://arxiv.org/abs/2410.15849)|null|
|**2024-10-21**|**Deep Graph Attention Networks**|Jun Kato et.al.|[2410.15640](http://arxiv.org/abs/2410.15640)|**[link](https://github.com/JNKT215/DeepGAT_CANDAR)**|
|**2024-10-21**|**Gradient Rewiring for Editable Graph Neural Network Training**|Zhimeng Jiang et.al.|[2410.15556](http://arxiv.org/abs/2410.15556)|**[link](https://github.com/zhimengj0326/gradient_rewiring_editing)**|
|**2024-10-20**|**DNA Language Model and Interpretable Graph Neural Network Identify Genes and Pathways Involved in Rare Diseases**|Ali Saadat et.al.|[2410.15367](http://arxiv.org/abs/2410.15367)|**[link](https://github.com/AliSaadatV/Causal-Gene-Pathway-Finder)**|
|**2024-10-20**|**Tensor-Fused Multi-View Graph Contrastive Learning**|Yujia Wu et.al.|[2410.15247](http://arxiv.org/abs/2410.15247)|**[link](https://github.com/cs-sail/tensor-mv-gcl)**|
|**2024-10-20**|**Conditional Uncertainty Quantification for Tensorized Topological Neural Networks**|Yujia Wu et.al.|[2410.15241](http://arxiv.org/abs/2410.15241)|null|
|**2024-10-20**|**Conditional Prediction ROC Bands for Graph Classification**|Yujia Wu et.al.|[2410.15239](http://arxiv.org/abs/2410.15239)|**[link](https://github.com/CS-SAIL/UQ-GNN-ROC)**|
|**2024-10-18**|**Convergence of Manifold Filter-Combine Networks**|David R. Johnson et.al.|[2410.14639](http://arxiv.org/abs/2410.14639)|**[link](https://github.com/dj408/mfcn)**|
|**2024-10-18**|**Graph Neural Patching for Cold-Start Recommendations**|Hao Chen et.al.|[2410.14241](http://arxiv.org/abs/2410.14241)|null|
|**2024-10-18**|**Improving Graph Neural Networks by Learning Continuous Edge Directions**|Seong Ho Pahng et.al.|[2410.14109](http://arxiv.org/abs/2410.14109)|**[link](https://github.com/hormoz-lab/coed-gnn)**|
|**2024-10-18**|**DMGNN: Detecting and Mitigating Backdoor Attacks in Graph Neural Networks**|Hao Sui et.al.|[2410.14105](http://arxiv.org/abs/2410.14105)|null|
|**2024-10-17**|**Conformal Prediction for Federated Graph Neural Networks with Missing Neighbor Information**|Ömer Faruk Akgül et.al.|[2410.14010](http://arxiv.org/abs/2410.14010)|null|
|**2024-10-17**|**Trojan Prompt Attacks on Graph Neural Networks**|Minhua Lin et.al.|[2410.13974](http://arxiv.org/abs/2410.13974)|null|
|**2024-10-17**|**Enhancing universal machine learning potentials with polarizable long-range interactions**|Rongzhi Gao et.al.|[2410.13820](http://arxiv.org/abs/2410.13820)|**[link](https://github.com/reaxnet/jax-nb)**|
|**2024-10-17**|**Learning Graph Quantized Tokenizers for Transformers**|Limei Wang et.al.|[2410.13798](http://arxiv.org/abs/2410.13798)|**[link](https://github.com/limei0307/graph-tokenizer)**|
|**2024-10-17**|**Rapid and Automated Alloy Design with Graph Neural Network-Powered LLM-Driven Multi-Agent Systems**|Alireza Ghafarollahi et.al.|[2410.13768](http://arxiv.org/abs/2410.13768)|null|
|**2024-10-17**|**GDeR: Safeguarding Efficiency, Balancing, and Robustness via Prototypical Graph Pruning**|Guibin Zhang et.al.|[2410.13761](http://arxiv.org/abs/2410.13761)|**[link](https://github.com/ins1stenc3/gder)**|
|**2024-10-17**|**Observation of a rare beta decay of the charmed baryon with a Graph Neural Network**|BESIII Collaboration et.al.|[2410.13515](http://arxiv.org/abs/2410.13515)|null|
|**2024-10-17**|**CERES: Critical-Event Reconstruction via Temporal Scene Graph Completion**|Efimia Panagiotaki et.al.|[2410.13514](http://arxiv.org/abs/2410.13514)|null|
|**2024-10-17**|**Interpreting Temporal Graph Neural Networks with Koopman Theory**|Michele Guerra et.al.|[2410.13469](http://arxiv.org/abs/2410.13469)|**[link](https://github.com/ngmlgroup/koopman-tgnn-interpretability)**|
|**2024-10-17**|**Multi-frame Detection via Graph Neural Networks: A Link Prediction Approach**|Zhihao Lin et.al.|[2410.13436](http://arxiv.org/abs/2410.13436)|null|
|**2024-10-17**|**Addressing Heterogeneity and Heterophily in Graphs: A Heterogeneous Heterophilic Spectral Graph Neural Network**|Kangkang Lu et.al.|[2410.13373](http://arxiv.org/abs/2410.13373)|null|
|**2024-10-17**|**GeSubNet: Gene Interaction Inference for Disease Subtype Network Generation**|Ziwei Yang et.al.|[2410.13178](http://arxiv.org/abs/2410.13178)|null|
|**2024-10-16**|**Just Ramp-up: Unleash the Potential of Regression-based Estimator for A/B Tests under Network Interference**|Qianyi Chen et.al.|[2410.12740](http://arxiv.org/abs/2410.12740)|**[link](https://github.com/cqyiiii/just-ramp-up)**|
|**2024-10-16**|**Expand and Compress: Exploring Tuning Principles for Continual Spatio-Temporal Graph Forecasting**|Wei Chen et.al.|[2410.12593](http://arxiv.org/abs/2410.12593)|null|
|**2024-10-16**|**Perseus: Leveraging Common Data Patterns with Curriculum Learning for More Robust Graph Neural Networks**|Kaiwen Xia et.al.|[2410.12425](http://arxiv.org/abs/2410.12425)|null|
|**2024-10-16**|**Federated Temporal Graph Clustering**|Yang Liu et.al.|[2410.12343](http://arxiv.org/abs/2410.12343)|null|
|**2024-10-16**|**Learning Differentiable Tensegrity Dynamics using Graph Neural Networks**|Nelson Chen et.al.|[2410.12216](http://arxiv.org/abs/2410.12216)|**[link](https://github.com/nchen9191/tensegrity_gnn_simulator_public)**|
|**2024-10-16**|**FragNet: A Graph Neural Network for Molecular Property Prediction with Four Layers of Interpretability**|Gihan Panapitiya et.al.|[2410.12156](http://arxiv.org/abs/2410.12156)|**[link](https://github.com/pnnl/FragNet)**|
|**2024-10-15**|**Bridging Large Language Models and Graph Structure Learning Models for Robust Representation Learning**|Guangxin Su et.al.|[2410.12096](http://arxiv.org/abs/2410.12096)|null|
|**2024-10-15**|**An Online Self-learning Graph-based Lateral Controller for Self-Driving Cars**|Jilan Samiuddin et.al.|[2410.11979](http://arxiv.org/abs/2410.11979)|null|
|**2024-10-15**|**Regional Ocean Forecasting with Hierarchical Graph Neural Networks**|Daniel Holmberg et.al.|[2410.11807](http://arxiv.org/abs/2410.11807)|**[link](https://github.com/deinal/seacast)**|
|**2024-10-15**|**G-Designer: Architecting Multi-agent Communication Topologies via Graph Neural Networks**|Guibin Zhang et.al.|[2410.11782](http://arxiv.org/abs/2410.11782)|null|
|**2024-10-15**|**ECGN: A Cluster-Aware Approach to Graph Neural Networks for Imbalanced Classification**|Bishal Thapaliya et.al.|[2410.11765](http://arxiv.org/abs/2410.11765)|**[link](https://github.com/anonymous753341/ecgn)**|
|**2024-10-15**|**Towards Fair Graph Representation Learning in Social Networks**|Guixian Zhang et.al.|[2410.11493](http://arxiv.org/abs/2410.11493)|null|
|**2024-10-15**|**CoActionGraphRec: Sequential Multi-Interest Recommendations Using Co-Action Graphs**|Yi Sun et.al.|[2410.11464](http://arxiv.org/abs/2410.11464)|null|
|**2024-10-15**|**Are High-Degree Representations Really Unnecessary in Equivariant Graph Neural Networks?**|Jiacheng Cen et.al.|[2410.11443](http://arxiv.org/abs/2410.11443)|**[link](https://github.com/GLAD-RUC/HEGNN)**|
|**2024-10-15**|**KA-GNN: Kolmogorov-Arnold Graph Neural Networks for Molecular Property Prediction**|Longlong Li et.al.|[2410.11323](http://arxiv.org/abs/2410.11323)|null|
|**2024-10-15**|**Backdoor Attack on Vertical Federated Graph Neural Network Learning**|Jirui Yang et.al.|[2410.11290](http://arxiv.org/abs/2410.11290)|null|
|**2024-10-15**|**Rethinking Graph Transformer Architecture Design for Node Classification**|Jiajun Zhou et.al.|[2410.11189](http://arxiv.org/abs/2410.11189)|null|
|**2024-10-16**|**NAR-*ICP: Neural Execution of Classical ICP-based Pointcloud Registration Algorithms**|Efimia Panagiotaki et.al.|[2410.11031](http://arxiv.org/abs/2410.11031)|null|
|**2024-10-14**|**Arrhythmia Classification Using Graph Neural Networks Based on Correlation Matrix**|Seungwoo Han et.al.|[2410.10758](http://arxiv.org/abs/2410.10758)|null|
|**2024-10-14**|**NT-LLM: A Novel Node Tokenizer for Integrating Graph Structure into Large Language Models**|Yanbiao Ji et.al.|[2410.10743](http://arxiv.org/abs/2410.10743)|null|
|**2024-10-14**|**A Personalized MOOC Learning Group and Course Recommendation Method Based on Graph Neural Network and Social Network Analysis**|Zijin Luo et.al.|[2410.10658](http://arxiv.org/abs/2410.10658)|null|
|**2024-10-14**|**TopoFR: A Closer Look at Topology Alignment on Face Recognition**|Jun Dan et.al.|[2410.10587](http://arxiv.org/abs/2410.10587)|**[link](https://github.com/modelscope/facechain)**|
|**2024-10-14**|**Graph Classification Gaussian Processes via Hodgelet Spectral Features**|Mathieu Alain et.al.|[2410.10546](http://arxiv.org/abs/2410.10546)|null|
|**2024-10-14**|**Replay-and-Forget-Free Graph Class-Incremental Learning: A Task Profiling and Prompting Approach**|Chaoxi Niu et.al.|[2410.10341](http://arxiv.org/abs/2410.10341)|**[link](https://github.com/mala-lab/tpp)**|
|**2024-10-14**|**DiRW: Path-Aware Digraph Learning for Heterophily**|Daohan Su et.al.|[2410.10320](http://arxiv.org/abs/2410.10320)|null|
|**2024-10-14**|**Enhancing Attributed Graph Networks with Alignment and Uniformity Constraints for Session-based Recommendation**|Xinping Zhao et.al.|[2410.10296](http://arxiv.org/abs/2410.10296)|**[link](https://github.com/itsukifujii/attrgau)**|
|**2024-10-14**|**Towards Bridging Generalization and Expressivity of Graph Neural Networks**|Shouheng Li et.al.|[2410.10051](http://arxiv.org/abs/2410.10051)|null|
|**2024-10-13**|**Online Multi-modal Root Cause Analysis**|Lecheng Zheng et.al.|[2410.10021](http://arxiv.org/abs/2410.10021)|null|
|**2024-10-11**|**M $^3$ -Impute: Mask-guided Representation Learning for Missing Value Imputation**|Zhongyi Yu et.al.|[2410.08794](http://arxiv.org/abs/2410.08794)|**[link](https://github.com/alleinx/m3-impute)**|
|**2024-10-11**|**Enhancing GNNs with Architecture-Agnostic Graph Transformations: A Systematic Analysis**|Zhifei Li et.al.|[2410.08759](http://arxiv.org/abs/2410.08759)|null|
|**2024-10-11**|**Enhanced Robot Planning and Perception through Environment Prediction**|Vishnu Dutt Sharma et.al.|[2410.08560](http://arxiv.org/abs/2410.08560)|null|
|**2024-10-11**|**IGNN-Solver: A Graph Neural Solver for Implicit Graph Neural Networks**|Junchao Lin et.al.|[2410.08524](http://arxiv.org/abs/2410.08524)|null|
|**2024-10-10**|**KnowGraph: Knowledge-Enabled Anomaly Detection via Logical Reasoning on Graph Data**|Andy Zhou et.al.|[2410.08390](http://arxiv.org/abs/2410.08390)|null|
|**2024-10-10**|**Heterogeneous Graph Auto-Encoder for CreditCard Fraud Detection**|Moirangthem Tiken Singh et.al.|[2410.08121](http://arxiv.org/abs/2410.08121)|null|
|**2024-10-10**|**Learning Equivariant Non-Local Electron Density Functionals**|Nicholas Gao et.al.|[2410.07972](http://arxiv.org/abs/2410.07972)|null|
|**2024-10-10**|**HeGraphAdapter: Tuning Multi-Modal Vision-Language Models with Heterogeneous Graph Adapter**|Yumiao Zhao et.al.|[2410.07854](http://arxiv.org/abs/2410.07854)|null|
|**2024-10-10**|**A note on the VC dimension of 1-dimensional GNNs**|Noah Daniëls et.al.|[2410.07829](http://arxiv.org/abs/2410.07829)|null|
|**2024-10-10**|**Generalizable Indoor Human Activity Recognition Method Based on Micro-Doppler Corner Point Cloud and Dynamic Graph Learning**|Xiaopeng Yang et.al.|[2410.07542](http://arxiv.org/abs/2410.07542)|null|
|**2024-10-09**|**Collective variables of neural networks: empirical time evolution and scaling laws**|Samuel Tovey et.al.|[2410.07451](http://arxiv.org/abs/2410.07451)|null|
|**2024-10-09**|**Collusion Detection with Graph Neural Networks**|Lucas Gomes et.al.|[2410.07091](http://arxiv.org/abs/2410.07091)|null|
|**2024-10-09**|**Let's Ask GNN: Empowering Large Language Model for Graph In-Context Learning**|Zhengyu Hu et.al.|[2410.07074](http://arxiv.org/abs/2410.07074)|null|
|**2024-10-09**|**AdaRC: Mitigating Graph Structure Shifts during Test-Time**|Wenxuan Bao et.al.|[2410.06976](http://arxiv.org/abs/2410.06976)|null|
|**2024-10-09**|**DLGNet: Hyperedge Classification through Directed Line Graphs for Chemical Reactions**|Stefano Fiorini et.al.|[2410.06969](http://arxiv.org/abs/2410.06969)|null|
|**2024-10-09**|**Faithful Interpretation for Graph Neural Networks**|Lijie Hu et.al.|[2410.06950](http://arxiv.org/abs/2410.06950)|null|
|**2024-10-09**|**TopoTune : A Framework for Generalized Combinatorial Complex Neural Networks**|Mathilde Papillon et.al.|[2410.06530](http://arxiv.org/abs/2410.06530)|**[link](https://github.com/geometric-intelligence/topobenchmark)**|
|**2024-10-09**|**A Benchmark on Directed Graph Representation Learning in Hardware Designs**|Haoyu Wang et.al.|[2410.06460](http://arxiv.org/abs/2410.06460)|null|
|**2024-10-08**|**UnSeGArmaNet: Unsupervised Image Segmentation using Graph Neural Networks with Convolutional ARMA Filters**|Kovvuri Sai Gopal Reddy et.al.|[2410.06114](http://arxiv.org/abs/2410.06114)|**[link](https://github.com/ksgr5566/unsegarmanet)**|
|**2024-10-08**|**TIMBA: Time series Imputation with Bi-directional Mamba Blocks and Diffusion models**|Javier Solís-García et.al.|[2410.05916](http://arxiv.org/abs/2410.05916)|null|
|**2024-10-08**|**Equi-GSPR: Equivariant SE(3) Graph Network Model for Sparse Point Cloud Registration**|Xueyang Kang et.al.|[2410.05729](http://arxiv.org/abs/2410.05729)|**[link](https://github.com/alexandor91/se3-equi-graph-registration)**|
|**2024-10-07**|**Taming Gradient Oversmoothing and Expansion in Graph Neural Networks**|MoonJeong Park et.al.|[2410.04824](http://arxiv.org/abs/2410.04824)|null|
|**2024-10-07**|**Physics-Informed GNN for non-linear constrained optimization: PINCO a solver for the AC-optimal power flow**|Anna Varbella et.al.|[2410.04818](http://arxiv.org/abs/2410.04818)|null|
|**2024-10-07**|**When GDD meets GNN: A Knowledge-driven Neural Connection for Effective Entity Resolution in Property Graphs**|Junwei Hu et.al.|[2410.04783](http://arxiv.org/abs/2410.04783)|**[link](https://github.com/zaiwen/entity_resolution_junwei_hu)**|
|**2024-10-07**|**A Clifford Algebraic Approach to E(n)-Equivariant High-order Graph Neural Networks**|Hoang-Viet Tran et.al.|[2410.04692](http://arxiv.org/abs/2410.04692)|null|
|**2024-10-06**|**Modeling Social Media Recommendation Impacts Using Academic Networks: A Graph Neural Network Approach**|Sabrina Guidotti et.al.|[2410.04552](http://arxiv.org/abs/2410.04552)|**[link](https://github.com/dimneurolab/academic_network_project)**|
|**2024-10-05**|**Unveiling the Impact of Local Homophily on GNN Fairness: In-Depth Analysis and New Benchmarks**|Donald Loveland et.al.|[2410.04287](http://arxiv.org/abs/2410.04287)|null|
|**2024-10-05**|**Applying Hybrid Graph Neural Networks to Strengthen Credit Risk Analysis**|Mengfang Sun et.al.|[2410.04283](http://arxiv.org/abs/2410.04283)|null|
|**2024-10-05**|**Enhancing Future Link Prediction in Quantum Computing Semantic Networks through LLM-Initiated Node Features**|Gilchan Park et.al.|[2410.04251](http://arxiv.org/abs/2410.04251)|**[link](https://github.com/boxorange/QC-LinkPrediction)**|
|**2024-10-05**|**Multimodal Large Language Models for Inverse Molecular Design with Retrosynthetic Planning**|Gang Liu et.al.|[2410.04223](http://arxiv.org/abs/2410.04223)|**[link](https://github.com/liugangcode/Llamole)**|
|**2024-10-05**|**Improving Temporal Link Prediction via Temporal Walk Matrix Projection**|Xiaodong Lu et.al.|[2410.04013](http://arxiv.org/abs/2410.04013)|**[link](https://github.com/lxd99/tpnet)**|
|**2024-10-04**|**Fine-Grained Expressive Power of Weisfeiler-Leman: A Homomorphism Counting Perspective**|Junru Zhou et.al.|[2410.03517](http://arxiv.org/abs/2410.03517)|**[link](https://github.com/zml72062/pebble_game)**|
|**2024-10-04**|**Self-supervised Spatio-Temporal Graph Mask-Passing Attention Network for Perceptual Importance Prediction of Multi-point Tactility**|Dazhong He et.al.|[2410.03434](http://arxiv.org/abs/2410.03434)|null|
|**2024-10-04**|**Cayley Graph Propagation**|JJ Wilson et.al.|[2410.03424](http://arxiv.org/abs/2410.03424)|**[link](https://github.com/josephjwilson/cayley_graph_propagation)**|
|**2024-10-03**|**LLMCO2: Advancing Accurate Carbon Footprint Prediction for LLM Inferences**|Zhenxiao Fu et.al.|[2410.02950](http://arxiv.org/abs/2410.02950)|null|
|**2024-10-03**|**Diss-l-ECT: Dissecting Graph Data with local Euler Characteristic Transforms**|Julius von Rohrscheidt et.al.|[2410.02622](http://arxiv.org/abs/2410.02622)|null|
|**2024-10-03**|**Boosting Sample Efficiency and Generalization in Multi-agent Reinforcement Learning via Equivariance**|Joshua McClellan et.al.|[2410.02581](http://arxiv.org/abs/2410.02581)|null|
|**2024-10-03**|**A Comprehensive Survey of Mamba Architectures for Medical Image Analysis: Classification, Segmentation, Restoration and Beyond**|Shubhi Bansal et.al.|[2410.02362](http://arxiv.org/abs/2410.02362)|**[link](https://github.com/madhavaprasath23/awesome-mamba-papers-on-medical-domain)**|
|**2024-10-03**|**Language Models are Graph Learners**|Zhe Xu et.al.|[2410.02296](http://arxiv.org/abs/2410.02296)|null|
|**2024-10-03**|**Model-Based GNN Enabled Energy-Efficient Beamforming for Ultra-Dense Wireless Networks**|Rongsheng Zhang et.al.|[2410.02289](http://arxiv.org/abs/2410.02289)|null|
|**2024-10-03**|**GNN-Enabled Optimization of Placement and Transmission Design for UAV Communications**|Qinyu Wang et.al.|[2410.02277](http://arxiv.org/abs/2410.02277)|null|
|**2024-10-03**|**ClassContrast: Bridging the Spatial and Contextual Gaps for Node Representations**|Md Joshem Uddin et.al.|[2410.02158](http://arxiv.org/abs/2410.02158)|null|
|**2024-10-03**|**A Comprehensive Review of Propagation Models in Complex Networks: From Deterministic to Deep Learning Approaches**|Bin Wu et.al.|[2410.02118](http://arxiv.org/abs/2410.02118)|null|
|**2024-10-02**|**FARM: Functional Group-Aware Representations for Small Molecules**|Thao Nguyen et.al.|[2410.02082](http://arxiv.org/abs/2410.02082)|null|
|**2024-10-02**|**FLAG: Financial Long Document Classification via AMR-based GNN**|Bolun et.al.|[2410.02024](http://arxiv.org/abs/2410.02024)|**[link](https://github.com/namir0806/flag)**|
|**2024-10-02**|**PROXI: Challenging the GNNs for Link Prediction**|Astrit Tola et.al.|[2410.01802](http://arxiv.org/abs/2410.01802)|**[link](https://github.com/workrep20232/proxi)**|
|**2024-10-02**|**Scalable and Consistent Graph Neural Networks for Distributed Mesh-based Data-driven Modeling**|Shivam Barwey et.al.|[2410.01657](http://arxiv.org/abs/2410.01657)|null|
|**2024-10-02**|**Accessing Numerical Energy Hessians with Graph Neural Network Potentials and Their Application in Heterogeneous Catalysis**|Brook Wander et.al.|[2410.01650](http://arxiv.org/abs/2410.01650)|**[link](https://github.com/jmusiel/gibby)**|
|**2024-10-02**|**Verbalized Graph Representation Learning: A Fully Interpretable Graph Model Based on Large Language Models Throughout the Entire Process**|Xingyu Ji et.al.|[2410.01457](http://arxiv.org/abs/2410.01457)|null|
|**2024-10-02**|**Towards Dynamic Graph Neural Networks with Provably High-Order Expressive Power**|Zhe Wang et.al.|[2410.01367](http://arxiv.org/abs/2410.01367)|null|
|**2024-10-02**|**Rethinking the Expressiveness of GNNs: A Computational Model Perspective**|Guanyu Cui et.al.|[2410.01308](http://arxiv.org/abs/2410.01308)|null|
|**2024-10-02**|**"No Matter What You Do!": Mitigating Backdoor Attacks in Graph Neural Networks**|Jiale Zhang et.al.|[2410.01272](http://arxiv.org/abs/2410.01272)|**[link](https://github.com/graph-axis/gcleaner)**|
|**2024-10-01**|**GAMMA-PD: Graph-based Analysis of Multi-Modal Motor Impairment Assessments in Parkinson's Disease**|Favour Nerrise et.al.|[2410.00944](http://arxiv.org/abs/2410.00944)|null|
|**2024-10-01**|**Review of blockchain application with Graph Neural Networks, Graph Convolutional Networks and Convolutional Neural Networks**|Amy Ancelotti et.al.|[2410.00875](http://arxiv.org/abs/2410.00875)|null|
|**2024-10-01**|**WiGNet: Windowed Vision Graph Neural Network**|Gabriele Spadaro et.al.|[2410.00807](http://arxiv.org/abs/2410.00807)|**[link](https://github.com/eidoslab/wignet)**|
|**2024-09-30**|**geom2vec: pretrained GNNs as geometric featurizers for conformational dynamics**|Zihan Pengmei et.al.|[2409.19838](http://arxiv.org/abs/2409.19838)|**[link](https://github.com/zpengmei/geom2vec)**|
|**2024-09-29**|**Generalizability of Graph Neural Networks for Decentralized Unlabeled Motion Planning**|Shreyas Muthusamy et.al.|[2409.19829](http://arxiv.org/abs/2409.19829)|null|
|**2024-09-29**|**A Survey on Graph Neural Networks for Remaining Useful Life Prediction: Methodologies, Evaluation and Future Trends**|Yucheng Wang et.al.|[2409.19629](http://arxiv.org/abs/2409.19629)|**[link](https://github.com/Frank-Wang-oss/GNN_RUL_Benchmarking)**|
|**2024-10-01**|**DropEdge not Foolproof: Effective Augmentation Method for Signed Graph Neural Networks**|Zeyu Zhang et.al.|[2409.19620](http://arxiv.org/abs/2409.19620)|null|
|**2024-09-29**|**DuoGNN: Topology-aware Graph Neural Network with Homophily and Heterophily Interaction-Decoupling**|K. Mancini et.al.|[2409.19616](http://arxiv.org/abs/2409.19616)|**[link](https://github.com/basiralab/duognn)**|
|**2024-09-29**|**MASKDROID: Robust Android Malware Detection with Masked Graph Representations**|Jingnan Zheng et.al.|[2409.19594](http://arxiv.org/abs/2409.19594)|**[link](https://github.com/SophieZheng998/MaskDroid)**|
|**2024-09-29**|**One Node Per User: Node-Level Federated Learning for Graph Neural Networks**|Zhidong Gao et.al.|[2409.19513](http://arxiv.org/abs/2409.19513)|null|
|**2024-09-28**|**Sequential Signal Mixing Aggregation for Message Passing Graph Neural Networks**|Mitchell Keren Taraday et.al.|[2409.19414](http://arxiv.org/abs/2409.19414)|**[link](https://github.com/AlmogDavid/SSMA)**|
|**2024-09-27**|**TwinCL: A Twin Graph Contrastive Learning Model for Collaborative Filtering**|Chengkai Liu et.al.|[2409.19169](http://arxiv.org/abs/2409.19169)|**[link](https://github.com/chengkai-liu/TwinCL)**|
|**2024-09-27**|**Enhancing Robustness of Graph Neural Networks through p-Laplacian**|Anuj Kumar Sirohi et.al.|[2409.19096](http://arxiv.org/abs/2409.19096)|null|
|**2024-09-27**|**Positional Encoder Graph Quantile Neural Networks for Geographic Data**|William E. R. de Amorim et.al.|[2409.18865](http://arxiv.org/abs/2409.18865)|**[link](https://github.com/konstantinklemmer/pe-gnn)**|
|**2024-09-27**|**HardCore Generation: Generating Hard UNSAT Problems for Data Augmentation**|Joseph Cotnareanu et.al.|[2409.18778](http://arxiv.org/abs/2409.18778)|null|
|**2024-09-27**|**Geometric deep learning for galaxy-halo connection: a case study for galaxy intrinsic alignments**|Yesukhei Jagvaral et.al.|[2409.18761](http://arxiv.org/abs/2409.18761)|null|
|**2024-09-27**|**Review of Digital Asset Development with Graph Neural Network Unlearning**|Zara Lisbon et.al.|[2409.18455](http://arxiv.org/abs/2409.18455)|null|
|**2024-09-26**|**Causality-based Subject and Task Fingerprints using fMRI Time-series Data**|Dachuan Song et.al.|[2409.18298](http://arxiv.org/abs/2409.18298)|null|
|**2024-09-26**|**Learning Beamforming in Cell-Free Massive MIMO ISAC Systems**|Umut Demirhan et.al.|[2409.18237](http://arxiv.org/abs/2409.18237)|null|
|**2024-09-26**|**Spatiotemporal Learning on Cell-embedded Graphs**|Yuan Mi et.al.|[2409.18013](http://arxiv.org/abs/2409.18013)|null|
|**2024-09-26**|**Supra-Laplacian Encoding for Transformer on Dynamic Graphs**|Yannis Karmim et.al.|[2409.17986](http://arxiv.org/abs/2409.17986)|**[link](https://github.com/ykrmm/slate)**|
|**2024-09-26**|**Modeling the Popularity of Events on Web by Sparsity and Mutual-Excitation Guided Graph Neural Network**|Jiaxin Deng et.al.|[2409.17678](http://arxiv.org/abs/2409.17678)|**[link](https://github.com/pangjunbiao/hot-events-dataset)**|
|**2024-09-26**|**Hand-object reconstruction via interaction-aware graph attention mechanism**|Taeyun Woo et.al.|[2409.17629](http://arxiv.org/abs/2409.17629)|null|
|**2024-09-26**|**Convolutional Signal Propagation: A Simple Scalable Algorithm for Hypergraphs**|Pavel Procházka et.al.|[2409.17628](http://arxiv.org/abs/2409.17628)|null|
|**2024-09-26**|**Neural P $^3$ M: A Long-Range Interaction Modeling Enhancer for Geometric GNNs**|Yusong Wang et.al.|[2409.17622](http://arxiv.org/abs/2409.17622)|null|
|**2024-09-26**|**Heterogeneous Hyper-Graph Neural Networks for Context-aware Human Activity Recognition**|Wen Ge et.al.|[2409.17483](http://arxiv.org/abs/2409.17483)|null|
|**2024-09-26**|**On the Impact of Feature Heterophily on Link Prediction with Graph Neural Networks**|Jiong Zhu et.al.|[2409.17475](http://arxiv.org/abs/2409.17475)|null|
|**2024-09-25**|**Predictive Covert Communication Against Multi-UAV Surveillance Using Graph Koopman Autoencoder**|Sivaram Krishnan et.al.|[2409.17048](http://arxiv.org/abs/2409.17048)|null|
|**2024-09-25**|**Erase then Rectify: A Training-Free Parameter Editing Approach for Cost-Effective Graph Unlearning**|Zhe-Rui Yang et.al.|[2409.16684](http://arxiv.org/abs/2409.16684)|**[link](https://github.com/allminerlab/etr)**|
|**2024-09-25**|**GraphLoRA: Structure-Aware Contrastive Low-Rank Adaptation for Cross-Graph Transfer Learning**|Zhe-Rui Yang et.al.|[2409.16670](http://arxiv.org/abs/2409.16670)|**[link](https://github.com/allminerlab/graphlora)**|
|**2024-09-25**|**Pre-trained Graphformer-based Ranking at Web-scale Search (Extended Abstract)**|Yuchen Li et.al.|[2409.16590](http://arxiv.org/abs/2409.16590)|null|
|**2024-09-24**|**AUGUR, A flexible and efficient optimization algorithm for identification of optimal adsorption sites**|Ioannis Kouroudis et.al.|[2409.16204](http://arxiv.org/abs/2409.16204)|null|
|**2024-09-24**|**Symmetries and Expressive Requirements for Learning General Policies**|Dominik Drexler et.al.|[2409.15892](http://arxiv.org/abs/2409.15892)|null|
|**2024-09-24**|**MGNN: Moment Graph Neural Network for Universal Molecular Potentials**|Jian Chang et.al.|[2409.15800](http://arxiv.org/abs/2409.15800)|null|
|**2024-09-24**|**GraphGI:A GNN Explanation Method using Game Interaction**|Xingping Xian et.al.|[2409.15698](http://arxiv.org/abs/2409.15698)|null|
|**2024-09-24**|**Double-Path Adaptive-correlation Spatial-Temporal Inverted Transformer for Stock Time Series Forecasting**|Wenbo Yan et.al.|[2409.15662](http://arxiv.org/abs/2409.15662)|null|
|**2024-09-23**|**MotifDisco: Motif Causal Discovery For Time Series Motifs**|Josephine Lamp et.al.|[2409.15219](http://arxiv.org/abs/2409.15219)|null|
|**2024-09-23**|**MSARS: A Meta-Learning and Reinforcement Learning Framework for SLO Resource Allocation and Adaptive Scaling for Microservices**|Kan Hu et.al.|[2409.14953](http://arxiv.org/abs/2409.14953)|null|
|**2024-09-23**|**FastGL: A GPU-Efficient Framework for Accelerating Sampling-Based GNN Training at Large Scale**|Zeyu Zhu et.al.|[2409.14939](http://arxiv.org/abs/2409.14939)|**[link](https://github.com/a1bc2def6g/fastgl-ae)**|
|**2024-09-22**|**TabGraphs: A Benchmark and Strong Baselines for Learning on Graphs with Tabular Features**|Gleb Bazhenov et.al.|[2409.14500](http://arxiv.org/abs/2409.14500)|**[link](https://github.com/yandex-research/tabgraphs)**|
|**2024-09-21**|**IPF-HMGNN: A novel integrative prediction framework for metro passenger flow**|Wenbo Lu et.al.|[2409.14104](http://arxiv.org/abs/2409.14104)|null|
|**2024-09-18**|**Topological Deep Learning with State-Space Models: A Mamba Approach for Simplicial Complexes**|Marco Montagna et.al.|[2409.12033](http://arxiv.org/abs/2409.12033)|null|
|**2024-09-18**|**Metric-Semantic Factor Graph Generation based on Graph Neural Networks**|Jose Andres Millan-Romera et.al.|[2409.11972](http://arxiv.org/abs/2409.11972)|null|
|**2024-09-18**|**Multi-Grid Graph Neural Networks with Self-Attention for Computational Mechanics**|Paul Garnier et.al.|[2409.11899](http://arxiv.org/abs/2409.11899)|**[link](https://github.com/donsetpg/multigrid-gnn)**|
|**2024-09-18**|**Edge-Based Graph Component Pooling**|T. Snelleman et.al.|[2409.11856](http://arxiv.org/abs/2409.11856)|null|
|**2024-09-18**|**Graph Neural Network-State Predictive Information Bottleneck (GNN-SPIB) approach for learning molecular thermodynamics and kinetics**|Ziyue Zou et.al.|[2409.11843](http://arxiv.org/abs/2409.11843)|null|
|**2024-09-18**|**World of Forms: Deformable Geometric Templates for One-Shot Surface Meshing in Coronary CT Angiography**|Rudolf L. M. van Herten et.al.|[2409.11837](http://arxiv.org/abs/2409.11837)|null|
|**2024-09-17**|**A Property Encoder for Graph Neural Networks**|Anwar Said et.al.|[2409.11554](http://arxiv.org/abs/2409.11554)|null|
|**2024-09-17**|**Uncertainty and Prediction Quality Estimation for Semantic Segmentation via Graph Neural Networks**|Edgar Heinert et.al.|[2409.11373](http://arxiv.org/abs/2409.11373)|**[link](https://github.com/eheinert/uncertainty-and-prediction-quality-estimation-for-semseg-via-gnns)**|
|**2024-09-18**|**High-Order Evolving Graphs for Enhanced Representation of Traffic Dynamics**|Aditya Humnabadkar et.al.|[2409.11206](http://arxiv.org/abs/2409.11206)|null|
|**2024-09-17**|**MI-HGNN: Morphology-Informed Heterogeneous Graph Neural Network for Legged Robot Contact Perception**|Daniel Butterfield et.al.|[2409.11146](http://arxiv.org/abs/2409.11146)|**[link](https://github.com/lunarlab-gatech/morphology-informed-hgnn)**|
|**2024-09-17**|**Can Graph Reordering Speed Up Graph Neural Network Training? An Experimental Study**|Nikolai Merkel et.al.|[2409.11129](http://arxiv.org/abs/2409.11129)|**[link](https://github.com/nikolaimerkel/reordering)**|
|**2024-09-17**|**GINTRIP: Interpretable Temporal Graph Regression using Information bottleneck and Prototype-based method**|Ali Royat et.al.|[2409.10996](http://arxiv.org/abs/2409.10996)|**[link](https://github.com/moghadas76/gintrip)**|
|**2024-09-17**|**Contrasformer: A Brain Network Contrastive Transformer for Neurodegenerative Condition Identification**|Jiaxing Xu et.al.|[2409.10944](http://arxiv.org/abs/2409.10944)|**[link](https://github.com/angusmonroe/contrasformer)**|
|**2024-09-17**|**Spatio-Temporal-Network Point Processes for Modeling Crime Events with Landmarks**|Zheng Dong et.al.|[2409.10882](http://arxiv.org/abs/2409.10882)|null|
|**2024-09-16**|**Recurrent Graph Transformer Network for Multiple Fault Localization in Naval Shipboard Systems**|Quang-Ha Ngo et.al.|[2409.10792](http://arxiv.org/abs/2409.10792)|null|
|**2024-09-16**|**Signed Graph Autoencoder for Explainable and Polarization-Aware Network Embeddings**|Nikolaos Nakis et.al.|[2409.10452](http://arxiv.org/abs/2409.10452)|null|
|**2024-09-16**|**Hyperedge Modeling in Hypergraph Neural Networks by using Densest Overlapping Subgraphs**|Mehrad Soltani et.al.|[2409.10340](http://arxiv.org/abs/2409.10340)|null|
|**2024-09-16**|**Deep Graph Anomaly Detection: A Survey and New Perspectives**|Hezhe Qiao et.al.|[2409.09957](http://arxiv.org/abs/2409.09957)|**[link](https://github.com/mala-lab/awesome-deep-graph-anomaly-detection)**|
|**2024-09-17**|**Mobility-GNN: a human mobility-based graph neural network for tracking and analyzing the spatial dynamics of the synthetic opioid crisis in the USA, 2013-2020**|Zhiyue Xia et.al.|[2409.09945](http://arxiv.org/abs/2409.09945)|null|
|**2024-09-16**|**Generalizability of Graph Neural Network Force Fields for Predicting Solid-State Properties**|Shaswat Mohanty et.al.|[2409.09931](http://arxiv.org/abs/2409.09931)|null|
|**2024-09-15**|**Dynamic Fraud Detection: Integrating Reinforcement Learning into Graph Neural Networks**|Yuxin Dong et.al.|[2409.09892](http://arxiv.org/abs/2409.09892)|null|
|**2024-09-15**|**Flexible Diffusion Scopes with Parameterized Laplacian for Heterophilic Graph Learning**|Qincheng Lu et.al.|[2409.09888](http://arxiv.org/abs/2409.09888)|null|
|**2024-09-15**|**Predicting building types and functions at transnational scale**|Jonas Fill et.al.|[2409.09692](http://arxiv.org/abs/2409.09692)|null|
|**2024-09-14**|**Improved Physics-Informed Neural Network based AC Power Flow for Distribution Networks**|Victor Eeckhout et.al.|[2409.09466](http://arxiv.org/abs/2409.09466)|null|
|**2024-09-17**|**Operational Wind Speed Forecasts for Chile's Electric Power Sector Using a Hybrid ML Model**|Dhruv Suri et.al.|[2409.09263](http://arxiv.org/abs/2409.09263)|null|
|**2024-09-13**|**SAUC: Sparsity-Aware Uncertainty Calibration for Spatiotemporal Prediction with Graph Neural Networks**|Dingyi Zhuang et.al.|[2409.08766](http://arxiv.org/abs/2409.08766)|**[link](https://github.com/AnonymousSAUC/SAUC)**|
|**2024-09-13**|**Redesigning graph filter-based GNNs to relax the homophily assumption**|Samuel Rey et.al.|[2409.08676](http://arxiv.org/abs/2409.08676)|**[link](https://github.com/reysam93/adaptive_agg_gcn)**|
|**2024-09-13**|**Sybil Detection using Graph Neural Networks**|Stuart Heeb et.al.|[2409.08631](http://arxiv.org/abs/2409.08631)|null|
|**2024-09-13**|**Molecular Graph Representation Learning via Structural Similarity Information**|Chengyu Yao et.al.|[2409.08580](http://arxiv.org/abs/2409.08580)|**[link](https://github.com/yaoyao-yaoyao-cell/mssm-gnn)**|
|**2024-09-13**|**Causal GNNs: A GNN-Driven Instrumental Variable Approach for Causal Inference in Networks**|Xiaojing Du et.al.|[2409.08544](http://arxiv.org/abs/2409.08544)|null|
|**2024-09-13**|**ATFLRec: A Multimodal Recommender System with Audio-Text Fusion and Low-Rank Adaptation via Instruction-Tuned Large Language Model**|Zezheng Qin et.al.|[2409.08543](http://arxiv.org/abs/2409.08543)|null|
|**2024-09-13**|**An Efficient Privacy-aware Split Learning Framework for Satellite Communications**|Jianfei Sun et.al.|[2409.08538](http://arxiv.org/abs/2409.08538)|null|
|**2024-09-12**|**Learning incomplete factorization preconditioners for GMRES**|Paul Häusner et.al.|[2409.08262](http://arxiv.org/abs/2409.08262)|**[link](https://github.com/paulhausner/neural-incomplete-factorization)**|
|**2024-09-12**|**CliquePH: Higher-Order Information for Graph Neural Networks through Persistent Homology on Clique Graphs**|Davide Buffelli et.al.|[2409.08217](http://arxiv.org/abs/2409.08217)|**[link](https://github.com/DavideBuffelli/CliquePH)**|
|**2024-09-12**|**Gaussian Garments: Reconstructing Simulation-Ready Clothing with Photorealistic Appearance from Multi-View Video**|Boxiang Rong et.al.|[2409.08189](http://arxiv.org/abs/2409.08189)|null|
|**2024-09-12**|**Hierarchical Symbolic Pop Music Generation with Graph Neural Networks**|Wen Qing Lim et.al.|[2409.08155](http://arxiv.org/abs/2409.08155)|null|
|**2024-09-12**|**Heterogeneous Sheaf Neural Networks**|Luke Braithwaite et.al.|[2409.08036](http://arxiv.org/abs/2409.08036)|null|
|**2024-09-12**|**Edge-Wise Graph-Instructed Neural Networks**|Francesco Della Santa et.al.|[2409.08023](http://arxiv.org/abs/2409.08023)|**[link](https://github.com/fra0013to/ginn)**|
|**2024-09-12**|**Data-efficient multi-fidelity training for high-fidelity machine learning interatomic potentials**|Jaesun Kim et.al.|[2409.07947](http://arxiv.org/abs/2409.07947)|null|
|**2024-09-12**|**Tera-SpaceCom: GNN-based Deep Reinforcement Learning for Joint Resource Allocation and Task Offloading in TeraHertz Band Space Networks**|Zhifeng Hu et.al.|[2409.07911](http://arxiv.org/abs/2409.07911)|null|
|**2024-09-13**|**Graph Neural Networks for Parkinsons Disease Detection**|Shakeel A. Sheikh et.al.|[2409.07884](http://arxiv.org/abs/2409.07884)|null|
|**2024-09-12**|**Mesh-based Super-Resolution of Fluid Flows with Multiscale Graph Neural Networks**|Shivam Barwey et.al.|[2409.07769](http://arxiv.org/abs/2409.07769)|null|
|**2024-09-11**|**Demo: SGCode: A Flexible Prompt-Optimizing System for Secure Generation of Code**|Khiem Ton et.al.|[2409.07368](http://arxiv.org/abs/2409.07368)|null|
|**2024-09-11**|**Descriptors-free Collective Variables From Geometric Graph Neural Networks**|Jintu Zhang et.al.|[2409.07339](http://arxiv.org/abs/2409.07339)|**[link](https://github.com/jintuzhang/gnncv)**|
|**2024-09-11**|**Recurrent Aggregators in Neural Algorithmic Reasoning**|Kaijia Xu et.al.|[2409.07154](http://arxiv.org/abs/2409.07154)|null|
|**2024-09-11**|**Learning Personalized Scoping for Graph Neural Networks under Heterophily**|Gangda Deng et.al.|[2409.06998](http://arxiv.org/abs/2409.06998)|null|
|**2024-09-10**|**Generative Hierarchical Materials Search**|Sherry Yang et.al.|[2409.06762](http://arxiv.org/abs/2409.06762)|null|
|**2024-09-10**|**EasyST: A Simple Framework for Spatio-Temporal Prediction**|Jiabin Tang et.al.|[2409.06748](http://arxiv.org/abs/2409.06748)|**[link](https://github.com/hkuds/easyst)**|
|**2024-09-10**|**Seg-HGNN: Unsupervised and Light-Weight Image Segmentation with Hyperbolic Graph Neural Networks**|Debjyoti Mondal et.al.|[2409.06589](http://arxiv.org/abs/2409.06589)|null|
|**2024-09-10**|**Learn2Aggregate: Supervised Generation of Chvátal-Gomory Cuts Using Graph Neural Networks**|Arnaud Deza et.al.|[2409.06559](http://arxiv.org/abs/2409.06559)|null|
|**2024-09-10**|**Neural Laplacian Operator for 3D Point Clouds**|Bo Pang et.al.|[2409.06506](http://arxiv.org/abs/2409.06506)|**[link](https://github.com/intelligentgeometry/nelo)**|
|**2024-09-10**|**LAMP: Learnable Meta-Path Guided Adversarial Contrastive Learning for Heterogeneous Graphs**|Siqing Li et.al.|[2409.06323](http://arxiv.org/abs/2409.06323)|null|
|**2024-09-09**|**Scalable Multitask Learning Using Gradient-based Estimation of Task Affinity**|Dongyue Li et.al.|[2409.06091](http://arxiv.org/abs/2409.06091)|**[link](https://github.com/virtuosoresearch/scalablemtl)**|
|**2024-09-09**|**Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling**|Stathis Megas et.al.|[2409.05804](http://arxiv.org/abs/2409.05804)|**[link](https://github.com/stathismegas/celcomen)**|
|**2024-09-09**|**Are Heterophily-Specific GNNs and Homophily Metrics Really Effective? Evaluation Pitfalls and New Benchmarks**|Sitao Luan et.al.|[2409.05755](http://arxiv.org/abs/2409.05755)|null|
|**2024-09-09**|**Enhancing Graph Contrastive Learning with Reliable and Informative Augmentation for Recommendation**|Bowen Zheng et.al.|[2409.05633](http://arxiv.org/abs/2409.05633)|**[link](https://github.com/rucaibox/cogcl)**|
|**2024-09-09**|**Learning to Model Graph Structural Information on MLPs via Graph Structure Self-Contrasting**|Lirong Wu et.al.|[2409.05573](http://arxiv.org/abs/2409.05573)|**[link](https://github.com/lirongwu/gssc)**|
|**2024-09-10**|**Retrofitting Temporal Graph Neural Networks with Transformer**|Qiang Huang et.al.|[2409.05477](http://arxiv.org/abs/2409.05477)|**[link](https://github.com/qianghuangwhu/tf-tgn)**|
|**2024-09-09**|**Graffin: Stand for Tails in Imbalanced Node Classification**|Xiaorui Qi et.al.|[2409.05339](http://arxiv.org/abs/2409.05339)|null|
|**2024-09-09**|**Investigating Material Interface Diffusion Phenomena through Graph Neural Networks in Applied Materials**|Zirui Zhao et.al.|[2409.05306](http://arxiv.org/abs/2409.05306)|null|
|**2024-09-08**|**Generalization of Geometric Graph Neural Networks**|Zhiyang Wang et.al.|[2409.05191](http://arxiv.org/abs/2409.05191)|null|
|**2024-09-08**|**Learning polycrystal plasticity using mesh-based subgraph geometric deep learning**|Hanfeng Zhai et.al.|[2409.05169](http://arxiv.org/abs/2409.05169)|**[link](https://gitlab.com/hanfengzhai2/gnn-fem-polyplas)**|
|**2024-09-10**|**MaxCutPool: differentiable feature-aware Maxcut for pooling in graph neural networks**|Carlo Abate et.al.|[2409.05100](http://arxiv.org/abs/2409.05100)|**[link](https://github.com/ngmlgroup/maxcutpool)**|
|**2024-09-06**|**Accelerating Training with Neuron Interaction and Nowcasting Networks**|Boris Knyazev et.al.|[2409.04434](http://arxiv.org/abs/2409.04434)|**[link](https://github.com/samsungsailmontreal/nino)**|
|**2024-09-06**|**GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding**|Ziyin Zhang et.al.|[2409.04183](http://arxiv.org/abs/2409.04183)|null|
|**2024-09-06**|**CUQ-GNN: Committee-based Graph Uncertainty Quantification using Posterior Networks**|Clemens Damke et.al.|[2409.04159](http://arxiv.org/abs/2409.04159)|**[link](https://github.com/cortys/gpn-extensions)**|
|**2024-09-05**|**Characterizing Massive Activations of Attention Mechanism in Graph Neural Networks**|Lorenzo Bini et.al.|[2409.03463](http://arxiv.org/abs/2409.03463)|**[link](https://github.com/msorbi/gnn-ma)**|
|**2024-09-05**|**Efficient prediction of potential energy surface and physical properties with Kolmogorov-Arnold Networks**|Rui Wang et.al.|[2409.03430](http://arxiv.org/abs/2409.03430)|null|
|**2024-09-04**|**Do We Trust What They Say or What They Do? A Multimodal User Embedding Provides Personalized Explanations**|Zhicheng Ren et.al.|[2409.02965](http://arxiv.org/abs/2409.02965)|null|
|**2024-09-04**|**Regional data-driven weather modeling with a global stretched-grid**|Thomas Nils Nipen et.al.|[2409.02891](http://arxiv.org/abs/2409.02891)|null|
|**2024-09-04**|**Task-Oriented Communication for Graph Data: A Graph Information Bottleneck Approach**|Shujing Li et.al.|[2409.02728](http://arxiv.org/abs/2409.02728)|null|
|**2024-09-02**|**GET-UP: GEomeTric-aware Depth Estimation with Radar Points UPsampling**|Huawei Sun et.al.|[2409.02720](http://arxiv.org/abs/2409.02720)|**[link](https://github.com/harborsarah/get-up)**|
|**2024-09-04**|**Word and Phrase Features in Graph Convolutional Network for Automatic Question Classification**|Junyoung Lee et.al.|[2409.02481](http://arxiv.org/abs/2409.02481)|null|
|**2024-09-03**|**A Lesion-aware Edge-based Graph Neural Network for Predicting Language Ability in Patients with Post-stroke Aphasia**|Zijian Chen et.al.|[2409.02303](http://arxiv.org/abs/2409.02303)|null|
|**2024-09-03**|**Accelerating Graph Neural Networks with a Novel Matrix Compression Format**|João N. F. Alves et.al.|[2409.02208](http://arxiv.org/abs/2409.02208)|null|
|**2024-09-03**|**Optimal Power Grid Operations with Foundation Models**|Alban Puech et.al.|[2409.02148](http://arxiv.org/abs/2409.02148)|null|
|**2024-09-06**|**Large-scale Urban Facility Location Selection with Knowledge-informed Reinforcement Learning**|Hongyuan Su et.al.|[2409.01588](http://arxiv.org/abs/2409.01588)|null|
|**2024-09-02**|**VLSI Hypergraph Partitioning with Deep Learning**|Muhammad Hadir Khan et.al.|[2409.01387](http://arxiv.org/abs/2409.01387)|null|
|**2024-09-02**|**Generating Packet-Level Header Traces Using GNN-powered GAN**|Zhen Xu et.al.|[2409.01265](http://arxiv.org/abs/2409.01265)|null|
|**2024-08-30**|**Leveraging Graph Neural Networks to Forecast Electricity Consumption**|Eloi Campagne et.al.|[2408.17366](http://arxiv.org/abs/2408.17366)|null|
|**2024-08-30**|**A Homogeneous Graph Neural Network for Precoding and Power Allocation in Scalable Wireless Networks**|Mingjun Sun et.al.|[2408.17252](http://arxiv.org/abs/2408.17252)|null|
|**2024-08-30**|**Search for $t\bar{t}H/A \rightarrow t\bar{t}t\bar{t}$ production in proton-proton collisions at $\sqrt{s}=13$ TeV with the ATLAS detector**|ATLAS Collaboration et.al.|[2408.17164](http://arxiv.org/abs/2408.17164)|null|
|**2024-09-03**|**Controllable Edge-Type-Specific Interpretation in Multi-Relational Graph Neural Networks for Drug Response Prediction**|Xiaodi Li et.al.|[2408.17129](http://arxiv.org/abs/2408.17129)|**[link](https://github.com/ahaubioinformatics/cetexplainer)**|
|**2024-08-29**|**H-SGANet: Hybrid Sparse Graph Attention Network for Deformable Medical Image Registration**|Yufeng Zhou et.al.|[2408.16719](http://arxiv.org/abs/2408.16719)|null|
|**2024-08-29**|**A GREAT Architecture for Edge-Based Graph Problems Like TSP**|Attila Lischka et.al.|[2408.16717](http://arxiv.org/abs/2408.16717)|null|
|**2024-08-29**|**SympGNNs: Symplectic Graph Neural Networks for identifiying high-dimensional Hamiltonian systems and node classification**|Alan John Varghese et.al.|[2408.16698](http://arxiv.org/abs/2408.16698)|null|
|**2024-09-01**|**SFR-GNN: Simple and Fast Robust GNNs against Structural Attacks**|Xing Ai et.al.|[2408.16537](http://arxiv.org/abs/2408.16537)|null|
|**2024-08-29**|**TempoKGAT: A Novel Graph Attention Network Approach for Temporal Graph Analysis**|Lena Sasal et.al.|[2408.16391](http://arxiv.org/abs/2408.16391)|**[link](https://github.com/capwidow/tempokgatcode)**|
|**2024-08-29**|**TG-PhyNN: An Enhanced Physically-Aware Graph Neural Network framework for forecasting Spatio-Temporal Data**|Zakaria Elabid et.al.|[2408.16379](http://arxiv.org/abs/2408.16379)|null|
|**2024-08-29**|**Do Graph Neural Networks Work for High Entropy Alloys?**|Hengrui Zhang et.al.|[2408.16337](http://arxiv.org/abs/2408.16337)|**[link](https://github.com/Henrium/LESets)**|
|**2024-08-29**|**OpenFGL: A Comprehensive Benchmarks for Federated Graph Learning**|Xunkai Li et.al.|[2408.16288](http://arxiv.org/abs/2408.16288)|**[link](https://github.com/xkli-allen/openfgl)**|
|**2024-08-29**|**A General Framework for Optimizing and Learning Nash Equilibrium**|Di Zhang et.al.|[2408.16260](http://arxiv.org/abs/2408.16260)|null|
|**2024-08-29**|**Meta-Learning Empowered Graph Neural Networks for Radio Resource Management**|Kai Huang et.al.|[2408.16239](http://arxiv.org/abs/2408.16239)|null|
|**2024-08-28**|**The Role of Fibration Symmetries in Geometric Deep Learning**|Osvaldo Velarde et.al.|[2408.15894](http://arxiv.org/abs/2408.15894)|null|
|**2024-08-28**|**Str-L Pose: Integrating Point and Structured Line for Relative Pose Estimation in Dual-Graph**|Zherong Zhang et.al.|[2408.15750](http://arxiv.org/abs/2408.15750)|null|
|**2024-08-28**|**Affordable HPC: Leveraging Small Clusters for Big Data and Graph Computing**|Ruilong Wu et.al.|[2408.15568](http://arxiv.org/abs/2408.15568)|null|
|**2024-08-27**|**Understanding GNNs for Boolean Satisfiability through Approximation Algorithms**|Jan Hůla et.al.|[2408.15418](http://arxiv.org/abs/2408.15418)|null|
|**2024-08-27**|**Temporal Graph Neural Network-Powered Paper Recommendation on Dynamic Citation Networks**|Junhao Shen et.al.|[2408.15371](http://arxiv.org/abs/2408.15371)|null|
|**2024-08-27**|**Multi-domain Network Slice Partitioning: A Graph Neural Network Algorithm**|Zhouxiang Wu et.al.|[2408.15342](http://arxiv.org/abs/2408.15342)|null|
|**2024-08-29**|**Evaluating the Predictive Features of Person-Centric Knowledge Graph Embeddings: Unfolding Ablation Studies**|Christos Theodoropoulos et.al.|[2408.15294](http://arxiv.org/abs/2408.15294)|null|
|**2024-08-27**|**SiHGNN: Leveraging Properties of Semantic Graphs for Efficient HGNN Acceleration**|Runzhen Xue et.al.|[2408.15089](http://arxiv.org/abs/2408.15089)|null|
|**2024-08-27**|**Earth Observation Satellite Scheduling with Graph Neural Networks**|Antoine Jacquet et.al.|[2408.15041](http://arxiv.org/abs/2408.15041)|null|
|**2024-08-27**|**Cross-Modal Learning for Chemistry Property Prediction: Large Language Models Meet Graph Machine Learning**|Sakhinana Sagar Srinivas et.al.|[2408.14964](http://arxiv.org/abs/2408.14964)|null|
|**2024-08-27**|**Graph and Sequential Neural Networks in Session-based Recommendation: A Survey**|Zihao Li et.al.|[2408.14851](http://arxiv.org/abs/2408.14851)|null|
|**2024-08-26**|**Meta Flow Matching: Integrating Vector Fields on the Wasserstein Manifold**|Lazar Atanackovic et.al.|[2408.14608](http://arxiv.org/abs/2408.14608)|null|
|**2024-08-26**|**Accelerated structure-stability energy-free calculator**|Alexandre Boucher et.al.|[2408.14577](http://arxiv.org/abs/2408.14577)|null|
|**2024-08-26**|**Retrieval Augmented Generation for Dynamic Graph Modeling**|Yuxia Wu et.al.|[2408.14523](http://arxiv.org/abs/2408.14523)|null|
|**2024-08-26**|**Integrated Brain Connectivity Analysis with fMRI, DTI, and sMRI Powered by Interpretable Graph Neural Networks**|Gang Qu et.al.|[2408.14254](http://arxiv.org/abs/2408.14254)|null|
|**2024-08-26**|**Exploring the Potential of Large Language Models for Heterophilic Graphs**|Yuxia Wu et.al.|[2408.14134](http://arxiv.org/abs/2408.14134)|null|
|**2024-08-26**|**PAGE: Parametric Generative Explainer for Graph Neural Network**|Yang Qiu et.al.|[2408.14042](http://arxiv.org/abs/2408.14042)|**[link](https://github.com/anders1123/PAGE)**|
|**2024-08-25**|**Optimizing Luxury Vehicle Dealership Networks: A Graph Neural Network Approach to Site Selection**|Luca Silvano Carocci et.al.|[2408.13961](http://arxiv.org/abs/2408.13961)|**[link](https://github.com/carocciluca/gnn-site-selection)**|
|**2024-08-25**|**Generalization of Graph Neural Networks is Robust to Model Mismatch**|Zhiyang Wang et.al.|[2408.13878](http://arxiv.org/abs/2408.13878)|null|
|**2024-08-25**|**RoCP-GNN: Robust Conformal Prediction for Graph Neural Networks in Node-Classification**|S. Akansha et.al.|[2408.13825](http://arxiv.org/abs/2408.13825)|null|
|**2024-08-27**|**GNN: Graph Neural Network and Large Language Model for Data Discovery**|Thomas Hoang et.al.|[2408.13609](http://arxiv.org/abs/2408.13609)|null|
|**2024-08-24**|**Knowledge-Aware Conversation Derailment Forecasting Using Graph Convolutional Networks**|Enas Altarawneh et.al.|[2408.13440](http://arxiv.org/abs/2408.13440)|null|
|**2024-08-23**|**Multivariate Time-Series Anomaly Detection based on Enhancing Graph Attention Networks with Topological Analysis**|Zhe Liu et.al.|[2408.13082](http://arxiv.org/abs/2408.13082)|**[link](https://github.com/ljj-cyber/topogdn)**|
|**2024-08-23**|**Disentangling, Amplifying, and Debiasing: Learning Disentangled Representations for Fair Graph Neural Networks**|Yeon-Chang Lee et.al.|[2408.12875](http://arxiv.org/abs/2408.12875)|**[link](https://github.com/bigdasgit/dab-gnn)**|
|**2024-08-23**|**HGNAS: Hardware-Aware Graph Neural Architecture Search for Edge Devices**|Ao Zhou et.al.|[2408.12840](http://arxiv.org/abs/2408.12840)|null|
|**2024-08-23**|**SIMPNet: Spatial-Informed Motion Planning Network**|Davood Soleymanzadeh et.al.|[2408.12831](http://arxiv.org/abs/2408.12831)|null|
|**2024-08-23**|**Data-Driven Parametrization of Molecular Mechanics Force Fields for Expansive Chemical Space Coverage**|Tianze Zheng et.al.|[2408.12817](http://arxiv.org/abs/2408.12817)|**[link](https://github.com/bytedance/byteff)**|
|**2024-08-23**|**Non-Homophilic Graph Pre-Training and Prompt Learning**|Xingtong Yu et.al.|[2408.12594](http://arxiv.org/abs/2408.12594)|**[link](https://github.com/jaygagaga/pronog)**|
|**2024-08-22**|**Advanced atom-level representations for protein flexibility prediction utilizing graph neural networks**|Sina Sarparast et.al.|[2408.12519](http://arxiv.org/abs/2408.12519)|null|
|**2024-08-22**|**Enhanced Expressivity in Graph Neural Networks with Lanczos-Based Linear Constraints**|Niloofar Azizi et.al.|[2408.12334](http://arxiv.org/abs/2408.12334)|null|
|**2024-08-22**|**Fair Augmentation for Graph Collaborative Filtering**|Ludovico Boratto et.al.|[2408.12208](http://arxiv.org/abs/2408.12208)|**[link](https://github.com/jackmedda/fa4gcf)**|
|**2024-08-22**|**Rank and Align: Towards Effective Source-free Graph Domain Adaptation**|Junyu Luo et.al.|[2408.12185](http://arxiv.org/abs/2408.12185)|null|
|**2024-08-22**|**Behavior Pattern Mining-based Multi-Behavior Recommendation**|Haojie Li et.al.|[2408.12152](http://arxiv.org/abs/2408.12152)|**[link](https://github.com/rookitkitlee/bpmr)**|
|**2024-08-21**|**Time Series Foundation Models and Deep Learning Architectures for Earthquake Temporal and Spatial Nowcasting**|Alireza Jafari et.al.|[2408.11990](http://arxiv.org/abs/2408.11990)|null|
|**2024-08-21**|**A Novel Evaluation Perspective on GNNs-based Recommender Systems through the Topology of the User-Item Graph**|Daniele Malitesta et.al.|[2408.11762](http://arxiv.org/abs/2408.11762)|**[link](https://github.com/sisinflab/topology-graph-collaborative-filtering)**|
|**2024-08-21**|**Optimizing Federated Graph Learning with Inherent Structural Knowledge and Dual-Densely Connected GNNs**|Longwen Wang et.al.|[2408.11662](http://arxiv.org/abs/2408.11662)|null|
|**2024-08-21**|**Slicing Input Features to Accelerate Deep Learning: A Case Study with Graph Neural Networks**|Zhengjia Xu et.al.|[2408.11500](http://arxiv.org/abs/2408.11500)|null|
|**2024-08-21**|**Estimating Peer Direct and Indirect Effects in Observational Network Data**|Xiaojing Du et.al.|[2408.11492](http://arxiv.org/abs/2408.11492)|null|
|**2024-08-21**|**Graph Classification via Reference Distribution Learning: Theory and Practice**|Zixiao Wang et.al.|[2408.11370](http://arxiv.org/abs/2408.11370)|null|
|**2024-08-21**|**Towards Probabilistic Inductive Logic Programming with Neurosymbolic Inference and Relaxation**|Fieke Hillerstrom et.al.|[2408.11367](http://arxiv.org/abs/2408.11367)|null|
|**2024-08-21**|**Modeling Reference-dependent Choices with Graph Neural Networks**|Liang Zhang et.al.|[2408.11302](http://arxiv.org/abs/2408.11302)|null|
|**2024-08-20**|**Multi-User Continuous-Aperture Array Communications: How to Learn Current Distribution?**|Jia Guo et.al.|[2408.11230](http://arxiv.org/abs/2408.11230)|null|
|**2024-08-20**|**Public Health in Disaster: Emotional Health and Life Incidents Extraction during Hurricane Harvey**|Thomas Hoang et.al.|[2408.11133](http://arxiv.org/abs/2408.11133)|null|
|**2024-08-20**|**GAIM: Attacking Graph Neural Networks via Adversarial Influence Maximization**|Xiaodong Yang et.al.|[2408.10948](http://arxiv.org/abs/2408.10948)|null|
|**2024-08-19**|**Learning Regularization for Graph Inverse Problems**|Moshe Eliasof et.al.|[2408.10436](http://arxiv.org/abs/2408.10436)|null|
|**2024-08-19**|**Expressive Power of Temporal Message Passing**|Przemysław Andrzej Wałęga et.al.|[2408.09918](http://arxiv.org/abs/2408.09918)|null|
|**2024-08-19**|**Community-Centric Graph Unlearning**|Yi Li et.al.|[2408.09705](http://arxiv.org/abs/2408.09705)|null|
|**2024-08-20**|**Heta: Distributed Training of Heterogeneous Graph Neural Networks**|Yuchen Zhong et.al.|[2408.09697](http://arxiv.org/abs/2408.09697)|null|
|**2024-08-18**|**Leveraging Invariant Principle for Heterophilic Graph Structure Distribution Shifts**|Jinluan Yang et.al.|[2408.09490](http://arxiv.org/abs/2408.09490)|null|
|**2024-08-18**|**Advances in Multiple Instance Learning for Whole Slide Image Analysis: Techniques, Challenges, and Future Directions**|Jun Wang et.al.|[2408.09476](http://arxiv.org/abs/2408.09476)|null|
|**2024-08-18**|**$\mathbb{BEHR}$ NOULLI: A Binary EHR Data-Oriented Medication Recommendation System**|Xihao Piao et.al.|[2408.09410](http://arxiv.org/abs/2408.09410)|**[link](https://github.com/chenzrg/behrmecom)**|
|**2024-08-18**|**Federated Graph Learning with Structure Proxy Alignment**|Xingbo Fu et.al.|[2408.09393](http://arxiv.org/abs/2408.09393)|**[link](https://github.com/xbfu/fedspray)**|
|**2024-08-17**|**Scalable and Certifiable Graph Unlearning via Lazy Local Propagation**|Lu Yi et.al.|[2408.09212](http://arxiv.org/abs/2408.09212)|**[link](https://github.com/luyi256/ScaleGUN)**|
|**2024-08-17**|**SA-GDA: Spectral Augmentation for Graph Domain Adaptation**|Jinhui Pang et.al.|[2408.09189](http://arxiv.org/abs/2408.09189)|null|
|**2024-08-17**|**Dynamic Neural Dowker Network: Approximating Persistent Homology in Dynamic Directed Graphs**|Hao Li et.al.|[2408.09123](http://arxiv.org/abs/2408.09123)|**[link](https://github.com/Lihaogx/DNDN)**|
|**2024-08-16**|**Neighbor Overlay-Induced Graph Attention Network**|Tiqiao Wei et.al.|[2408.08788](http://arxiv.org/abs/2408.08788)|null|
|**2024-08-16**|**SE-SGformer: A Self-Explainable Signed Graph Transformer for Link Sign Prediction**|Lu Li et.al.|[2408.08754](http://arxiv.org/abs/2408.08754)|**[link](https://github.com/liule66/SE-SGformer)**|
|**2024-08-16**|**Can Large Language Models Improve the Adversarial Robustness of Graph Neural Networks?**|Zhongjian Zhang et.al.|[2408.08685](http://arxiv.org/abs/2408.08685)|**[link](https://github.com/zhongjian-zhang/llm4rgnn)**|
|**2024-08-16**|**GrassNet: State Space Model Meets Graph Neural Network**|Gongpei Zhao et.al.|[2408.08583](http://arxiv.org/abs/2408.08583)|null|
|**2024-08-16**|**Mitigating Degree Bias in Signed Graph Neural Networks**|Fang He et.al.|[2408.08508](http://arxiv.org/abs/2408.08508)|null|
|**2024-08-16**|**Accelerating Mini-batch HGNN Training by Reducing CUDA Kernels**|Meng Wu et.al.|[2408.08490](http://arxiv.org/abs/2408.08490)|null|
|**2024-08-16**|**An Unsupervised Learning Framework Combined with Heuristics for the Maximum Minimal Cut Problem**|Huaiyuan Liu et.al.|[2408.08484](http://arxiv.org/abs/2408.08484)|**[link](https://github.com/luckyseasalt/pioneer)**|
|**2024-08-14**|**Graph neural network surrogate for strategic transport planning**|Nikita Makarov et.al.|[2408.07726](http://arxiv.org/abs/2408.07726)|**[link](https://github.com/nikita6187/transportplanningdataset)**|
|**2024-08-14**|**Interpretable Graph Neural Networks for Heterogeneous Tabular Data**|Amr Alkhatib et.al.|[2408.07661](http://arxiv.org/abs/2408.07661)|**[link](https://github.com/amrmalkhatib/ignh)**|
|**2024-08-14**|**Multi-task Heterogeneous Graph Learning on Electronic Health Records**|Tsai Hor Chan et.al.|[2408.07569](http://arxiv.org/abs/2408.07569)|**[link](https://github.com/hku-medai/mult-ehr)**|
|**2024-08-14**|**Towards Few-shot Self-explaining Graph Neural Networks**|Jingyu Peng et.al.|[2408.07340](http://arxiv.org/abs/2408.07340)|**[link](https://github.com/jypeng28/mse-gnn)**|
|**2024-08-14**|**RSEA-MVGNN: Multi-View Graph Neural Network with Reliable Structural Enhancement and Aggregation**|Junyu Chen et.al.|[2408.07331](http://arxiv.org/abs/2408.07331)|null|
|**2024-08-13**|**Pan-cancer gene set discovery via scRNA-seq for optimal deep learning based downstream tasks**|Jong Hyun Kim et.al.|[2408.07233](http://arxiv.org/abs/2408.07233)|null|
|**2024-08-13**|**Joint Graph Rewiring and Feature Denoising via Spectral Resonance**|Jonas Linkerhägner et.al.|[2408.07191](http://arxiv.org/abs/2408.07191)|**[link](https://github.com/jlinki/JDR)**|
|**2024-08-13**|**Physics-informed graph neural networks for flow field estimation in carotid arteries**|Julian Suk et.al.|[2408.07110](http://arxiv.org/abs/2408.07110)|null|
|**2024-08-13**|**Machine Learning Message-Passing for the Scalable Decoding of QLDPC Codes**|Arshpreet Singh Maan et.al.|[2408.07038](http://arxiv.org/abs/2408.07038)|**[link](https://github.com/arshpreetmaan/astra)**|
|**2024-08-13**|**LLMs can Schedule**|Henrik Abgaryan et.al.|[2408.06993](http://arxiv.org/abs/2408.06993)|**[link](https://github.com/starjob42/datasetjsp)**|
|**2024-08-13**|**Graph Neural Network Approach to Predict the Effects of Road Capacity Reduction Policies: A Case Study for Paris, France**|Elena Natterer et.al.|[2408.06762](http://arxiv.org/abs/2408.06762)|null|
|**2024-08-13**|**Computation-friendly Graph Neural Network Design by Accumulating Knowledge on Large Language Models**|Jialiang Wang et.al.|[2408.06717](http://arxiv.org/abs/2408.06717)|null|
|**2024-08-13**|**RW-NSGCN: A Robust Approach to Structural Attacks via Negative Sampling**|Shuqi He et.al.|[2408.06665](http://arxiv.org/abs/2408.06665)|null|
|**2024-08-12**|**From Graphs to Qubits: A Critical Review of Quantum Graph Neural Networks**|Andrea Ceschini et.al.|[2408.06524](http://arxiv.org/abs/2408.06524)|null|
|**2024-08-12**|**Decentralized Cooperation in Heterogeneous Multi-Agent Reinforcement Learning via Graph Neural Network-Based Intrinsic Motivation**|Jahir Sadik Monon et.al.|[2408.06503](http://arxiv.org/abs/2408.06503)|**[link](https://github.com/jahirsadik/cohet-implementation)**|
|**2024-08-12**|**What Ails Generative Structure-based Drug Design: Too Little or Too Much Expressivity?**|Rafał Karczewski et.al.|[2408.06050](http://arxiv.org/abs/2408.06050)|**[link](https://github.com/rafalkarczewski/simplesbdd)**|
|**2024-08-12**|**ARPA: A Novel Hybrid Model for Advancing Visual Word Disambiguation Using Large Language Models and Transformers**|Aristi Papastavrou et.al.|[2408.06040](http://arxiv.org/abs/2408.06040)|null|
|**2024-08-12**|**Spacetime $E(n)$ -Transformer: Equivariant Attention for Spatio-temporal Graphs**|Sergio G. Charles et.al.|[2408.06039](http://arxiv.org/abs/2408.06039)|null|
|**2024-08-11**|**GraphTransfer: A Generic Feature Fusion Framework for Collaborative Filtering**|Jiafeng Xia et.al.|[2408.05792](http://arxiv.org/abs/2408.05792)|null|
|**2024-08-11**|**On zero-shot learning in neural state estimation of power distribution systems**|Aleksandr Berezin et.al.|[2408.05787](http://arxiv.org/abs/2408.05787)|**[link](https://gitlab.com/transense/nse-tl-paper)**|
|**2024-08-11**|**Swarm-Net: Firmware Attestation in IoT Swarms using Graph Neural Networks and Volatile Memory**|Varun Kohli et.al.|[2408.05680](http://arxiv.org/abs/2408.05680)|**[link](https://github.com/VarunKohli18/swarm-net)**|
|**2024-08-10**|**An Information-Theoretic Analysis of Temporal GNNs**|Amirmohammad Farzaneh et.al.|[2408.05624](http://arxiv.org/abs/2408.05624)|null|
|**2024-08-13**|**A Laplacian-based Quantum Graph Neural Network for Semi-Supervised Learning**|Hamed Gholipour et.al.|[2408.05498](http://arxiv.org/abs/2408.05498)|null|
|**2024-08-10**|**Path-LLM: A Shortest-Path-based LLM Learning for Unified Graph Representation**|Wenbo Shang et.al.|[2408.05456](http://arxiv.org/abs/2408.05456)|null|
|**2024-08-10**|**Modeling Multi-Step Scientific Processes with Graph Transformer Networks**|Amanda A. Volk et.al.|[2408.05425](http://arxiv.org/abs/2408.05425)|null|
|**2024-08-09**|**Decoding Quantum LDPC Codes Using Graph Neural Networks**|Vukan Ninkovic et.al.|[2408.05170](http://arxiv.org/abs/2408.05170)|null|
|**2024-08-09**|**Federated Hypergraph Learning with Hyperedge Completion**|Linfeng Luo et.al.|[2408.05160](http://arxiv.org/abs/2408.05160)|null|
|**2024-08-09**|**Variational Bayesian Phylogenetic Inference with Semi-implicit Branch Length Distributions**|Tianyu Xie et.al.|[2408.05058](http://arxiv.org/abs/2408.05058)|**[link](https://github.com/tyuxie/vbpi-sibranch)**|
|**2024-08-09**|**Graph Neural Networks as Ordering Heuristics for Parallel Graph Coloring**|Kenneth Langedal et.al.|[2408.05054](http://arxiv.org/abs/2408.05054)|null|
|**2024-08-09**|**A GNN Model with Adaptive Weights for Session-Based Recommendation Systems**|Begüm Özbay et.al.|[2408.05051](http://arxiv.org/abs/2408.05051)|null|
|**2024-08-09**|**Better Not to Propagate: Understanding Edge Uncertainty and Over-smoothing in Signed Graph Neural Networks**|Yoonhyuk Choi et.al.|[2408.04895](http://arxiv.org/abs/2408.04895)|null|
|**2024-08-09**|**MDS-GNN: A Mutual Dual-Stream Graph Neural Network on Graphs with Incomplete Features and Structure**|Peng Yuan et.al.|[2408.04845](http://arxiv.org/abs/2408.04845)|null|
|**2024-08-09**|**Dual-Channel Latent Factor Analysis Enhanced Graph Contrastive Learning for Recommendation**|Junfeng Long et.al.|[2408.04838](http://arxiv.org/abs/2408.04838)|null|
|**2024-08-08**|**Advancing Molecular Machine (Learned) Representations with Stereoelectronics-Infused Molecular Graphs**|Daniil A. Boiko et.al.|[2408.04520](http://arxiv.org/abs/2408.04520)|**[link](https://github.com/gomesgroup/simg)**|
|**2024-08-08**|**Understanding and Modeling Job Marketplace with Pretrained Language Models**|Yaochen Zhu et.al.|[2408.04381](http://arxiv.org/abs/2408.04381)|null|
|**2024-08-08**|**Uncertainty-Aware Crime Prediction With Spatial Temporal Multivariate Graph Neural Networks**|Zepu Wang et.al.|[2408.04193](http://arxiv.org/abs/2408.04193)|null|
|**2024-08-08**|**wav2graph: A Framework for Supervised Learning Knowledge Graph from Speech**|Khai Le-Duc et.al.|[2408.04174](http://arxiv.org/abs/2408.04174)|**[link](https://github.com/leduckhai/wav2graph)**|
|**2024-08-07**|**Heterogeneous Graph Sequence Neural Networks for Dynamic Traffic Assignment**|Tong Liu et.al.|[2408.04131](http://arxiv.org/abs/2408.04131)|null|
|**2024-08-07**|**Deep Generative Models for Subgraph Prediction**|Erfaneh Mahmoudzadeh et.al.|[2408.04053](http://arxiv.org/abs/2408.04053)|**[link](https://github.com/erfmah/answering_graph_queries)**|
|**2024-08-07**|**Knowledge Probing for Graph Representation Learning**|Mingyu Zhao et.al.|[2408.03877](http://arxiv.org/abs/2408.03877)|null|
|**2024-08-07**|**Beyond Over-smoothing: Uncovering the Trainability Challenges in Deep Graph Neural Networks**|Jie Peng et.al.|[2408.03669](http://arxiv.org/abs/2408.03669)|null|
|**2024-08-06**|**A Study on Quantum Graph Neural Networks Applied to Molecular Physics**|Simone Piperno et.al.|[2408.03427](http://arxiv.org/abs/2408.03427)|null|
|**2024-08-06**|**MLC-GCN: Multi-Level Generated Connectome Based GCN for AD Analysis**|Wenqi Zhu et.al.|[2408.03358](http://arxiv.org/abs/2408.03358)|null|
|**2024-08-06**|**RELIEF: Reinforcement Learning Empowered Graph Feature Prompt Tuning**|Jiapeng Zhu et.al.|[2408.03195](http://arxiv.org/abs/2408.03195)|**[link](https://github.com/JasonZhujp/RELIEF)**|
|**2024-08-06**|**CADRL: Category-aware Dual-agent Reinforcement Learning for Explainable Recommendations over Knowledge Graphs**|Shangfei Zheng et.al.|[2408.03166](http://arxiv.org/abs/2408.03166)|null|
|**2024-08-06**|**SETN: Stock Embedding Enhanced with Textual and Network Information**|Takehiro Takayanagi et.al.|[2408.02899](http://arxiv.org/abs/2408.02899)|null|
|**2024-08-05**|**Algorithm-Informed Graph Neural Networks for Leakage Detection and Localization in Water Distribution Networks**|Zepeng Zhang et.al.|[2408.02797](http://arxiv.org/abs/2408.02797)|null|
|**2024-08-04**|**Understanding Deep Learning via Notions of Rank**|Noam Razin et.al.|[2408.02111](http://arxiv.org/abs/2408.02111)|null|
|**2024-08-04**|**Optimal and efficient text counterfactuals using Graph Neural Networks**|Dimitris Lymperopoulos et.al.|[2408.01969](http://arxiv.org/abs/2408.01969)|**[link](https://github.com/Jimlibo/GNN-Counterfactual-Editor)**|
|**2024-08-04**|**Top K Enhanced Reinforcement Learning Attacks on Heterogeneous Graph Node Classification**|Honglin Gao et.al.|[2408.01964](http://arxiv.org/abs/2408.01964)|null|
|**2024-08-04**|**Bilateral Trade Flow Prediction by Gravity-informed Graph Auto-encoder**|Naoto Minakawa et.al.|[2408.01938](http://arxiv.org/abs/2408.01938)|null|
|**2024-08-04**|**A Comprehensive Survey on GNN Characterization**|Meng Wu et.al.|[2408.01902](http://arxiv.org/abs/2408.01902)|null|
|**2024-08-03**|**Invariant Graph Learning Meets Information Bottleneck for Out-of-Distribution Generalization**|Wenyu Mao et.al.|[2408.01697](http://arxiv.org/abs/2408.01697)|**[link](https://github.com/maowenyu-11/infoigl)**|
|**2024-08-02**|**Efficient Graph Coloring with Neural Networks: A Physics-Inspired Approach for Large Graphs**|Lorenzo Colantonio et.al.|[2408.01503](http://arxiv.org/abs/2408.01503)|null|
|**2024-08-02**|**Tailoring Graph Neural Network-based Flow-guided Localization to Individual Bloodstreams and Activities**|Pablo Galván et.al.|[2408.01239](http://arxiv.org/abs/2408.01239)|null|
|**2024-08-02**|**HeteroMorpheus: Universal Control Based on Morphological Heterogeneity Modeling**|YiFan Hao et.al.|[2408.01230](http://arxiv.org/abs/2408.01230)|**[link](https://github.com/hyf1530588058/HeteroMorpheus)**|
|**2024-08-02**|**GNN-MolKAN: Harnessing the Power of KAN to Advance Molecular Representation Learning with GNNs**|Ruifeng Li et.al.|[2408.01018](http://arxiv.org/abs/2408.01018)|null|
|**2024-08-02**|**GraphAge: Unleashing the power of Graph Neural Network to Decode Epigenetic Aging**|Saleh Sakib Ahmed et.al.|[2408.00984](http://arxiv.org/abs/2408.00984)|**[link](https://github.com/bojack-horseman91/GraphAge)**|
|**2024-08-01**|**Parkinson's Disease Detection from Resting State EEG using Multi-Head Graph Structure Learning with Gradient Weighted Graph Attention Explanations**|Christopher Neves et.al.|[2408.00906](http://arxiv.org/abs/2408.00906)|null|
|**2024-08-01**|**You Can't Ignore Either: Unifying Structure and Feature Denoising for Robust Graph Learning**|Tianmeng Yang et.al.|[2408.00700](http://arxiv.org/abs/2408.00700)|**[link](https://github.com/youngtimmy/ugd)**|
|**2024-08-01**|**Graph Representation Learning via Causal Diffusion for Out-of-Distribution Recommendation**|Chu Zhao et.al.|[2408.00490](http://arxiv.org/abs/2408.00490)|**[link](https://github.com/user683/CausalDiffRec)**|
|**2024-08-01**|**Contrastive Graph Representation Learning with Adversarial Cross-view Reconstruction and Information Bottleneck**|Yuntao Shou et.al.|[2408.00295](http://arxiv.org/abs/2408.00295)|null|
|**2024-08-01**|**Multi-Modal Parameter-Efficient Fine-tuning via Graph Neural Network**|Bin Cheng et.al.|[2408.00290](http://arxiv.org/abs/2408.00290)|null|
|**2024-08-01**|**CDFGNN: a Systematic Design of Cache-based Distributed Full-Batch Graph Neural Network Training with Communication Reduction**|Shuai Zhang et.al.|[2408.00232](http://arxiv.org/abs/2408.00232)|null|
|**2024-07-31**|**Non-convolutional Graph Neural Networks**|Yuanqing Wang et.al.|[2408.00165](http://arxiv.org/abs/2408.00165)|**[link](https://github.com/yuanqing-wang/rum)**|
|**2024-07-31**|**HGOE: Hybrid External and Internal Graph Outlier Exposure for Graph Out-of-Distribution Detection**|Junwei He et.al.|[2407.21742](http://arxiv.org/abs/2407.21742)|null|
|**2024-07-31**|**UMMAN: Unsupervised Multi-graph Merge Adversarial Network for Disease Prediction Based on Intestinal Flora**|Dingkun Liu et.al.|[2407.21714](http://arxiv.org/abs/2407.21714)|null|
|**2024-07-31**|**MART: MultiscAle Relational Transformer Networks for Multi-agent Trajectory Prediction**|Seongju Lee et.al.|[2407.21635](http://arxiv.org/abs/2407.21635)|**[link](https://github.com/gist-ailab/mart)**|
|**2024-07-31**|**MicroMIL: Graph-based Contextual Multiple Instance Learning for Patient Diagnosis Using Microscopy Images**|JongWoo Kim et.al.|[2407.21604](http://arxiv.org/abs/2407.21604)|null|
|**2024-07-31**|**GEGA: Graph Convolutional Networks and Evidence Retrieval Guided Attention for Enhanced Document-level Relation Extraction**|Yanxu Mao et.al.|[2407.21384](http://arxiv.org/abs/2407.21384)|null|
|**2024-07-30**|**GNUMAP: A Parameter-Free Approach to Unsupervised Dimensionality Reduction via Graph Neural Networks**|Jihee You et.al.|[2407.21236](http://arxiv.org/abs/2407.21236)|null|
|**2024-07-30**|**What Are Good Positional Encodings for Directed Graphs?**|Yinan Huang et.al.|[2407.20912](http://arxiv.org/abs/2407.20912)|**[link](https://github.com/graph-com/multi-q-maglap)**|
|**2024-07-30**|**Leveraging Multi-facet Paths for Heterogeneous Graph Representation Learning**|JongWoo Kim et.al.|[2407.20648](http://arxiv.org/abs/2407.20648)|null|
|**2024-07-30**|**Joint Diffusion Processes as an Inductive Bias in Sheaf Neural Networks**|Ferran Hernandez Caralt et.al.|[2407.20597](http://arxiv.org/abs/2407.20597)|null|
|**2024-07-30**|**Automated Physical Design Watermarking Leveraging Graph Neural Networks**|Ruisi Zhang et.al.|[2407.20544](http://arxiv.org/abs/2407.20544)|**[link](https://github.com/ruisizhang123/pd_wm_gnn)**|
|**2024-07-30**|**Unveiling the Potential of Spiking Dynamics in Graph Representation Learning through Spatial-Temporal Normalization and Coding Strategies**|Mingkun Xu et.al.|[2407.20508](http://arxiv.org/abs/2407.20508)|null|
|**2024-07-30**|**Optimizing Long-tailed Link Prediction in Graph Neural Networks through Structure Representation Enhancement**|Yakun Wang et.al.|[2407.20499](http://arxiv.org/abs/2407.20499)|null|
|**2024-07-30**|**Relaxed Equivariant Graph Neural Networks**|Elyssa Hofgard et.al.|[2407.20471](http://arxiv.org/abs/2407.20471)|**[link](https://github.com/atomicarchitects/RelaxedE3NN)**|
|**2024-07-29**|**Unified Deep Learning Framework for Many-Body Quantum Chemistry via Green's Functions**|Christian Venturella et.al.|[2407.20384](http://arxiv.org/abs/2407.20384)|null|
|**2024-07-29**|**rLLM: Relational Table Learning with LLMs**|Weichen Li et.al.|[2407.20157](http://arxiv.org/abs/2407.20157)|**[link](https://github.com/rllm-project/rllm)**|
|**2024-07-29**|**xAI-Drop: Don't Use What You Cannot Explain**|Vincenzo Marco De Luca et.al.|[2407.20067](http://arxiv.org/abs/2407.20067)|null|
|**2024-07-29**|**RelBench: A Benchmark for Deep Learning on Relational Databases**|Joshua Robinson et.al.|[2407.20060](http://arxiv.org/abs/2407.20060)|**[link](https://github.com/snap-stanford/relbench)**|
|**2024-07-29**|**Noise-Resilient Unsupervised Graph Representation Learning via Multi-Hop Feature Quality Estimation**|Shiyuan Li et.al.|[2407.19944](http://arxiv.org/abs/2407.19944)|null|
|**2024-07-29**|**Aero-Nef: Neural Fields for Rapid Aircraft Aerodynamics Simulations**|Giovanni Catalani et.al.|[2407.19916](http://arxiv.org/abs/2407.19916)|**[link](https://gitlab.isae-supaero.fr/gi.catalani/aero-nepf)**|
|**2024-07-29**|**A Unified Graph Transformer for Overcoming Isolations in Multi-modal Recommendation**|Zixuan Yi et.al.|[2407.19886](http://arxiv.org/abs/2407.19886)|null|
|**2024-07-28**|**Sharp Bounds for Poly-GNNs and the Effect of Graph Noise**|Luciano Vinas et.al.|[2407.19567](http://arxiv.org/abs/2407.19567)|null|
|**2024-07-28**|**Interpretable Triplet Importance for Personalized Ranking**|Bowei He et.al.|[2407.19469](http://arxiv.org/abs/2407.19469)|**[link](https://github.com/bokwaiho/itipr)**|
|**2024-07-28**|**Reputation-Driven Asynchronous Federated Learning for Enhanced Trajectory Prediction with Blockchain**|Weiliang Chen et.al.|[2407.19428](http://arxiv.org/abs/2407.19428)|null|
|**2024-07-28**|**IDEA: A Flexible Framework of Certified Unlearning for Graph Neural Networks**|Yushun Dong et.al.|[2407.19398](http://arxiv.org/abs/2407.19398)|null|
|**2024-07-26**|**Enhancing material property prediction with ensemble deep graph convolutional networks**|Chowdhury Mohammad Abid Rahman et.al.|[2407.18847](http://arxiv.org/abs/2407.18847)|null|
|**2024-07-26**|**Robust Learning in Bayesian Parallel Branching Graph Neural Networks: The Narrow Width Limit**|Zechen Zhang et.al.|[2407.18807](http://arxiv.org/abs/2407.18807)|null|
|**2024-07-26**|**Learning production functions for supply chains with graph neural networks**|Serina Chang et.al.|[2407.18772](http://arxiv.org/abs/2407.18772)|**[link](https://github.com/snap-stanford/supply-chains)**|
|**2024-07-26**|**AutoRDF2GML: Facilitating RDF Integration in Graph Machine Learning**|Michael Färber et.al.|[2407.18735](http://arxiv.org/abs/2407.18735)|**[link](https://github.com/davidlamprecht/autordf2gml)**|
|**2024-07-26**|**Graph Neural Networks for Virtual Sensing in Complex Systems: Addressing Heterogeneous Temporal Dynamics**|Mengjie Zhao et.al.|[2407.18691](http://arxiv.org/abs/2407.18691)|null|
|**2024-07-26**|**DTFormer: A Transformer-Based Method for Discrete-Time Dynamic Graph Representation Learning**|Xi Chen et.al.|[2407.18523](http://arxiv.org/abs/2407.18523)|null|
|**2024-07-26**|**TCGPN: Temporal-Correlation Graph Pre-trained Network for Stock Forecasting**|Wenbo Yan et.al.|[2407.18519](http://arxiv.org/abs/2407.18519)|null|
|**2024-07-26**|**Scalable Graph Compressed Convolutions**|Junshu Sun et.al.|[2407.18480](http://arxiv.org/abs/2407.18480)|**[link](https://github.com/sunjss/cocn)**|
|**2024-07-26**|**Multi-turn Response Selection with Commonsense-enhanced Language Models**|Yuandong Wang et.al.|[2407.18479](http://arxiv.org/abs/2407.18479)|null|
|**2024-07-25**|**AsEP: Benchmarking Deep Learning Methods for Antibody-specific Epitope Prediction**|Chunan Liu et.al.|[2407.18184](http://arxiv.org/abs/2407.18184)|**[link](https://github.com/biochunan/asep-dataset)**|
|**2024-07-25**|**Gene Regulatory Network Inference from Pre-trained Single-Cell Transcriptomics Transformer with Joint Graph Learning**|Sindhura Kommu et.al.|[2407.18181](http://arxiv.org/abs/2407.18181)|null|
|**2024-07-25**|**RIDA: A Robust Attack Framework on Incomplete Graphs**|Jianke Yu et.al.|[2407.18170](http://arxiv.org/abs/2407.18170)|null|
|**2024-07-25**|**Personalized and Context-aware Route Planning for Edge-assisted Vehicles**|Dinesh Cyril Selvaraj et.al.|[2407.17980](http://arxiv.org/abs/2407.17980)|null|
|**2024-07-25**|**Mew: Multiplexed Immunofluorescence Image Analysis through an Efficient Multiplex Network**|Sukwon Yun et.al.|[2407.17857](http://arxiv.org/abs/2407.17857)|**[link](https://github.com/unites-lab/mew)**|
|**2024-07-25**|**Your Graph Recommender is Provably a Single-view Graph Contrastive Learning**|Wenjie Yang et.al.|[2407.17723](http://arxiv.org/abs/2407.17723)|null|
|**2024-07-25**|**Context-aware knowledge graph framework for traffic speed forecasting using graph neural network**|Yatao Zhang et.al.|[2407.17703](http://arxiv.org/abs/2407.17703)|**[link](https://github.com/mie-lab/ckg-traffic-forecasting)**|
|**2024-07-24**|**Systematic Reasoning About Relational Domains With Graph Neural Networks**|Irtaza Khalid et.al.|[2407.17396](http://arxiv.org/abs/2407.17396)|**[link](https://github.com/erg0dic/gnn-sg)**|
|**2024-07-24**|**Global and Local Confidence Based Fraud Detection Graph Neural Network**|Jiaxun Liu et.al.|[2407.17333](http://arxiv.org/abs/2407.17333)|null|
|**2024-07-24**|**Graph Neural Networks: A suitable Alternative to MLPs in Latent 3D Medical Image Classification?**|Johannes Kiechle et.al.|[2407.17219](http://arxiv.org/abs/2407.17219)|**[link](https://github.com/compai-lab/2024-miccai-grail-kiechle)**|
|**2024-07-24**|**Curriculum Negative Mining For Temporal Networks**|Ziyue Chen et.al.|[2407.17070](http://arxiv.org/abs/2407.17070)|**[link](https://github.com/zziyue83/curnm)**|
|**2024-07-23**|**Learning Networked Dynamical System Models with Weak Form and Graph Neural Networks**|Yin Yu et.al.|[2407.16779](http://arxiv.org/abs/2407.16779)|null|
|**2024-07-23**|**Enhancing GNNs Performance on Combinatorial Optimization by Recurrent Feature Update**|Daria Pugacheva et.al.|[2407.16468](http://arxiv.org/abs/2407.16468)|null|
|**2024-07-23**|**Ranking protein-protein models with large language models and graph neural networks**|Xiaotong Xu et.al.|[2407.16375](http://arxiv.org/abs/2407.16375)|**[link](https://github.com/haddocking/deeprank-gnn-esm)**|
|**2024-07-23**|**Transformer-based Graph Neural Networks for Battery Range Prediction in AIoT Battery-Swap Services**|Zhao Li et.al.|[2407.16115](http://arxiv.org/abs/2407.16115)|null|
|**2024-07-22**|**Link Polarity Prediction from Sparse and Noisy Labels via Multiscale Social Balance**|Marco Minici et.al.|[2407.15643](http://arxiv.org/abs/2407.15643)|**[link](https://github.com/mminici/SGNNfromSparseAndNoisyLabels)**|
|**2024-07-22**|**Large-scale Time-Varying Portfolio Optimisation using Graph Attention Networks**|Kamesh Korangi et.al.|[2407.15532](http://arxiv.org/abs/2407.15532)|null|
|**2024-07-22**|**GraphScale: A Framework to Enable Machine Learning over Billion-node Graphs**|Vipul Gupta et.al.|[2407.15452](http://arxiv.org/abs/2407.15452)|null|
|**2024-07-22**|**Pre-Training and Prompting for Few-Shot Node Classification on Text-Attributed Graphs**|Huanjing Zhao et.al.|[2407.15431](http://arxiv.org/abs/2407.15431)|null|
|**2024-07-23**|**LLMExplainer: Large Language Model based Bayesian Inference for Graph Explanation Generation**|Jiaxing Zhang et.al.|[2407.15351](http://arxiv.org/abs/2407.15351)|null|
|**2024-07-21**|**Revisiting Neighborhood Aggregation in Graph Neural Networks for Node Classification using Statistical Signal Processing**|Mounir Ghogho et.al.|[2407.15284](http://arxiv.org/abs/2407.15284)|null|
|**2024-07-21**|**LSM-GNN: Large-scale Storage-based Multi-GPU GNN Training by Optimizing Data Transfer Scheme**|Jeongmin Brian Park et.al.|[2407.15264](http://arxiv.org/abs/2407.15264)|null|
|**2024-07-21**|**A Spatio-Temporal Approach with Self-Corrective Causal Inference for Flight Delay Prediction**|Qihui Zhu et.al.|[2407.15185](http://arxiv.org/abs/2407.15185)|null|
|**2024-07-20**|**All Against Some: Efficient Integration of Large Language Models for Message Passing in Graph Neural Networks**|Ajay Jaiswal et.al.|[2407.14996](http://arxiv.org/abs/2407.14996)|null|
|**2024-07-20**|**Enhancing High-Energy Particle Physics Collision Analysis through Graph Data Attribution Techniques**|A. Verdone et.al.|[2407.14859](http://arxiv.org/abs/2407.14859)|null|
|**2024-07-22**|**Red-QAOA: Efficient Variational Optimization through Circuit Reduction**|Meng Wang et.al.|[2407.14490](http://arxiv.org/abs/2407.14490)|null|
|**2024-07-19**|**PolyFormer: Scalable Node-wise Filters via Polynomial Graph Transformer**|Jiahong Ma et.al.|[2407.14459](http://arxiv.org/abs/2407.14459)|**[link](https://github.com/air029/polyformer)**|
|**2024-07-19**|**L^2CL: Embarrassingly Simple Layer-to-Layer Contrastive Learning for Graph Collaborative Filtering**|Xinzhou Jin et.al.|[2407.14266](http://arxiv.org/abs/2407.14266)|**[link](https://github.com/downeykking/l2cl)**|
|**2024-07-19**|**Comparing and Contrasting Deep Learning Weather Prediction Backbones on Navier-Stokes and Atmospheric Dynamics**|Matthias Karlbauer et.al.|[2407.14129](http://arxiv.org/abs/2407.14129)|**[link](https://github.com/amazon-science/dlwp-benchmark)**|
|**2024-07-19**|**Enhancing Data-Limited Graph Neural Networks by Actively Distilling Knowledge from Large Language Models**|Quan Li et.al.|[2407.13989](http://arxiv.org/abs/2407.13989)|null|
|**2024-07-18**|**EggNet: An Evolving Graph-based Graph Attention Network for Particle Track Reconstruction**|Paolo Calafiura et.al.|[2407.13925](http://arxiv.org/abs/2407.13925)|null|
|**2024-07-18**|**Improving Malware Detection with Adversarial Domain Adaptation and Control Flow Graphs**|Adrian Shuai Li et.al.|[2407.13918](http://arxiv.org/abs/2407.13918)|null|
|**2024-07-18**|**Temperature Distribution Prediction in Laser Powder Bed Fusion using Transferable and Scalable Graph Neural Networks**|Riddhiman Raut et.al.|[2407.13838](http://arxiv.org/abs/2407.13838)|null|
|**2024-07-18**|**Predicting dark matter halo masses from simulated galaxy images and environments**|Austin J. Larson et.al.|[2407.13735](http://arxiv.org/abs/2407.13735)|null|
|**2024-07-18**|**Exploring End-to-end Differentiable Neural Charged Particle Tracking -- A Loss Landscape Perspective**|Tobias Kortus et.al.|[2407.13420](http://arxiv.org/abs/2407.13420)|**[link](https://github.com/SIVERT-pCT/e2e-tracking)**|
|**2024-07-18**|**HHGT: Hierarchical Heterogeneous Graph Transformer for Heterogeneous Graph Representation Learning**|Qiuyu Zhu et.al.|[2407.13158](http://arxiv.org/abs/2407.13158)|null|
|**2024-07-18**|**Krait: A Backdoor Attack Against Graph Prompt Tuning**|Ying Song et.al.|[2407.13068](http://arxiv.org/abs/2407.13068)|null|
|**2024-07-17**|**GraphMuse: A Library for Symbolic Music Graph Processing**|Emmanouil Karystinaios et.al.|[2407.12671](http://arxiv.org/abs/2407.12671)|**[link](https://github.com/manoskary/graphmuse)**|
|**2024-07-17**|**Fusion Flow-enhanced Graph Pooling Residual Networks for Unmanned Aerial Vehicles Surveillance in Day and Night Dual Visions**|Alam Noor et.al.|[2407.12647](http://arxiv.org/abs/2407.12647)|null|
|**2024-07-17**|**A Brief Review of Quantum Machine Learning for Financial Services**|Mina Doosti et.al.|[2407.12618](http://arxiv.org/abs/2407.12618)|null|
|**2024-07-17**|**SENC: Handling Self-collision in Neural Cloth Simulation**|Zhouyingcheng Liao et.al.|[2407.12479](http://arxiv.org/abs/2407.12479)|null|
|**2024-07-17**|**SafePowerGraph: Safety-aware Evaluation of Graph Neural Networks for Transmission Power Grids**|Salah Ghamizi et.al.|[2407.12421](http://arxiv.org/abs/2407.12421)|**[link](https://github.com/yamizi/safepowergraph)**|
|**2024-07-17**|**Dirac--Bianconi Graph Neural Networks -- Enabling Non-Diffusive Long-Range Graph Predictions**|Christian Nauck et.al.|[2407.12419](http://arxiv.org/abs/2407.12419)|**[link](https://github.com/PIK-ICoNe/DBGNN_paper-companion)**|
|**2024-07-17**|**Urban Traffic Forecasting with Integrated Travel Time and Data Availability in a Conformal Graph Neural Network Framework**|Mayur Patil et.al.|[2407.12238](http://arxiv.org/abs/2407.12238)|null|
|**2024-07-16**|**Molecular Topological Profile (MOLTOP) -- Simple and Strong Baseline for Molecular Graph Classification**|Jakub Adamczyk et.al.|[2407.12136](http://arxiv.org/abs/2407.12136)|null|
|**2024-07-16**|**Graph Neural Network-Based Track Finding in the LHCb Vertex Detector**|Anthony Correia et.al.|[2407.12119](http://arxiv.org/abs/2407.12119)|null|
|**2024-07-16**|**A Graph-based Adversarial Imitation Learning Framework for Reliable & Realtime Fleet Scheduling in Urban Air Mobility**|Prithvi Poddar et.al.|[2407.12113](http://arxiv.org/abs/2407.12113)|null|
|**2024-07-16**|**Tackling Oversmoothing in GNN via Graph Sparsification: A Truss-based Approach**|Tanvir Hossain et.al.|[2407.11928](http://arxiv.org/abs/2407.11928)|null|
|**2024-07-16**|**GraphFM: A Scalable Framework for Multi-Graph Pretraining**|Divyansha Lachi et.al.|[2407.11907](http://arxiv.org/abs/2407.11907)|null|
|**2024-07-16**|**Characterizing and Understanding HGNN Training on GPUs**|Dengke Han et.al.|[2407.11790](http://arxiv.org/abs/2407.11790)|null|
|**2024-07-16**|**Relaxing Graph Transformers for Adversarial Attacks**|Philipp Foth et.al.|[2407.11764](http://arxiv.org/abs/2407.11764)|null|
|**2024-07-16**|**$α$ -SGHN: A Robust Model for Learning Particle Interactions in Lattice Systems**|Yixian Gao et.al.|[2407.11684](http://arxiv.org/abs/2407.11684)|null|
|**2024-07-16**|**Rethinking Fair Graph Neural Networks from Re-balancing**|Zhixun Li et.al.|[2407.11624](http://arxiv.org/abs/2407.11624)|**[link](https://github.com/zhixunlee/fairgb)**|
|**2024-07-16**|**Graph Dimension Attention Networks for Enterprise Credit Assessment**|Shaopeng Wei et.al.|[2407.11615](http://arxiv.org/abs/2407.11615)|null|
|**2024-07-16**|**HyperAggregation: Aggregating over Graph Edges with Hypernetworks**|Nicolas Lell et.al.|[2407.11596](http://arxiv.org/abs/2407.11596)|**[link](https://github.com/foisunt/hyperaggregation)**|
|**2024-07-16**|**AU-vMAE: Knowledge-Guide Action Units Detection via Video Masked Autoencoder**|Qiaoqiao Jin et.al.|[2407.11468](http://arxiv.org/abs/2407.11468)|null|
|**2024-07-16**|**Accounting for Work Zone Disruptions in Traffic Flow Forecasting**|Yuanjie Lu et.al.|[2407.11407](http://arxiv.org/abs/2407.11407)|null|
|**2024-07-15**|**Provable Robustness of (Graph) Neural Networks Against Data Poisoning and Backdoor Attacks**|Lukas Gosch et.al.|[2407.10867](http://arxiv.org/abs/2407.10867)|**[link](https://github.com/saper0/qpcert)**|
|**2024-07-15**|**Rotationally Invariant Latent Distances for Uncertainty Estimation of Relaxed Energy Predictions by Graph Neural Network Potentials**|Joseph Musielewicz et.al.|[2407.10844](http://arxiv.org/abs/2407.10844)|null|
|**2024-07-15**|**Probability Passing for Graph Neural Networks: Graph Structure and Representations Joint Learning**|Ziyan Wang et.al.|[2407.10688](http://arxiv.org/abs/2407.10688)|**[link](https://github.com/jiyawang/ppgnn)**|
|**2024-07-15**|**Automated Label Unification for Multi-Dataset Semantic Segmentation with GNNs**|Rong Ma et.al.|[2407.10534](http://arxiv.org/abs/2407.10534)|null|
|**2024-07-15**|**Predicting doping strategies for ternary nickel-cobalt-manganese cathode materials to enhance battery performance using graph neural networks**|Zirui Zhao et.al.|[2407.10458](http://arxiv.org/abs/2407.10458)|null|
|**2024-07-15**|**Expanding the Scope: Inductive Knowledge Graph Reasoning with Multi-Starting Progressive Propagation**|Zhoutian Shao et.al.|[2407.10430](http://arxiv.org/abs/2407.10430)|**[link](https://github.com/nju-websoft/mstar)**|
|**2024-07-14**|**Toward Explainable Reasoning in 6G: A Proof of Concept Study on Radio Resource Allocation**|Farhad Rezazadeh et.al.|[2407.10186](http://arxiv.org/abs/2407.10186)|null|
|**2024-07-14**|**Warming Up Cold-Start CTR Prediction by Learning Item-Specific Feature Interactions**|Yaqing Wang et.al.|[2407.10112](http://arxiv.org/abs/2407.10112)|null|
|**2024-07-13**|**Biased Backpressure Routing Using Link Features and Graph Neural Networks**|Zhongyuan Zhao et.al.|[2407.09753](http://arxiv.org/abs/2407.09753)|**[link](https://github.com/zhongyuanzhao/dutybp)**|
|**2024-07-12**|**The Heterophilic Graph Learning Handbook: Benchmarks, Models, Theoretical Analysis, Applications and Challenges**|Sitao Luan et.al.|[2407.09618](http://arxiv.org/abs/2407.09618)|null|
|**2024-07-12**|**The $μ\mathcal{G}$ Language for Programming Graph Neural Networks**|Matteo Belenchia et.al.|[2407.09441](http://arxiv.org/abs/2407.09441)|null|
|**2024-07-12**|**A Perspective on Foundation Models for the Electric Power Grid**|Hendrik F. Hamann et.al.|[2407.09434](http://arxiv.org/abs/2407.09434)|null|
|**2024-07-12**|**The Effectiveness of Curvature-Based Rewiring and the Role of Hyperparameters in GNNs Revisited**|Floriano Tori et.al.|[2407.09381](http://arxiv.org/abs/2407.09381)|**[link](https://github.com/FloTori/Revisiting-Graph-Curvature-Rewiring)**|
|**2024-07-12**|**Graph Neural Network Causal Explanation via Neural Causal Models**|Arman Behnam et.al.|[2407.09378](http://arxiv.org/abs/2407.09378)|**[link](https://github.com/armanbehnam/cxgnn)**|
|**2024-07-12**|**GNN with Model-based RL for Multi-agent Systems**|Hanxiao Chen et.al.|[2407.09249](http://arxiv.org/abs/2407.09249)|null|
|**2024-07-12**|**Conformal Inductive Graph Neural Networks**|Soroush H. Zargarbashi et.al.|[2407.09173](http://arxiv.org/abs/2407.09173)|null|
|**2024-07-12**|**SlideGCD: Slide-based Graph Collaborative Training with Knowledge Distillation for Whole Slide Image Classification**|Tong Shu et.al.|[2407.08968](http://arxiv.org/abs/2407.08968)|**[link](https://github.com/hfut-mialab/slidegcd)**|
|**2024-07-12**|**Domain-Hierarchy Adaptation via Chain of Iterative Reasoning for Few-shot Hierarchical Text Classification**|Ke Ji et.al.|[2407.08959](http://arxiv.org/abs/2407.08959)|null|
|**2024-07-11**|**Deep Inverse Design for High-Level Synthesis**|Ping Chang et.al.|[2407.08797](http://arxiv.org/abs/2407.08797)|null|
|**2024-07-11**|**Robust Generalization of Graph Neural Networks for Carrier Scheduling**|Daniel F. Perez-Ramirez et.al.|[2407.08479](http://arxiv.org/abs/2407.08479)|null|
|**2024-07-11**|**Improving Molecular Modeling with Geometric GNNs: an Empirical Study**|Ali Ramlaoui et.al.|[2407.08313](http://arxiv.org/abs/2407.08313)|null|
|**2024-07-11**|**HRRPGraphNet: A Graph Neural Network Based Approach for HRRP Radar Target Recognition**|Lingfeng Chen et.al.|[2407.08236](http://arxiv.org/abs/2407.08236)|**[link](https://github.com/MountainChenCad/HRRPGraphNet)**|
|**2024-07-10**|**TinyGraph: Joint Feature and Node Condensation for Graph Neural Networks**|Yezi Liu et.al.|[2407.08064](http://arxiv.org/abs/2407.08064)|**[link](https://github.com/brandones/graphpca)**|
|**2024-07-10**|**AdaptiGraph: Material-Adaptive Graph-Based Neural Dynamics for Robotic Manipulation**|Kaifeng Zhang et.al.|[2407.07889](http://arxiv.org/abs/2407.07889)|null|
|**2024-07-10**|**Prediction of Frequency-Dependent Optical Spectrum for Solid Materials: A Multi-Output & Multi-Fidelity Machine Learning Approach**|Akram Ibrahim et.al.|[2407.07736](http://arxiv.org/abs/2407.07736)|null|
|**2024-07-10**|**Deep-Graph-Sprints: Accelerated Representation Learning in Continuous-Time Dynamic Graphs**|Ahmad Naser Eddin et.al.|[2407.07712](http://arxiv.org/abs/2407.07712)|null|
|**2024-07-10**|**Explaining Graph Neural Networks for Node Similarity on Graphs**|Daniel Daza et.al.|[2407.07639](http://arxiv.org/abs/2407.07639)|null|
|**2024-07-11**|**GLBench: A Comprehensive Benchmark for Graph with Large Language Models**|Yuhan Li et.al.|[2407.07457](http://arxiv.org/abs/2407.07457)|**[link](https://github.com/nineabyss/glbench)**|
|**2024-07-09**|**Graph Reinforcement Learning for Exploring BSM Model Spaces**|George N. Wojcik et.al.|[2407.07203](http://arxiv.org/abs/2407.07203)|null|
|**2024-07-09**|**Modularity aided consistent attributed graph clustering via coarsening**|Samarth Bhatia et.al.|[2407.07128](http://arxiv.org/abs/2407.07128)|null|
|**2024-07-09**|**Decoding Climate Disagreement: A Graph Neural Network-Based Approach to Understanding Social Media Dynamics**|Ruiran Su et.al.|[2407.07038](http://arxiv.org/abs/2407.07038)|null|
|**2024-07-09**|**Changepoint Detection in Highly-Attributed Dynamic Graphs**|Emiliano Penaloza et.al.|[2407.06998](http://arxiv.org/abs/2407.06998)|**[link](https://github.com/Emilianopp/ChangesHighlyAttributedGraphs)**|
|**2024-07-09**|**Limiting Over-Smoothing and Over-Squashing of Graph Message Passing by Deep Scattering Transforms**|Yuanhong Jiang et.al.|[2407.06988](http://arxiv.org/abs/2407.06988)|**[link](https://github.com/jyh6681/dsmp)**|
|**2024-07-09**|**Deep-Motion-Net: GNN-based volumetric organ shape reconstruction from single-view 2D projections**|Isuru Wijesinghe et.al.|[2407.06692](http://arxiv.org/abs/2407.06692)|null|
|**2024-07-09**|**Advanced Financial Fraud Detection Using GNN-CL Model**|Yu Cheng et.al.|[2407.06529](http://arxiv.org/abs/2407.06529)|null|
|**2024-07-09**|**Graph Neural Networks and Deep Reinforcement Learning Based Resource Allocation for V2X Communications**|Maoxin Ji et.al.|[2407.06518](http://arxiv.org/abs/2407.06518)|**[link](https://github.com/qiongwu86/gnn-and-drl-based-resource-allocation-for-v2x-communications)**|
|**2024-07-09**|**Using Graph Neural Networks and Frequency Domain Data for Automated Operational Modal Analysis of Populations of Structures**|Xudong Jian et.al.|[2407.06492](http://arxiv.org/abs/2407.06492)|**[link](https://github.com/JxdEngineer/ModalGNN_Freq_Domain)**|
|**2024-07-09**|**T2MAT (text-to-materials): A universal framework for generating material structures with goal properties from a single sentence**|Zhilong Song et.al.|[2407.06489](http://arxiv.org/abs/2407.06489)|null|
|**2024-07-09**|**Enhancing the Prediction of Glass Dynamics by Incorporating the Direction of Deviation from Equilibrium Positions**|Xiao Jiang et.al.|[2407.06111](http://arxiv.org/abs/2407.06111)|null|
|**2024-07-08**|**Graph Reasoning Networks**|Markus Zopf et.al.|[2407.05816](http://arxiv.org/abs/2407.05816)|null|
|**2024-07-08**|**Graph Attention with Random Rewiring**|Tongzhou Liao et.al.|[2407.05649](http://arxiv.org/abs/2407.05649)|null|
|**2024-07-08**|**MEEG and AT-DGNN: Advancing EEG Emotion Recognition with Music and Graph Learning**|Minghao Xiao et.al.|[2407.05550](http://arxiv.org/abs/2407.05550)|**[link](https://github.com/xmh1011/at-dgnn)**|
|**2024-07-07**|**PICA: Physics-Integrated Clothed Avatar**|Bo Peng et.al.|[2407.05324](http://arxiv.org/abs/2407.05324)|null|
|**2024-07-07**|**Vulnerability-Hunter: An Adaptive Feature Perception Attention Network for Smart Contract Vulnerabilities**|Yizhou Chen et.al.|[2407.05318](http://arxiv.org/abs/2407.05318)|null|
|**2024-07-06**|**Leveraging Persistent Homology Features for Accurate Defect Formation Energy Predictions via Graph Neural Networks**|Zhenyao Fang et.al.|[2407.05204](http://arxiv.org/abs/2407.05204)|null|
|**2024-07-06**|**A Generalized Transformer-based Radio Link Failure Prediction Framework in 5G RANs**|Kazi Hasan et.al.|[2407.05197](http://arxiv.org/abs/2407.05197)|null|
|**2024-07-06**|**GCON: Differentially Private Graph Convolutional Network via Objective Perturbation**|Jianxin Wei et.al.|[2407.05034](http://arxiv.org/abs/2407.05034)|null|
|**2024-07-06**|**Rethinking the Effectiveness of Graph Classification Datasets in Benchmarks for Assessing GNNs**|Zhengdao Li et.al.|[2407.04999](http://arxiv.org/abs/2407.04999)|**[link](https://github.com/ICLab4DL/GNNBenchEffectiveness)**|
|**2024-07-05**|**Peering inside the black box: Learning the relevance of many-body functions in Neural Network potentials**|Klara Bonneau et.al.|[2407.04526](http://arxiv.org/abs/2407.04526)|null|
|**2024-07-05**|**G-Adaptive mesh refinement -- leveraging graph neural networks and differentiable finite element solvers**|James Rowbottom et.al.|[2407.04516](http://arxiv.org/abs/2407.04516)|**[link](https://github.com/JRowbottomGit/g-adaptivity)**|
|**2024-07-05**|**Wavelet-based Temporal Attention Improves Traffic Forecasting**|Yash Jakhmola et.al.|[2407.04440](http://arxiv.org/abs/2407.04440)|**[link](https://github.com/yash-jakhmola/w-dstagnn)**|
|**2024-07-05**|**Dance of the ADS: Orchestrating Failures through Historically-Informed Scenario Fuzzing**|Tong Wang et.al.|[2407.04359](http://arxiv.org/abs/2407.04359)|null|
|**2024-07-08**|**SSP-GNN: Learning to Track via Bilevel Optimization**|Griffin Golias et.al.|[2407.04308](http://arxiv.org/abs/2407.04308)|null|
|**2024-07-05**|**Graph Pooling via Ricci Flow**|Amy Feng et.al.|[2407.04236](http://arxiv.org/abs/2407.04236)|null|
|**2024-07-04**|**Benchmark on Drug Target Interaction Modeling from a Structure Perspective**|Xinnan Zhang et.al.|[2407.04055](http://arxiv.org/abs/2407.04055)|**[link](https://github.com/justinwjl/gtb-dti)**|
|**2024-07-04**|**Reduced-Order Neural Operators: Learning Lagrangian Dynamics on Highly Sparse Graphs**|Hrishikesh Viswanath et.al.|[2407.03925](http://arxiv.org/abs/2407.03925)|**[link](https://github.com/hrishikeshvish/giorom)**|
|**2024-07-04**|**GraphCNNpred: A stock market indices prediction using a Graph based deep learning system**|Yuhui Jin et.al.|[2407.03760](http://arxiv.org/abs/2407.03760)|null|
|**2024-07-03**|**MHNet: Multi-view High-order Network for Diagnosing Neurodevelopmental Disorders Using Resting-state fMRI**|Yueyang Li et.al.|[2407.03217](http://arxiv.org/abs/2407.03217)|**[link](https://github.com/wayfear/brainnetworktransformer)**|
|**2024-07-03**|**Foundations and Frontiers of Graph Learning Theory**|Yu Huang et.al.|[2407.03125](http://arxiv.org/abs/2407.03125)|null|
|**2024-07-03**|**SF-GNN: Self Filter for Message Lossless Propagation in Deep Graph Neural Network**|Yushan Zhu et.al.|[2407.02762](http://arxiv.org/abs/2407.02762)|null|
|**2024-07-02**|**Holistically-Nested Structure-Aware Graph Neural Network for Road Extraction**|Tinghuai Wang et.al.|[2407.02639](http://arxiv.org/abs/2407.02639)|null|
|**2024-07-02**|**On the Robustness of Graph Reduction Against GNN Backdoor**|Yuxuan Zhu et.al.|[2407.02431](http://arxiv.org/abs/2407.02431)|null|
|**2024-07-02**|**Structure-Aware Consensus Network on Graphs with Few Labeled Nodes**|Shuaike Xu et.al.|[2407.02188](http://arxiv.org/abs/2407.02188)|null|
|**2024-07-02**|**Counterfactual Data Augmentation with Denoising Diffusion for Graph Anomaly Detection**|Chunjing Xiao et.al.|[2407.02143](http://arxiv.org/abs/2407.02143)|**[link](https://github.com/ChunjingXiao/CAGAD)**|
|**2024-07-02**|**CGAP: Urban Region Representation Learning with Coarsened Graph Attention Pooling**|Zhuo Xu et.al.|[2407.02074](http://arxiv.org/abs/2407.02074)|null|
|**2024-07-02**|**HC-GLAD: Dual Hyperbolic Contrastive Learning for Unsupervised Graph-Level Anomaly Detection**|Yali Fu et.al.|[2407.02057](http://arxiv.org/abs/2407.02057)|**[link](https://github.com/yali-f/hc-glad)**|
|**2024-07-02**|**DiGRAF: Diffeomorphic Graph-Adaptive Activation Function**|Krishna Sri Ipsit Mantri et.al.|[2407.02013](http://arxiv.org/abs/2407.02013)|**[link](https://github.com/ipsitmantri/digraf)**|
|**2024-07-02**|**Unveiling Global Interactive Patterns across Graphs: Towards Interpretable Graph Neural Networks**|Yuwen Wang et.al.|[2407.01979](http://arxiv.org/abs/2407.01979)|**[link](https://github.com/Wangyuwen0627/GIP-Framework)**|
|**2024-07-01**|**Hadronic Top Quark Polarimetry with ParticleNet**|Zhongtian Dong et.al.|[2407.01663](http://arxiv.org/abs/2407.01663)|null|
|**2024-07-01**|**GAT-Steiner: Rectilinear Steiner Minimal Tree Prediction Using GNNs**|Bugra Onal et.al.|[2407.01440](http://arxiv.org/abs/2407.01440)|null|
|**2024-07-01**|**RoboPack: Learning Tactile-Informed Dynamics Models for Dense Packing**|Bo Ai et.al.|[2407.01418](http://arxiv.org/abs/2407.01418)|null|
|**2024-06-28**|**Modeling the Real World with High-Density Visual Particle Dynamics**|William F. Whitney et.al.|[2406.19800](http://arxiv.org/abs/2406.19800)|null|
|**2024-06-28**|**SPIRONet: Spatial-Frequency Learning and Topological Channel Interaction Network for Vessel Segmentation**|De-Xing Huang et.al.|[2406.19749](http://arxiv.org/abs/2406.19749)|**[link](https://github.com/dxhuang-casia/spironet)**|
|**2024-06-27**|**Leveraging Contrastive Learning for Enhanced Node Representations in Tokenized Graph Transformers**|Jinsong Chen et.al.|[2406.19258](http://arxiv.org/abs/2406.19258)|null|
|**2024-06-27**|**NTFormer: A Composite Node Tokenized Graph Transformer for Node Classification**|Jinsong Chen et.al.|[2406.19249](http://arxiv.org/abs/2406.19249)|null|
|**2024-06-27**|**Improving the Expressiveness of $K$ -hop Message-Passing GNNs by Injecting Contextualized Substructure Information**|Tianjun Yao et.al.|[2406.19244](http://arxiv.org/abs/2406.19244)|**[link](https://github.com/tianyao-aka/expresive_k_hop_gnns)**|
|**2024-06-27**|**Heterogeneous Causal Metapath Graph Neural Network for Gene-Microbe-Disease Association Prediction**|Kexin Zhang et.al.|[2406.19156](http://arxiv.org/abs/2406.19156)|**[link](https://github.com/zkxinxin/hcmgnn)**|
|**2024-06-27**|**Constructing and Analyzing Different Density Graphs for Path Extrapolation in Wikipedia**|Martha Sotiroudi et.al.|[2406.19039](http://arxiv.org/abs/2406.19039)|null|
|**2024-07-01**|**Amplify Graph Learning for Recommendation via Sparsity Completion**|Peng Yuan et.al.|[2406.18984](http://arxiv.org/abs/2406.18984)|**[link](https://github.com/yp8976/AGL_SC)**|
|**2024-06-29**|**Federated Graph Semantic and Structural Learning**|Wenke Huang et.al.|[2406.18937](http://arxiv.org/abs/2406.18937)|**[link](https://github.com/guanchengwan/fgssl)**|
|**2024-06-27**|**What Is Missing In Homophily? Disentangling Graph Homophily For Graph Neural Networks**|Yilun Zheng et.al.|[2406.18854](http://arxiv.org/abs/2406.18854)|**[link](https://github.com/zylmozart/disentangle_graphhom)**|
|**2024-06-27**|**Retain, Blend, and Exchange: A Quality-aware Spatial-Stereo Fusion Approach for Event Stream Recognition**|Lan Chen et.al.|[2406.18845](http://arxiv.org/abs/2406.18845)|**[link](https://github.com/event-ahu/efv_event_classification)**|
|**2024-06-27**|**MissionGNN: Hierarchical Multimodal GNN-based Weakly Supervised Video Anomaly Recognition with Mission-Specific Knowledge Graph Generation**|Sanggeon Yun et.al.|[2406.18815](http://arxiv.org/abs/2406.18815)|null|
|**2024-06-26**|**Graph Neural Networks for Emulation of Finite-Element Ice Dynamics in Greenland and Antarctic Ice Sheets**|Younghyun Koo et.al.|[2406.18423](http://arxiv.org/abs/2406.18423)|null|
|**2024-06-26**|**KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning**|Roman Bresson et.al.|[2406.18380](http://arxiv.org/abs/2406.18380)|**[link](https://github.com/RomanBresson/KAGNN)**|
|**2024-06-26**|**Kolmogorov-Arnold Graph Neural Networks**|Gianluca De Carlo et.al.|[2406.18354](http://arxiv.org/abs/2406.18354)|null|
|**2024-06-26**|**ContactNet: Geometric-Based Deep Learning Model for Predicting Protein-Protein Interactions**|Matan Halfon et.al.|[2406.18314](http://arxiv.org/abs/2406.18314)|null|
|**2024-06-25**|**Efficient and Effective Implicit Dynamic Graph Neural Network**|Yongjian Zhong et.al.|[2406.17894](http://arxiv.org/abs/2406.17894)|**[link](https://github.com/yongjian16/IDGNN)**|
|**2024-06-25**|**Compositional Models for Estimating Causal Effects**|Purva Pruthi et.al.|[2406.17714](http://arxiv.org/abs/2406.17714)|null|
|**2024-06-25**|**Distributed Training of Large Graph Neural Networks with Variable Communication Rates**|Juan Cervino et.al.|[2406.17611](http://arxiv.org/abs/2406.17611)|null|
|**2024-06-25**|**Joint Admission Control and Resource Allocation of Virtual Network Embedding via Hierarchical Deep Reinforcement Learning**|Tianfu Wang et.al.|[2406.17334](http://arxiv.org/abs/2406.17334)|**[link](https://github.com/geminilight/hrl-acra)**|
|**2024-06-25**|**Distance Recomputator and Topology Reconstructor for Graph Neural Networks**|Dong Liu et.al.|[2406.17281](http://arxiv.org/abs/2406.17281)|**[link](https://github.com/NoakLiu/Distance-Recomputator-and-Topology-Reconstructor)**|
|**2024-06-25**|**TopoGCL: Topological Graph Contrastive Learning**|Yuzhou Chen et.al.|[2406.17251](http://arxiv.org/abs/2406.17251)|**[link](https://github.com/topogclaaai24/topogcl)**|
|**2024-06-24**|**Meta-GCN: A Dynamically Weighted Loss Minimization Method for Dealing with the Data Imbalance in Graph Neural Networks**|Mahdi Mohammadizadeh et.al.|[2406.17073](http://arxiv.org/abs/2406.17073)|null|
|**2024-06-24**|**GC-Bench: A Benchmark Framework for Graph Condensation with New Insights**|Shengbo Gong et.al.|[2406.16715](http://arxiv.org/abs/2406.16715)|**[link](https://github.com/emory-melody/graphslim)**|
|**2024-06-24**|**Link Prediction with Untrained Message Passing Layers**|Lisi Qarkaxhija et.al.|[2406.16687](http://arxiv.org/abs/2406.16687)|null|
|**2024-06-24**|**Ensemble-Embedding Graph Neural Network for Direct Prediction of Optical Spectra from Crystal Structure**|Nguyen Tuan Hung et.al.|[2406.16654](http://arxiv.org/abs/2406.16654)|**[link](https://github.com/nguyen-group/GNNOpt)**|
|**2024-06-24**|**Inference of Sequential Patterns for Neural Message Passing in Temporal Graphs**|Jan von Pichowski et.al.|[2406.16552](http://arxiv.org/abs/2406.16552)|null|
|**2024-06-24**|**Towards Lightweight Graph Neural Network Search with Curriculum Graph Sparsification**|Beini Xie et.al.|[2406.16357](http://arxiv.org/abs/2406.16357)|null|
|**2024-06-24**|**Multimodal Graph Benchmark**|Jing Zhu et.al.|[2406.16321](http://arxiv.org/abs/2406.16321)|**[link](https://github.com/mm-graph-benchmark/mm-graph-benchmark)**|
|**2024-06-24**|**Relaxing Continuous Constraints of Equivariant Graph Neural Networks for Physical Dynamics Learning**|Zinan Zheng et.al.|[2406.16295](http://arxiv.org/abs/2406.16295)|**[link](https://github.com/compasszzn/degnn)**|
|**2024-06-23**|**F-FOMAML: GNN-Enhanced Meta-Learning for Peak Period Demand Forecasting with Proxy Data**|Zexing Xu et.al.|[2406.16221](http://arxiv.org/abs/2406.16221)|null|
|**2024-06-22**|**Automatic AI Model Selection for Wireless Systems: Online Learning via Digital Twinning**|Qiushuo Hou et.al.|[2406.15819](http://arxiv.org/abs/2406.15819)|**[link](https://github.com/qiushuo0913/DT-powered-AMS)**|
|**2024-06-22**|**Synergistic Deep Graph Clustering Network**|Benyu Wu et.al.|[2406.15797](http://arxiv.org/abs/2406.15797)|**[link](https://github.com/Marigoldwu/SynC)**|
|**2024-06-21**|**Learning Spatio-Temporal Patterns of Polar Ice Layers With Physics-Informed Graph Neural Network**|Zesheng Liu et.al.|[2406.15299](http://arxiv.org/abs/2406.15299)|null|
|**2024-06-21**|**FT-AED: Benchmark Dataset for Early Freeway Traffic Anomalous Event Detection**|Austin Coursey et.al.|[2406.15283](http://arxiv.org/abs/2406.15283)|**[link](https://github.com/acoursey3/freeway-anomaly-data)**|
|**2024-06-21**|**Perks and Pitfalls of Faithfulness in Regular, Self-Explainable and Domain Invariant GNNs**|Steve Azzolin et.al.|[2406.15156](http://arxiv.org/abs/2406.15156)|null|
|**2024-06-21**|**Towards General Negotiation Strategies with End-to-End Reinforcement Learning**|Bram M. Renting et.al.|[2406.15096](http://arxiv.org/abs/2406.15096)|**[link](https://github.com/brenting/RL-negotiation)**|
|**2024-06-21**|**Efficient Graph Similarity Computation with Alignment Regularization**|Wei Zhuo et.al.|[2406.14929](http://arxiv.org/abs/2406.14929)|**[link](https://github.com/jhuow/eric)**|
|**2024-06-20**|**Relational Reasoning On Graphs Using Opinion Dynamics**|Yulong Yang et.al.|[2406.14746](http://arxiv.org/abs/2406.14746)|null|
|**2024-06-20**|**Graph Representation Learning Strategies for Omics Data: A Case Study on Parkinson's Disease**|Elisa Gómez de Lope et.al.|[2406.14442](http://arxiv.org/abs/2406.14442)|null|
|**2024-06-20**|**Iterative Sizing Field Prediction for Adaptive Mesh Generation From Expert Demonstrations**|Niklas Freymuth et.al.|[2406.14161](http://arxiv.org/abs/2406.14161)|**[link](https://github.com/NiklasFreymuth/AMBER)**|
|**2024-06-20**|**Geometric Self-Supervised Pretraining on 3D Protein Structures using Subgraphs**|Michail Chatzianastasis et.al.|[2406.14142](http://arxiv.org/abs/2406.14142)|null|
|**2024-06-20**|**Graph Neural Networks for Job Shop Scheduling Problems: A Survey**|Igor G. Smit et.al.|[2406.14096](http://arxiv.org/abs/2406.14096)|null|
|**2024-06-20**|**HIGHT: Hierarchical Graph Tokenization for Graph-Language Alignment**|Yongqiang Chen et.al.|[2406.14021](http://arxiv.org/abs/2406.14021)|null|
|**2024-06-20**|**Reducing Memory Contention and I/O Congestion for Disk-based GNN Training**|Qisheng Jiang et.al.|[2406.13984](http://arxiv.org/abs/2406.13984)|**[link](https://github.com/toast-lab/gnndrive)**|
|**2024-06-20**|**Explainable AI Security: Exploring Robustness of Graph Neural Networks to Adversarial Attacks**|Tao Wu et.al.|[2406.13920](http://arxiv.org/abs/2406.13920)|null|
|**2024-06-19**|**A Pure Transformer Pretraining Framework on Text-attributed Graphs**|Yu Song et.al.|[2406.13873](http://arxiv.org/abs/2406.13873)|**[link](https://github.com/songyyyy/gspt)**|
|**2024-06-19**|**Global Human-guided Counterfactual Explanations for Molecular Properties via Reinforcement Learning**|Danqing Wang et.al.|[2406.13869](http://arxiv.org/abs/2406.13869)|**[link](https://github.com/dqwang122/rlhex)**|
|**2024-06-19**|**Evaluating representation learning on the protein structure universe**|Arian R. Jamasb et.al.|[2406.13864](http://arxiv.org/abs/2406.13864)|**[link](https://github.com/a-r-j/proteinworkshop)**|
|**2024-06-18**|**Demystifying Higher-Order Graph Neural Networks**|Maciej Besta et.al.|[2406.12841](http://arxiv.org/abs/2406.12841)|null|
|**2024-06-18**|**Graph Neural Networks in Histopathology: Emerging Trends and Future Directions**|Siemen Brussee et.al.|[2406.12808](http://arxiv.org/abs/2406.12808)|null|
|**2024-06-18**|**Research and Implementation of Data Enhancement Techniques for Graph Neural Networks**|Jingzhao Gu et.al.|[2406.12640](http://arxiv.org/abs/2406.12640)|null|
|**2024-06-18**|**Bridging Local Details and Global Context in Text-Attributed Graphs**|Yaoke Wang et.al.|[2406.12608](http://arxiv.org/abs/2406.12608)|**[link](https://github.com/wykk00/graphbridge)**|
|**2024-06-18**|**The Heterophilic Snowflake Hypothesis: Training and Empowering GNNs for Heterophilic Graphs**|Kun Wang et.al.|[2406.12539](http://arxiv.org/abs/2406.12539)|**[link](https://github.com/bingreeky/heterosnoh)**|
|**2024-06-18**|**A data-centric approach for assessing progress of Graph Neural Networks**|Tianqi Zhao et.al.|[2406.12439](http://arxiv.org/abs/2406.12439)|**[link](https://github.com/tianqi-py/mlgnc)**|
|**2024-06-18**|**Federated Learning with Limited Node Labels**|Bisheng Tang et.al.|[2406.12435](http://arxiv.org/abs/2406.12435)|null|
|**2024-06-18**|**SAGDFN: A Scalable Adaptive Graph Diffusion Forecasting Network for Multivariate Time Series Forecasting**|Yue Jiang et.al.|[2406.12282](http://arxiv.org/abs/2406.12282)|**[link](https://github.com/JIANGYUE61610306/SAGDFN)**|
|**2024-06-17**|**Thermodynamic Transferability in Coarse-Grained Force Fields using Graph Neural Networks**|Emily Shinkle et.al.|[2406.12112](http://arxiv.org/abs/2406.12112)|null|
|**2024-06-17**|**STNAGNN: Spatiotemporal Node Attention Graph Neural Network for Task-based fMRI Analysis**|Jiyao Wang et.al.|[2406.12065](http://arxiv.org/abs/2406.12065)|null|
|**2024-06-17**|**Composing Object Relations and Attributes for Image-Text Matching**|Khoi Pham et.al.|[2406.11820](http://arxiv.org/abs/2406.11820)|**[link](https://github.com/vkhoi/cora_cvpr24)**|
|**2024-06-17**|**Graph Neural Re-Ranking via Corpus Graph**|Andrea Giuseppe Di Francesco et.al.|[2406.11720](http://arxiv.org/abs/2406.11720)|null|
|**2024-06-17**|**Scalable Expressiveness through Preprocessed Graph Perturbations**|Danial Saber et.al.|[2406.11714](http://arxiv.org/abs/2406.11714)|**[link](https://github.com/Danial-sb/SE2P)**|
|**2024-06-17**|**On the Feasibility of Fidelity $^-$ for Graph Pruning**|Yong-Min Shin et.al.|[2406.11504](http://arxiv.org/abs/2406.11504)|null|
|**2024-06-17**|**Attention-Based Deep Reinforcement Learning for Qubit Allocation in Modular Quantum Architectures**|Enrico Russo et.al.|[2406.11452](http://arxiv.org/abs/2406.11452)|null|
|**2024-06-17**|**Analysing the Behaviour of Tree-Based Neural Networks in Regression Tasks**|Peter Samoaa et.al.|[2406.11437](http://arxiv.org/abs/2406.11437)|**[link](https://github.com/petersamoaa/tree_based_nn_error_analysis)**|
|**2024-06-17**|**Dredge Word, Social Media, and Webgraph Networks for Unreliable Website Classification and Identification**|Evan M. Williams et.al.|[2406.11423](http://arxiv.org/abs/2406.11423)|null|
|**2024-06-17**|**DeFiGuard: A Price Manipulation Detection Service in DeFi using Graph Neural Networks**|Dabao Wang et.al.|[2406.11157](http://arxiv.org/abs/2406.11157)|null|
|**2024-06-16**|**Graph Neural Reaction Diffusion Models**|Moshe Eliasof et.al.|[2406.10871](http://arxiv.org/abs/2406.10871)|null|
|**2024-06-16**|**Global-Local Graph Neural Networks for Node-Classification**|Moshe Eliasof et.al.|[2406.10863](http://arxiv.org/abs/2406.10863)|null|
|**2024-06-14**|**Compressed Sensor Caching and Collaborative Sparse Data Recovery with Anchor Alignment**|Yi-Jen Yang et.al.|[2406.10137](http://arxiv.org/abs/2406.10137)|null|
|**2024-06-14**|**Rule Based Learning with Dynamic (Graph) Neural Networks**|Florian Seiffarth et.al.|[2406.09954](http://arxiv.org/abs/2406.09954)|**[link](https://github.com/fseiffarth/gnn-comparison)**|
|**2024-06-14**|**IGL-Bench: Establishing the Comprehensive Benchmark for Imbalanced Graph Learning**|Jiawen Qin et.al.|[2406.09870](http://arxiv.org/abs/2406.09870)|**[link](https://github.com/ringbdstack/igl-bench)**|
|**2024-06-14**|**Robustness-Inspired Defense Against Backdoor Attacks on Graph Neural Networks**|Zhiwei Zhang et.al.|[2406.09836](http://arxiv.org/abs/2406.09836)|null|
|**2024-06-14**|**Benchmarking Spectral Graph Neural Networks: A Comprehensive Study on Effectiveness and Efficiency**|Ningyi Liao et.al.|[2406.09675](http://arxiv.org/abs/2406.09675)|**[link](https://github.com/gdmnl/spectral-gnn-benchmark)**|
|**2024-06-13**|**Automated Molecular Concept Generation and Labeling with Large Language Models**|Shichang Zhang et.al.|[2406.09612](http://arxiv.org/abs/2406.09612)|**[link](https://github.com/ziminz19/automolco)**|
|**2024-06-13**|**Differentiable Reasoning about Knowledge Graphs with Region-based Graph Neural Networks**|Aleksandar Pavlovic et.al.|[2406.09529](http://arxiv.org/abs/2406.09529)|null|
|**2024-06-13**|**On the Expressibility of the Reconstructional Color Refinement**|V. Arvind et.al.|[2406.09351](http://arxiv.org/abs/2406.09351)|null|
|**2024-06-13**|**Scoreformer: A Surrogate Model For Large-Scale Prediction of Docking Scores**|Álvaro Ciudad et.al.|[2406.09346](http://arxiv.org/abs/2406.09346)|null|
|**2024-06-13**|**Transformers meet Neural Algorithmic Reasoners**|Wilfried Bounsi et.al.|[2406.09308](http://arxiv.org/abs/2406.09308)|null|
|**2024-06-13**|**A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products and Graph Coarsening**|Guy Bar-Shalom et.al.|[2406.09291](http://arxiv.org/abs/2406.09291)|null|
|**2024-06-13**|**ALPHAGMUT: A Rationale-Guided Alpha Shape Graph Neural Network to Evaluate Mutation Effects**|Boshen Wang et.al.|[2406.09159](http://arxiv.org/abs/2406.09159)|null|
|**2024-06-13**|**Classic GNNs are Strong Baselines: Reassessing GNNs for Node Classification**|Yuankai Luo et.al.|[2406.08993](http://arxiv.org/abs/2406.08993)|**[link](https://github.com/LUOyk1999/tunedGNN)**|
|**2024-06-13**|**Self-supervised Graph Neural Network for Mechanical CAD Retrieval**|Yuhan Quan et.al.|[2406.08863](http://arxiv.org/abs/2406.08863)|null|
|**2024-06-13**|**Trajectory Planning for Autonomous Driving in Unstructured Scenarios Based on Graph Neural Network and Numerical Optimization**|Sumin Zhang et.al.|[2406.08855](http://arxiv.org/abs/2406.08855)|null|
|**2024-06-14**|**LGB: Language Model and Graph Neural Network-Driven Social Bot Detection**|Ming Zhou et.al.|[2406.08762](http://arxiv.org/abs/2406.08762)|null|
|**2024-06-13**|**Introducing Diminutive Causal Structure into Graph Representation Learning**|Hang Gao et.al.|[2406.08709](http://arxiv.org/abs/2406.08709)|null|
|**2024-06-12**|**GraphFM: A Comprehensive Benchmark for Graph Foundation Model**|Yuhao Xu et.al.|[2406.08310](http://arxiv.org/abs/2406.08310)|**[link](https://github.com/nyushcs/graphfm)**|
|**2024-06-12**|**Pre-Training Identification of Graph Winning Tickets in Adaptive Spatial-Temporal Graph Neural Networks**|Wenying Duan et.al.|[2406.08287](http://arxiv.org/abs/2406.08287)|null|
|**2024-06-12**|**Conformal Load Prediction with Transductive Graph Autoencoders**|Rui Luo et.al.|[2406.08281](http://arxiv.org/abs/2406.08281)|**[link](https://github.com/luo-lorry/conformal-load-forecasting)**|
|**2024-06-12**|**Expressivity and Generalization: Fragment-Biases for Molecular GNNs**|Tom Wollschläger et.al.|[2406.08210](http://arxiv.org/abs/2406.08210)|null|
|**2024-06-12**|**Balancing Molecular Information and Empirical Data in the Prediction of Physico-Chemical Properties**|Johannes Zenn et.al.|[2406.08075](http://arxiv.org/abs/2406.08075)|**[link](https://github.com/jzenn/gnn-mcm)**|
|**2024-06-12**|**Heuristic Learning with Graph Neural Networks: A Unified Framework for Link Prediction**|Juzhen Zhang et.al.|[2406.07979](http://arxiv.org/abs/2406.07979)|**[link](https://github.com/LARS-research/HL-GNN)**|
|**2024-06-12**|**How Interpretable Are Interpretable Graph Neural Networks?**|Yongqiang Chen et.al.|[2406.07955](http://arxiv.org/abs/2406.07955)|**[link](https://github.com/LFhase/GMT)**|
|**2024-06-12**|**Graph Transductive Defense: a Two-Stage Defense for Graph Membership Inference Attacks**|Peizhi Niu et.al.|[2406.07917](http://arxiv.org/abs/2406.07917)|null|
|**2024-06-11**|**Graph Reasoning for Explainable Cold Start Recommendation**|Jibril Frej et.al.|[2406.07420](http://arxiv.org/abs/2406.07420)|null|
|**2024-06-11**|**Rethinking the impact of noisy labels in graph classification: A utility and privacy perspective**|De Li et.al.|[2406.07314](http://arxiv.org/abs/2406.07314)|null|
|**2024-06-11**|**Logical Distillation of Graph Neural Networks**|Alexander Pluska et.al.|[2406.07126](http://arxiv.org/abs/2406.07126)|**[link](https://github.com/lexpk/logicaldistillationofgnns)**|
|**2024-06-11**|**CHARME: A chain-based reinforcement learning approach for the minor embedding problem**|Hoang M. Ngo et.al.|[2406.07124](http://arxiv.org/abs/2406.07124)|null|
|**2024-06-11**|**On the Hölder Stability of Multiset and Graph Neural Networks**|Yair Davidson et.al.|[2406.06984](http://arxiv.org/abs/2406.06984)|null|
|**2024-06-11**|**Non-autoregressive Personalized Bundle Generation**|Wenchuan Yang et.al.|[2406.06925](http://arxiv.org/abs/2406.06925)|null|
|**2024-06-10**|**Spatiotemporal Graph Neural Network Modelling Perfusion MRI**|Ruodan Yan et.al.|[2406.06434](http://arxiv.org/abs/2406.06434)|null|
|**2024-06-10**|**Explainable Graph Neural Networks Under Fire**|Zhong Li et.al.|[2406.06417](http://arxiv.org/abs/2406.06417)|**[link](https://github.com/zhonglifr/gxattack)**|
|**2024-06-10**|**Learning Physical Simulation with Message Passing Transformer**|Zeyi Xu et.al.|[2406.06060](http://arxiv.org/abs/2406.06060)|null|
|**2024-06-10**|**MAGNOLIA: Matching Algorithms via GNNs for Online Value-to-go Approximation**|Alexandre Hayderi et.al.|[2406.05959](http://arxiv.org/abs/2406.05959)|**[link](https://github.com/anders-wikum/GNN-OBM)**|
|**2024-06-09**|**Expressive Power of Graph Neural Networks for (Mixed-Integer) Quadratic Programs**|Ziang Chen et.al.|[2406.05938](http://arxiv.org/abs/2406.05938)|null|
|**2024-06-09**|**Security Vulnerability Detection with Multitask Self-Instructed Fine-Tuning of Large Language Models**|Aidan Z. H. Yang et.al.|[2406.05892](http://arxiv.org/abs/2406.05892)|null|
|**2024-06-09**|**Scaling Graph Convolutions for Mobile Vision**|William Avery et.al.|[2406.05850](http://arxiv.org/abs/2406.05850)|**[link](https://github.com/sldgroup/mobilevigv2)**|
|**2024-06-09**|**Distributed Combinatorial Optimization of Downlink User Assignment in mmWave Cell-free Massive MIMO Using Graph Neural Networks**|Bile Peng et.al.|[2406.05652](http://arxiv.org/abs/2406.05652)|null|
|**2024-06-09**|**What is my quantum computer good for? Quantum capability learning with physics-aware neural networks**|Daniel Hothem et.al.|[2406.05636](http://arxiv.org/abs/2406.05636)|null|
|**2024-06-08**|**Prioritizing Potential Wetland Areas via Region-to-Region Knowledge Transfer and Adaptive Propagation**|Yoonhyuk Choi et.al.|[2406.05578](http://arxiv.org/abs/2406.05578)|null|
|**2024-06-07**|**Online Frequency Scheduling by Learning Parallel Actions**|Anastasios Giovanidis et.al.|[2406.05041](http://arxiv.org/abs/2406.05041)|null|
|**2024-06-07**|**SpanGNN: Towards Memory-Efficient Graph Neural Networks via Spanning Subgraph Training**|Xizhi Gu et.al.|[2406.04938](http://arxiv.org/abs/2406.04938)|**[link](https://github.com/guxizhi/spangnn)**|
|**2024-06-07**|**QAGCF: Graph Collaborative Filtering for Q&A Recommendation**|Changshuo Zhang et.al.|[2406.04828](http://arxiv.org/abs/2406.04828)|null|
|**2024-06-07**|**Graph Mining under Data scarcity**|Appan Rakaraddi et.al.|[2406.04825](http://arxiv.org/abs/2406.04825)|null|
|**2024-06-07**|**GENIE: Watermarking Graph Neural Networks for Link Prediction**|Venkata Sai Pranav Bachina et.al.|[2406.04805](http://arxiv.org/abs/2406.04805)|null|
|**2024-06-07**|**Mobile Network Configuration Recommendation using Deep Generative Graph Neural Network**|Shirwan Piroti et.al.|[2406.04779](http://arxiv.org/abs/2406.04779)|null|
|**2024-06-07**|**Probabilistic Weather Forecasting with Hierarchical Graph Neural Networks**|Joel Oskarsson et.al.|[2406.04759](http://arxiv.org/abs/2406.04759)|**[link](https://github.com/mllam/neural-lam)**|
|**2024-06-07**|**Enhancing Size Generalization in Graph Neural Networks through Disentangled Representation Learning**|Zheng Huang et.al.|[2406.04601](http://arxiv.org/abs/2406.04601)|**[link](https://github.com/graphminddartmouth/disgen)**|
|**2024-06-06**|**GNNAnatomy: Systematic Generation and Evaluation of Multi-Level Explanations for Graph Neural Networks**|Hsiao-Ying Lu et.al.|[2406.04548](http://arxiv.org/abs/2406.04548)|null|
|**2024-06-06**|**Learning Optimal Linear Precoding for Cell-Free Massive MIMO with GNN**|Benjamin Parlier et.al.|[2406.04456](http://arxiv.org/abs/2406.04456)|**[link](https://github.com/Nokia-Bell-Labs/olp-gnn)**|
|**2024-06-06**|**On the Expressive Power of Spectral Invariant Graph Neural Networks**|Bohang Zhang et.al.|[2406.04336](http://arxiv.org/abs/2406.04336)|**[link](https://github.com/LingxiaoShawn/EPNN-Experiments)**|
|**2024-06-07**|**NoisyGL: A Comprehensive Benchmark for Graph Neural Networks under Label Noise**|Zhonghao Wang et.al.|[2406.04299](http://arxiv.org/abs/2406.04299)|**[link](https://github.com/eaglelab-zju/noisygl)**|
|**2024-06-06**|**Transformers need glasses! Information over-squashing in language tasks**|Federico Barbero et.al.|[2406.04267](http://arxiv.org/abs/2406.04267)|null|
|**2024-06-06**|**Multivector Neurons: Better and Faster O(n)-Equivariant Clifford Graph Neural Networks**|Cong Liu et.al.|[2406.04052](http://arxiv.org/abs/2406.04052)|**[link](https://github.com/congliuUvA/Multivector-Neurons)**|
|**2024-06-06**|**Energy-based Epistemic Uncertainty for Graph Neural Networks**|Dominik Fuchsgruber et.al.|[2406.04043](http://arxiv.org/abs/2406.04043)|null|
|**2024-06-06**|**Exploiting Global Graph Homophily for Generalized Defense in Graph Neural Networks**|Duanyu Li et.al.|[2406.03833](http://arxiv.org/abs/2406.03833)|null|
|**2024-06-06**|**BindGPT: A Scalable Framework for 3D Molecular Design via Language Modeling and Reinforcement Learning**|Artem Zholus et.al.|[2406.03686](http://arxiv.org/abs/2406.03686)|null|
|**2024-06-06**|**PANDA: Expanded Width-Aware Message Passing Beyond Rewiring**|Jeongwhan Choi et.al.|[2406.03671](http://arxiv.org/abs/2406.03671)|**[link](https://github.com/jeongwhanchoi/panda)**|
|**2024-06-05**|**Decision-focused Graph Neural Networks for Combinatorial Optimization**|Yang Liu et.al.|[2406.03647](http://arxiv.org/abs/2406.03647)|null|
|**2024-06-05**|**Equivariant Graph Neural Networks for Prediction of Tensor Material Properties of Crystals**|Alex Heilman et.al.|[2406.03563](http://arxiv.org/abs/2406.03563)|null|
|**2024-06-05**|**Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach**|Haoyu Han et.al.|[2406.03464](http://arxiv.org/abs/2406.03464)|null|
|**2024-06-05**|**Learning Long Range Dependencies on Graphs via Random Walks**|Dexiong Chen et.al.|[2406.03386](http://arxiv.org/abs/2406.03386)|**[link](https://github.com/borgwardtlab/neuralwalker)**|
|**2024-06-05**|**Using GNN property predictors as molecule generators**|Félix Therrien et.al.|[2406.03278](http://arxiv.org/abs/2406.03278)|**[link](https://github.com/ftherrien/inv-design)**|
|**2024-06-06**|**Generating Explanations for Cellular Neural Networks**|Akshit Sinha et.al.|[2406.03253](http://arxiv.org/abs/2406.03253)|null|
|**2024-06-05**|**Graph Neural Network Explanations are Fragile**|Jiate Li et.al.|[2406.03193](http://arxiv.org/abs/2406.03193)|**[link](https://github.com/JetRichardLee/Attack-XGNN)**|
|**2024-06-05**|**Topological Neural Networks go Persistent, Equivariant, and Continuous**|Yogesh Verma et.al.|[2406.03164](http://arxiv.org/abs/2406.03164)|null|
|**2024-06-05**|**Aligning Transformers with Weisfeiler-Leman**|Luis Müller et.al.|[2406.03148](http://arxiv.org/abs/2406.03148)|**[link](https://github.com/luis-mueller/wl-transformers)**|
|**2024-06-06**|**E(n) Equivariant Message Passing Cellular Networks**|Veljko Kovač et.al.|[2406.03145](http://arxiv.org/abs/2406.03145)|null|
|**2024-06-05**|**A Data and Model-Driven Deep Learning Approach to Robust Downlink Beamforming Optimization**|Kai Liang et.al.|[2406.03098](http://arxiv.org/abs/2406.03098)|null|
|**2024-06-05**|**Enhancing the Resilience of Graph Neural Networks to Topological Perturbations in Sparse Graphs**|Shuqi He et.al.|[2406.03097](http://arxiv.org/abs/2406.03097)|null|
|**2024-06-04**|**XRec: Large Language Models for Explainable Recommendation**|Qiyao Ma et.al.|[2406.02377](http://arxiv.org/abs/2406.02377)|**[link](https://github.com/hkuds/xrec)**|
|**2024-06-05**|**Temporal Graph Rewiring with Expander Graphs**|Katarina Petrović et.al.|[2406.02362](http://arxiv.org/abs/2406.02362)|**[link](https://github.com/kpetrovicc/tgr)**|
|**2024-06-04**|**AMOSL: Adaptive Modality-wise Structure Learning in Multi-view Graph Neural Networks For Enhanced Unified Representation**|Peiyu Liang et.al.|[2406.02348](http://arxiv.org/abs/2406.02348)|null|
|**2024-06-04**|**Graph Neural Networks Do Not Always Oversmooth**|Bastian Epping et.al.|[2406.02269](http://arxiv.org/abs/2406.02269)|**[link](https://github.com/bepping/non-oversmoothing-gcns)**|
|**2024-06-04**|**DFA-GNN: Forward Learning of Graph Neural Networks by Direct Feedback Alignment**|Gongpei Zhao et.al.|[2406.02040](http://arxiv.org/abs/2406.02040)|null|
|**2024-06-04**|**Bayesian Mesh Optimization for Graph Neural Networks to Enhance Engineering Performance Prediction**|Jangseop Park et.al.|[2406.01996](http://arxiv.org/abs/2406.01996)|null|
|**2024-06-04**|**PDHG-Unrolled Learning-to-Optimize Method for Large-Scale Linear Programming**|Bingheng Li et.al.|[2406.01908](http://arxiv.org/abs/2406.01908)|**[link](https://github.com/netsysopt/pdhg-net)**|
|**2024-06-03**|**In-Context Learning of Physical Properties: Few-Shot Adaptation to Out-of-Distribution Molecular Graphs**|Grzegorz Kaszuba et.al.|[2406.01808](http://arxiv.org/abs/2406.01808)|null|
|**2024-06-03**|**AIFS - ECMWF's data-driven forecasting system**|Simon Lang et.al.|[2406.01465](http://arxiv.org/abs/2406.01465)|null|
|**2024-06-03**|**The Intelligible and Effective Graph Neural Additive Networks**|Maya Bechler-Speicher et.al.|[2406.01317](http://arxiv.org/abs/2406.01317)|**[link](https://github.com/mayabechlerspeicher/Graph-Neural-Additive-Networks---GNAN)**|
|**2024-06-03**|**Graph External Attention Enhanced Transformer**|Jianqing Liang et.al.|[2405.21061](http://arxiv.org/abs/2405.21061)|**[link](https://github.com/icm1018/geaet)**|
|**2024-05-31**|**Sheaf HyperNetworks for Personalized Federated Learning**|Bao Nguyen et.al.|[2405.20882](http://arxiv.org/abs/2405.20882)|null|
|**2024-05-31**|**SelfGNN: Self-Supervised Graph Neural Networks for Sequential Recommendation**|Yuxi Liu et.al.|[2405.20878](http://arxiv.org/abs/2405.20878)|**[link](https://github.com/hkuds/selfgnn)**|
|**2024-05-31**|**Sign is Not a Remedy: Multiset-to-Multiset Message Passing for Learning on Heterophilic Graphs**|Langzhang Liang et.al.|[2405.20652](http://arxiv.org/abs/2405.20652)|**[link](https://github.com/Jinx-byebye/m2mgnn)**|
|**2024-05-31**|**Heterophilous Distribution Propagation for Graph Neural Networks**|Zhuonan Zheng et.al.|[2405.20640](http://arxiv.org/abs/2405.20640)|null|
|**2024-05-31**|**Towards a General GNN Framework for Combinatorial Optimization**|Frederik Wenkel et.al.|[2405.20543](http://arxiv.org/abs/2405.20543)|**[link](https://github.com/wenkelf/copt)**|
|**2024-06-03**|**GraphAny: A Foundation Model for Node Classification on Any Graph**|Jianan Zhao et.al.|[2405.20445](http://arxiv.org/abs/2405.20445)|**[link](https://github.com/deepgraphlearning/graphany)**|
|**2024-05-30**|**Flexible SE(2) graph neural networks with applications to PDE surrogates**|Maria Bånkestad et.al.|[2405.20287](http://arxiv.org/abs/2405.20287)|**[link](https://github.com/mariabankestad/se2-gnn)**|
|**2024-05-30**|**Pre-train and Refine: Towards Higher Efficiency in K-Agnostic Community Detection without Quality Degradation**|Meng Qin et.al.|[2405.20277](http://arxiv.org/abs/2405.20277)|**[link](https://github.com/KuroginQin/PRoCD)**|
|**2024-05-30**|**GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning**|Costas Mavromatis et.al.|[2405.20139](http://arxiv.org/abs/2405.20139)|**[link](https://github.com/cmavro/gnn-rag)**|
|**2024-05-30**|**Chemical Space-Informed Machine Learning Models for Rapid Predictions of X-ray Photoelectron Spectra of Organic Molecules**|Susmita Tripathy et.al.|[2405.20033](http://arxiv.org/abs/2405.20033)|**[link](https://github.com/moldis-group/cebeconf)**|
|**2024-05-30**|**FlexiDrop: Theoretical Insights and Practical Advances in Random Dropout Method on GNNs**|Zhiheng Zhou et.al.|[2405.20012](http://arxiv.org/abs/2405.20012)|**[link](https://github.com/Amihua/Flexi-Drop)**|
|**2024-05-30**|**Combining physics-informed graph neural network and finite difference for solving forward and inverse spatiotemporal PDEs**|Hao Zhang et.al.|[2405.20000](http://arxiv.org/abs/2405.20000)|**[link](https://github.com/YuanAHa/PIGNN)**|
|**2024-05-30**|**Learning Latent Graph Structures and their Uncertainty**|Alessandro Manenti et.al.|[2405.19933](http://arxiv.org/abs/2405.19933)|null|
|**2024-05-30**|**Unsupervised Mutual Learning of Dialogue Discourse Parsing and Topic Segmentation**|Jiahui Xu et.al.|[2405.19799](http://arxiv.org/abs/2405.19799)|**[link](https://github.com/jeff-sue/urt)**|
|**2024-05-30**|**Few-shot fault diagnosis based on multi-scale graph convolution filtering for industry**|Mengjie Gan et.al.|[2405.19642](http://arxiv.org/abs/2405.19642)|null|
|**2024-05-29**|**Valid Conformal Prediction for Dynamic GNNs**|Ed Davis et.al.|[2405.19230](http://arxiv.org/abs/2405.19230)|**[link](https://github.com/edwarddavis1/valid_conformal_for_dynamic_gnn)**|
|**2024-05-29**|**Spatio-Spectral Graph Neural Networks**|Simon Geisler et.al.|[2405.19121](http://arxiv.org/abs/2405.19121)|**[link](https://github.com/sigeisler/s2gnn)**|
|**2024-05-29**|**Can Graph Learning Improve Task Planning?**|Xixi Wu et.al.|[2405.19119](http://arxiv.org/abs/2405.19119)|**[link](https://github.com/wxxshirley/gnn4taskplan)**|
|**2024-05-29**|**SIG: Efficient Self-Interpretable Graph Neural Network for Continuous-time Dynamic Graphs**|Lanting Fang et.al.|[2405.19062](http://arxiv.org/abs/2405.19062)|**[link](https://github.com/2024sig/sig)**|
|**2024-05-29**|**Multiscale Spatio-Temporal Enhanced Short-term Load Forecasting of Electric Vehicle Charging Stations**|Zongbao Zhang et.al.|[2405.19053](http://arxiv.org/abs/2405.19053)|null|
|**2024-05-29**|**CiliaGraph: Enabling Expression-enhanced Hyper-Dimensional Computation in Ultra-Lightweight and One-Shot Graph Classification on Edge**|Yuxi Han et.al.|[2405.19033](http://arxiv.org/abs/2405.19033)|null|
|**2024-05-29**|**LSPI: Heterogeneous Graph Neural Network Classification Aggregation Algorithm Based on Size Neighbor Path Identification**|Yufei Zhaoa et.al.|[2405.18933](http://arxiv.org/abs/2405.18933)|**[link](https://github.com/liuhua811/lspia)**|
|**2024-05-29**|**Inverse Design of Promising Alloys for Electrocatalytic CO $_2$ Reduction via Generative Graph Neural Networks Combined with Bird Swarm Algorithm**|Zhilong Song et.al.|[2405.18891](http://arxiv.org/abs/2405.18891)|null|
|**2024-05-29**|**Spatiotemporal Forecasting Meets Efficiency: Causal Graph Process Neural Networks**|Aref Einizade et.al.|[2405.18879](http://arxiv.org/abs/2405.18879)|null|
|**2024-05-29**|**Continuous Product Graph Neural Networks**|Aref Einizade et.al.|[2405.18877](http://arxiv.org/abs/2405.18877)|**[link](https://github.com/arefeinizade2/citrus)**|
|**2024-05-28**|**Don't Forget to Connect! Improving RAG with Graph-based Reranking**|Jialin Dong et.al.|[2405.18414](http://arxiv.org/abs/2405.18414)|null|
|**2024-05-28**|**A Vlogger-augmented Graph Neural Network Model for Micro-video Recommendation**|Weijiang Lai et.al.|[2405.18260](http://arxiv.org/abs/2405.18260)|**[link](https://github.com/laiweijiang/VAGNN)**|
|**2024-05-28**|**Graph Coarsening with Message-Passing Guarantees**|Antonin Joly et.al.|[2405.18127](http://arxiv.org/abs/2405.18127)|null|
|**2024-05-28**|**ForecastGrapher: Redefining Multivariate Time Series Forecasting with Graph Neural Networks**|Wanlin Cai et.al.|[2405.18036](http://arxiv.org/abs/2405.18036)|null|
|**2024-05-28**|**Revisiting the Message Passing in Heterophilous Graph Neural Networks**|Zhuonan Zheng et.al.|[2405.17768](http://arxiv.org/abs/2405.17768)|**[link](https://github.com/zfx233/CMGNN)**|
|**2024-05-28**|**Rethinking Pruning for Backdoor Mitigation: An Optimization Perspective**|Nan Li et.al.|[2405.17746](http://arxiv.org/abs/2405.17746)|null|
|**2024-05-27**|**Spectral Greedy Coresets for Graph Neural Networks**|Mucong Ding et.al.|[2405.17404](http://arxiv.org/abs/2405.17404)|null|
|**2024-05-27**|**Probabilistic Graph Rewiring via Virtual Nodes**|Chendi Qian et.al.|[2405.17311](http://arxiv.org/abs/2405.17311)|**[link](https://github.com/chendiqian/IPR-MPNN)**|
|**2024-05-27**|**Survey of Graph Neural Network for Internet of Things and NextG Networks**|Sabarish Krishna Moorthy et.al.|[2405.17309](http://arxiv.org/abs/2405.17309)|null|
|**2024-05-27**|**R-ODE: Ricci Curvature Tells When You Will be Informed**|Li Sun et.al.|[2405.17282](http://arxiv.org/abs/2405.17282)|null|
|**2024-05-27**|**Your decision path does matter in pre-training industrial recommenders with multi-source behaviors**|Chunjing Gan et.al.|[2405.17132](http://arxiv.org/abs/2405.17132)|null|
|**2024-05-27**|**Graph Neural Networks on Quantum Computers**|Yidong Liao et.al.|[2405.17060](http://arxiv.org/abs/2405.17060)|null|
|**2024-05-27**|**FUGNN: Harmonizing Fairness and Utility in Graph Neural Networks**|Renqiang Luo et.al.|[2405.17034](http://arxiv.org/abs/2405.17034)|null|
|**2024-05-27**|**Graph Condensation for Open-World Graph Learning**|Xinyi Gao et.al.|[2405.17003](http://arxiv.org/abs/2405.17003)|null|
|**2024-05-26**|**Graph neural networks with configuration cross-attention for tensor compilers**|Dmitrii Khizbullin et.al.|[2405.16623](http://arxiv.org/abs/2405.16623)|**[link](https://github.com/thanhhau097/google_fast_or_slow)**|
|**2024-05-26**|**Link Prediction on Textual Edge Graphs**|Chen Ling et.al.|[2405.16606](http://arxiv.org/abs/2405.16606)|null|
|**2024-05-24**|**Rethinking Independent Cross-Entropy Loss For Graph-Structured Data**|Rui Miao et.al.|[2405.15564](http://arxiv.org/abs/2405.15564)|**[link](https://github.com/mr9812/joint-cluster-supervised-learning)**|
|**2024-05-24**|**Learning from Linear Algebra: A Graph Neural Network Approach to Preconditioner Design for Conjugate Gradient Solvers**|Vladislav Trifonov et.al.|[2405.15557](http://arxiv.org/abs/2405.15557)|null|
|**2024-05-24**|**SATSense: Multi-Satellite Collaborative Framework for Spectrum Sensing**|Haoxuan Yuan et.al.|[2405.15542](http://arxiv.org/abs/2405.15542)|null|
|**2024-05-24**|**E(n) Equivariant Topological Neural Networks**|Claudio Battiloro et.al.|[2405.15429](http://arxiv.org/abs/2405.15429)|**[link](https://github.com/NSAPH-Projects/topological-equivariant-networks)**|
|**2024-05-24**|**DFGNN: Dual-frequency Graph Neural Network for Sign-aware Feedback**|Yiqing Wu et.al.|[2405.15280](http://arxiv.org/abs/2405.15280)|null|
|**2024-05-24**|**Cardinality Estimation on Hyper-relational Knowledge Graphs**|Fei Teng et.al.|[2405.15231](http://arxiv.org/abs/2405.15231)|null|
|**2024-05-24**|**AGS-GNN: Attribute-guided Sampling for Graph Neural Networks**|Siddhartha Shankar Das et.al.|[2405.15218](http://arxiv.org/abs/2405.15218)|**[link](https://github.com/siddhartha047/AGS-GNN)**|
|**2024-05-24**|**TrojanForge: Adversarial Hardware Trojan Examples with Reinforcement Learning**|Amin Sarihi et.al.|[2405.15184](http://arxiv.org/abs/2405.15184)|null|
|**2024-05-23**|**Message-Passing Monte Carlo: Generating low-discrepancy point sets via Graph Neural Networks**|T. Konstantin Rusch et.al.|[2405.15059](http://arxiv.org/abs/2405.15059)|**[link](https://github.com/tk-rusch/mpmc)**|
|**2024-05-23**|**Analysis of Atom-level pretraining with QM data for Graph Neural Networks Molecular property models**|Jose Arjona-Medina et.al.|[2405.14837](http://arxiv.org/abs/2405.14837)|null|
|**2024-05-23**|**Development of a Gaussian Approximation Potential to Study Structure and Thermodynamics of Nickel Nanoclusters**|Suvo Banik et.al.|[2405.14683](http://arxiv.org/abs/2405.14683)|null|
|**2024-05-23**|**Logical Characterizations of Recurrent Graph Neural Networks with Reals and Floats**|Veeti Ahvonen et.al.|[2405.14606](http://arxiv.org/abs/2405.14606)|null|
|**2024-05-23**|**Gradient Transformation: Towards Efficient and Model-Agnostic Unlearning for Dynamic Graph Neural Networks**|He Zhang et.al.|[2405.14407](http://arxiv.org/abs/2405.14407)|null|
|**2024-05-23**|**Explaining Graph Neural Networks via Structure-aware Interaction Index**|Ngoc Bui et.al.|[2405.14352](http://arxiv.org/abs/2405.14352)|**[link](https://github.com/ngocbh/mage)**|
|**2024-05-23**|**AdaGMLP: AdaBoosting GNN-to-MLP Knowledge Distillation**|Weigang Lu et.al.|[2405.14307](http://arxiv.org/abs/2405.14307)|**[link](https://github.com/weiganglu/adagmlp-kdd24)**|
|**2024-05-23**|**Similarity-Navigated Conformal Prediction for Graph Neural Networks**|Jianqing Song et.al.|[2405.14303](http://arxiv.org/abs/2405.14303)|**[link](https://github.com/janqsong/snaps)**|
|**2024-05-23**|**Graphcode: Learning from multiparameter persistent homology using graph neural networks**|Michael Kerber et.al.|[2405.14302](http://arxiv.org/abs/2405.14302)|null|
|**2024-05-23**|**Graph Sparsification via Mixture of Graphs**|Guibin Zhang et.al.|[2405.14260](http://arxiv.org/abs/2405.14260)|**[link](https://github.com/yanweiyue/mog)**|
|**2024-05-23**|**Automated Loss function Search for Class-imbalanced Node Classification**|Xinyu Guo et.al.|[2405.14133](http://arxiv.org/abs/2405.14133)|null|
|**2024-05-21**|**Equivariant Spatio-Temporal Attentive Graph Networks to Simulate Physical Dynamics**|Liming Wu et.al.|[2405.12868](http://arxiv.org/abs/2405.12868)|**[link](https://github.com/ManlioWu/ESTAG)**|
|**2024-05-21**|**Utilizing Description Logics for Global Explanations of Heterogeneous Graph Neural Networks**|Dominik Köhler et.al.|[2405.12654](http://arxiv.org/abs/2405.12654)|**[link](https://github.com/ds-jrg/xgnn-dl)**|
|**2024-05-21**|**Unleash Graph Neural Networks from Heavy Tuning**|Lequan Lin et.al.|[2405.12521](http://arxiv.org/abs/2405.12521)|null|
|**2024-05-21**|**MAGE: Model-Level Graph Neural Networks Explanations via Motif-based Graph Generation**|Zhaoning Yu et.al.|[2405.12519](http://arxiv.org/abs/2405.12519)|null|
|**2024-05-21**|**How Universal Polynomial Bases Enhance Spectral Graph Neural Networks: Heterophily, Over-smoothing, and Over-squashing**|Keke Huang et.al.|[2405.12474](http://arxiv.org/abs/2405.12474)|**[link](https://github.com/kkhuang81/UniFilter)**|
|**2024-05-21**|**Prompt-Enhanced Spatio-Temporal Graph Transfer Learning**|Junfeng Hu et.al.|[2405.12452](http://arxiv.org/abs/2405.12452)|**[link](https://github.com/hjf1997/stgp)**|
|**2024-05-20**|**Efficient Model-Stealing Attacks Against Inductive Graph Neural Networks**|Marcin Podhajski et.al.|[2405.12295](http://arxiv.org/abs/2405.12295)|**[link](https://github.com/m-podhajski/efficientgnnstealing)**|
|**2024-05-20**|**Conditional Shift-Robust Conformal Prediction for Graph Neural Network**|S. Akansha et.al.|[2405.11968](http://arxiv.org/abs/2405.11968)|null|
|**2024-05-20**|**CaseGNN++: Graph Contrastive Learning for Legal Case Retrieval with Graph Augmentation**|Yanran Tang et.al.|[2405.11791](http://arxiv.org/abs/2405.11791)|**[link](https://github.com/yanran-tang/casegnn)**|
|**2024-05-19**|**Knowledge Graph Pruning for Recommendation**|Fake Lin et.al.|[2405.11531](http://arxiv.org/abs/2405.11531)|null|
|**2024-05-19**|**CTGNN: Crystal Transformer Graph Neural Network for Crystal Material Property Prediction**|Zijian Du et.al.|[2405.11502](http://arxiv.org/abs/2405.11502)|null|
|**2024-05-18**|**Hierarchical Reinforcement Learning Empowered Task Offloading in V2I Networks**|Xinyu You et.al.|[2405.11352](http://arxiv.org/abs/2405.11352)|null|
|**2024-05-18**|**Detecting Complex Multi-step Attacks with Explainable Graph Neural Network**|Wei Liu et.al.|[2405.11335](http://arxiv.org/abs/2405.11335)|null|
|**2024-05-18**|**GinAR: An End-To-End Multivariate Time Series Forecasting Model Suitable for Variable Missing**|Chengqing Yu et.al.|[2405.11333](http://arxiv.org/abs/2405.11333)|**[link](https://github.com/chengqingyu/ginar)**|
|**2024-05-18**|**SeBot: Structural Entropy Guided Multi-View Contrastive Learning for Social Bot Detection**|Yingguang Yang et.al.|[2405.11225](http://arxiv.org/abs/2405.11225)|**[link](https://github.com/846468230/sebot)**|
|**2024-05-17**|**GraSS: Combining Graph Neural Networks with Expert Knowledge for SAT Solver Selection**|Zhanguang Zhang et.al.|[2405.11024](http://arxiv.org/abs/2405.11024)|null|
|**2024-05-17**|**Rethinking Graph Backdoor Attacks: A Distribution-Preserving Perspective**|Zhiwei Zhang et.al.|[2405.10757](http://arxiv.org/abs/2405.10757)|**[link](https://github.com/zzwjames/dpgba)**|
|**2024-05-17**|**Hi-GMAE: Hierarchical Graph Masked Autoencoders**|Chuang Liu et.al.|[2405.10642](http://arxiv.org/abs/2405.10642)|**[link](https://github.com/liuchuang0059/hi-gmae)**|
|**2024-05-17**|**Harnessing Collective Structure Knowledge in Data Augmentation for Graph Neural Networks**|Rongrong Ma et.al.|[2405.10633](http://arxiv.org/abs/2405.10633)|**[link](https://github.com/rongrongma/cos-gnn)**|
|**2024-05-17**|**CACL: Community-Aware Heterogeneous Graph Contrastive Learning for Social Media Bot Detection**|Sirry Chen et.al.|[2405.10558](http://arxiv.org/abs/2405.10558)|**[link](https://github.com/SirryChen/CACL)**|
|**2024-05-17**|**Multi-Evidence based Fact Verification via A Confidential Graph Neural Network**|Yuqing Lan et.al.|[2405.10481](http://arxiv.org/abs/2405.10481)|**[link](https://github.com/neuir/co-gat)**|
|**2024-05-16**|**Physics-Informed Heterogeneous Graph Neural Networks for DC Blocker Placement**|Hongwei Jin et.al.|[2405.10389](http://arxiv.org/abs/2405.10389)|**[link](https://github.com/cshjin/swmp_ml)**|
|**2024-05-16**|**ENADPool: The Edge-Node Attention-based Differentiable Pooling for Graph Neural Networks**|Zhehan Zhao et.al.|[2405.10218](http://arxiv.org/abs/2405.10218)|null|
|**2024-05-16**|**Hierarchical Attention Graph for Scientific Document Summarization in Global and Local Level**|Chenlong Zhao et.al.|[2405.10202](http://arxiv.org/abs/2405.10202)|**[link](https://github.com/molichenxi/haesum)**|
|**2024-05-16**|**Integrating Uncertainty-Aware Human Motion Prediction into Graph-Based Manipulator Motion Planning**|Wansong Liu et.al.|[2405.09779](http://arxiv.org/abs/2405.09779)|null|
|**2024-05-15**|**ContourCraft: Learning to Resolve Intersections in Neural Multi-Garment Simulations**|Artur Grigorev et.al.|[2405.09522](http://arxiv.org/abs/2405.09522)|null|
|**2024-05-15**|**Desk-AId: Humanitarian Aid Desk Assessment with Geospatial AI for Predicting Landmine Areas**|Flavio Cirillo et.al.|[2405.09444](http://arxiv.org/abs/2405.09444)|null|
|**2024-05-15**|**Learning Coarse-Grained Dynamics on Graph**|Yin Yu et.al.|[2405.09324](http://arxiv.org/abs/2405.09324)|null|
|**2024-05-15**|**Graph Neural Network based Handwritten Trajectories Recognition**|Anuj Sharma et.al.|[2405.09247](http://arxiv.org/abs/2405.09247)|null|
|**2024-05-15**|**SMUG-Explain: A Framework for Symbolic Music Graph Explanations**|Emmanouil Karystinaios et.al.|[2405.09241](http://arxiv.org/abs/2405.09241)|**[link](https://github.com/manoskary/smug-explain)**|
|**2024-05-15**|**Unraveling impacts of polycrystalline microstructures on ionic conductivity of ceramic electrolytes by computational homogenization and machine learning**|Xiang-Long Peng et.al.|[2405.09227](http://arxiv.org/abs/2405.09227)|null|
|**2024-05-15**|**Enhancing Function Name Prediction using Votes-Based Name Tokenization and Multi-Task Learning**|Xiaoling Zhang et.al.|[2405.09112](http://arxiv.org/abs/2405.09112)|**[link](https://github.com/Xiaolinger-Z/Epitome)**|
|**2024-05-15**|**Deep Learning in Earthquake Engineering: A Comprehensive Review**|Yazhou Xie et.al.|[2405.09021](http://arxiv.org/abs/2405.09021)|null|
|**2024-05-14**|**Chemical-motif characterization of short-range order with E(3)-equivariant graph neural networks**|Killian Sheriff et.al.|[2405.08628](http://arxiv.org/abs/2405.08628)|null|
|**2024-05-14**|**Improving the Real-Data Driven Network Evaluation Model for Digital Twin Networks**|Hyeju Shin et.al.|[2405.08473](http://arxiv.org/abs/2405.08473)|null|
|**2024-05-13**|**Graph Neural Networks for Parameterized Quantum Circuits Expressibility Estimation**|Shamminuj Aktar et.al.|[2405.08100](http://arxiv.org/abs/2405.08100)|null|
|**2024-05-13**|**KG-Planner: Knowledge-Informed Graph Neural Planning for Collaborative Manipulators**|Wansong Liu et.al.|[2405.07962](http://arxiv.org/abs/2405.07962)|null|
|**2024-05-13**|**Discovery of highly anisotropic dielectric crystals with equivariant graph neural networks**|Yuchen Lou et.al.|[2405.07915](http://arxiv.org/abs/2405.07915)|**[link](https://github.com/virtualatoms/AnisoNet)**|
|**2024-05-13**|**All Nodes are created Not Equal: Node-Specific Layer Aggregation and Filtration for GNN**|Shilong Wang et.al.|[2405.07892](http://arxiv.org/abs/2405.07892)|null|
|**2024-05-13**|**Hamiltonian-based Quantum Reinforcement Learning for Neural Combinatorial Optimization**|Georg Kruse et.al.|[2405.07790](http://arxiv.org/abs/2405.07790)|null|
|**2024-05-12**|**Graph neural networks for power grid operational risk assessment under evolving grid topology**|Yadong Zhang et.al.|[2405.07343](http://arxiv.org/abs/2405.07343)|null|
|**2024-05-12**|**Context Neural Networks: A Scalable Multivariate Model for Time Series Forecasting**|Abishek Sriramulu et.al.|[2405.07117](http://arxiv.org/abs/2405.07117)|null|
|**2024-05-11**|**Fair Graph Representation Learning via Sensitive Attribute Disentanglement**|Yuchang Zhu et.al.|[2405.07011](http://arxiv.org/abs/2405.07011)|**[link](https://github.com/zzoomd/fairsad)**|
|**2024-05-11**|**Input Snapshots Fusion for Scalable Discrete Dynamic Graph Nerual Networks**|QingGuo Qi et.al.|[2405.06975](http://arxiv.org/abs/2405.06975)|null|
|**2024-05-11**|**Design Requirements for Human-Centered Graph Neural Network Explanations**|Pantea Habibi et.al.|[2405.06917](http://arxiv.org/abs/2405.06917)|null|
|**2024-05-10**|**GreedyViG: Dynamic Axial Graph Construction for Efficient Vision GNNs**|Mustafa Munir et.al.|[2405.06849](http://arxiv.org/abs/2405.06849)|**[link](https://github.com/SLDGroup/GreedyViG)**|
|**2024-05-10**|**Scalable Property Valuation Models via Graph-based Deep Learning**|Enrique Riveros et.al.|[2405.06553](http://arxiv.org/abs/2405.06553)|null|
|**2024-05-10**|**Heterogeneous Graph Neural Networks with Loss-decrease-aware Curriculum Learning**|Yili Wang et.al.|[2405.06522](http://arxiv.org/abs/2405.06522)|**[link](https://github.com/wangyili00/ldhgnn)**|
|**2024-05-10**|**PAC-Bayesian Generalization Bounds for Knowledge Graph Representation Learning**|Jaejun Lee et.al.|[2405.06418](http://arxiv.org/abs/2405.06418)|**[link](https://github.com/bdi-lab/reed)**|
|**2024-05-10**|**Disttack: Graph Adversarial Attacks Toward Distributed GNN Training**|Yuxiang Zhang et.al.|[2405.06247](http://arxiv.org/abs/2405.06247)|**[link](https://github.com/zhangyxrepo/disttack)**|
|**2024-05-09**|**UnSegGNet: Unsupervised Image Segmentation using Graph Neural Networks**|Kovvuri Sai Gopal Reddy et.al.|[2405.06057](http://arxiv.org/abs/2405.06057)|**[link](https://github.com/ksgr5566/unseggnet)**|
|**2024-05-09**|**Deploying Graph Neural Networks in Wireless Networks: A Link Stability Viewpoint**|Jun Li et.al.|[2405.05802](http://arxiv.org/abs/2405.05802)|null|
|**2024-05-09**|**Link Stealing Attacks Against Inductive Graph Neural Networks**|Yixin Wu et.al.|[2405.05784](http://arxiv.org/abs/2405.05784)|**[link](https://github.com/yxoh/link_steal_pets2024)**|
|**2024-05-09**|**G-SAP: Graph-based Structure-Aware Prompt Learning over Heterogeneous Knowledge for Commonsense Reasoning**|Ruiting Dai et.al.|[2405.05616](http://arxiv.org/abs/2405.05616)|null|
|**2024-05-08**|**DiskGNN: Bridging I/O Efficiency and Model Accuracy for Out-of-Core GNN Training**|Renjie Liu et.al.|[2405.05231](http://arxiv.org/abs/2405.05231)|null|
|**2024-05-08**|**Hybrid Quantum Graph Neural Network for Molecular Property Prediction**|Michael Vitz et.al.|[2405.05205](http://arxiv.org/abs/2405.05205)|null|
|**2024-05-08**|**Dual-domain Collaborative Denoising for Social Recommendation**|Wenjie Chen et.al.|[2405.04942](http://arxiv.org/abs/2405.04942)|null|
|**2024-05-08**|**Empowering Wireless Networks with Artificial Intelligence Generated Graph**|Jiacheng Wang et.al.|[2405.04907](http://arxiv.org/abs/2405.04907)|null|
|**2024-05-08**|**Imbalanced Graph Classification with Multi-scale Oversampling Graph Neural Networks**|Rongrong Ma et.al.|[2405.04903](http://arxiv.org/abs/2405.04903)|**[link](https://github.com/rongrongma/mosgnn)**|
|**2024-05-08**|**A Novel Technique for Query Plan Representation Based on Graph Neural Networks**|Baoming Chang et.al.|[2405.04814](http://arxiv.org/abs/2405.04814)|null|
|**2024-05-08**|**Hypergraph-enhanced Dual Semi-supervised Graph Classification**|Wei Ju et.al.|[2405.04773](http://arxiv.org/abs/2405.04773)|null|
|**2024-05-08**|**Conditional Local Feature Encoding for Graph Neural Networks**|Yongze Wang et.al.|[2405.04755](http://arxiv.org/abs/2405.04755)|null|
|**2024-05-07**|**Exploration of Novel Neuromorphic Methodologies for Materials Applications**|Derek Gobin et.al.|[2405.04478](http://arxiv.org/abs/2405.04478)|null|
|**2024-05-07**|**A fully differentiable GNN-based PDE Solver: With Applications to Poisson and Navier-Stokes Equations**|Tianyu Li et.al.|[2405.04466](http://arxiv.org/abs/2405.04466)|**[link](https://github.com/Litianyu141/Gen-FVGN-steady)**|
|**2024-05-07**|**Parallelized Multi-Agent Bayesian Optimization in Lava**|Shay Snyder et.al.|[2405.04387](http://arxiv.org/abs/2405.04387)|**[link](https://github.com/Parsa-Research-Laboratory/lmao)**|
|**2024-05-07**|**Temporal and Heterogeneous Graph Neural Network for Remaining Useful Life Prediction**|Zhihao Wen et.al.|[2405.04336](http://arxiv.org/abs/2405.04336)|null|
|**2024-05-07**|**Acceleration Algorithms in GNNs: A Survey**|Lu Ma et.al.|[2405.04114](http://arxiv.org/abs/2405.04114)|**[link](https://github.com/PKU-DAIR/SGL)**|
|**2024-05-07**|**Adaptive Least Mean pth Power Graph Neural Networks**|Changran Peng et.al.|[2405.04111](http://arxiv.org/abs/2405.04111)|null|
|**2024-05-07**|**Binarized Simplicial Convolutional Neural Networks**|Yi Yan et.al.|[2405.04098](http://arxiv.org/abs/2405.04098)|null|
|**2024-05-07**|**Structured Click Control in Transformer-based Interactive Segmentation**|Long Xu et.al.|[2405.04009](http://arxiv.org/abs/2405.04009)|**[link](https://github.com/hahamyt/scc)**|
|**2024-05-07**|**ESIHGNN: Event-State Interactions Infused Heterogeneous Graph Neural Network for Conversational Emotion Recognition**|Xupeng Zha et.al.|[2405.03960](http://arxiv.org/abs/2405.03960)|null|
|**2024-05-07**|**Relating-Up: Advancing Graph Neural Networks through Inter-Graph Relationships**|Qi Zou et.al.|[2405.03950](http://arxiv.org/abs/2405.03950)|null|
|**2024-05-06**|**AtomGPT: Atomistic Generative Pre-trained Transformer for Forward and Inverse Materials Design**|Kamal Choudhary et.al.|[2405.03680](http://arxiv.org/abs/2405.03680)|**[link](https://github.com/usnistgov/atomgpt)**|
|**2024-05-06**|**Reinforcement Nash Equilibrium Solver**|Xinrun Wang et.al.|[2405.03518](http://arxiv.org/abs/2405.03518)|null|
|**2024-05-06**|**AnchorGT: Efficient and Flexible Attention Architecture for Scalable Graph Transformers**|Wenhao Zhu et.al.|[2405.03481](http://arxiv.org/abs/2405.03481)|null|
|**2024-05-06**|**A method for quantifying the generalization capabilities of generative models for solving Ising models**|Qunlong Ma et.al.|[2405.03435](http://arxiv.org/abs/2405.03435)|null|
|**2024-05-06**|**E2GNN: Efficient Graph Neural Network Ensembles for Semi-Supervised Classification**|Xin Zhang et.al.|[2405.03401](http://arxiv.org/abs/2405.03401)|**[link](https://github.com/qiaoyu-tan/E2GNN)**|
|**2024-05-06**|**Denoising of Geodetic Time Series Using Spatiotemporal Graph Neural Networks: Application to Slow Slip Event Extraction**|Giuseppe Costantino et.al.|[2405.03320](http://arxiv.org/abs/2405.03320)|null|
|**2024-05-06**|**Coefficient Decomposition for Spectral Graph Convolution**|Feng Huang et.al.|[2405.03296](http://arxiv.org/abs/2405.03296)|**[link](https://github.com/fhuang233/CoDeSGC)**|
|**2024-05-06**|**Active Sensing for Multiuser Beam Tracking with Reconfigurable Intelligent Surface**|Han Han et.al.|[2405.03129](http://arxiv.org/abs/2405.03129)|null|
|**2024-05-05**|**Convolutional Learning on Directed Acyclic Graphs**|Samuel Rey et.al.|[2405.03056](http://arxiv.org/abs/2405.03056)|**[link](https://github.com/reysam93/dag_conv_nn)**|
|**2024-05-05**|**E-TSL: A Continuous Educational Turkish Sign Language Dataset with Baseline Methods**|Şükrü Öztürk et.al.|[2405.02984](http://arxiv.org/abs/2405.02984)|null|
|**2024-05-03**|**CatTSunami: Accelerating Transition State Energy Calculations with Pre-trained Graph Neural Networks**|Brook Wander et.al.|[2405.02078](http://arxiv.org/abs/2405.02078)|null|
|**2024-05-03**|**Graph Neural Network based Active and Passive Beamforming for Distributed STAR-RIS-Assisted Multi-User MISO Systems**|Ha An Le et.al.|[2405.01979](http://arxiv.org/abs/2405.01979)|null|
|**2024-05-03**|**Conservative semi-lagrangian finite difference scheme for transport simulations using graph neural networks**|Yongsheng Chen et.al.|[2405.01938](http://arxiv.org/abs/2405.01938)|**[link](https://github.com/chenyongssss/GNN-SLFD)**|
|**2024-05-03**|**SlotGAT: Slot-based Message Passing for Heterogeneous Graph Neural Network**|Ziang Zhou et.al.|[2405.01927](http://arxiv.org/abs/2405.01927)|**[link](https://github.com/scottjiao/slotgat_icml23)**|
|**2024-05-02**|**EiG-Search: Generating Edge-Induced Subgraphs for GNN Explanation in Linear Time**|Shengyao Lu et.al.|[2405.01762](http://arxiv.org/abs/2405.01762)|**[link](https://github.com/sluxsr/EiG-Search)**|
|**2024-05-02**|**ATNPA: A Unified View of Oversmoothing Alleviation in Graph Neural Networks**|Yufei Jin et.al.|[2405.01663](http://arxiv.org/abs/2405.01663)|null|
|**2024-05-02**|**GTX: A Transactional Graph Data System For HTAP Workloads**|Libin Zhou et.al.|[2405.01448](http://arxiv.org/abs/2405.01448)|null|
|**2024-05-02**|**The Importance of Model Inspection for Better Understanding Performance Characteristics of Graph Neural Networks**|Nairouz Shehata et.al.|[2405.01270](http://arxiv.org/abs/2405.01270)|**[link](https://github.com/biomedia-mira/medmesh)**|
|**2024-05-02**|**IntraMix: Intra-Class Mixup Generation for Accurate Labels and Neighbors**|Shenghe Zheng et.al.|[2405.00957](http://arxiv.org/abs/2405.00957)|**[link](https://github.com/zhengsh123/intramix)**|
|**2024-05-01**|**Solving Maxwell's equations with Non-Trainable Graph Neural Network Message Passing**|Stefanos Bakirtzis et.al.|[2405.00814](http://arxiv.org/abs/2405.00814)|null|
|**2024-05-01**|**Discovering robust biomarkers of neurological disorders from functional MRI using graph neural networks: A Review**|Yi Hao Chan et.al.|[2405.00577](http://arxiv.org/abs/2405.00577)|null|
|**2024-05-01**|**WEST GCN-LSTM: Weighted Stacked Spatio-Temporal Graph Neural Networks for Regional Traffic Forecasting**|Theodoros Theodoropoulos et.al.|[2405.00570](http://arxiv.org/abs/2405.00570)|null|
|**2024-05-01**|**A Comprehensive Survey of Dynamic Graph Neural Networks: Models, Frameworks, Benchmarks, Experiments and Challenges**|ZhengZhao Feng et.al.|[2405.00476](http://arxiv.org/abs/2405.00476)|null|
|**2024-05-01**|**Message-Passing Interatomic Potentials Learn Non-Local Electrostatic Interactions**|Sungwoo Kang et.al.|[2405.00290](http://arxiv.org/abs/2405.00290)|null|
|**2024-04-30**|**A Logic for Reasoning About Aggregate-Combine Graph Neural Networks**|Pierre Nunn et.al.|[2405.00205](http://arxiv.org/abs/2405.00205)|null|
|**2024-04-30**|**Graph Neural Network Approach to Semantic Type Detection in Tables**|Ehsan Hoseinzade et.al.|[2405.00123](http://arxiv.org/abs/2405.00123)|**[link](https://github.com/hoseinzadeehsan/gait)**|
|**2024-04-30**|**Generating Robust Counterfactual Witnesses for Graph Neural Networks**|Dazhuo Qiu et.al.|[2404.19519](http://arxiv.org/abs/2404.19519)|null|
|**2024-04-30**|**EvGNN: An Event-driven Graph Neural Network Accelerator for Edge Vision**|Yufeng Yang et.al.|[2404.19489](http://arxiv.org/abs/2404.19489)|null|
|**2024-04-30**|**Deep Learning Forecasts Caldera Collapse Events at Kīlauea Volcano**|Ian W. McBrearty et.al.|[2404.19351](http://arxiv.org/abs/2404.19351)|null|
|**2024-04-30**|**Multi-Scale Heterogeneity-Aware Hypergraph Representation for Histopathology Whole Slide Images**|Minghao Han et.al.|[2404.19334](http://arxiv.org/abs/2404.19334)|**[link](https://github.com/hanminghao/h2gt)**|
|**2024-04-30**|**Training-free Graph Neural Networks and the Power of Labels as Features**|Ryoma Sato et.al.|[2404.19288](http://arxiv.org/abs/2404.19288)|**[link](https://github.com/joisino/laf)**|
|**2024-05-01**|**The Shape of Money Laundering: Subgraph Representation Learning on the Blockchain with the Elliptic2 Dataset**|Claudio Bellei et.al.|[2404.19109](http://arxiv.org/abs/2404.19109)|**[link](https://github.com/mitibmxgraph/elliptic2)**|
|**2024-04-28**|**Multi-stage Attack Detection and Prediction Using Graph Neural Networks: An IoT Feasibility Study**|Hamdi Friji et.al.|[2404.18328](http://arxiv.org/abs/2404.18328)|null|
|**2024-04-28**|**Parameter-Efficient Tuning Large Language Models for Graph Representation Learning**|Qi Zhu et.al.|[2404.18271](http://arxiv.org/abs/2404.18271)|null|
|**2024-04-28**|**A survey of dynamic graph neural networks**|Yanping Zheng et.al.|[2404.18211](http://arxiv.org/abs/2404.18211)|null|
|**2024-04-30**|**Decidability of Graph Neural Networks via Logical Characterizations**|Michael Benedikt et.al.|[2404.18151](http://arxiv.org/abs/2404.18151)|null|
|**2024-04-28**|**Fashion Recommendation: Outfit Compatibility using GNN**|Samaksh Gulati et.al.|[2404.18040](http://arxiv.org/abs/2404.18040)|**[link](https://github.com/outfit-net/outfit-commpatibility)**|
|**2024-04-27**|**Bounding the Expected Robustness of Graph Neural Networks Subject to Node Feature Attacks**|Yassine Abbahaddou et.al.|[2404.17947](http://arxiv.org/abs/2404.17947)|**[link](https://github.com/sennadir/gcorn)**|
|**2024-04-27**|**Noisy Node Classification by Bi-level Optimization based Multi-teacher Distillation**|Yujing Liu et.al.|[2404.17875](http://arxiv.org/abs/2404.17875)|null|
|**2024-04-27**|**Revisiting Multimodal Emotion Recognition in Conversation from the Perspective of Graph Spectrum**|Tao Meng et.al.|[2404.17862](http://arxiv.org/abs/2404.17862)|null|
|**2024-04-26**|**Bridging the Fairness Divide: Achieving Group and Individual Fairness in Graph Neural Networks**|Duna Zhan et.al.|[2404.17511](http://arxiv.org/abs/2404.17511)|null|
|**2024-04-26**|**Similarity Equivariant Graph Neural Networks for Homogenization of Metamaterials**|Fleur Hendriks et.al.|[2404.17365](http://arxiv.org/abs/2404.17365)|**[link](https://github.com/fhendriks11/simegnn)**|
|**2024-04-26**|**FairGT: A Fairness-aware Graph Transformer**|Renqiang Luo et.al.|[2404.17169](http://arxiv.org/abs/2404.17169)|**[link](https://github.com/yushuowiki/fairgt)**|
|**2024-04-26**|**DPGAN: A Dual-Path Generative Adversarial Network for Missing Data Imputation in Graphs**|Xindi Zheng et.al.|[2404.17164](http://arxiv.org/abs/2404.17164)|null|
|**2024-04-26**|**Sub-6GHz Assisted mmWave Hybrid Beamforming with Heterogeneous Graph Neural Network**|Zhaohui Huang et.al.|[2404.17138](http://arxiv.org/abs/2404.17138)|null|
|**2024-04-26**|**Unleashing the Potential of Fractional Calculus in Graph Neural Networks with FROND**|Qiyu Kang et.al.|[2404.17099](http://arxiv.org/abs/2404.17099)|**[link](https://github.com/zknus/torchfde)**|
|**2024-04-25**|**Transductive Spiking Graph Neural Networks for Loihi**|Shay Snyder et.al.|[2404.17048](http://arxiv.org/abs/2404.17048)|null|
|**2024-04-25**|**HEroBM: a deep equivariant graph neural network for universal backmapping from coarse-grained to all-atom representations**|Daniele Angioletti et.al.|[2404.16911](http://arxiv.org/abs/2404.16911)|**[link](https://github.com/limresgrp/herobm)**|
|**2024-04-25**|**Global Concept Explanations for Graphs by Contrastive Learning**|Jonas Teufel et.al.|[2404.16532](http://arxiv.org/abs/2404.16532)|**[link](https://github.com/aimat-lab/megan_global_explanations)**|
|**2024-04-25**|**Guarding Graph Neural Networks for Unsupervised Graph Anomaly Detection**|Yuanchen Bei et.al.|[2404.16366](http://arxiv.org/abs/2404.16366)|null|
|**2024-04-24**|**Power Failure Cascade Prediction using Graph Neural Networks**|Sathwik Chadaga et.al.|[2404.16134](http://arxiv.org/abs/2404.16134)|**[link](https://github.com/sathwikchadaga/failure-cascade)**|
|**2024-04-26**|**A General Black-box Adversarial Attack on Graph-based Fake News Detectors**|Peican Zhu et.al.|[2404.15744](http://arxiv.org/abs/2404.15744)|null|
|**2024-04-24**|**Gradformer: Graph Transformer with Exponential Decay**|Chuang Liu et.al.|[2404.15729](http://arxiv.org/abs/2404.15729)|**[link](https://github.com/liuchuang0059/gradformer)**|
|**2024-04-24**|**Graph Neural Networks for Vulnerability Detection: A Counterfactual Explanation**|Zhaoyang Chu et.al.|[2404.15687](http://arxiv.org/abs/2404.15687)|**[link](https://github.com/Zhaoyang-Chu/counterfactual-vulnerability-detection)**|
|**2024-04-24**|**FR-NAS: Forward-and-Reverse Graph Predictor for Efficient Neural Architecture Search**|Haoming Zhang et.al.|[2404.15622](http://arxiv.org/abs/2404.15622)|**[link](https://github.com/emi-group/fr-nas)**|
|**2024-04-24**|**DyGCL: Dynamic Graph Contrastive Learning For Event Prediction**|Muhammed Ifte Khairul Islam et.al.|[2404.15612](http://arxiv.org/abs/2404.15612)|null|
|**2024-04-25**|**NeuraChip: Accelerating GNN Computations with a Hash-based Decoupled Spatial Accelerator**|Kaustubh Shivdikar et.al.|[2404.15510](http://arxiv.org/abs/2404.15510)|**[link](https://github.com/neurachip/neurachip)**|
|**2024-04-23**|**NMBEnet: Efficient Near-field mmWave Beam Training for Multiuser OFDM Systems Using Sub-6 GHz Pilots**|Wang Liu et.al.|[2404.15469](http://arxiv.org/abs/2404.15469)|null|
|**2024-04-23**|**PHLP: Sole Persistent Homology for Link Prediction -- Interpretable Feature Extraction**|Junwon You et.al.|[2404.15225](http://arxiv.org/abs/2404.15225)|null|
|**2024-04-23**|**Formal Verification of Graph Convolutional Networks with Uncertain Node Features and Uncertain Graph Structure**|Tobias Ladner et.al.|[2404.15065](http://arxiv.org/abs/2404.15065)|null|
|**2024-04-23**|**Digital Twin of Industrial Networked Control System based on Value of Information**|Van-Phuc Bui et.al.|[2404.14960](http://arxiv.org/abs/2404.14960)|null|
|**2024-04-23**|**Delayed Bottlenecking: Alleviating Forgetting in Pre-trained Graph Neural Networks**|Zhe Zhao et.al.|[2404.14941](http://arxiv.org/abs/2404.14941)|null|
|**2024-04-23**|**Graph Machine Learning in the Era of Large Language Models (LLMs)**|Wenqi Fan et.al.|[2404.14928](http://arxiv.org/abs/2404.14928)|null|
|**2024-04-23**|**CNN2GNN: How to Bridge CNN with GNN**|Ziheng Jiao et.al.|[2404.14822](http://arxiv.org/abs/2404.14822)|null|
|**2024-04-23**|**Source Code Vulnerability Detection: Combining Code Language Models and Code Property Graphs**|Ruitong Liu et.al.|[2404.14719](http://arxiv.org/abs/2404.14719)|**[link](https://github.com/vul-lmgnn/vul-lmggnn)**|
|**2024-04-23**|**Deep Overlapping Community Search via Subspace Embedding**|Qing Sima et.al.|[2404.14692](http://arxiv.org/abs/2404.14692)|null|
|**2024-04-23**|**Uncertainty Quantification on Graph Learning: A Survey**|Chao Chen et.al.|[2404.14642](http://arxiv.org/abs/2404.14642)|null|
|**2024-04-22**|**FedTAD: Topology-aware Data-free Knowledge Distillation for Subgraph Federated Learning**|Yinlin Zhu et.al.|[2404.14061](http://arxiv.org/abs/2404.14061)|null|
|**2024-04-22**|**Liquid-Graph Time-Constant Network for Multi-Agent Systems Control**|Antonio Marino et.al.|[2404.13982](http://arxiv.org/abs/2404.13982)|null|
|**2024-04-21**|**SPGNN: Recognizing Salient Subgraph Patterns via Enhanced Graph Convolution and Pooling**|Zehao Dong et.al.|[2404.13655](http://arxiv.org/abs/2404.13655)|null|
|**2024-04-21**|**Unsupervised Social Bot Detection via Structural Information Theory**|Hao Peng et.al.|[2404.13595](http://arxiv.org/abs/2404.13595)|**[link](https://github.com/selgroup/undbot)**|
|**2024-04-21**|**Test-Time Training on Graphs with Large Language Models (LLMs)**|Jiaxin Zhang et.al.|[2404.13571](http://arxiv.org/abs/2404.13571)|null|
|**2024-04-21**|**Graph4GUI: Graph Neural Networks for Representing Graphical User Interfaces**|Yue Jiang et.al.|[2404.13521](http://arxiv.org/abs/2404.13521)|null|
|**2024-04-21**|**Authentic Emotion Mapping: Benchmarking Facial Expressions in Real News**|Qixuan Zhang et.al.|[2404.13493](http://arxiv.org/abs/2404.13493)|null|
|**2024-04-20**|**GRANOLA: Adaptive Normalization for Graph Neural Networks**|Moshe Eliasof et.al.|[2404.13344](http://arxiv.org/abs/2404.13344)|null|
|**2024-04-19**|**Grasper: A Generalist Pursuer for Pursuit-Evasion Problems**|Pengdeng Li et.al.|[2404.12626](http://arxiv.org/abs/2404.12626)|**[link](https://github.com/ipadli/grasper)**|
|**2024-04-19**|**Multi-View Subgraph Neural Networks: Self-Supervised Learning with Scarce Labeled Data**|Zhenzhong Wang et.al.|[2404.12569](http://arxiv.org/abs/2404.12569)|null|
|**2024-04-18**|**Improving the interpretability of GNN predictions through conformal-based graph sparsification**|Pablo Sanchez-Martin et.al.|[2404.12356](http://arxiv.org/abs/2404.12356)|**[link](https://github.com/psanch21/cores)**|
|**2024-04-18**|**Graph Neural Networks for Wireless Networks: Graph Representation, Architecture and Evaluation**|Yang Lu et.al.|[2404.11858](http://arxiv.org/abs/2404.11858)|null|
|**2024-04-17**|**End-to-End Mesh Optimization of a Hybrid Deep Learning Black-Box PDE Solver**|Shaocong Ma et.al.|[2404.11766](http://arxiv.org/abs/2404.11766)|null|
|**2024-04-17**|**On the Scalability of GNNs for Molecular Graphs**|Maciej Sypetkowski et.al.|[2404.11568](http://arxiv.org/abs/2404.11568)|null|
|**2024-04-17**|**Tensor Factorisation for Polypharmacy Side Effect Prediction**|Oliver Lloyd et.al.|[2404.11374](http://arxiv.org/abs/2404.11374)|null|
|**2024-04-17**|**RiboDiffusion: Tertiary Structure-based RNA Inverse Folding with Generative Diffusion Models**|Han Huang et.al.|[2404.11199](http://arxiv.org/abs/2404.11199)|**[link](https://github.com/ml4bio/ribodiffusion)**|
|**2024-04-17**|**EEG_GLT-Net: Optimising EEG Graphs for Real-time Motor Imagery Signals Classification**|Htoo Wai Aung et.al.|[2404.11075](http://arxiv.org/abs/2404.11075)|null|
|**2024-04-17**|**You do not have to train Graph Neural Networks at all on text-attributed graphs**|Kaiwen Dong et.al.|[2404.11019](http://arxiv.org/abs/2404.11019)|null|
|**2024-04-17**|**Graph Continual Learning with Debiased Lossless Memory Replay**|Chaoxi Niu et.al.|[2404.10984](http://arxiv.org/abs/2404.10984)|null|
|**2024-04-16**|**Interpolation and differentiation of alchemical degrees of freedom in machine learning interatomic potentials**|Juno Nam et.al.|[2404.10746](http://arxiv.org/abs/2404.10746)|**[link](https://github.com/learningmatter-mit/alchemical-mlip)**|
|**2024-04-16**|**Graph Neural Networks for Protein-Protein Interactions - A Short Survey**|Mingda Xu et.al.|[2404.10450](http://arxiv.org/abs/2404.10450)|null|
|**2024-04-16**|**AGHINT: Attribute-Guided Representation Learning on Heterogeneous Information Networks with Transformer**|Jinhui Yuan et.al.|[2404.10443](http://arxiv.org/abs/2404.10443)|null|
|**2024-04-16**|**Physical formula enhanced multi-task learning for pharmacokinetics prediction**|Ruifeng Li et.al.|[2404.10354](http://arxiv.org/abs/2404.10354)|null|
|**2024-04-16**|**Rethinking the Graph Polynomial Filter via Positive and Negative Coupling Analysis**|Haodong Wen et.al.|[2404.10353](http://arxiv.org/abs/2404.10353)|null|
|**2024-04-16**|**Graph neural network-based surrogate modelling for real-time hydraulic prediction of urban drainage networks**|Zhiyu Zhang et.al.|[2404.10324](http://arxiv.org/abs/2404.10324)|**[link](https://github.com/Zhiyu014/GNN-UDS)**|
|**2024-04-16**|**Two-Stage Stance Labeling: User-Hashtag Heuristics with Graph Neural Networks**|Joshua Melton et.al.|[2404.10228](http://arxiv.org/abs/2404.10228)|null|
|**2024-04-15**|**Solving the Tree Containment Problem Using Graph Neural Networks**|Arkadiy Dushatskiy et.al.|[2404.09812](http://arxiv.org/abs/2404.09812)|**[link](https://github.com/arkadiyd/phylognn)**|
|**2024-04-15**|**Enhancing Code Vulnerability Detection via Vulnerability-Preserving Data Augmentation**|Shangqing Liu et.al.|[2404.09599](http://arxiv.org/abs/2404.09599)|null|
|**2024-04-15**|**GNNavigator: Towards Adaptive Training of Graph Neural Networks via Automatic Guideline Exploration**|Tong Qiao et.al.|[2404.09544](http://arxiv.org/abs/2404.09544)|null|
|**2024-04-14**|**Hierarchical Attention Models for Multi-Relational Graphs**|Roshni G. Iyer et.al.|[2404.09365](http://arxiv.org/abs/2404.09365)|**[link](https://github.com/roshnigiyer/br-gcn)**|
|**2024-04-14**|**DEGNN: Dual Experts Graph Neural Network Handling Both Edge and Node Feature Noise**|Tai Hasegawa et.al.|[2404.09207](http://arxiv.org/abs/2404.09207)|**[link](https://github.com/taihasegawa/degnn)**|
|**2024-04-12**|**Phase transitions of correlated systems from graph neural networks with quantum embedding techniques**|Rishi Rao et.al.|[2404.08782](http://arxiv.org/abs/2404.08782)|null|
|**2024-04-12**|**Learning-Based Joint Antenna Selection and Precoding Design for Cell-Free MIMO Networks**|Liangzhi Wang et.al.|[2404.08607](http://arxiv.org/abs/2404.08607)|null|
|**2024-04-12**|**Seismic First Break Picking in a Higher Dimension Using Deep Graph Learning**|Hongtao Wang et.al.|[2404.08408](http://arxiv.org/abs/2404.08408)|null|
|**2024-04-12**|**Relational Prompt-based Pre-trained Language Models for Social Event Detection**|Pu Li et.al.|[2404.08263](http://arxiv.org/abs/2404.08263)|**[link](https://github.com/ringbdstack/rplm_sed)**|
|**2024-04-11**|**Physics-Enhanced Graph Neural Networks For Soft Sensing in Industrial Internet of Things**|Keivan Faghih Niresi et.al.|[2404.08061](http://arxiv.org/abs/2404.08061)|**[link](https://github.com/EPFL-IMOS/PEGNN_SS)**|
|**2024-04-11**|**Pathology-genomic fusion via biologically informed cross-modality graph learning for survival analysis**|Zeyu Zhang et.al.|[2404.08023](http://arxiv.org/abs/2404.08023)|null|
|**2024-04-11**|**VeTraSS: Vehicle Trajectory Similarity Search Through Graph Modeling and Representation Learning**|Ming Cheng et.al.|[2404.08021](http://arxiv.org/abs/2404.08021)|null|
|**2024-04-11**|**GNN-based Probabilistic Supply and Inventory Predictions in Supply Chain Networks**|Hyung-il Ahn et.al.|[2404.07523](http://arxiv.org/abs/2404.07523)|null|
|**2024-04-11**|**Generative Probabilistic Planning for Optimizing Supply Chain Networks**|Hyung-il Ahn et.al.|[2404.07511](http://arxiv.org/abs/2404.07511)|null|
|**2024-04-11**|**Characterizing the Influence of Topology on Graph Learning Tasks**|Kailong Wu et.al.|[2404.07493](http://arxiv.org/abs/2404.07493)|null|
|**2024-04-10**|**Gaze-Guided Graph Neural Network for Action Anticipation Conditioned on Intention**|Suleyman Ozdel et.al.|[2404.07347](http://arxiv.org/abs/2404.07347)|null|
|**2024-04-10**|**VN-EGNN: E(3)-Equivariant Graph Neural Networks with Virtual Nodes Enhance Protein Binding Site Identification**|Florian Sestak et.al.|[2404.07194](http://arxiv.org/abs/2404.07194)|**[link](https://github.com/ml-jku/vnegnn)**|
|**2024-04-10**|**GCV-Turbo: End-to-end Acceleration of GNN-based Computer Vision Tasks on FPGA**|Bingyi Zhang et.al.|[2404.07188](http://arxiv.org/abs/2404.07188)|null|
|**2024-04-10**|**Fast System Technology Co-Optimization Framework for Emerging Technology Based on Graph Neural Networks**|Tianliang Ma et.al.|[2404.06939](http://arxiv.org/abs/2404.06939)|null|
|**2024-04-10**|**GraSAME: Injecting Token-Level Structural Information to Pretrained Language Models via Graph-guided Self-Attention Mechanism**|Shuzhou Yuan et.al.|[2404.06911](http://arxiv.org/abs/2404.06911)|null|
|**2024-04-10**|**NFARec: A Negative Feedback-Aware Recommender Model**|Xinfeng Wang et.al.|[2404.06900](http://arxiv.org/abs/2404.06900)|**[link](https://github.com/wangxfng/nfarec)**|
|**2024-04-10**|**CaDRec: Contextualized and Debiased Recommender Model**|Xinfeng Wang et.al.|[2404.06895](http://arxiv.org/abs/2404.06895)|**[link](https://github.com/wangxfng/cadrec)**|
|**2024-04-10**|**Forecasting the Future with Future Technologies: Advancements in Large Meteorological Models**|Hailong Shu et.al.|[2404.06668](http://arxiv.org/abs/2404.06668)|null|
|**2024-04-09**|**Quantum Graph Optimization Algorithm**|Yuhan Huang et.al.|[2404.06434](http://arxiv.org/abs/2404.06434)|null|
|**2024-04-09**|**Large Language Models to the Rescue: Deadlock Resolution in Multi-Robot Systems**|Kunal Garg et.al.|[2404.06413](http://arxiv.org/abs/2404.06413)|null|
|**2024-04-09**|**Oracle-Net for nonlinear compressed sensing in Electrical Impedance Tomography reconstruction problems**|Damiana Lazzaro et.al.|[2404.06342](http://arxiv.org/abs/2404.06342)|null|
|**2024-04-09**|**Message Passing Variational Autoregressive Network for Solving Intractable Ising Models**|Qunlong Ma et.al.|[2404.06225](http://arxiv.org/abs/2404.06225)|null|
|**2024-04-09**|**scCDCG: Efficient Deep Structural Clustering for single-cell RNA-seq via Deep Cut-informed Graph Embedding**|Ping Xu et.al.|[2404.06167](http://arxiv.org/abs/2404.06167)|**[link](https://github.com/xpgogogo/sccdcg)**|
|**2024-04-09**|**Fair Graph Neural Network with Supervised Contrastive Regularization**|Mahdi Tavassoli Kejani et.al.|[2404.06090](http://arxiv.org/abs/2404.06090)|null|
|**2024-04-09**|**Object Dynamics Modeling with Hierarchical Point Cloud-based Representations**|Chanho Kim et.al.|[2404.06044](http://arxiv.org/abs/2404.06044)|null|
|**2024-04-09**|**Commute with Community: Enhancing Shared Travel through Social Networks**|Tian Siyuan et.al.|[2404.05987](http://arxiv.org/abs/2404.05987)|null|
|**2024-04-08**|**Rapid and Precise Topological Comparison with Merge Tree Neural Networks**|Yu Qin et.al.|[2404.05879](http://arxiv.org/abs/2404.05879)|null|
|**2024-04-08**|**Graph Neural Networks Automated Design and Deployment on Device-Edge Co-Inference Systems**|Ao Zhou et.al.|[2404.05605](http://arxiv.org/abs/2404.05605)|null|
|**2024-04-08**|**Technical Report: The Graph Spectral Token -- Enhancing Graph Transformers with Spectral Information**|Zihan Pengmei et.al.|[2404.05604](http://arxiv.org/abs/2404.05604)|**[link](https://github.com/zpengmei/SubFormer-Spec)**|
|**2024-04-08**|**Back to the Future: GNN-based NO $_2$ Forecasting via Future Covariates**|Antonio Giganti et.al.|[2404.05324](http://arxiv.org/abs/2404.05324)|**[link](https://github.com/polimi-ispl/magcrn)**|
|**2024-04-08**|**HOEG: A New Approach for Object-Centric Predictive Process Monitoring**|Tim K. Smit et.al.|[2404.05316](http://arxiv.org/abs/2404.05316)|**[link](https://github.com/tkforgeron/ocppm)**|
|**2024-04-07**|**Temporal Generalization Estimation in Evolving Graphs**|Bin Lu et.al.|[2404.04969](http://arxiv.org/abs/2404.04969)|null|
|**2024-04-07**|**Graph Neural Network Meets Multi-Agent Reinforcement Learning: Fundamentals, Applications, and Future Directions**|Ziheng Liu et.al.|[2404.04898](http://arxiv.org/abs/2404.04898)|null|
|**2024-04-07**|**Graph Neural Networks for Binary Programming**|Moshe Eliasof et.al.|[2404.04874](http://arxiv.org/abs/2404.04874)|null|
|**2024-04-07**|**GDR-HGNN: A Heterogeneous Graph Neural Networks Accelerator Frontend with Graph Decoupling and Recoupling**|Runzhen Xue et.al.|[2404.04792](http://arxiv.org/abs/2404.04792)|null|
|**2024-04-06**|**Spectral Graph Pruning Against Over-Squashing and Over-Smoothing**|Adarsh Jamadandi et.al.|[2404.04612](http://arxiv.org/abs/2404.04612)|**[link](https://github.com/relationalml/spectralpruningbraess)**|
|**2024-04-06**|**Spectral GNN via Two-dimensional (2-D) Graph Convolution**|Guoming Li et.al.|[2404.04559](http://arxiv.org/abs/2404.04559)|null|
|**2024-04-04**|**Free Energy Calculations using Smooth Basin Classification**|Sander Vandenhaute et.al.|[2404.03777](http://arxiv.org/abs/2404.03777)|null|
|**2024-04-04**|**Generalization Bounds for Message Passing Networks on Mixture of Graphons**|Sohir Maskey et.al.|[2404.03473](http://arxiv.org/abs/2404.03473)|null|
|**2024-04-04**|**On the Theoretical Expressive Power and the Design Space of Higher-Order Graph Transformers**|Cai Zhou et.al.|[2404.03380](http://arxiv.org/abs/2404.03380)|**[link](https://github.com/zhouc20/k-transformer)**|
|**2024-04-04**|**Graph Neural Networks for Electric and Hydraulic Data Fusion to Enhance Short-term Forecasting of Pumped-storage Hydroelectricity**|Raffael Theiler et.al.|[2404.03368](http://arxiv.org/abs/2404.03368)|null|
|**2024-04-04**|**Decentralized Learning Strategies for Estimation Error Minimization with Graph Neural Networks**|Xingran Chen et.al.|[2404.03227](http://arxiv.org/abs/2404.03227)|null|
|**2024-04-04**|**Theoretical and Empirical Insights into the Origins of Degree Bias in Graph Neural Networks**|Arjun Subramonian et.al.|[2404.03139](http://arxiv.org/abs/2404.03139)|**[link](https://github.com/arjunsubramonian/degree-bias-exploration)**|
|**2024-04-03**|**First-order PDES for Graph Neural Networks: Advection And Burgers Equation Models**|Yifan Qu et.al.|[2404.03081](http://arxiv.org/abs/2404.03081)|null|
|**2024-04-03**|**GeoT: Tensor Centric Library for Graph Neural Network via Efficient Segment Reduction on GPU**|Zhongming Yu et.al.|[2404.03019](http://arxiv.org/abs/2404.03019)|**[link](https://github.com/fishmingyu/geot)**|
|**2024-04-03**|**Generative-Contrastive Heterogeneous Graph Neural Network**|Yu Wang et.al.|[2404.02810](http://arxiv.org/abs/2404.02810)|null|
|**2024-04-03**|**Weakly-Supervised 3D Scene Graph Generation via Visual-Linguistic Assisted Pseudo-labeling**|Xu Wang et.al.|[2404.02527](http://arxiv.org/abs/2404.02527)|null|
|**2024-04-02**|**Unmasking Correlations in Nuclear Cross Sections with Graph Neural Networks**|Sinjini Mitra et.al.|[2404.02332](http://arxiv.org/abs/2404.02332)|null|
|**2024-04-02**|**Virtual Sensor for Real-Time Bearing Load Prediction Using Heterogeneous Temporal Graph Neural Networks**|Mengjie Zhao et.al.|[2404.02304](http://arxiv.org/abs/2404.02304)|null|
|**2024-04-02**|**CATGNN: Cost-Efficient and Scalable Distributed Training for Graph Neural Networks**|Xin Huang et.al.|[2404.02300](http://arxiv.org/abs/2404.02300)|null|
|**2024-04-02**|**Multi-Level Label Correction by Distilling Proximate Patterns for Semi-supervised Semantic Segmentation**|Hui Xiao et.al.|[2404.02065](http://arxiv.org/abs/2404.02065)|null|
|**2024-04-02**|**DSGNN: A Dual-View Supergrid-Aware Graph Neural Network for Regional Air Quality Estimation**|Xin Zhang et.al.|[2404.01975](http://arxiv.org/abs/2404.01975)|null|
|**2024-04-02**|**Continuous Spiking Graph Neural Networks**|Nan Yin et.al.|[2404.01897](http://arxiv.org/abs/2404.01897)|null|
|**2024-04-02**|**HeMeNet: Heterogeneous Multichannel Equivariant Network for Protein Multitask Learning**|Rong Han et.al.|[2404.01693](http://arxiv.org/abs/2404.01693)|null|
|**2024-04-01**|**Machine Learning in High Energy Physics: A review of heavy-flavor jet tagging at the LHC**|Spandan Mondal et.al.|[2404.01071](http://arxiv.org/abs/2404.01071)|null|
|**2024-04-01**|**Equivariant Local Reference Frames for Unsupervised Non-rigid Point Cloud Shape Correspondence**|Ling Wang et.al.|[2404.00959](http://arxiv.org/abs/2404.00959)|null|
|**2024-03-31**|**PyTorch Frame: A Modular Framework for Multi-Modal Tabular Learning**|Weihua Hu et.al.|[2404.00776](http://arxiv.org/abs/2404.00776)|**[link](https://github.com/pyg-team/pytorch-frame)**|
|**2024-03-30**|**DE-HNN: An effective neural model for Circuit Netlist representation**|Zhishang Luo et.al.|[2404.00477](http://arxiv.org/abs/2404.00477)|**[link](https://github.com/tilos-ai-institute/dehnn)**|
|**2024-03-30**|**Constrained Layout Generation with Factor Graphs**|Mohammed Haroon Dupty et.al.|[2404.00385](http://arxiv.org/abs/2404.00385)|null|
|**2024-03-30**|**EventGround: Narrative Reasoning by Grounding to Eventuality-centric Knowledge Graphs**|Cheng Jiayang et.al.|[2404.00209](http://arxiv.org/abs/2404.00209)|**[link](https://github.com/hkust-knowcomp/eventground)**|
|**2024-03-29**|**Graph Neural Aggregation-diffusion with Metastability**|Kaiyuan Cui et.al.|[2403.20221](http://arxiv.org/abs/2403.20221)|null|
|**2024-03-29**|**On Size and Hardness Generalization in Unsupervised Learning for the Travelling Salesman Problem**|Yimeng Min et.al.|[2403.20212](http://arxiv.org/abs/2403.20212)|null|
|**2024-03-29**|**Na Vacancy Driven Phase Transformation and Fast Ion Conduction in W-doped Na $_3$SbS$_4$ from Machine Learning Force Fields**|Johan Klarbring et.al.|[2403.20138](http://arxiv.org/abs/2403.20138)|null|
|**2024-03-29**|**KGUF: Simple Knowledge-aware Graph-based Recommender with User-based Semantic Features Filtering**|Salvatore Bufi et.al.|[2403.20095](http://arxiv.org/abs/2403.20095)|**[link](https://github.com/sisinflab/kguf)**|
|**2024-03-29**|**Beyond the Known: Novel Class Discovery for Open-world Graph Learning**|Yucheng Jin et.al.|[2403.19907](http://arxiv.org/abs/2403.19907)|null|
|**2024-03-28**|**A Review of Graph Neural Networks in Epidemic Modeling**|Zewen Liu et.al.|[2403.19852](http://arxiv.org/abs/2403.19852)|**[link](https://github.com/emory-melody/awesome-epidemic-modeling-papers)**|
|**2024-03-28**|**Gegenbauer Graph Neural Networks for Time-varying Signal Reconstruction**|Jhon A. Castro-Correa et.al.|[2403.19800](http://arxiv.org/abs/2403.19800)|**[link](https://github.com/jcastro295/gegengnn)**|
|**2024-03-28**|**SG-PGM: Partial Graph Matching Network with Semantic Geometric Fusion for 3D Scene Graph Alignment and Its Downstream Tasks**|Yaxu Xie et.al.|[2403.19474](http://arxiv.org/abs/2403.19474)|**[link](https://github.com/dfki-av/sg-pgm)**|
|**2024-03-28**|**Exploiting Individual Graph Structures to Enhance Ecological Momentary Assessment (EMA) Forecasting**|Mandani Ntekouli et.al.|[2403.19442](http://arxiv.org/abs/2403.19442)|null|
|**2024-03-28**|**Graph Neural Networks for Treatment Effect Prediction**|George Panagopoulos et.al.|[2403.19289](http://arxiv.org/abs/2403.19289)|**[link](https://github.com/geopanag/UMGNet)**|
|**2024-03-28**|**Tiny Graph Neural Networks for Radio Resource Management**|Ahmad Ghasemi et.al.|[2403.19143](http://arxiv.org/abs/2403.19143)|null|
|**2024-03-28**|**FluxGAT: Integrating Flux Sampling with Graph Neural Networks for Unbiased Gene Essentiality Classification**|Kieren Sharma et.al.|[2403.18666](http://arxiv.org/abs/2403.18666)|**[link](https://github.com/kierensharma/fluxgat)**|
|**2024-03-27**|**Physics-Informed Graph Neural Networks for Water Distribution Systems**|Inaam Ashraf et.al.|[2403.18570](http://arxiv.org/abs/2403.18570)|**[link](https://github.com/HammerLabML/physics_informed_gnns_for_wds)**|
|**2024-03-28**|**Lightweight Embeddings for Graph Collaborative Filtering**|Xurong Liang et.al.|[2403.18479](http://arxiv.org/abs/2403.18479)|**[link](https://github.com/xurong-liang/LEGCF)**|
|**2024-03-27**|**Deciphering Chemical Ordering in High Entropy Materials: A Machine Learning-Accelerated High-throughput Cluster Expansion Approach**|Guillermo Vazquez et.al.|[2403.18298](http://arxiv.org/abs/2403.18298)|null|
|**2024-03-27**|**GeNet: A Graph Neural Network-based Anti-noise Task-Oriented Semantic Communication Paradigm**|Chunhang Zheng et.al.|[2403.18296](http://arxiv.org/abs/2403.18296)|**[link](https://github.com/chunbaobao/genet)**|
|**2024-03-26**|**HERTA: A High-Efficiency and Rigorous Training Algorithm for Unfolded Graph Neural Networks**|Yongyi Yang et.al.|[2403.18142](http://arxiv.org/abs/2403.18142)|null|
|**2024-03-26**|**Securing GNNs: Explanation-Based Identification of Backdoored Training Graphs**|Jane Downer et.al.|[2403.18136](http://arxiv.org/abs/2403.18136)|null|
|**2024-03-26**|**CANOS: A Fast and Scalable Neural AC-OPF Solver Robust To N-1 Perturbations**|Luis Piloto et.al.|[2403.17660](http://arxiv.org/abs/2403.17660)|null|
|**2024-03-27**|**Intrinsic Subgraph Generation for Interpretable Graph based Visual Question Answering**|Pascal Tilli et.al.|[2403.17647](http://arxiv.org/abs/2403.17647)|**[link](https://github.com/digitalphonetics/intrinsic-subgraph-generation-for-vqa)**|
|**2024-03-26**|**EL-MLFFs: Ensemble Learning of Machine Leaning Force Fields**|Bangchen Yin et.al.|[2403.17507](http://arxiv.org/abs/2403.17507)|null|
|**2024-03-26**|**Variational Graph Auto-Encoder Based Inductive Learning Method for Semi-Supervised Classification**|Hanxuan Yang et.al.|[2403.17500](http://arxiv.org/abs/2403.17500)|null|
|**2024-03-26**|**AFDGCF: Adaptive Feature De-correlation Graph Collaborative Filtering for Recommendations**|Wei Wu et.al.|[2403.17416](http://arxiv.org/abs/2403.17416)|**[link](https://github.com/u-rara/afdgcf)**|
|**2024-03-26**|**Explainable Graph Neural Networks for Observation Impact Analysis in Atmospheric State Estimation**|Hyeon-Ju Jeon et.al.|[2403.17384](http://arxiv.org/abs/2403.17384)|null|
|**2024-03-26**|**Learn from Heterophily: Heterophilous Information-enhanced Graph Neural Network**|Yilun Zheng et.al.|[2403.17351](http://arxiv.org/abs/2403.17351)|**[link](https://github.com/zylMozart/HiGNN)**|
|**2024-03-25**|**Manufacturing Service Capability Prediction with Graph Neural Networks**|Yunqing Li et.al.|[2403.17239](http://arxiv.org/abs/2403.17239)|null|
|**2024-03-25**|**AnimateMe: 4D Facial Expressions via Diffusion Models**|Dimitrios Gerogiannis et.al.|[2403.17213](http://arxiv.org/abs/2403.17213)|null|
|**2024-03-25**|**CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions**|Azmine Toushik Wasi et.al.|[2403.17210](http://arxiv.org/abs/2403.17210)|null|
|**2024-03-25**|**Graph Augmentation for Recommendation**|Qianru Zhang et.al.|[2403.16656](http://arxiv.org/abs/2403.16656)|**[link](https://github.com/hkuds/graphaug)**|
|**2024-03-25**|**LSTTN: A Long-Short Term Transformer-based Spatio-temporal Neural Network for Traffic Flow Forecasting**|Qinyao Luo et.al.|[2403.16495](http://arxiv.org/abs/2403.16495)|**[link](https://github.com/geox-lab/lsttn)**|
|**2024-03-25**|**ChebMixer: Efficient Graph Representation Learning with MLP Mixer**|Xiaoyan Kui et.al.|[2403.16358](http://arxiv.org/abs/2403.16358)|null|
|**2024-03-26**|**Rumor Detection with a novel graph neural network approach**|Tianrui Liu et.al.|[2403.16206](http://arxiv.org/abs/2403.16206)|null|
|**2024-03-24**|**A Survey on Self-Supervised Pre-Training of Graph Foundation Models: A Knowledge-Based Perspective**|Ziwen Zhao et.al.|[2403.16137](http://arxiv.org/abs/2403.16137)|**[link](https://github.com/newiz430/pretext)**|
|**2024-03-24**|**SSHPool: The Separated Subgraph-based Hierarchical Pooling**|Zhuo Xu et.al.|[2403.16133](http://arxiv.org/abs/2403.16133)|null|
|**2024-03-24**|**Segment Anything Model for Road Network Graph Extraction**|Congrui Hetang et.al.|[2403.16051](http://arxiv.org/abs/2403.16051)|**[link](https://github.com/htcr/sam_road)**|
|**2024-03-24**|**Node Classification via Semantic-Structural Attention-Enhanced Graph Convolutional Networks**|Hongyin Zhu et.al.|[2403.16033](http://arxiv.org/abs/2403.16033)|null|
|**2024-03-24**|**A Federated Parameter Aggregation Method for Node Classification Tasks with Different Graph Network Structures**|Hao Song et.al.|[2403.16004](http://arxiv.org/abs/2403.16004)|null|
|**2024-03-22**|**Efficient first principles based modeling via machine learning: from simple representations to high entropy materials**|Kangming Li et.al.|[2403.15579](http://arxiv.org/abs/2403.15579)|**[link](https://github.com/mathsphy/high-entropy-alloys-dataset-ml)**|
|**2024-03-22**|**Cascading Blackout Severity Prediction with Statistically-Augmented Graph Neural Networks**|Joe Gorka et.al.|[2403.15363](http://arxiv.org/abs/2403.15363)|null|
|**2024-03-22**|**Benchmarking of machine learning interatomic potentials for reactive hydrogen dynamics at metal surfaces**|Wojciech G. Stark et.al.|[2403.15334](http://arxiv.org/abs/2403.15334)|null|
|**2024-03-22**|**Graph neural network coarse-grain force field for the molecular crystal RDX**|Brian H. Lee et.al.|[2403.15266](http://arxiv.org/abs/2403.15266)|null|
|**2024-03-22**|**GTAGCN: Generalized Topology Adaptive Graph Convolutional Networks**|Sukhdeep Singh et.al.|[2403.15077](http://arxiv.org/abs/2403.15077)|null|
|**2024-03-22**|**Simple Graph Condensation**|Zhenbang Xiao et.al.|[2403.14951](http://arxiv.org/abs/2403.14951)|**[link](https://github.com/banghonor/simgc)**|
|**2024-03-21**|**iSpLib: A Library for Accelerating Graph Neural Networks using Auto-tuned Sparse Operations**|Md Saidul Hoque Anik et.al.|[2403.14853](http://arxiv.org/abs/2403.14853)|**[link](https://github.com/hipgraph/isplib)**|
|**2024-03-21**|**NaNa and MiGu: Semantic Data Augmentation Techniques to Enhance Protein Classification in Graph Neural Networks**|Yi-Shan Lan et.al.|[2403.14736](http://arxiv.org/abs/2403.14736)|**[link](https://github.com/r08b46009/code_for_migu_nana)**|
|**2024-03-21**|**Knowledge-Enhanced Recommendation with User-Centric Subgraph Network**|Guangyi Liu et.al.|[2403.14377](http://arxiv.org/abs/2403.14377)|**[link](https://github.com/leolouis14/kucnet)**|
|**2024-03-20**|**Data-Driven Modeling of Dislocation Mobility from Atomistics using Physics-Informed Machine Learning**|Yifeng Tian et.al.|[2403.14015](http://arxiv.org/abs/2403.14015)|null|
|**2024-03-20**|**Considerations in the use of ML interaction potentials for free energy calculations**|Orlando A. Mendible et.al.|[2403.13952](http://arxiv.org/abs/2403.13952)|**[link](https://github.com/omendibleba/considerations_for_mlps_fes)**|
|**2024-03-20**|**Graph Neural Network for Crawling Target Nodes in Social Networks**|Kirill Lukyanov et.al.|[2403.13865](http://arxiv.org/abs/2403.13865)|null|
|**2024-03-20**|**Sparse Implementation of Versatile Graph-Informed Layers**|Francesco Della Santa et.al.|[2403.13781](http://arxiv.org/abs/2403.13781)|**[link](https://github.com/fra0013to/ginn)**|
|**2024-03-20**|**Unifews: Unified Entry-Wise Sparsification for Efficient Graph Neural Network**|Ningyi Liao et.al.|[2403.13268](http://arxiv.org/abs/2403.13268)|null|
|**2024-03-20**|**A Comparative Study of Machine Learning Models Predicting Energetics of Interacting Defects**|Hao Yu et.al.|[2403.13243](http://arxiv.org/abs/2403.13243)|null|
|**2024-03-19**|**Improving tracking algorithms with machine learning: a case for line-segment tracking at the High Luminosity LHC**|Jonathan Guiang et.al.|[2403.13166](http://arxiv.org/abs/2403.13166)|null|
|**2024-03-19**|**Graph Neural Network-based Multi-agent Reinforcement Learning for Resilient Distributed Coordination of Multi-Robot Systems**|Anthony Goeckner et.al.|[2403.13093](http://arxiv.org/abs/2403.13093)|**[link](https://github.com/nu-ideas-lab/patrolling_zoo)**|
|**2024-03-21**|**FlowerFormer: Empowering Neural Architecture Encoding using a Flow-aware Graph Transformer**|Dongyeong Hwang et.al.|[2403.12821](http://arxiv.org/abs/2403.12821)|**[link](https://github.com/y0ngjaenius/cvpr2024_flowerformer)**|
|**2024-03-19**|**Contextualized Messages Boost Graph Representations**|Brian Godwin Lim et.al.|[2403.12529](http://arxiv.org/abs/2403.12529)|**[link](https://github.com/briangodwinlim/sir-gcn)**|
|**2024-03-19**|**FairSIN: Achieving Fairness in Graph Neural Networks through Sensitive Information Neutralization**|Cheng Yang et.al.|[2403.12474](http://arxiv.org/abs/2403.12474)|null|
|**2024-03-19**|**STG-Mamba: Spatial-Temporal Graph Learning via Selective State Space Model**|Lincan Li et.al.|[2403.12418](http://arxiv.org/abs/2403.12418)|**[link](https://github.com/LincanLi98/STG-Mamba)**|
|**2024-03-18**|**Molecular dynamics simulation with finite electric fields using Perturbed Neural Network Potentials**|Kit Joll et.al.|[2403.12319](http://arxiv.org/abs/2403.12319)|**[link](https://github.com/pschienbein/atomicpolartensor)**|
|**2024-03-18**|**Molecular Classification Using Hyperdimensional Graph Classification**|Pere Verges et.al.|[2403.12307](http://arxiv.org/abs/2403.12307)|null|
|**2024-03-18**|**Graph Neural Networks for Learning Equivariant Representations of Neural Networks**|Miltiadis Kofinas et.al.|[2403.12143](http://arxiv.org/abs/2403.12143)|**[link](https://github.com/mkofinas/neural-graphs)**|
|**2024-03-19**|**Leveraging Spatial and Semantic Feature Extraction for Skin Cancer Diagnosis with Capsule Networks and Graph Neural Networks**|K. P. Santoso et.al.|[2403.12009](http://arxiv.org/abs/2403.12009)|null|
|**2024-03-18**|**CASPER: Causality-Aware Spatiotemporal Graph Neural Networks for Spatiotemporal Time Series Imputation**|Baoyu Jing et.al.|[2403.11960](http://arxiv.org/abs/2403.11960)|null|
|**2024-03-18**|**NuGraph2: A Graph Neural Network for Neutrino Physics Event Reconstruction**|V Hewes et.al.|[2403.11872](http://arxiv.org/abs/2403.11872)|null|
|**2024-03-18**|**Dual-Channel Multiplex Graph Neural Networks for Recommendation**|Xiang Li et.al.|[2403.11624](http://arxiv.org/abs/2403.11624)|null|
|**2024-03-18**|**Graph Partial Label Learning with Potential Cause Discovering**|Hang Gao et.al.|[2403.11449](http://arxiv.org/abs/2403.11449)|null|
|**2024-03-18**|**Layer-diverse Negative Sampling for Graph Neural Networks**|Wei Duan et.al.|[2403.11408](http://arxiv.org/abs/2403.11408)|null|
|**2024-03-19**|**DynamicGlue: Epipolar and Time-Informed Data Association in Dynamic Environments using Graph Neural Networks**|Theresa Huber et.al.|[2403.11370](http://arxiv.org/abs/2403.11370)|null|
|**2024-03-17**|**Phonon predictions with E(3)-equivariant graph neural networks**|Shiang Fang et.al.|[2403.11347](http://arxiv.org/abs/2403.11347)|null|
|**2024-03-17**|**Graph Neural Network based Double Machine Learning Estimator of Network Causal Effects**|Seyedeh Baharan Khatami et.al.|[2403.11332](http://arxiv.org/abs/2403.11332)|null|
|**2024-03-17**|**Multi-Relational Graph Neural Network for Out-of-Domain Link Prediction**|Asma Sattar et.al.|[2403.11292](http://arxiv.org/abs/2403.11292)|null|
|**2024-03-17**|**Jointly Optimizing Terahertz based Sensing and Communications in Vehicular Networks: A Dynamic Graph Neural Network Approach**|Xuefei Li et.al.|[2403.11102](http://arxiv.org/abs/2403.11102)|null|
|**2024-03-16**|**Forward Learning of Graph Neural Networks**|Namyong Park et.al.|[2403.11004](http://arxiv.org/abs/2403.11004)|**[link](https://github.com/facebookresearch/forwardgnn)**|
|**2024-03-16**|**Edge Private Graph Neural Networks with Singular Value Perturbation**|Tingting Tang et.al.|[2403.10995](http://arxiv.org/abs/2403.10995)|null|
|**2024-03-15**|**Generation is better than Modification: Combating High Class Homophily Variance in Graph Anomaly Detection**|Rui Zhang et.al.|[2403.10339](http://arxiv.org/abs/2403.10339)|null|
|**2024-03-15**|**From Chaos to Clarity: Time Series Anomaly Detection in Astronomical Observations**|Xinli Hao et.al.|[2403.10220](http://arxiv.org/abs/2403.10220)|**[link](https://github.com/xinlihao/aero)**|
|**2024-03-15**|**HeR-DRL:Heterogeneous Relational Deep Reinforcement Learning for Decentralized Multi-Robot Crowd Navigation**|Xinyu Zhou et.al.|[2403.10083](http://arxiv.org/abs/2403.10083)|**[link](https://github.com/zhouxy-debugging-den/her-drl)**|
|**2024-03-15**|**Thermal Earth Model for the Conterminous United States Using an Interpolative Physics-Informed Graph Neural Network (InterPIGNN)**|Mohammad J. Aljubran et.al.|[2403.09961](http://arxiv.org/abs/2403.09961)|null|
|**2024-03-14**|**Robust Subgraph Learning by Monitoring Early Training Representations**|Sepideh Neshatfar et.al.|[2403.09901](http://arxiv.org/abs/2403.09901)|null|
|**2024-03-14**|**Code Revert Prediction with Graph Neural Networks: A Case Study at J.P. Morgan Chase**|Yulong Pei et.al.|[2403.09507](http://arxiv.org/abs/2403.09507)|null|
|**2024-03-14**|**Rumor Mitigation in Social Media Platforms with Deep Reinforcement Learning**|Hongyuan Su et.al.|[2403.09217](http://arxiv.org/abs/2403.09217)|**[link](https://github.com/tsinghua-fib-lab/drl-rumor-mitigation)**|
|**2024-03-14**|**MetroGNN: Metro Network Expansion with Reinforcement Learning**|Hongyuan Su et.al.|[2403.09197](http://arxiv.org/abs/2403.09197)|**[link](https://github.com/tsinghua-fib-lab/metrognn)**|
|**2024-03-14**|**ADEdgeDrop: Adversarial Edge Dropping for Robust Graph Neural Networks**|Zhaoliang Chen et.al.|[2403.09171](http://arxiv.org/abs/2403.09171)|null|
|**2024-03-14**|**Spatial-temporal Memories Enhanced Graph Autoencoder for Anomaly Detection in Dynamic Graphs**|Jie Liu et.al.|[2403.09039](http://arxiv.org/abs/2403.09039)|null|
|**2024-03-13**|**Link Prediction for Social Networks using Representation Learning and Heuristic-based Features**|Samarth Khanna et.al.|[2403.08613](http://arxiv.org/abs/2403.08613)|null|
|**2024-03-13**|**Reproducibility and Geometric Intrinsic Dimensionality: An Investigation on Graph Neural Network Research**|Tobias Hille et.al.|[2403.08438](http://arxiv.org/abs/2403.08438)|null|
|**2024-03-13**|**Causal Graph Neural Networks for Wildfire Danger Prediction**|Shan Zhao et.al.|[2403.08414](http://arxiv.org/abs/2403.08414)|null|
|**2024-03-13**|**Fast Inference of Removal-Based Node Influence**|Weikai Li et.al.|[2403.08333](http://arxiv.org/abs/2403.08333)|**[link](https://github.com/weikai-li/nora)**|
|**2024-03-13**|**BG-HGNN: Toward Scalable and Efficient Heterogeneous Graph Neural Network**|Junwei Su et.al.|[2403.08207](http://arxiv.org/abs/2403.08207)|null|
|**2024-03-12**|**Optimizing Polynomial Graph Filters: A Novel Adaptive Krylov Subspace Approach**|Keke Huang et.al.|[2403.07954](http://arxiv.org/abs/2403.07954)|**[link](https://github.com/kkhuang81/AdaptKry)**|
|**2024-03-12**|**Iterative Graph Neural Network Enhancement via Frequent Subgraph Mining of Explanations**|Harish G. Naik et.al.|[2403.07849](http://arxiv.org/abs/2403.07849)|null|
|**2024-03-12**|**OmniMatch: Effective Self-Supervised Any-Join Discovery in Tabular Data Repositories**|Christos Koutras et.al.|[2403.07653](http://arxiv.org/abs/2403.07653)|null|
|**2024-03-12**|**Towards Graph Foundation Models for Personalization**|Andreas Damianou et.al.|[2403.07478](http://arxiv.org/abs/2403.07478)|null|
|**2024-03-12**|**One for All and All for One: GNN-based Control-Flow Attestation for Embedded Devices**|Marco Chilese et.al.|[2403.07465](http://arxiv.org/abs/2403.07465)|null|
|**2024-03-13**|**Graph Unlearning with Efficient Partial Retraining**|Jiahao Zhang et.al.|[2403.07353](http://arxiv.org/abs/2403.07353)|null|
|**2024-03-12**|**Graph Data Condensation via Self-expressive Graph Structure Reconstruction**|Zhanyu Liu et.al.|[2403.07294](http://arxiv.org/abs/2403.07294)|**[link](https://github.com/zclzcl0223/GCSR)**|
|**2024-03-11**|**Uncertainty in Graph Neural Networks: A Survey**|Fangxin Wang et.al.|[2403.07185](http://arxiv.org/abs/2403.07185)|null|
|**2024-03-11**|**All in One: Multi-Task Prompting for Graph Neural Networks (Extended Abstract)**|Xiangguo Sun et.al.|[2403.07040](http://arxiv.org/abs/2403.07040)|null|
|**2024-03-11**|**Are Targeted Messages More Effective?**|Martin Grohe et.al.|[2403.06817](http://arxiv.org/abs/2403.06817)|null|
|**2024-03-11**|**Advancing Graph Neural Networks with HL-HGAT: A Hodge-Laplacian and Attention Mechanism Approach for Heterogeneous Graph-Structured Data**|Jinghan Huang et.al.|[2403.06687](http://arxiv.org/abs/2403.06687)|null|
|**2024-03-11**|**Graph Neural Network with Two Uplift Estimators for Label-Scarcity Individual Uplift Modeling**|Dingyuan Zhu et.al.|[2403.06489](http://arxiv.org/abs/2403.06489)|null|
|**2024-03-11**|**Financial Default Prediction via Motif-preserving Graph Neural Network with Curriculum Learning**|Daixin Wang et.al.|[2403.06482](http://arxiv.org/abs/2403.06482)|null|
|**2024-03-11**|**Ensemble Quadratic Assignment Network for Graph Matching**|Haoru Tan et.al.|[2403.06457](http://arxiv.org/abs/2403.06457)|null|
|**2024-03-11**|**Joint-Embedding Masked Autoencoder for Self-supervised Learning of Dynamic Functional Connectivity from the Human Brain**|Jungwon Choi et.al.|[2403.06432](http://arxiv.org/abs/2403.06432)|null|
|**2024-03-11**|**A Differential Geometric View and Explainability of GNN on Evolving Graphs**|Yazheng Liu et.al.|[2403.06425](http://arxiv.org/abs/2403.06425)|null|
|**2024-03-10**|**Cooperative Classification and Rationalization for Graph Generalization**|Linan Yue et.al.|[2403.06239](http://arxiv.org/abs/2403.06239)|**[link](https://github.com/yuelinan/codes-of-c2r)**|
|**2024-03-10**|**Local Vertex Colouring Graph Neural Networks**|Shouheng Li et.al.|[2403.06080](http://arxiv.org/abs/2403.06080)|**[link](https://github.com/seanli3/lvc)**|
|**2024-03-10**|**Generalization of Graph Neural Networks through the Lens of Homomorphism**|Shouheng Li et.al.|[2403.06079](http://arxiv.org/abs/2403.06079)|null|
|**2024-03-08**|**Advances of Deep Learning in Protein Science: A Comprehensive Survey**|Bozhen Hu et.al.|[2403.05314](http://arxiv.org/abs/2403.05314)|null|
|**2024-03-08**|**Personalized Audiobook Recommendations at Spotify Through Graph Neural Networks**|Marco De Nadai et.al.|[2403.05185](http://arxiv.org/abs/2403.05185)|null|
|**2024-03-08**|**Spectral Invariant Learning for Dynamic Graphs under Distribution Shifts**|Zeyang Zhang et.al.|[2403.05026](http://arxiv.org/abs/2403.05026)|**[link](https://github.com/wondergo2017/sild)**|
|**2024-03-08**|**Jet Discrimination with Quantum Complete Graph Neural Network**|Yi-An Chen et.al.|[2403.04990](http://arxiv.org/abs/2403.04990)|**[link](https://github.com/ntuhep-qml/qcgnn)**|
|**2024-03-08**|**Node Centrality Approximation For Large Networks Based On Inductive Graph Neural Networks**|Yiwei Zou et.al.|[2403.04977](http://arxiv.org/abs/2403.04977)|null|
|**2024-03-07**|**BloomGML: Graph Machine Learning through the Lens of Bilevel Optimization**|Amber Yijia Zheng et.al.|[2403.04763](http://arxiv.org/abs/2403.04763)|**[link](https://github.com/amberyzheng/bloomgml)**|
|**2024-03-07**|**GNN-VPA: A Variance-Preserving Aggregation Strategy for Graph Neural Networks**|Lisa Schneckenreiter et.al.|[2403.04747](http://arxiv.org/abs/2403.04747)|**[link](https://github.com/ml-jku/gnn-vpa)**|
|**2024-03-07**|**Entropy Aware Message Passing in Graph Neural Networks**|Philipp Nazari et.al.|[2403.04636](http://arxiv.org/abs/2403.04636)|**[link](https://github.com/oliver-lemke/entropy_aware_message_passing)**|
|**2024-03-08**|**In-n-Out: Calibrating Graph Neural Networks for Link Prediction**|Erik Nascimento et.al.|[2403.04605](http://arxiv.org/abs/2403.04605)|null|
|**2024-03-07**|**Uncertainty-Aware Relational Graph Neural Network for Few-Shot Knowledge Graph Completion**|Qian Li et.al.|[2403.04521](http://arxiv.org/abs/2403.04521)|null|
|**2024-03-07**|**Improving Matrix Completion by Exploiting Rating Ordinality in Graph Neural Networks**|Jaehyun Lee et.al.|[2403.04504](http://arxiv.org/abs/2403.04504)|null|
|**2024-03-07**|**On the Topology Awareness and Generalization Performance of Graph Neural Networks**|Junwei Su et.al.|[2403.04482](http://arxiv.org/abs/2403.04482)|null|
|**2024-03-07**|**A Survey of Graph Neural Networks in Real world: Imbalance, Noise, Privacy and OOD Challenges**|Wei Ju et.al.|[2403.04468](http://arxiv.org/abs/2403.04468)|null|
|**2024-03-07**|**Performance Assessment of Universal Machine Learning Interatomic Potentials: Challenges and Directions for Materials' Surfaces**|Bruno Focassio et.al.|[2403.04217](http://arxiv.org/abs/2403.04217)|null|
|**2024-03-06**|**Graph neural network outputs are almost surely asymptotically constant**|Sam Adam-Day et.al.|[2403.03880](http://arxiv.org/abs/2403.03880)|**[link](https://github.com/benfinkelshtein/gnn-asymptotically-constant)**|
|**2024-03-06**|**Predicting the Temperature Dependence of Surfactant CMCs Using Graph Neural Networks**|Christoforos Brozos et.al.|[2403.03767](http://arxiv.org/abs/2403.03767)|**[link](https://github.com/brozosc/predicting-the-temperature-dependence-of-surfactant-cmcs-using-graph-neural-networks)**|
|**2024-03-06**|**Intent-aware Recommendation via Disentangled Graph Contrastive Learning**|Yuling Wang et.al.|[2403.03714](http://arxiv.org/abs/2403.03714)|null|
|**2024-03-06**|**Simplified PCNet with Robustness**|Bingheng Li et.al.|[2403.03676](http://arxiv.org/abs/2403.03676)|null|
|**2024-03-06**|**Provable Filter for Real-world Graph Clustering**|Xuanting Xie et.al.|[2403.03666](http://arxiv.org/abs/2403.03666)|null|
|**2024-03-06**|**K-Link: Knowledge-Link Graph from LLMs for Enhanced Representation Learning in Multivariate Time-Series Data**|Yucheng Wang et.al.|[2403.03645](http://arxiv.org/abs/2403.03645)|null|
|**2024-03-06**|**Learning Invariant Representations of Graph Neural Networks via Cluster Generalization**|Donglin Xia et.al.|[2403.03599](http://arxiv.org/abs/2403.03599)|**[link](https://github.com/bupt-gamma/citgnn)**|
|**2024-03-06**|**LDSF: Lightweight Dual-Stream Framework for SAR Target Recognition by Coupling Local Electromagnetic Scattering Features and Global Visual Features**|Xuying Xiong et.al.|[2403.03527](http://arxiv.org/abs/2403.03527)|null|
|**2024-03-06**|**IB-Net: Initial Branch Network for Variable Decision in Boolean Satisfiability**|Tsz Ho Chan et.al.|[2403.03517](http://arxiv.org/abs/2403.03517)|null|
|**2024-03-06**|**A Teacher-Free Graph Knowledge Distillation Framework with Dual Self-Distillation**|Lirong Wu et.al.|[2403.03483](http://arxiv.org/abs/2403.03483)|**[link](https://github.com/lirongwu/tgs)**|
|**2024-03-05**|**Semi-Supervised Graph Representation Learning with Human-centric Explanation for Predicting Fatty Liver Disease**|So Yeon Kim et.al.|[2403.02786](http://arxiv.org/abs/2403.02786)|null|
|**2024-03-05**|**Minimum Topology Attacks for Graph Neural Networks**|Mengmei Zhang et.al.|[2403.02723](http://arxiv.org/abs/2403.02723)|null|
|**2024-03-04**|**MPI Errors Detection using GNN Embedding and Vector Embedding over LLVM IR**|Jad El Karchi et.al.|[2403.02518](http://arxiv.org/abs/2403.02518)|null|
|**2024-03-04**|**Better Schedules for Low Precision Training of Deep Neural Networks**|Cameron R. Wolfe et.al.|[2403.02243](http://arxiv.org/abs/2403.02243)|null|
|**2024-03-04**|**Mitigating Label Noise on Graph via Topological Sample Selection**|Yuhao Wu et.al.|[2403.01942](http://arxiv.org/abs/2403.01942)|**[link](https://github.com/wu-yu-hao/2024_icml_tss)**|
|**2024-03-04**|**MaliGNNoma: GNN-Based Malicious Circuit Classifier for Secure Cloud FPGAs**|Lilas Alrahis et.al.|[2403.01860](http://arxiv.org/abs/2403.01860)|null|
|**2024-03-04**|**Graph neural network for in-network placement of real-time metaverse tasks in next-generation network**|Sulaiman Muhammad Rashid et.al.|[2403.01780](http://arxiv.org/abs/2403.01780)|null|
|**2024-03-03**|**Applying Self-supervised Learning to Network Intrusion Detection for Network Flows with Graph Neural Network**|Renjie Xu et.al.|[2403.01501](http://arxiv.org/abs/2403.01501)|**[link](https://github.com/renj-xu/negsc)**|
|**2024-03-03**|**Representation Learning on Heterophilic Graph with Directional Neighborhood Attention**|Qincheng Lu et.al.|[2403.01475](http://arxiv.org/abs/2403.01475)|null|
|**2024-03-02**|**Less is More: Hop-Wise Graph Attention for Scalable and Generalizable Learning on Circuits**|Chenhui Deng et.al.|[2403.01317](http://arxiv.org/abs/2403.01317)|**[link](https://github.com/cornell-zhang/hoga)**|
|**2024-03-02**|**Polynormer: Polynomial-Expressive Graph Transformer in Linear Time**|Chenhui Deng et.al.|[2403.01232](http://arxiv.org/abs/2403.01232)|**[link](https://github.com/cornell-zhang/polynormer)**|
|**2024-03-02**|**COOL: A Conjoint Perspective on Spatio-Temporal Graph Neural Network for Traffic Forecasting**|Wei Ju et.al.|[2403.01091](http://arxiv.org/abs/2403.01091)|null|
|**2024-03-02**|**Teaching MLP More Graph Information: A Three-stage Multitask Knowledge Distillation Framework**|Junxian Li et.al.|[2403.01079](http://arxiv.org/abs/2403.01079)|null|
|**2024-03-01**|**An Interpretable Ensemble of Graph and Language Models for Improving Search Relevance in E-Commerce**|Nurendra Choudhary et.al.|[2403.00923](http://arxiv.org/abs/2403.00923)|null|
|**2024-03-01**|**PowerFlowMultiNet: Multigraph Neural Networks for Unbalanced Three-Phase Distribution Systems**|Salah Ghamizi et.al.|[2403.00892](http://arxiv.org/abs/2403.00892)|null|
|**2024-03-01**|**Subhomogeneous Deep Equilibrium Models**|Pietro Sittoni et.al.|[2403.00720](http://arxiv.org/abs/2403.00720)|**[link](https://github.com/COMPiLELab/SubDEQ)**|
|**2024-03-04**|**Toward Autonomous Cooperation in Heterogeneous Nanosatellite Constellations Using Dynamic Graph Neural Networks**|Guillem Casadesus-Vila et.al.|[2403.00692](http://arxiv.org/abs/2403.00692)|null|
|**2024-03-01**|**Graph Theory and GNNs to Unravel the Topographical Organization of Brain Lesions in Variants of Alzheimer's Disease Progression**|Leopold Hebert-Stevens et.al.|[2403.00636](http://arxiv.org/abs/2403.00636)|null|
|**2024-03-01**|**A Survey of Geometric Graph Neural Networks: Data Structures, Models and Applications**|Jiaqi Han et.al.|[2403.00485](http://arxiv.org/abs/2403.00485)|null|
|**2024-02-29**|**Arrow Matrix Decomposition: A Novel Approach for Communication-Efficient Sparse Matrix Multiplication**|Lukas Gianinazzi et.al.|[2402.19364](http://arxiv.org/abs/2402.19364)|**[link](https://github.com/spcl/arrow-matrix)**|
|**2024-02-29**|**DiffAssemble: A Unified Graph-Diffusion Model for 2D and 3D Reassembly**|Gianluca Scarpellini et.al.|[2402.19302](http://arxiv.org/abs/2402.19302)|**[link](https://github.com/iit-pavis/diffassemble)**|
|**2024-02-29**|**Machine learning-enabled exploration of mesoscale architectures in amphiphilic-molecule self-assembly**|Takeo Sudo et.al.|[2402.19019](http://arxiv.org/abs/2402.19019)|null|
|**2024-02-29**|**Always be Pre-Training: Representation Learning for Network Intrusion Detection with GNNs**|Zhengyao Gu et.al.|[2402.18986](http://arxiv.org/abs/2402.18986)|null|
|**2024-02-29**|**Benchmarking phonon anharmonicity in machine learning interatomic potentials**|Sasaank Bandi et.al.|[2402.18891](http://arxiv.org/abs/2402.18891)|null|
|**2024-02-29**|**Loss-aware Curriculum Learning for Heterogeneous Graph Neural Networks**|Zhen Hao Wong et.al.|[2402.18875](http://arxiv.org/abs/2402.18875)|**[link](https://github.com/lars-research/clgnn)**|
|**2024-02-28**|**GNSS Positioning using Cost Function Regulated Multilateration and Graph Neural Networks**|Amir Jalalirad et.al.|[2402.18630](http://arxiv.org/abs/2402.18630)|null|
|**2024-02-28**|**HemaGraph: Breaking Barriers in Hematologic Single Cell Classification with Graph Attention**|Lorenzo Bini et.al.|[2402.18611](http://arxiv.org/abs/2402.18611)|**[link](https://github.com/LorenzoBini4/GNN-HemaGraph)**|
|**2024-02-28**|**Universal neural network potentials as descriptors: Towards scalable chemical property prediction using quantum and classical computers**|Tomoya Shiota et.al.|[2402.18433](http://arxiv.org/abs/2402.18433)|null|
|**2024-02-28**|**CafkNet: GNN-Empowered Forward Kinematic Modeling for Cable-Driven Parallel Robots**|Zeqing Zhang et.al.|[2402.18420](http://arxiv.org/abs/2402.18420)|null|
|**2024-02-28**|**Recursive GNNs for Learning Precoding Policies with Size-Generalizability**|Jia Guo et.al.|[2402.18332](http://arxiv.org/abs/2402.18332)|null|
|**2024-02-28**|**Reinforcement Learning and Graph Neural Networks for Probabilistic Risk Assessment**|Joachim Grimstad et.al.|[2402.18246](http://arxiv.org/abs/2402.18246)|null|
|**2024-02-28**|**Challenges in Pre-Training Graph Neural Networks for Context-Based Fake News Detection: An Evaluation of Current Strategies and Resource Limitations**|Gregor Donabauer et.al.|[2402.18179](http://arxiv.org/abs/2402.18179)|**[link](https://github.com/dogregor/pretrain_gnns_fakenewsnet)**|
|**2024-02-27**|**Using Graph Neural Networks to Predict Local Culture**|Thiago H Silva et.al.|[2402.17905](http://arxiv.org/abs/2402.17905)|null|
|**2024-02-27**|**Graph Neural Networks and Arithmetic Circuits**|Timon Barlag et.al.|[2402.17805](http://arxiv.org/abs/2402.17805)|null|
|**2024-02-27**|**Predicting Instability in Complex Oscillator Networks: Limitations and Potentials of Network Measures and Machine Learning**|Christian Nauck et.al.|[2402.17500](http://arxiv.org/abs/2402.17500)|**[link](https://github.com/pik-icone/networkscienceml_paper-companion)**|
|**2024-02-27**|**Fraud Detection with Binding Global and Local Relational Interaction**|Haolin Li et.al.|[2402.17472](http://arxiv.org/abs/2402.17472)|**[link](https://github.com/tdlhl/RAGFormer)**|
|**2024-02-27**|**A case study of sending graph neural networks back to the test bench for applications in high-energy particle physics**|Emanuel Pfeffer et.al.|[2402.17386](http://arxiv.org/abs/2402.17386)|null|
|**2024-02-27**|**A new graph-neural-network flavor tagger for Belle II and measurement of $\sin2φ_1$ in $B^0 \to J/ψK^0_\text{S}$ decays**|Belle II Collaboration et.al.|[2402.17260](http://arxiv.org/abs/2402.17260)|null|
|**2024-02-27**|**Prediction of the SYM-H Index Using a Bayesian Deep Learning Method with Uncertainty Quantification**|Yasser Abduallah et.al.|[2402.17196](http://arxiv.org/abs/2402.17196)|null|
|**2024-02-26**|**One-Shot Graph Representation Learning Using Hyperdimensional Computing**|Abhishek Dalvi et.al.|[2402.17073](http://arxiv.org/abs/2402.17073)|null|
|**2024-02-26**|**Minimize Control Inputs for Strong Structural Controllability Using Reinforcement Learning with Graph Neural Network**|Mengbang Zou et.al.|[2402.16925](http://arxiv.org/abs/2402.16925)|null|
|**2024-02-26**|**Accelerating Graph Neural Networks on Real Processing-In-Memory Systems**|Christina Giannoula et.al.|[2402.16731](http://arxiv.org/abs/2402.16731)|**[link](https://github.com/cmu-safari/pygim)**|
|**2024-02-26**|**Two-stage Generative Question Answering on Temporal Knowledge Graph Using Large Language Models**|Yifu Gao et.al.|[2402.16568](http://arxiv.org/abs/2402.16568)|null|
|**2024-02-26**|**Integrating Large Language Models with Graphical Session-Based Recommendation**|Naicheng Guo et.al.|[2402.16539](http://arxiv.org/abs/2402.16539)|null|
|**2024-02-26**|**Graph Learning with Distributional Edge Layouts**|Xinjian Zhao et.al.|[2402.16402](http://arxiv.org/abs/2402.16402)|null|
|**2024-02-26**|**Boosting Graph Pooling with Persistent Homology**|Chaolong Ying et.al.|[2402.16346](http://arxiv.org/abs/2402.16346)|**[link](https://github.com/LOGO-CUHKSZ/TIP)**|
|**2024-02-26**|**High-Frequency-aware Hierarchical Contrastive Selective Coding for Representation Learning on Text-attributed Graphs**|Peiyan Zhang et.al.|[2402.16240](http://arxiv.org/abs/2402.16240)|null|
|**2024-02-25**|**HiGPT: Heterogeneous Graph Language Model**|Jiabin Tang et.al.|[2402.16024](http://arxiv.org/abs/2402.16024)|**[link](https://github.com/hkuds/higpt)**|
|**2024-02-24**|**Pretraining Strategy for Neural Potentials**|Zehua Zhang et.al.|[2402.15921](http://arxiv.org/abs/2402.15921)|**[link](https://github.com/stevenzhang904/masked_pretrain)**|
|**2024-02-23**|**Dual Encoder: Exploiting the Potential of Syntactic and Semantic for Aspect Sentiment Triplet Extraction**|Xiaowei Zhao et.al.|[2402.15370](http://arxiv.org/abs/2402.15370)|null|
|**2024-02-23**|**Understanding Oversmoothing in Diffusion-Based GNNs From the Perspective of Operator Semigroup Theory**|Weichen Zhao et.al.|[2402.15326](http://arxiv.org/abs/2402.15326)|null|
|**2024-02-23**|**Open Ad Hoc Teamwork with Cooperative Game Theory**|Jianhong Wang et.al.|[2402.15259](http://arxiv.org/abs/2402.15259)|**[link](https://github.com/hsvgbkhgbv/ciao)**|
|**2024-02-23**|**GraphEdit: Large Language Models for Graph Structure Learning**|Zirui Guo et.al.|[2402.15183](http://arxiv.org/abs/2402.15183)|**[link](https://github.com/hkuds/graphedit)**|
|**2024-02-23**|**MSPipe: Efficient Temporal GNN Training via Staleness-aware Pipeline**|Guangming Sheng et.al.|[2402.15113](http://arxiv.org/abs/2402.15113)|**[link](https://github.com/petersh6/mspipe)**|
|**2024-02-23**|**Sampling-based Distributed Training with Message Passing Neural Network**|Priyesh Kakka et.al.|[2402.15106](http://arxiv.org/abs/2402.15106)|null|
|**2024-02-22**|**Path Planning based on 2D Object Bounding-box**|Yanliang Huang et.al.|[2402.14933](http://arxiv.org/abs/2402.14933)|null|
|**2024-02-22**|**Link Prediction under Heterophily: A Physics-Inspired Graph Neural Network Approach**|Andrea Giuseppe Di Francesco et.al.|[2402.14802](http://arxiv.org/abs/2402.14802)|null|
|**2024-02-22**|**CaT-GNN: Enhancing Credit Card Fraud Detection via Causal Temporal Graph Neural Networks**|Yifan Duan et.al.|[2402.14708](http://arxiv.org/abs/2402.14708)|null|
|**2024-02-22**|**Representation Learning for Frequent Subgraph Mining**|Rex Ying et.al.|[2402.14367](http://arxiv.org/abs/2402.14367)|null|
|**2024-02-22**|**Velocity recostruction with graph neural networks**|Hideki Tanimura et.al.|[2402.14239](http://arxiv.org/abs/2402.14239)|null|
|**2024-02-21**|**A Simple and Yet Fairly Effective Defense for Graph Neural Networks**|Sofiane Ennadir et.al.|[2402.13987](http://arxiv.org/abs/2402.13987)|**[link](https://github.com/sennadir/noisygnn)**|
|**2024-02-21**|**Linear-Time Graph Neural Networks for Scalable Recommendations**|Jiahao Zhang et.al.|[2402.13973](http://arxiv.org/abs/2402.13973)|**[link](https://github.com/qwq2000/thewebconf24-ltgnn-pytorch)**|
|**2024-02-21**|**AttackGNN: Red-Teaming GNNs in Hardware Security Using Reinforcement Learning**|Vasudev Gohil et.al.|[2402.13946](http://arxiv.org/abs/2402.13946)|null|
|**2024-02-21**|**Verifying message-passing neural networks via topology-based bounds tightening**|Christopher Hojny et.al.|[2402.13937](http://arxiv.org/abs/2402.13937)|**[link](https://github.com/christopherhojny/SCIP-MPNN)**|
|**2024-02-21**|**General Debiasing for Graph-based Collaborative Filtering via Adversarial Graph Dropout**|An Zhang et.al.|[2402.13769](http://arxiv.org/abs/2402.13769)|**[link](https://github.com/arthurma71/advdrop)**|
|**2024-02-21**|**Reasoning Algorithmically in Graph Neural Networks**|Danilo Numeroso et.al.|[2402.13744](http://arxiv.org/abs/2402.13744)|null|
|**2024-02-21**|**UniGraph: Learning a Cross-Domain Graph Foundation Model From Natural Language**|Yufei He et.al.|[2402.13630](http://arxiv.org/abs/2402.13630)|**[link](https://github.com/yf-he/UniGraph)**|
|**2024-02-21**|**Near-Field Multiuser Beam-Training for Extremely Large-Scale MIMO Systems**|Wang Liu et.al.|[2402.13597](http://arxiv.org/abs/2402.13597)|null|
|**2024-02-21**|**Inductive Graph Alignment Prompt: Bridging the Gap between Graph Pre-training and Inductive Fine-tuning From Spectral Perspective**|Yuchen Yan et.al.|[2402.13556](http://arxiv.org/abs/2402.13556)|null|
|**2024-02-21**|**Balancing Spectral, Temporal and Spatial Information for EEG-based Alzheimer's Disease Classification**|Stephan Goerttler et.al.|[2402.13523](http://arxiv.org/abs/2402.13523)|null|
|**2024-02-20**|**BuffGraph: Enhancing Class-Imbalanced Node Classification via Buffer Nodes**|Qian Wang et.al.|[2402.13114](http://arxiv.org/abs/2402.13114)|null|
|**2024-02-20**|**A Microstructure-based Graph Neural Network for Accelerating Multiscale Simulations**|J. Storm et.al.|[2402.13101](http://arxiv.org/abs/2402.13101)|**[link](https://github.com/joepstorm/microscale-gnn-surrogate)**|
|**2024-02-20**|**Enhancing Real-World Complex Network Representations with Hyperedge Augmentation**|Xiangyu Zhao et.al.|[2402.13033](http://arxiv.org/abs/2402.13033)|**[link](https://github.com/victorzxy/topoaug)**|
|**2024-02-20**|**Heterogeneous Graph Reasoning for Fact Checking over Texts and Tables**|Haisong Gong et.al.|[2402.13028](http://arxiv.org/abs/2402.13028)|**[link](https://github.com/deno-v/heterfc)**|
|**2024-02-20**|**A unifying primary framework for quantum graph neural networks from quantum graph states**|Ammar Daskin et.al.|[2402.13001](http://arxiv.org/abs/2402.13001)|null|
|**2024-02-20**|**Distributionally Robust Graph-based Recommendation System**|Bohao Wang et.al.|[2402.12994](http://arxiv.org/abs/2402.12994)|**[link](https://github.com/WANGBohaO-jpg/DR-GNN)**|
|**2024-02-20**|**Can GNN be Good Adapter for LLMs?**|Xuanwen Huang et.al.|[2402.12984](http://arxiv.org/abs/2402.12984)|**[link](https://github.com/hxttkl/GraphAdapter)**|
|**2024-02-20**|**Cell Graph Transformer for Nuclei Classification**|Wei Lou et.al.|[2402.12946](http://arxiv.org/abs/2402.12946)|**[link](https://github.com/lhaof/cgt)**|
|**2024-02-20**|**GRAPHGINI: Fostering Individual and Group Fairness in Graph Neural Networks**|Anuj Kumar Sirohi et.al.|[2402.12937](http://arxiv.org/abs/2402.12937)|null|
|**2024-02-20**|**Studies on $R_K$ with Large Dilepton Invariant-Mass, Scalable Pythonic Fitting, and Online Event Interpretation with GNNs at LHCb**|Jonas Eschle et.al.|[2402.12622](http://arxiv.org/abs/2402.12622)|null|
|**2024-02-19**|**LLM as Prompter: Low-resource Inductive Reasoning on Arbitrary Knowledge Graphs**|Kai Wang et.al.|[2402.11804](http://arxiv.org/abs/2402.11804)|**[link](https://github.com/kynewang/prolink)**|
|**2024-02-18**|**GNNavi: Navigating the Information Flow in Large Language Models by Graph Neural Network**|Shuzhou Yuan et.al.|[2402.11709](http://arxiv.org/abs/2402.11709)|**[link](https://github.com/shuzhouyuan/gnnavi)**|
|**2024-02-18**|**Large Language Model-driven Meta-structure Discovery in Heterogeneous Information Network**|Lin Chen et.al.|[2402.11518](http://arxiv.org/abs/2402.11518)|**[link](https://github.com/linchen-65/restruct)**|
|**2024-02-18**|**Graph Out-of-Distribution Generalization via Causal Intervention**|Qitian Wu et.al.|[2402.11494](http://arxiv.org/abs/2402.11494)|**[link](https://github.com/fannie1208/canet)**|
|**2024-02-18**|**DDIPrompt: Drug-Drug Interaction Event Prediction based on Graph Prompt Learning**|Yingying Wang et.al.|[2402.11472](http://arxiv.org/abs/2402.11472)|null|
|**2024-02-17**|**Graph Neural Networks for Predicting Solubility in Diverse Solvents using MolMerger incorporating Solute-solvent Interactions**|Vansh Ramani et.al.|[2402.11340](http://arxiv.org/abs/2402.11340)|null|
|**2024-02-17**|**LiGNN: Graph Neural Networks at LinkedIn**|Fedor Borisyuk et.al.|[2402.11139](http://arxiv.org/abs/2402.11139)|null|
|**2024-02-16**|**ASGEA: Exploiting Logic Rules from Align-Subgraphs for Entity Alignment**|Yangyifei Luo et.al.|[2402.11000](http://arxiv.org/abs/2402.11000)|**[link](https://github.com/zjukg/MEAformer)**|
|**2024-02-16**|**Masked Attention is All You Need for Graphs**|David Buterez et.al.|[2402.10793](http://arxiv.org/abs/2402.10793)|null|
|**2024-02-16**|**Unlink to Unlearn: Simplifying Edge Unlearning in GNNs**|Jiajun Tan et.al.|[2402.10695](http://arxiv.org/abs/2402.10695)|**[link](https://github.com/sumsky21/unlink-to-unlearn)**|
|**2024-02-16**|**Graph-based Forecasting with Missing Data through Spatiotemporal Downsampling**|Ivan Marisca et.al.|[2402.10634](http://arxiv.org/abs/2402.10634)|**[link](https://github.com/marshka/hdtts)**|
|**2024-02-16**|**Subgraph-level Universal Prompt Tuning**|Junhyun Lee et.al.|[2402.10380](http://arxiv.org/abs/2402.10380)|null|
|**2024-02-15**|**Deep Spectral Meshes: Multi-Frequency Facial Mesh Processing with Graph Neural Networks**|Robert Kosk et.al.|[2402.10365](http://arxiv.org/abs/2402.10365)|null|
|**2024-02-15**|**Can we soft prompt LLMs for graph learning tasks?**|Zheyuan Liu et.al.|[2402.10359](http://arxiv.org/abs/2402.10359)|null|
|**2024-02-15**|**Ising on the Graph: Task-specific Graph Subsampling via the Ising Model**|Maria Bånkestad et.al.|[2402.10206](http://arxiv.org/abs/2402.10206)|null|
|**2024-02-15**|**Reconstruction of Short-Lived Particles using Graph-Hypergraph Representation Learning**|Callum Birch-Sykes et.al.|[2402.10149](http://arxiv.org/abs/2402.10149)|null|
|**2024-02-15**|**GraphCBAL: Class-Balanced Active Learning for Graph Neural Networks via Reinforcement Learning**|Chengcheng Yu et.al.|[2402.10074](http://arxiv.org/abs/2402.10074)|null|
|**2024-02-15**|**Approximate Message Passing-Enhanced Graph Neural Network for OTFS Data Detection**|Wenhao Zhuang et.al.|[2402.10071](http://arxiv.org/abs/2402.10071)|null|
|**2024-02-15**|**Clifford Group Equivariant Simplicial Message Passing Networks**|Cong Liu et.al.|[2402.10011](http://arxiv.org/abs/2402.10011)|**[link](https://github.com/congliuuva/clifford-group-equivariant-simplicial-message-passing-networks)**|
|**2024-02-15**|**ViGEO: an Assessment of Vision GNNs in Earth Observation**|Luca Colomba et.al.|[2402.09962](http://arxiv.org/abs/2402.09962)|**[link](https://github.com/lccol/vig-eo)**|
|**2024-02-15**|**Node Duplication Improves Cold-start Link Prediction**|Zhichun Guo et.al.|[2402.09711](http://arxiv.org/abs/2402.09711)|**[link](https://github.com/snap-research/nodedup)**|
|**2024-02-15**|**Graph Neural Network-based Tracking as a Service**|Haoran Zhao et.al.|[2402.09633](http://arxiv.org/abs/2402.09633)|null|
|**2024-02-14**|**LLM-Enhanced User-Item Interactions: Leveraging Edge Information for Optimized Recommendations**|Xinyuan Wang et.al.|[2402.09617](http://arxiv.org/abs/2402.09617)|**[link](https://github.com/anord-wang/llm4rec)**|
|**2024-02-14**|**Low-Rank Graph Contrastive Learning for Node Classification**|Yancheng Wang et.al.|[2402.09600](http://arxiv.org/abs/2402.09600)|null|
|**2024-02-14**|**Safe Distributed Control of Multi-Robot Systems with Communication Delays**|Luca Ballotta et.al.|[2402.09382](http://arxiv.org/abs/2402.09382)|null|
|**2024-02-14**|**GraSSRep: Graph-Based Self-Supervised Learning for Repeat Detection in Metagenomic Assembly**|Ali Azizpour et.al.|[2402.09381](http://arxiv.org/abs/2402.09381)|**[link](https://github.com/aliaaz99/grassrep)**|
|**2024-02-14**|**Uncertainty-Aware Transient Stability-Constrained Preventive Redispatch: A Distributional Reinforcement Learning Approach**|Zhengcheng Wang et.al.|[2402.09263](http://arxiv.org/abs/2402.09263)|null|
|**2024-02-14**|**Robust Training of Temporal GNNs using Nearest Neighbours based Hard Negatives**|Shubham Gupta et.al.|[2402.09239](http://arxiv.org/abs/2402.09239)|null|
|**2024-02-14**|**DisGNet: A Distance Graph Neural Network for Forward Kinematics Learning of Gough-Stewart Platform**|Huizhi Zhu et.al.|[2402.09077](http://arxiv.org/abs/2402.09077)|**[link](https://github.com/flamezz5201/disgnet)**|
|**2024-02-14**|**Graph Inference Acceleration by Learning MLPs on Graphs without Supervision**|Zehong Wang et.al.|[2402.08918](http://arxiv.org/abs/2402.08918)|**[link](https://github.com/zehong-wang/simmlp)**|
|**2024-02-14**|**Multiscale graph neural networks with adaptive mesh refinement for accelerating mesh-based simulations**|Roberto Perera et.al.|[2402.08863](http://arxiv.org/abs/2402.08863)|null|
|**2024-02-13**|**Disambiguated Node Classification with Graph Neural Networks**|Tianxiang Zhao et.al.|[2402.08824](http://arxiv.org/abs/2402.08824)|**[link](https://github.com/tianxiangzhao/disambiguatedgnn)**|
|**2024-02-13**|**Graph Mamba: Towards Learning on Graphs with State Space Models**|Ali Behrouz et.al.|[2402.08678](http://arxiv.org/abs/2402.08678)|**[link](https://github.com/graphmamba/gmn)**|
|**2024-02-13**|**SAGMAN: Stability Analysis of Graph Neural Networks on the Manifolds**|Wuxinlin Cheng et.al.|[2402.08653](http://arxiv.org/abs/2402.08653)|null|
|**2024-02-13**|**Homomorphism Counts for Graph Neural Networks: All About That Basis**|Emily Jin et.al.|[2402.08595](http://arxiv.org/abs/2402.08595)|**[link](https://github.com/icml2024357/hombasis-gnn)**|
|**2024-02-13**|**Graph Feature Preprocessor: Real-time Extraction of Subgraph-based Features from Transaction Graphs**|Jovan Blanuša et.al.|[2402.08593](http://arxiv.org/abs/2402.08593)|null|
|**2024-02-13**|**Mixture of Link Predictors**|Li Ma et.al.|[2402.08583](http://arxiv.org/abs/2402.08583)|**[link](https://github.com/ml-ml/link-moe)**|
|**2024-02-13**|**Revealing Decurve Flows for Generalized Graph Propagation**|Chen Lin et.al.|[2402.08480](http://arxiv.org/abs/2402.08480)|null|
|**2024-02-13**|**Parallel-friendly Spatio-Temporal Graph Learning for Photovoltaic Degradation Analysis at Scale**|Yangxin Fan et.al.|[2402.08470](http://arxiv.org/abs/2402.08470)|**[link](https://github.com/yangxin666/st-gtrend)**|
|**2024-02-13**|**Subgraphormer: Unifying Subgraph GNNs and Graph Transformers via Graph Products**|Guy Bar-Shalom et.al.|[2402.08450](http://arxiv.org/abs/2402.08450)|**[link](https://github.com/barsguy/subgraphormer)**|
|**2024-02-13**|**LOSS-GAT: Label Propagation and One-Class Semi-Supervised Graph Attention Network for Fake News Detection**|Batool Lakzaei et.al.|[2402.08401](http://arxiv.org/abs/2402.08401)|null|
|**2024-02-13**|**NeuRes: Learning Proofs of Propositional Satisfiability**|Mohamed Ghanem et.al.|[2402.08365](http://arxiv.org/abs/2402.08365)|**[link](https://github.com/oschart/neures)**|
|**2024-02-12**|**An Investigation into Using Unsupervised Metrics to Optimise GNNs for Node Clustering**|William Leeney et.al.|[2402.07845](http://arxiv.org/abs/2402.07845)|null|
|**2024-02-12**|**Extensible Multi-Granularity Fusion Network for Aspect-based Sentiment Analysis**|Xiaowei Zhao et.al.|[2402.07787](http://arxiv.org/abs/2402.07787)|**[link](https://github.com/TYZY89/EMGF)**|
|**2024-02-12**|**G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering**|Xiaoxin He et.al.|[2402.07630](http://arxiv.org/abs/2402.07630)|**[link](https://github.com/xiaoxinhe/g-retriever)**|
|**2024-02-12**|**Weisfeiler-Leman at the margin: When more expressivity matters**|Billy J. Franks et.al.|[2402.07568](http://arxiv.org/abs/2402.07568)|null|
|**2024-02-12**|**Random Geometric Graph Alignment with Graph Neural Networks**|Suqi Liu et.al.|[2402.07340](http://arxiv.org/abs/2402.07340)|null|
|**2024-02-11**|**Highly Accurate Disease Diagnosis and Highly Reproducible Biomarker Identification with PathFormer**|Zehao Dong et.al.|[2402.07268](http://arxiv.org/abs/2402.07268)|null|
|**2024-02-11**|**Large-Language-Model Empowered Dose Volume Histogram Prediction for Intensity Modulated Radiotherapy**|Zehao Dong et.al.|[2402.07167](http://arxiv.org/abs/2402.07167)|null|
|**2024-02-11**|**Explainable Global Wildfire Prediction Models using Graph Neural Networks**|Dayou Chen et.al.|[2402.07152](http://arxiv.org/abs/2402.07152)|**[link](https://github.com/dl-wg/gcn-lstm-wildfire)**|
|**2024-02-11**|**Rethinking the Capacity of Graph Neural Networks for Branching Strategy**|Ziang Chen et.al.|[2402.07099](http://arxiv.org/abs/2402.07099)|null|
|**2024-02-10**|**Generalization Error of Graph Neural Networks in the Mean-field Regime**|Gholamali Aminian et.al.|[2402.07025](http://arxiv.org/abs/2402.07025)|**[link](https://github.com/sherylhyx/gnn_mf_ge)**|
|**2024-02-09**|**Deceptive Path Planning via Reinforcement Learning with Graph Neural Networks**|Michael Y. Fatemi et.al.|[2402.06552](http://arxiv.org/abs/2402.06552)|**[link](https://github.com/myfatemi04/rl-deceptive-graph-planning)**|
|**2024-02-09**|**The Deep Equilibrium Algorithmic Reasoner**|Dobrik Georgiev et.al.|[2402.06445](http://arxiv.org/abs/2402.06445)|null|
|**2024-02-09**|**Neural SPH: Improved Neural Modeling of Lagrangian Fluid Dynamics**|Artur P. Toshev et.al.|[2402.06275](http://arxiv.org/abs/2402.06275)|**[link](https://github.com/tumaer/neuralsph)**|
|**2024-02-09**|**N-1 Reduced Optimal Power Flow Using Augmented Hierarchical Graph Neural Network**|Thuan Pham et.al.|[2402.06226](http://arxiv.org/abs/2402.06226)|null|
|**2024-02-09**|**Rethinking Node-wise Propagation for Large-scale Graph Learning**|Xunkai Li et.al.|[2402.06128](http://arxiv.org/abs/2402.06128)|**[link](https://github.com/xkli-allen/atp)**|
|**2024-02-08**|**Deep Learning for Data-Driven Districting-and-Routing**|Arthur Ferraz et.al.|[2402.06040](http://arxiv.org/abs/2402.06040)|**[link](https://github.com/vidalt/districting-routing)**|
|**2024-02-08**|**Game-theoretic Counterfactual Explanation for Graph Neural Networks**|Chirag Chhablani et.al.|[2402.06030](http://arxiv.org/abs/2402.06030)|null|
|**2024-02-08**|**Classifying Nodes in Graphs without GNNs**|Daniel Winter et.al.|[2402.05934](http://arxiv.org/abs/2402.05934)|**[link](https://github.com/dani3lwinter/cohop)**|
|**2024-02-09**|**Large Language Model Meets Graph Neural Network in Knowledge Distillation**|Shengxiang Hu et.al.|[2402.05894](http://arxiv.org/abs/2402.05894)|null|
|**2024-02-08**|**Rethinking Propagation for Unsupervised Graph Domain Adaptation**|Meihan Liu et.al.|[2402.05660](http://arxiv.org/abs/2402.05660)|**[link](https://github.com/meihan-liu/24aaai-a2gnn)**|
|**2024-02-08**|**Hypergraph Node Classification With Graph Neural Networks**|Bohan Tang et.al.|[2402.05569](http://arxiv.org/abs/2402.05569)|null|
|**2024-02-08**|**TASER: Temporal Adaptive Sampling for Fast and Accurate Dynamic Graph Representation Learning**|Gangda Deng et.al.|[2402.05396](http://arxiv.org/abs/2402.05396)|**[link](https://github.com/facebookresearch/taser-tgnn)**|
|**2024-02-08**|**Graph Neural Networks for Physical-Layer Security in Multi-User Flexible-Duplex Networks**|Tharaka Perera et.al.|[2402.05378](http://arxiv.org/abs/2402.05378)|null|
|**2024-02-07**|**Graph Neural Networks as Fast and High-fidelity Emulators for Finite-Element Ice Sheet Modeling**|Maryam Rahnemoonfar et.al.|[2402.05291](http://arxiv.org/abs/2402.05291)|null|
|**2024-02-07**|**PAC Learnability under Explanation-Preserving Graph Perturbations**|Xu Zheng et.al.|[2402.05039](http://arxiv.org/abs/2402.05039)|null|
|**2024-02-07**|**Navigating Complexity: Toward Lossless Graph Condensation via Expanding Window Matching**|Yuchen Zhang et.al.|[2402.05011](http://arxiv.org/abs/2402.05011)|**[link](https://github.com/nus-hpc-ai-lab/geom)**|
|**2024-02-07**|**Moco: A Learnable Meta Optimizer for Combinatorial Optimization**|Tim Dernedde et.al.|[2402.04915](http://arxiv.org/abs/2402.04915)|**[link](https://github.com/timd3/moco)**|
|**2024-02-07**|**E(3)-Equivariant Mesh Neural Networks**|Thuan Trang et.al.|[2402.04821](http://arxiv.org/abs/2402.04821)|**[link](https://github.com/hysonlab/equimesh)**|
|**2024-02-07**|**Incorporating Retrieval-based Causal Learning with Information Bottlenecks for Interpretable Graph Neural Networks**|Jiahua Rao et.al.|[2402.04710](http://arxiv.org/abs/2402.04710)|null|
|**2024-02-07**|**Feature Distribution on Graph Topology Mediates the Effect of Graph Convolution: Homophily Perspective**|Soo Yong Lee et.al.|[2402.04621](http://arxiv.org/abs/2402.04621)|null|
|**2024-02-06**|**PreGIP: Watermarking the Pretraining of Graph Neural Networks for Deep Intellectual Property Protection**|Enyan Dai et.al.|[2402.04435](http://arxiv.org/abs/2402.04435)|null|
|**2024-02-06**|**LIPSTICK: Corruptibility-Aware and Explainable Graph Neural Network-based Oracle-Less Attack on Logic Locking**|Yeganeh Aghamohammadi et.al.|[2402.04235](http://arxiv.org/abs/2402.04235)|null|
|**2024-02-06**|**Link Prediction with Relational Hypergraphs**|Xingyue Huang et.al.|[2402.04062](http://arxiv.org/abs/2402.04062)|null|
|**2024-02-06**|**PAC-Bayesian Adversarially Robust Generalization Bounds for Graph Neural Network**|Tan Sun et.al.|[2402.04038](http://arxiv.org/abs/2402.04038)|null|
|**2024-02-06**|**On dimensionality of feature vectors in MPNNs**|César Bravo et.al.|[2402.03966](http://arxiv.org/abs/2402.03966)|null|
|**2024-02-06**|**Masked Graph Autoencoder with Non-discrete Bandwidths**|Ziwen Zhao et.al.|[2402.03814](http://arxiv.org/abs/2402.03814)|**[link](https://github.com/newiz430/bandana)**|
|**2024-02-06**|**Scalable Parallel Algorithm for Graph Neural Network Interatomic Potentials in Molecular Dynamics Simulations**|Yutack Park et.al.|[2402.03789](http://arxiv.org/abs/2402.03789)|**[link](https://github.com/mdil-snu/sevennet)**|
|**2024-02-06**|**ARGO: An Auto-Tuning Runtime System for Scalable GNN Training on Multi-Core Processor**|Yi-Chien Lin et.al.|[2402.03671](http://arxiv.org/abs/2402.03671)|**[link](https://github.com/jasonlin316/argo)**|
|**2024-02-05**|**Path Signatures and Graph Neural Networks for Slow Earthquake Analysis: Better Together?**|Hans Riess et.al.|[2402.03558](http://arxiv.org/abs/2402.03558)|null|
|**2024-02-05**|**Single-GPU GNN Systems: Traps and Pitfalls**|Yidong Gong et.al.|[2402.03548](http://arxiv.org/abs/2402.03548)|null|
|**2024-02-05**|**Physics-Encoded Graph Neural Networks for Deformation Prediction under Contact**|Mahdi Saleh et.al.|[2402.03466](http://arxiv.org/abs/2402.03466)|null|
|**2024-02-05**|**Graph Neural Machine: A New Model for Learning with Tabular Data**|Giannis Nikolentzos et.al.|[2402.02862](http://arxiv.org/abs/2402.02862)|**[link](https://github.com/giannisnik/gnm)**|
|**2024-02-05**|**PowerGraph: A power grid benchmark dataset for graph neural networks**|Anna Varbella et.al.|[2402.02827](http://arxiv.org/abs/2402.02827)|null|
|**2024-02-05**|**Statistical Guarantees for Link Prediction using Graph Neural Networks**|Alan Chung et.al.|[2402.02692](http://arxiv.org/abs/2402.02692)|null|
|**2024-02-05**|**GraphRT: A graph-based deep learning model for predicting the retention time of peptides**|Mark Drvodelic et.al.|[2402.02661](http://arxiv.org/abs/2402.02661)|null|
|**2024-02-04**|**Weisfeiler Leman for Euclidean Equivariant Machine Learning**|Snir Hordan et.al.|[2402.02484](http://arxiv.org/abs/2402.02484)|**[link](https://github.com/intellifinder/welnet)**|
|**2024-02-04**|**Active Learning for Graphs with Noisy Structures**|Hongliang Chi et.al.|[2402.02321](http://arxiv.org/abs/2402.02321)|null|
|**2024-02-03**|**SemPool: Simple, robust, and interpretable KG pooling for enhancing language models**|Costas Mavromatis et.al.|[2402.02289](http://arxiv.org/abs/2402.02289)|null|
|**2024-02-03**|**Future Directions in Foundations of Graph Machine Learning**|Christopher Morris et.al.|[2402.02287](http://arxiv.org/abs/2402.02287)|null|
|**2024-02-03**|**Neural Scaling Laws on Graphs**|Jingzhe Liu et.al.|[2402.02054](http://arxiv.org/abs/2402.02054)|**[link](https://github.com/liu-jingzhe/graph-scaling-laws)**|
|**2024-02-03**|**Interpreting Graph Neural Networks with In-Distributed Proxies**|Zhuomin Chen et.al.|[2402.02036](http://arxiv.org/abs/2402.02036)|**[link](https://github.com/realmoana/proxyexplainer)**|
|**2024-02-02**|**TEDDY: Trimming Edges with Degree-based Discrimination strategY**|Hyunjin Seo et.al.|[2402.01261](http://arxiv.org/abs/2402.01261)|**[link](https://github.com/hyunjin72/teddy)**|
|**2024-02-02**|**Two Heads Are Better Than One: Boosting Graph Sparse Training via Semantic and Topological Awareness**|Guibin Zhang et.al.|[2402.01242](http://arxiv.org/abs/2402.01242)|null|
|**2024-02-02**|**Unveiling Delay Effects in Traffic Forecasting: A Perspective from Spatial-Temporal Delay Differential Equations**|Qingqing Long et.al.|[2402.01231](http://arxiv.org/abs/2402.01231)|null|
|**2024-02-02**|**Graph Neural Networks in EEG-based Emotion Recognition: A Survey**|Chenyu Liu et.al.|[2402.01138](http://arxiv.org/abs/2402.01138)|null|
|**2024-02-02**|**Learning Which Side to Scan: Multi-View Informed Active Perception with Side Scan Sonar for Autonomous Underwater Vehicles**|Advaith V. Sethuraman et.al.|[2402.01106](http://arxiv.org/abs/2402.01106)|null|
|**2024-02-02**|**DoseGNN: Improving the Performance of Deep Learning Models in Adaptive Dose-Volume Histogram Prediction through Graph Neural Networks**|Zehao Dong et.al.|[2402.01076](http://arxiv.org/abs/2402.01076)|null|
|**2024-02-01**|**A Comparative Analysis of Gene Expression Profiling by Statistical and Machine Learning Approaches**|Myriam Bontonou et.al.|[2402.00926](http://arxiv.org/abs/2402.00926)|**[link](https://github.com/mbonto/xai_in_genomics)**|
|**2024-02-01**|**X-CBA: Explainability Aided CatBoosted Anomal-E for Intrusion Detection System**|Kiymet Kaya et.al.|[2402.00839](http://arxiv.org/abs/2402.00839)|**[link](https://github.com/kiymetkaya/xai-catboosted-anomale)**|
|**2024-02-01**|**CPT: Competence-progressive Training Strategy for Few-shot Node Classification**|Qilong Yan et.al.|[2402.00450](http://arxiv.org/abs/2402.00450)|null|
|**2024-02-01**|**A Survey of Data-Efficient Graph Learning**|Wei Ju et.al.|[2402.00447](http://arxiv.org/abs/2402.00447)|null|
|**2024-02-01**|**Attention-based Dynamic Multilayer Graph Neural Networks for Loan Default Prediction**|Sahab Zandi et.al.|[2402.00299](http://arxiv.org/abs/2402.00299)|null|
|**2024-01-31**|**Benchmarking Sensitivity of Continual Graph Learning for Skeleton-Based Action Recognition**|Wei Wei et.al.|[2401.18054](http://arxiv.org/abs/2401.18054)|null|
|**2024-01-31**|**Attention Graph for Multi-Robot Social Navigation with Deep Reinforcement Learning**|Erwan Escudie et.al.|[2401.17914](http://arxiv.org/abs/2401.17914)|null|
|**2024-01-31**|**Graph Transformers without Positional Encodings**|Ayush Garg et.al.|[2401.17791](http://arxiv.org/abs/2401.17791)|null|
|**2024-01-31**|**PF-GNN: Differentiable particle filtering based approximation of universal graph representations**|Mohammed Haroon Dupty et.al.|[2401.17752](http://arxiv.org/abs/2401.17752)|**[link](https://github.com/pfgnn/pf-gnn)**|
|**2024-01-31**|**Towards Personalized Privacy: User-Governed Data Contribution for Federated Recommendation**|Liang Qu et.al.|[2401.17630](http://arxiv.org/abs/2401.17630)|null|
|**2024-01-31**|**IGCN: Integrative Graph Convolutional Networks for Multi-modal Data**|Cagri Ozdemir et.al.|[2401.17612](http://arxiv.org/abs/2401.17612)|**[link](https://github.com/bozdaglab/igcn)**|
|**2024-01-30**|**Timeseries Suppliers Allocation Risk Optimization via Deep Black Litterman Model**|Jiayuan Luo et.al.|[2401.17350](http://arxiv.org/abs/2401.17350)|**[link](https://github.com/wentaozhang2001/dblm)**|
|**2024-01-30**|**Energy-conserving equivariant GNN for elasticity of lattice architected metamaterials**|Ivan Grega et.al.|[2401.16914](http://arxiv.org/abs/2401.16914)|**[link](https://github.com/igrega348/energy-equiv-lattice-gnn)**|
|**2024-01-30**|**Online Algorithm for Node Feature Forecasting in Temporal Graphs**|Aniq Ur Rahman et.al.|[2401.16800](http://arxiv.org/abs/2401.16800)|null|
|**2024-01-30**|**Graph Fairness Learning under Distribution Shifts**|Yibo Li et.al.|[2401.16784](http://arxiv.org/abs/2401.16784)|null|
|**2024-01-29**|**Accelerating superconductor discovery through tempered deep learning of the electron-phonon spectral function**|Jason B. Gibson et.al.|[2401.16611](http://arxiv.org/abs/2401.16611)|**[link](https://github.com/henniggroup/bete-net)**|
|**2024-01-29**|**Towards Accurate Prediction of Configurational Disorder Properties in Materials using Graph Neural Networks**|Zhenyao Fang et.al.|[2401.16565](http://arxiv.org/abs/2401.16565)|**[link](https://github.com/qmatyanlab/configurational-disorder)**|
|**2024-01-29**|**Enhancing Molecular Property Prediction with Auxiliary Learning and Task-Specific Adaptation**|Vishal Dey et.al.|[2401.16299](http://arxiv.org/abs/2401.16299)|**[link](https://github.com/vishaldeyiiest/graphta)**|
|**2024-01-29**|**Graph Neural Networks: Theory for Estimation with Application on Network Heterogeneity**|Yike Wang et.al.|[2401.16275](http://arxiv.org/abs/2401.16275)|null|
|**2024-01-29**|**AnisoGNN: graph neural networks generalizing to anisotropic properties of polycrystals**|Guangyu Hu et.al.|[2401.16271](http://arxiv.org/abs/2401.16271)|**[link](https://github.com/materials-informatics-az/anisognn)**|
|**2024-01-29**|**Graph Neural Network-based Joint Equalization and Decoding**|Jannis Clausius et.al.|[2401.16187](http://arxiv.org/abs/2401.16187)|null|
|**2024-01-29**|**Combined track finding with GNN & CKF**|Lukas Heinrich et.al.|[2401.16016](http://arxiv.org/abs/2401.16016)|null|
|**2024-01-29**|**Spatio-Temporal Attention Graph Neural Network for Remaining Useful Life Prediction**|Zhixin Huang et.al.|[2401.15964](http://arxiv.org/abs/2401.15964)|null|
|**2024-01-29**|**A Gated MLP Architecture for Learning Topological Dependencies in Spatio-Temporal Graphs**|Yun Young Choi et.al.|[2401.15894](http://arxiv.org/abs/2401.15894)|**[link](https://github.com/leemingo/cy2mixer)**|
|**2024-01-28**|**Improving Expressive Power of Spectral Graph Neural Networks with Eigenvalue Correction**|Kangkang Lu et.al.|[2401.15603](http://arxiv.org/abs/2401.15603)|**[link](https://github.com/lukangkang123/ec-gnn)**|
|**2024-01-28**|**DGNN: Decoupled Graph Neural Networks with Structural Consistency between Attribute and Graph Embedding Representations**|Jinlu Wang et.al.|[2401.15584](http://arxiv.org/abs/2401.15584)|**[link](https://github.com/jinluwang1002/dgnn)**|
|**2024-01-28**|**Efficient Tuning and Inference for Large Language Models on Textual Graphs**|Yun Zhu et.al.|[2401.15569](http://arxiv.org/abs/2401.15569)|**[link](https://github.com/ZhuYun97/ENGINE)**|
|**2024-01-26**|**Macro Graph Neural Networks for Online Billion-Scale Recommender Systems**|Hao Chen et.al.|[2401.14939](http://arxiv.org/abs/2401.14939)|**[link](https://github.com/yuanchenbei/macgnn)**|
|**2024-01-26**|**Coca: Improving and Explaining Graph Neural Network-Based Vulnerability Detection Systems**|Sicong Cao et.al.|[2401.14886](http://arxiv.org/abs/2401.14886)|null|
|**2024-01-26**|**PepGB: Facilitating peptide drug discovery via graph neural networks**|Yipin Lei et.al.|[2401.14665](http://arxiv.org/abs/2401.14665)|null|
|**2024-01-26**|**Design Your Own Universe: A Physics-Informed Agnostic Method for Enhancing Graph Neural Networks**|Dai Shi et.al.|[2401.14580](http://arxiv.org/abs/2401.14580)|null|
|**2024-01-26**|**GOAt: Explaining Graph Neural Networks via Graph Output Attribution**|Shengyao Lu et.al.|[2401.14578](http://arxiv.org/abs/2401.14578)|**[link](https://github.com/sluxsr/goat)**|
|**2024-01-25**|**GCBF+: A Neural Graph Control Barrier Function Framework for Distributed Safe Multi-Agent Control**|Songyuan Zhang et.al.|[2401.14554](http://arxiv.org/abs/2401.14554)|**[link](https://github.com/MIT-REALM/gcbfplus)**|
|**2024-01-25**|**Manifold GCN: Diffusion-based Convolutional Neural Network for Manifold-valued Graphs**|Martin Hanik et.al.|[2401.14381](http://arxiv.org/abs/2401.14381)|null|
|**2024-01-25**|**Estimation of partially known Gaussian graphical models with score-based structural priors**|Martín Sevilla et.al.|[2401.14340](http://arxiv.org/abs/2401.14340)|**[link](https://github.com/tenceto/langevin_ggm)**|
|**2024-01-25**|**Energy-Efficient Power Allocation in Cell-Free Massive MIMO via Graph Neural Networks**|Ramprasad Raghunath et.al.|[2401.14281](http://arxiv.org/abs/2401.14281)|**[link](https://gitlab.com/ichbinram/ee_cell_free)**|
|**2024-01-25**|**MTRGL:Effective Temporal Correlation Discerning through Multi-modal Temporal Relational Graph Learning**|Junwei Su et.al.|[2401.14199](http://arxiv.org/abs/2401.14199)|null|
|**2024-01-25**|**Alleviating Structural Distribution Shift in Graph Anomaly Detection**|Yuan Gao et.al.|[2401.14155](http://arxiv.org/abs/2401.14155)|**[link](https://github.com/blacksingular/wsdm_gdn)**|
|**2024-01-25**|**A Survey of Deep Learning and Foundation Models for Time Series Forecasting**|John A. Miller et.al.|[2401.13912](http://arxiv.org/abs/2401.13912)|null|
|**2024-01-25**|**Edge Conditional Node Update Graph Neural Network for Multi-variate Time Series Anomaly Detection**|Hayoung Jo et.al.|[2401.13872](http://arxiv.org/abs/2401.13872)|null|
|**2024-01-24**|**Multitask Active Learning for Graph Anomaly Detection**|Wenjing Chang et.al.|[2401.13210](http://arxiv.org/abs/2401.13210)|**[link](https://github.com/ahachang/mitigate)**|
|**2024-01-24**|**Topology-aware Embedding Memory for Learning on Expanding Graphs**|Xikun Zhang et.al.|[2401.13200](http://arxiv.org/abs/2401.13200)|**[link](https://github.com/imzhangxikun/pdgnns)**|
|**2024-01-23**|**Probabilistic Demand Forecasting with Graph Neural Networks**|Nikita Kozodoi et.al.|[2401.13096](http://arxiv.org/abs/2401.13096)|null|
|**2024-01-23**|**Truck Parking Usage Prediction with Decomposed Graph Neural Networks**|Rei Tamaru et.al.|[2401.12920](http://arxiv.org/abs/2401.12920)|null|
|**2024-01-23**|**Overlap-aware End-to-End Supervised Hierarchical Graph Clustering for Speaker Diarization**|Prachi Singh et.al.|[2401.12850](http://arxiv.org/abs/2401.12850)|**[link](https://github.com/prachiisc/SHARC)**|
|**2024-01-23**|**MAPPING: Debiasing Graph Neural Networks for Fair Node Classification with Limited Sensitive Information Leakage**|Ying Song et.al.|[2401.12824](http://arxiv.org/abs/2401.12824)|**[link](https://github.com/yings0930/MAPPING)**|
|**2024-01-23**|**DeepRicci: Self-supervised Graph Structure-Feature Co-Refinement for Alleviating Over-squashing**|Li Sun et.al.|[2401.12780](http://arxiv.org/abs/2401.12780)|null|
|**2024-01-23**|**PolyCF: Towards the Optimal Spectral Graph Filters for Collaborative Filtering**|Yifang Qin et.al.|[2401.12590](http://arxiv.org/abs/2401.12590)|null|
|**2024-01-22**|**VC dimension of Graph Neural Networks with Pfaffian activation functions**|Giuseppe Alessio D'Inverno et.al.|[2401.12362](http://arxiv.org/abs/2401.12362)|**[link](https://github.com/aledinve/vc-dim-gnn)**|
|**2024-01-22**|**Connecting the Dots: Leveraging Spatio-Temporal Graph Neural Networks for Accurate Bangla Sign Language Recognition**|Haz Sameen Shahgir et.al.|[2401.12210](http://arxiv.org/abs/2401.12210)|null|
|**2024-01-22**|**Tensor-view Topological Graph Neural Network**|Tao Wen et.al.|[2401.12007](http://arxiv.org/abs/2401.12007)|**[link](https://github.com/taowen0309/ttg-nn)**|
|**2024-01-22**|**Learning to Approximate Adaptive Kernel Convolution on Graphs**|Jaeyoon Sim et.al.|[2401.11840](http://arxiv.org/abs/2401.11840)|null|
|**2024-01-22**|**Knowledge Distillation on Spatial-Temporal Graph Convolutional Network for Traffic Prediction**|Mohammad Izadi et.al.|[2401.11798](http://arxiv.org/abs/2401.11798)|null|
|**2024-01-22**|**Full-Body Motion Reconstruction with Sparse Sensing from Graph Perspective**|Feiyu Yao et.al.|[2401.11783](http://arxiv.org/abs/2401.11783)|**[link](https://github.com/Feiyu-Yao/Full-Body-Motion-Reconstruction-with-Sparse-Sensing-from-Graph-Perspective)**|
|**2024-01-22**|**LightDiC: A Simple yet Effective Approach for Large-scale Digraph Representation Learning**|Xunkai Li et.al.|[2401.11772](http://arxiv.org/abs/2401.11772)|**[link](https://github.com/xkli-allen/lightdic)**|
|**2024-01-22**|**ADA-GNN: Atom-Distance-Angle Graph Neural Network for Crystal Material Property Prediction**|Jiao Huang et.al.|[2401.11768](http://arxiv.org/abs/2401.11768)|null|
|**2024-01-22**|**Integrated Sensing, Communication, and Computing: An Information-oriented Resource Transaction Mechanism**|Ning Chen et.al.|[2401.11759](http://arxiv.org/abs/2401.11759)|null|
|**2024-01-22**|**AdaFGL: A New Paradigm for Federated Node Classification with Topology Heterogeneity**|Xunkai Li et.al.|[2401.11750](http://arxiv.org/abs/2401.11750)|null|
|**2024-01-22**|**Graph Condensation: A Survey**|Xinyi Gao et.al.|[2401.11720](http://arxiv.org/abs/2401.11720)|**[link](https://github.com/xygaog/graph-condensation-papers)**|
|**2024-01-19**|**Co-Pilot for Health: Personalized Algorithmic AI Nudging to Improve Health Outcomes**|Jodi Chiam et.al.|[2401.10816](http://arxiv.org/abs/2401.10816)|null|
|**2024-01-19**|**Novel Representation Learning Technique using Graphs for Performance Analytics**|Tarek Ramadan et.al.|[2401.10799](http://arxiv.org/abs/2401.10799)|null|
|**2024-01-19**|**BoolGebra: Attributed Graph-learning for Boolean Algebraic Manipulation**|Yingjie Li et.al.|[2401.10753](http://arxiv.org/abs/2401.10753)|null|
|**2024-01-19**|**Adversarially Robust Signed Graph Contrastive Learning from Balance Augmentation**|Jialong Zhou et.al.|[2401.10590](http://arxiv.org/abs/2401.10590)|null|
|**2024-01-19**|**Symbol as Points: Panoptic Symbol Spotting via Point-based Representation**|Wenlong Liu et.al.|[2401.10556](http://arxiv.org/abs/2401.10556)|**[link](https://github.com/nicehuster/sympoint)**|
|**2024-01-19**|**FARe: Fault-Aware GNN Training on ReRAM-based PIM Accelerators**|Pratyush Dhingra et.al.|[2401.10522](http://arxiv.org/abs/2401.10522)|null|
|**2024-01-18**|**Distribution Consistency based Self-Training for Graph Neural Networks with Sparse Labels**|Fali Wang et.al.|[2401.10394](http://arxiv.org/abs/2401.10394)|null|
|**2024-01-18**|**Exploring General Intelligence via Gated Graph Transformer in Functional Connectivity Studies**|Gang Qu et.al.|[2401.10348](http://arxiv.org/abs/2401.10348)|null|
|**2024-01-18**|**A rotation-equivariant graph neural network for learning hadronic SMEFT effects**|Suman Chatterjee et.al.|[2401.10323](http://arxiv.org/abs/2401.10323)|null|
|**2024-01-18**|**Through the Dual-Prism: A Spectral Perspective on Graph Data Augmentation for Graph Classification**|Yutong Xia et.al.|[2401.09953](http://arxiv.org/abs/2401.09953)|**[link](https://github.com/yu-rp/dualprism)**|
|**2024-01-18**|**HGAttack: Transferable Heterogeneous Graph Adversarial Attack**|He Zhao et.al.|[2401.09945](http://arxiv.org/abs/2401.09945)|null|
|**2024-01-18**|**Infinite-Horizon Graph Filters: Leveraging Power Series to Enhance Sparse Information Aggregation**|Ruizhe Zhang et.al.|[2401.09943](http://arxiv.org/abs/2401.09943)|**[link](https://github.com/gpfn-anonymous/gpfn)**|
|**2024-01-18**|**Crystal Transformer Based Universal Atomic Embedding for Accurate and Transferable Prediction of Materials Properties**|Luozhijie Jin et.al.|[2401.09755](http://arxiv.org/abs/2401.09755)|null|
|**2024-01-18**|**Universally Robust Graph Neural Networks by Preserving Neighbor Similarity**|Yulin Zhu et.al.|[2401.09754](http://arxiv.org/abs/2401.09754)|null|
|**2024-01-18**|**Predicting Viral Rumors and Vulnerable Users for Infodemic Surveillance**|Xuan Zhang et.al.|[2401.09724](http://arxiv.org/abs/2401.09724)|**[link](https://github.com/jadecurl/predicting-viral-rumors-and-vulnerable-users)**|
|**2024-01-18**|**EfficientRec an unlimited user-item scale recommendation system based on clustering and users interaction embedding profile**|Vu Hong Quan et.al.|[2401.09693](http://arxiv.org/abs/2401.09693)|**[link](https://github.com/quanvu0996/efficientrec)**|
|**2024-01-17**|**BENO: Boundary-embedded Neural Operators for Elliptic PDEs**|Haixin Wang et.al.|[2401.09323](http://arxiv.org/abs/2401.09323)|**[link](https://github.com/ai4science-westlakeu/beno)**|
|**2024-01-17**|**GNN-LoFI: a Novel Graph Neural Network through Localized Feature-based Histogram Intersection**|Alessandro Bicciato et.al.|[2401.09193](http://arxiv.org/abs/2401.09193)|**[link](https://github.com/gdl-unive/histogram-intersection-kernel)**|
|**2024-01-17**|**Understanding Heterophily for Graph Neural Networks**|Junfu Wang et.al.|[2401.09125](http://arxiv.org/abs/2401.09125)|null|
|**2024-01-17**|**Rethinking Spectral Graph Neural Networks with Spatially Adaptive Filtering**|Jingwei Guo et.al.|[2401.09071](http://arxiv.org/abs/2401.09071)|null|
|**2024-01-16**|**Beyond Weisfeiler-Lehman: A Quantitative Framework for GNN Expressiveness**|Bohang Zhang et.al.|[2401.08514](http://arxiv.org/abs/2401.08514)|**[link](https://github.com/subgraph23/homomorphism-expressivity)**|
|**2024-01-16**|**Spoofing Detection in the Physical Layer with Graph Neural Networks**|Tien Ngoc Ha et.al.|[2401.08220](http://arxiv.org/abs/2401.08220)|null|
|**2024-01-16**|**Structure-based out-of-distribution (OOD) materials property prediction: a benchmark study**|Sadman Sadeed Omee et.al.|[2401.08032](http://arxiv.org/abs/2401.08032)|**[link](https://github.com/sadmanomee/ood_materials_benchmark)**|
|**2024-01-15**|**Integrate Any Omics: Towards genome-wide data integration for patient stratification**|Shihao Ma et.al.|[2401.07937](http://arxiv.org/abs/2401.07937)|**[link](https://github.com/bowang-lab/integrao)**|
|**2024-01-15**|**Multimodal Language and Graph Learning of Adsorption Configuration in Catalysis**|Janghoon Ock et.al.|[2401.07408](http://arxiv.org/abs/2401.07408)|**[link](https://github.com/hoon-ock/multi-view)**|
|**2024-01-13**|**Graph Language Models**|Moritz Plenz et.al.|[2401.07105](http://arxiv.org/abs/2401.07105)|**[link](https://github.com/heidelberg-nlp/graphlanguagemodels)**|
|**2024-01-13**|**Reinforcement Learning for Scalable Train Timetable Rescheduling with Graph Representation**|Peng Yue et.al.|[2401.06952](http://arxiv.org/abs/2401.06952)|null|
|**2024-01-12**|**Accelerating Neural Networks for Large Language Models and Graph Processing with Silicon Photonics**|Salma Afifi et.al.|[2401.06885](http://arxiv.org/abs/2401.06885)|null|
|**2024-01-12**|**A General Benchmark Framework is Dynamic Graph Neural Network Need**|Yusen Zhang et.al.|[2401.06559](http://arxiv.org/abs/2401.06559)|null|
|**2024-01-12**|**Treatment-Aware Hyperbolic Representation Learning for Causal Effect Estimation with Social Networks**|Ziqiang Cui et.al.|[2401.06557](http://arxiv.org/abs/2401.06557)|**[link](https://github.com/ziqiangcui/tahyper)**|
|**2024-01-11**|**Learning Crowd Behaviors in Navigation with Attention-based Spatial-Temporal Graphs**|Yanying Zhou et.al.|[2401.06226](http://arxiv.org/abs/2401.06226)|null|
|**2024-01-11**|**On the Power of Graph Neural Networks and Feature Augmentation Strategies to Classify Social Networks**|Walid Guettala et.al.|[2401.06048](http://arxiv.org/abs/2401.06048)|**[link](https://github.com/walidgeuttala/Synthetic-Benchmark-for-Graph-Classification)**|
|**2024-01-11**|**Wavelet-Inspired Multiscale Graph Convolutional Recurrent Network for Traffic Forecasting**|Qipeng Qian et.al.|[2401.06040](http://arxiv.org/abs/2401.06040)|**[link](https://github.com/qqian99/wavgcrn)**|
|**2024-01-11**|**Use of Graph Neural Networks in Aiding Defensive Cyber Operations**|Shaswata Mitra et.al.|[2401.05680](http://arxiv.org/abs/2401.05680)|null|
|**2024-01-11**|**Graph Q-Learning for Combinatorial Optimization**|Victoria M. Dax et.al.|[2401.05610](http://arxiv.org/abs/2401.05610)|null|
|**2024-01-10**|**Population Graph Cross-Network Node Classification for Autism Detection Across Sample Groups**|Anna Stephens et.al.|[2401.05478](http://arxiv.org/abs/2401.05478)|**[link](https://github.com/ajoystephens/otgcn)**|
|**2024-01-10**|**Introducing New Node Prediction in Graph Mining: Predicting All Links from Isolated Nodes with Graph Neural Networks**|Damiano Zanardini et.al.|[2401.05468](http://arxiv.org/abs/2401.05468)|null|
|**2024-01-10**|**Arrival Time Prediction for Autonomous Shuttle Services in the Real World: Evidence from Five Cities**|Carolin Schmidt et.al.|[2401.05322](http://arxiv.org/abs/2401.05322)|null|
|**2024-01-10**|**Physics guided dual Self-supervised learning for structure-based materials property prediction**|Nihang Fu et.al.|[2401.05223](http://arxiv.org/abs/2401.05223)|**[link](https://github.com/usccolumbia/dssl)**|
|**2024-01-10**|**MGNet: Learning Correspondences via Multiple Graphs**|Luanyuan Dai et.al.|[2401.04984](http://arxiv.org/abs/2401.04984)|null|
|**2024-01-10**|**LPAC: Learnable Perception-Action-Communication Loops with Applications to Coverage Control**|Saurav Agarwal et.al.|[2401.04855](http://arxiv.org/abs/2401.04855)|**[link](https://github.com/kumarrobotics/coveragecontrol)**|
|**2024-01-09**|**GNNShap: Fast and Accurate GNN Explanations using Shapley Values**|Selahattin Akkas et.al.|[2401.04829](http://arxiv.org/abs/2401.04829)|**[link](https://github.com/HipGraph/GNNShap)**|
|**2024-01-09**|**Coupling Graph Neural Networks with Fractional Order Continuous Dynamics: A Robustness Study**|Qiyu Kang et.al.|[2401.04331](http://arxiv.org/abs/2401.04331)|null|
|**2024-01-08**|**Explaining the Power of Topological Data Analysis in Graph Machine Learning**|Funmilola Mary Taiwo et.al.|[2401.04250](http://arxiv.org/abs/2401.04250)|**[link](https://github.com/phunmey/xtda-paper)**|
|**2024-01-07**|**Global-Aware Enhanced Spatial-Temporal Graph Recurrent Networks: A New Framework For Traffic Flow Prediction**|Haiyang Liu et.al.|[2401.04135](http://arxiv.org/abs/2401.04135)|null|
|**2024-01-09**|**A Primer on Temporal Graph Learning**|Aniq Ur Rahman et.al.|[2401.03988](http://arxiv.org/abs/2401.03988)|null|
|**2024-01-08**|**Inferring Properties of Graph Neural Networks**|Dat Nguyen et.al.|[2401.03790](http://arxiv.org/abs/2401.03790)|null|
|**2024-01-08**|**Joint Power Allocation and User Scheduling in Integrated Satellite-Terrestrial Cell-Free Massive MIMO IoT Systems**|Trinh Van Chien et.al.|[2401.03754](http://arxiv.org/abs/2401.03754)|null|
|**2024-01-08**|**Boosting Column Generation with Graph Neural Networks for Joint Rider Trip Planning and Crew Shift Scheduling**|Jiawei Lu et.al.|[2401.03692](http://arxiv.org/abs/2401.03692)|null|
|**2024-01-08**|**GrainGNN: A dynamic graph neural network for predicting 3D grain microstructure**|Yigong Qin et.al.|[2401.03661](http://arxiv.org/abs/2401.03661)|**[link](https://github.com/yigongqin/graingraphnn)**|
|**2024-01-07**|**Few-Shot Causal Representation Learning for Out-of-Distribution Generalization on Heterogeneous Graphs**|Pengfei Ding et.al.|[2401.03597](http://arxiv.org/abs/2401.03597)|null|
|**2024-01-07**|**Global Prediction of COVID-19 Variant Emergence Using Dynamics-Informed Graph Neural Networks**|Majd Al Aawar et.al.|[2401.03390](http://arxiv.org/abs/2401.03390)|**[link](https://github.com/itssmutnuri/gnnvariants)**|
|**2024-01-07**|**Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural Networks**|Puja Trivedi et.al.|[2401.03350](http://arxiv.org/abs/2401.03350)|null|
|**2024-01-06**|**TelTrans: Applying Multi-Type Telecom Data to Transportation Evaluation and Prediction via Multifaceted Graph Modeling**|ChungYi Lin et.al.|[2401.03138](http://arxiv.org/abs/2401.03138)|null|
|**2024-01-06**|**GLISP: A Scalable GNN Learning System by Exploiting Inherent Structural Properties of Graphs**|Zhongshu Zhu et.al.|[2401.03114](http://arxiv.org/abs/2401.03114)|null|
|**2024-01-05**|**Graph2Tac: Learning Hierarchical Representations of Math Concepts in Theorem proving**|Jason Rute et.al.|[2401.02949](http://arxiv.org/abs/2401.02949)|null|
|**2024-01-05**|**H2G2-Net: A Hierarchical Heterogeneous Graph Generative Network Framework for Discovery of Multi-Modal Physiological Responses**|Haidong Gu et.al.|[2401.02905](http://arxiv.org/abs/2401.02905)|null|
|**2024-01-05**|**DocGraphLM: Documental Graph Language Model for Information Extraction**|Dongsheng Wang et.al.|[2401.02823](http://arxiv.org/abs/2401.02823)|null|
|**2024-01-05**|**Powerformer: A Section-adaptive Transformer for Power Flow Adjustment**|Kaixuan Chen et.al.|[2401.02771](http://arxiv.org/abs/2401.02771)|**[link](https://github.com/Cra2yDavid/Powerformer)**|
|**2024-01-05**|**Verifying Relational Explanations: A Probabilistic Approach**|Abisha Thapa Magar et.al.|[2401.02703](http://arxiv.org/abs/2401.02703)|**[link](https://github.com/abisha-thapa/explain)**|
|**2024-01-05**|**PAHD: Perception-Action based Human Decision Making using Explainable Graph Neural Networks on SAR Images**|Sasindu Wijeratne et.al.|[2401.02687](http://arxiv.org/abs/2401.02687)|null|
|**2024-01-05**|**Homophily-Related: Adaptive Hybrid Graph Filter for Multi-View Graph Clustering**|Zichen Wen et.al.|[2401.02682](http://arxiv.org/abs/2401.02682)|null|
|**2024-01-05**|**A backdoor attack against link prediction tasks with graph neural networks**|Jiazhu Dai et.al.|[2401.02663](http://arxiv.org/abs/2401.02663)|null|
|**2024-01-04**|**A Community Detection and Graph Neural Network Based Link Prediction Approach for Scientific Literature**|Chunjiang Liu et.al.|[2401.02542](http://arxiv.org/abs/2401.02542)|null|
|**2024-01-04**|**Detection and Discovery of Misinformation Sources using Attributed Webgraphs**|Peter Carragher et.al.|[2401.02379](http://arxiv.org/abs/2401.02379)|**[link](https://github.com/CASOS-IDeaS-CMU/Detection-and-Discovery-of-Misinformation-Sources)**|
|**2024-01-04**|**Path-based Explanation for Knowledge Graph Completion**|Heng Chang et.al.|[2401.02290](http://arxiv.org/abs/2401.02290)|**[link](https://github.com/OUTHIM/power-link)**|
|**2024-01-04**|**Graph Neural Networks for Tabular Data Learning: A Survey with Taxonomy and Directions**|Cheng-Te Li et.al.|[2401.02143](http://arxiv.org/abs/2401.02143)|**[link](https://github.com/roytsai27/awesome-gnn4tdl)**|
|**2024-01-04**|**Spectral-based Graph Neutral Networks for Complementary Item Recommendation**|Haitong Luo et.al.|[2401.02130](http://arxiv.org/abs/2401.02130)|null|
|**2024-01-04**|**View-based Explanations for Graph Neural Networks**|Tingyang Chen et.al.|[2401.02086](http://arxiv.org/abs/2401.02086)|**[link](https://github.com/zju-daily/gvex)**|
|**2024-01-04**|**Accelerated Band Offset Prediction in Semiconductor Interfaces with DFT and Deep Learning**|Kamal Choudhary et.al.|[2401.02021](http://arxiv.org/abs/2401.02021)|**[link](https://github.com/usnistgov/intermat)**|
|**2024-01-03**|**Graph Neural Networks for Surfactant Multi-Property Prediction**|Christoforos Brozos et.al.|[2401.01874](http://arxiv.org/abs/2401.01874)|**[link](https://github.com/brozosc/graph-neural-networks-for-surfactant-multi-property-prediction)**|
|**2024-01-03**|**On the hardness of learning under symmetries**|Bobak T. Kiani et.al.|[2401.01869](http://arxiv.org/abs/2401.01869)|null|
|**2024-01-03**|**DGDNN: Decoupled Graph Diffusion Neural Network for Stock Movement Prediction**|Zinuo You et.al.|[2401.01846](http://arxiv.org/abs/2401.01846)|**[link](https://github.com/pixelhero98/dgdnn)**|
|**2024-01-03**|**A quatum inspired neural network for geometric modeling**|Weitao Du et.al.|[2401.01801](http://arxiv.org/abs/2401.01801)|null|
|**2024-01-03**|**MLPs Compass: What is learned when MLPs are combined with PLMs?**|Li Zhou et.al.|[2401.01667](http://arxiv.org/abs/2401.01667)|null|
|**2024-01-03**|**On the Expressive Power of Graph Neural Networks**|Ashwin Nalwade et.al.|[2401.01626](http://arxiv.org/abs/2401.01626)|null|
|**2024-01-01**|**Strong Transitivity Relations and Graph Neural Networks**|Yassin Mohamadi et.al.|[2401.01384](http://arxiv.org/abs/2401.01384)|**[link](https://github.com/yassinmihemedi/strong-transitivity-relations-and-graph-neural-network)**|
|**2024-01-02**|**Graph Elimination Networks**|Shuo Wang et.al.|[2401.01233](http://arxiv.org/abs/2401.01233)|null|
|**2024-01-02**|**Motif-aware Riemannian Graph Neural Network with Generative-Contrastive Learning**|Li Sun et.al.|[2401.01232](http://arxiv.org/abs/2401.01232)|**[link](https://github.com/riemanngraph/motifrgc)**|
|**2024-01-01**|**Saliency-Aware Regularized Graph Neural Network**|Wenjie Pei et.al.|[2401.00755](http://arxiv.org/abs/2401.00755)|null|
|**2024-01-02**|**A Survey on Graph Neural Networks in Intelligent Transportation Systems**|Hourun Li et.al.|[2401.00713](http://arxiv.org/abs/2401.00713)|null|
|**2024-01-01**|**On Discprecncies between Perturbation Evaluations of Graph Neural Network Attributions**|Razieh Rezaei et.al.|[2401.00633](http://arxiv.org/abs/2401.00633)|**[link](https://github.com/alirezadizaji/graphroar)**|
|**2023-12-31**|**Generating High-Precision Force Fields for Molecular Dynamics Simulations to Study Chemical Reaction Mechanisms using Molecular Configuration Transformer**|Sihao Yuan et.al.|[2401.00499](http://arxiv.org/abs/2401.00499)|null|
|**2023-12-31**|**Deeper and Wider Networks for Performance Metrics Prediction in Communication Networks**|Aijia Liu et.al.|[2401.00429](http://arxiv.org/abs/2401.00429)|null|
|**2023-12-31**|**FusionMind -- Improving question and answering with external context fusion**|Shreyas Verma et.al.|[2401.00388](http://arxiv.org/abs/2401.00388)|null|
|**2023-12-30**|**A clean-label graph backdoor attack method in node classification task**|Xiaogang Xing et.al.|[2401.00163](http://arxiv.org/abs/2401.00163)|null|
|**2023-12-30**|**ReasoningLM: Enabling Structural Subgraph Reasoning in Pre-trained Language Models for Question Answering over Knowledge Graph**|Jinhao Jiang et.al.|[2401.00158](http://arxiv.org/abs/2401.00158)|null|
|**2023-12-29**|**Physics-informed Graphical Neural Network for Power System State Estimation**|Quang-Ha Ngo et.al.|[2312.17738](http://arxiv.org/abs/2312.17738)|null|
|**2023-12-29**|**Data Augmentation for Supervised Graph Outlier Detection with Latent Diffusion Models**|Kay Liu et.al.|[2312.17679](http://arxiv.org/abs/2312.17679)|**[link](https://github.com/kayzliu/godm)**|
|**2023-12-29**|**A graph neural network-based model with Out-of-Distribution Robustness for enhancing Antiretroviral Therapy Outcome Prediction for HIV-1**|Giulia Di Teodoro et.al.|[2312.17506](http://arxiv.org/abs/2312.17506)|**[link](https://github.com/federicosiciliano/graph-ood-hiv)**|
|**2023-12-28**|**Explainability-Based Adversarial Attack on Graphs Through Edge Perturbation**|Dibaloke Chanda et.al.|[2312.17301](http://arxiv.org/abs/2312.17301)|null|
|**2023-12-28**|**TSPP: A Unified Benchmarking Tool for Time-series Forecasting**|Jan Bączek et.al.|[2312.17100](http://arxiv.org/abs/2312.17100)|**[link](https://github.com/NVIDIA/DeepLearningExamples)**|
|**2023-12-28**|**Molecular Property Prediction Based on Graph Structure Learning**|Bangyi Zhao et.al.|[2312.16855](http://arxiv.org/abs/2312.16855)|null|
|**2023-12-28**|**Learning Scalable Structural Representations for Link Prediction with Bloom Signatures**|Tianyi Zhang et.al.|[2312.16784](http://arxiv.org/abs/2312.16784)|null|
|**2023-12-28**|**Graph Neural Networks for Antisocial Behavior Detection on Twitter**|Martina Toshevska et.al.|[2312.16755](http://arxiv.org/abs/2312.16755)|null|
|**2023-12-27**|**Performance Comparison of Session-based Recommendation Algorithms based on GNNs**|Faisal Shehzad et.al.|[2312.16695](http://arxiv.org/abs/2312.16695)|null|
|**2023-12-27**|**FALCON: Feature-Label Constrained Graph Net Collapse for Memory Efficient GNNs**|Christopher Adnel et.al.|[2312.16542](http://arxiv.org/abs/2312.16542)|**[link](https://github.com/basiralab/falcon)**|
|**2023-12-27**|**MolSets: Molecular Graph Deep Sets Learning for Mixture Property Modeling**|Hengrui Zhang et.al.|[2312.16473](http://arxiv.org/abs/2312.16473)|**[link](https://github.com/henrium/molsets)**|
|**2023-12-27**|**Learning Time-aware Graph Structures for Spatially Correlated Time Series Forecasting**|Minbo Ma et.al.|[2312.16403](http://arxiv.org/abs/2312.16403)|null|
|**2023-12-26**|**BalMCTS: Balancing Objective Function and Search Nodes in MCTS for Constraint Optimization Problems**|Yingkai Xiao et.al.|[2312.15864](http://arxiv.org/abs/2312.15864)|null|
|**2023-12-25**|**Comparative Analysis of Radiomic Features and Gene Expression Profiles in Histopathology Data Using Graph Neural Networks**|Luis Carlos Rivera Monroy et.al.|[2312.15825](http://arxiv.org/abs/2312.15825)|null|
|**2023-12-24**|**Graph Coarsening via Convolution Matching for Scalable Graph Neural Network Training**|Charles Dickens et.al.|[2312.15520](http://arxiv.org/abs/2312.15520)|**[link](https://github.com/amazon-science/convolution-matching)**|
|**2023-12-24**|**Combinatorial music generation model with song structure graph analysis**|Seonghyeon Go et.al.|[2312.15400](http://arxiv.org/abs/2312.15400)|**[link](https://github.com/slslslrhfem/song_structure_graph)**|
|**2023-12-23**|**Towards Fine-Grained Explainability for Heterogeneous Graph Neural Network**|Tong Li et.al.|[2312.15237](http://arxiv.org/abs/2312.15237)|**[link](https://github.com/litong99/xpath)**|
|**2023-12-25**|**Large Scale Training of Graph Neural Networks for Optimal Markov-Chain Partitioning Using the Kemeny Constant**|Sam Alexander Martino et.al.|[2312.14847](http://arxiv.org/abs/2312.14847)|null|
|**2023-12-22**|**Learning Lagrangian Multipliers for the Travelling Salesman Problem**|Augustin Parjadis et.al.|[2312.14836](http://arxiv.org/abs/2312.14836)|null|
|**2023-12-22**|**Joint Learning Neuronal Skeleton and Brain Circuit Topology with Permutation Invariant Encoders for Neuron Classification**|Minghui Liao et.al.|[2312.14518](http://arxiv.org/abs/2312.14518)|**[link](https://github.com/whuminghui/neunet)**|
|**2023-12-21**|**Behaviour Modelling of Social Animals via Causal Structure Discovery and Graph Neural Networks**|Gaël Gendron et.al.|[2312.14333](http://arxiv.org/abs/2312.14333)|**[link](https://github.com/strong-ai-lab/behavior-causal-discovery)**|
|**2023-12-21**|**Social Recommendation through Heterogeneous Graph Modeling of the Long-term and Short-term Preference Defined by Dynamic Periods**|Behafarid Mohammad Jafari et.al.|[2312.14306](http://arxiv.org/abs/2312.14306)|**[link](https://github.com/BehafaridMjf/Social-Recommendation-System)**|
|**2023-12-21**|**Fine-tuning Graph Neural Networks by Preserving Graph Generative Patterns**|Yifei Sun et.al.|[2312.13583](http://arxiv.org/abs/2312.13583)|**[link](https://github.com/zjunet/G-Tuning)**|
|**2023-12-21**|**Domain Adaptive Graph Classification**|Siyang Luo et.al.|[2312.13536](http://arxiv.org/abs/2312.13536)|null|
|**2023-12-21**|**Molecular Hypergraph Neural Networks**|Junwu Chen et.al.|[2312.13136](http://arxiv.org/abs/2312.13136)|**[link](https://github.com/schwallergroup/mhnn)**|
|**2023-12-20**|**Optimizing Ego Vehicle Trajectory Prediction: The Graph Enhancement Approach**|Sushil Sharma et.al.|[2312.13104](http://arxiv.org/abs/2312.13104)|null|
|**2023-12-21**|**NodeMixup: Tackling Under-Reaching for Graph Neural Networks**|Weigang Lu et.al.|[2312.13032](http://arxiv.org/abs/2312.13032)|**[link](https://github.com/weiganglu/nodemixup)**|
|**2023-12-20**|**Fast Cell Library Characterization for Design Technology Co-Optimization Based on Graph Neural Networks**|Tianliang Ma et.al.|[2312.12784](http://arxiv.org/abs/2312.12784)|null|
|**2023-12-20**|**Cross-Modal Reasoning with Event Correlation for Video Question Answering**|Chengxiang Yin et.al.|[2312.12721](http://arxiv.org/abs/2312.12721)|null|
|**2023-12-20**|**DGCLUSTER: A Neural Framework for Attributed Graph Clustering via Modularity Maximization**|Aritra Bhowmick et.al.|[2312.12697](http://arxiv.org/abs/2312.12697)|**[link](https://github.com/pyrobits/dgcluster)**|
|**2023-12-21**|**Data-driven Design of High Pressure Hydride Superconductors using DFT and Deep Learning**|Daniel Wines et.al.|[2312.12694](http://arxiv.org/abs/2312.12694)|null|
|**2023-12-19**|**Chasing Fairness in Graphs: A GNN Architecture Perspective**|Zhimeng Jiang et.al.|[2312.12369](http://arxiv.org/abs/2312.12369)|**[link](https://github.com/zhimengj0326/fmp)**|
|**2023-12-19**|**Poincaré Differential Privacy for Hierarchy-aware Graph Embedding**|Yuecen Wei et.al.|[2312.12183](http://arxiv.org/abs/2312.12183)|null|
|**2023-12-19**|**Hierarchical and Incremental Structural Entropy Minimization for Unsupervised Social Event Detection**|Yuwei Cao et.al.|[2312.11891](http://arxiv.org/abs/2312.11891)|**[link](https://github.com/selgroup/hisevent)**|
|**2023-12-19**|**SimCalib: Graph Neural Network Calibration based on Similarity between Nodes**|Boshi Tang et.al.|[2312.11858](http://arxiv.org/abs/2312.11858)|null|
|**2023-12-18**|**Stronger Graph Transformer with Regularized Attention Scores**|Eugene Ku et.al.|[2312.11730](http://arxiv.org/abs/2312.11730)|**[link](https://github.com/eugene29/graphgps_edge_regularization)**|
|**2023-12-18**|**Reinforcement Learning Based Quantum Circuit Optimization via ZX-Calculus**|Jordi Riu et.al.|[2312.11597](http://arxiv.org/abs/2312.11597)|null|
|**2023-12-19**|**CaseGNN: Graph Neural Networks for Legal Case Retrieval with Text-Attributed Graphs**|Yanran Tang et.al.|[2312.11229](http://arxiv.org/abs/2312.11229)|**[link](https://github.com/yanran-tang/casegnn)**|
|**2023-12-18**|**Signed Graph Neural Ordinary Differential Equation for Modeling Continuous-time Dynamics**|Lanlan Chen et.al.|[2312.11198](http://arxiv.org/abs/2312.11198)|**[link](https://github.com/beautyonce/sgode)**|
|**2023-12-18**|**Learning Domain-Independent Heuristics for Grounded and Lifted Planning**|Dillon Z. Chen et.al.|[2312.11143](http://arxiv.org/abs/2312.11143)|**[link](https://github.com/DillonZChen/goose)**|
|**2023-12-18**|**Graph Invariant Learning with Subgraph Co-mixup for Out-Of-Distribution Generalization**|Tianrui Jia et.al.|[2312.10988](http://arxiv.org/abs/2312.10988)|**[link](https://github.com/bupt-gamma/igm)**|
|**2023-12-17**|**Non-Euclidean Spatial Graph Neural Network**|Zheng Zhang et.al.|[2312.10808](http://arxiv.org/abs/2312.10808)|**[link](https://github.com/anonymous-submitter-1234/manifold_spatial_networks)**|
|**2023-12-17**|**p-Laplacian Adaptation for Generative Pre-trained Vision-Language Models**|Haoyuan Wu et.al.|[2312.10613](http://arxiv.org/abs/2312.10613)|**[link](https://github.com/wuhy68/p-adapter)**|
|**2023-12-16**|**Enabling Accelerators for Graph Computing**|Kaustubh Shivdikar et.al.|[2312.10561](http://arxiv.org/abs/2312.10561)|null|
|**2023-12-16**|**Degree-based stratification of nodes in Graph Neural Networks**|Ameen Ali et.al.|[2312.10458](http://arxiv.org/abs/2312.10458)|null|
|**2023-12-16**|**scBiGNN: Bilevel Graph Representation Learning for Cell Type Classification from Single-cell RNA Sequencing Data**|Rui Yang et.al.|[2312.10310](http://arxiv.org/abs/2312.10310)|null|
|**2023-12-16**|**Inductive Link Prediction in Knowledge Graphs using Path-based Neural Networks**|Canlin Zhang et.al.|[2312.10293](http://arxiv.org/abs/2312.10293)|**[link](https://github.com/canlinzhang/siailp)**|
|**2023-12-16**|**A charge-preserving method for solving graph neural diffusion networks**|Lidia Aceto et.al.|[2312.10279](http://arxiv.org/abs/2312.10279)|null|
|**2023-12-15**|**Concept Prerequisite Relation Prediction by Using Permutation-Equivariant Directed Graph Neural Networks**|Xiran Qu et.al.|[2312.09802](http://arxiv.org/abs/2312.09802)|null|
|**2023-12-15**|**Bridging the Semantic-Numerical Gap: A Numerical Reasoning Method of Cross-modal Knowledge Graph for Material Property Prediction**|Guangxuan Song et.al.|[2312.09744](http://arxiv.org/abs/2312.09744)|null|
|**2023-12-15**|**GraphRARE: Reinforcement Learning Enhanced Graph Neural Network with Relative Entropy**|Tianhao Peng et.al.|[2312.09708](http://arxiv.org/abs/2312.09708)|null|
|**2023-12-15**|**nuScenes Knowledge Graph -- A comprehensive semantic representation of traffic scenes for trajectory prediction**|Leon Mlodzian et.al.|[2312.09676](http://arxiv.org/abs/2312.09676)|**[link](https://github.com/boschresearch/nuscenes_knowledge_graph)**|
|**2023-12-15**|**Rethinking Causal Relationships Learning in Graph Neural Networks**|Hang Gao et.al.|[2312.09613](http://arxiv.org/abs/2312.09613)|**[link](https://github.com/yaoyao-yaoyao-cell/crcg)**|
|**2023-12-15**|**Hierarchical Graph Pattern Understanding for Zero-Shot VOS**|Gensheng Pei et.al.|[2312.09525](http://arxiv.org/abs/2312.09525)|**[link](https://github.com/nust-machine-intelligence-laboratory/hgpu)**|
|**2023-12-14**|**COMBHelper: A Neural Approach to Reduce Search Space for Graph Combinatorial Problems**|Hao Tian et.al.|[2312.09086](http://arxiv.org/abs/2312.09086)|**[link](https://github.com/1041877801/COMBHelper)**|
|**2023-12-14**|**Graph Neural Networks with Diverse Spectral Filtering**|Jingwei Guo et.al.|[2312.09041](http://arxiv.org/abs/2312.09041)|**[link](https://github.com/jingweio/dsf)**|
|**2023-12-14**|**Uncertainty in GNN Learning Evaluations: A Comparison Between Measures for Quantifying Randomness in GNN Community Detection**|William Leeney et.al.|[2312.09015](http://arxiv.org/abs/2312.09015)|null|
|**2023-12-14**|**Multi-Scene Generalized Trajectory Global Graph Solver with Composite Nodes for Multiple Object Tracking**|Yan Gao et.al.|[2312.08951](http://arxiv.org/abs/2312.08951)|null|
|**2023-12-14**|**Heterogeneous Graph Neural Architecture Search with GPT-4**|Haoyuan Dong et.al.|[2312.08680](http://arxiv.org/abs/2312.08680)|**[link](https://github.com/cold-rivers/LLM4HGNAS)**|
|**2023-12-14**|**Uplifting the Expressive Power of Graph Neural Networks through Graph Partitioning**|Asela Hevapathige et.al.|[2312.08671](http://arxiv.org/abs/2312.08671)|null|
|**2023-12-14**|**MaxK-GNN: Towards Theoretical Speed Limits for Accelerating Graph Neural Networks Training**|Hongwu Peng et.al.|[2312.08656](http://arxiv.org/abs/2312.08656)|**[link](https://github.com/harveyp123/maxk-gnn)**|
|**2023-12-14**|**Towards Inductive Robustness: Distilling and Fostering Wave-induced Resonance in Transductive GCNs Against Graph Adversarial Attacks**|Ao Liu et.al.|[2312.08651](http://arxiv.org/abs/2312.08651)|null|
|**2023-12-13**|**SAM-guided Graph Cut for 3D Instance Segmentation**|Haoyu Guo et.al.|[2312.08372](http://arxiv.org/abs/2312.08372)|null|
|**2023-12-13**|**CUTTANA: Scalable Graph Partitioning for Faster Distributed Graph Databases and Analytics**|Milad Rezaei Hajidehi et.al.|[2312.08356](http://arxiv.org/abs/2312.08356)|null|
|**2023-12-13**|**On the verification of Embeddings using Hybrid Markov Logic**|Anup Shakya et.al.|[2312.08287](http://arxiv.org/abs/2312.08287)|null|
|**2023-12-13**|**Patch-wise Graph Contrastive Learning for Image Translation**|Chanyong Jung et.al.|[2312.08223](http://arxiv.org/abs/2312.08223)|**[link](https://github.com/jcy132/PatchGCL)**|
|**2023-12-14**|**Curriculum-Enhanced Residual Soft An-Isotropic Normalization for Over-smoothness in Deep GNNs**|Jin Li et.al.|[2312.08221](http://arxiv.org/abs/2312.08221)|**[link](https://github.com/jslijin/research-paper-codes)**|
|**2023-12-13**|**Adversarial Attacks on Graph Neural Networks based Spatial Resource Management in P2P Wireless Communications**|Ahmad Ghasemi et.al.|[2312.08181](http://arxiv.org/abs/2312.08181)|null|
|**2023-12-13**|**Artificial Intelligence Studies in Cartography: A Review and Synthesis of Methods, Applications, and Ethics**|Yuhao Kang et.al.|[2312.07901](http://arxiv.org/abs/2312.07901)|null|
|**2023-12-13**|**Securing Graph Neural Networks in MLaaS: A Comprehensive Realization of Query-based Integrity Verification**|Bang Wu et.al.|[2312.07870](http://arxiv.org/abs/2312.07870)|null|
|**2023-12-13**|**GraphGuard: Detecting and Counteracting Training Data Misuse in Graph Neural Networks**|Bang Wu et.al.|[2312.07861](http://arxiv.org/abs/2312.07861)|**[link](https://github.com/graphguard/graphguard-proactive)**|
|**2023-12-12**|**I Open at the Close: A Deep Reinforcement Learning Evaluation of Open Streets Initiatives**|R. Teal Witter et.al.|[2312.07680](http://arxiv.org/abs/2312.07680)|**[link](https://github.com/rtealwitter/openstreets)**|
|**2023-12-12**|**A Hitchhiker's Guide to Geometric GNNs for 3D Atomic Systems**|Alexandre Duval et.al.|[2312.07511](http://arxiv.org/abs/2312.07511)|**[link](https://github.com/alexduvalinho/geometric-gnns)**|
|**2023-12-12**|**Cost Aware Untargeted Poisoning Attack against Graph Neural Networks,**|Yuwei Han et.al.|[2312.07158](http://arxiv.org/abs/2312.07158)|null|
|**2023-12-12**|**Neural Reasoning About Agents' Goals, Preferences, and Actions**|Matteo Bortoletto et.al.|[2312.07122](http://arxiv.org/abs/2312.07122)|null|
|**2023-12-12**|**Benchmarking Deep Learning Classifiers for SAR Automatic Target Recognition**|Jacob Fein-Ashley et.al.|[2312.06940](http://arxiv.org/abs/2312.06940)|null|
|**2023-12-11**|**A Novel Differentiable Loss Function for Unsupervised Graph Neural Networks in Graph Partitioning**|Vivek Chaudhary et.al.|[2312.06877](http://arxiv.org/abs/2312.06877)|null|
|**2023-12-11**|**Optimizing High Throughput Inference on Graph Neural Networks at Shared Computing Facilities with the NVIDIA Triton Inference Server**|Claire Savard et.al.|[2312.06838](http://arxiv.org/abs/2312.06838)|**[link](https://github.com/cgsavard/triton_multiuser_benchmarks)**|
|**2023-12-11**|**HyPE-GT: where Graph Transformers meet Hyperbolic Positional Encodings**|Kushal Bose et.al.|[2312.06576](http://arxiv.org/abs/2312.06576)|**[link](https://github.com/kushalbose92/hype-gt)**|
|**2023-12-11**|**Sparse but Strong: Crafting Adversarially Robust Graph Lottery Tickets**|Subhajit Dutta Chowdhury et.al.|[2312.06568](http://arxiv.org/abs/2312.06568)|null|
|**2023-12-11**|**Robust Graph Neural Network based on Graph Denoising**|Victor M. Tenorio et.al.|[2312.06557](http://arxiv.org/abs/2312.06557)|**[link](https://github.com/vmtenorio/robust_gnn)**|
|**2023-12-11**|**A GAN Approach for Node Embedding in Heterogeneous Graphs Using Subgraph Sampling**|Hung Chun Hsu et.al.|[2312.06519](http://arxiv.org/abs/2312.06519)|null|
|**2023-12-11**|**Revisiting Graph-based Fraud Detection in Sight of Heterophily and Spectrum**|Fan Xu et.al.|[2312.06441](http://arxiv.org/abs/2312.06441)|**[link](https://github.com/sunxkissed/sec-gfd)**|
|**2023-12-11**|**Detecting Contextual Network Anomalies with Graph Neural Networks**|Hamid Latif-Martínez et.al.|[2312.06342](http://arxiv.org/abs/2312.06342)|null|
|**2023-12-11**|**Deep Imbalanced Learning for Multimodal Emotion Recognition in Conversations**|Tao Meng et.al.|[2312.06337](http://arxiv.org/abs/2312.06337)|null|
|**2023-12-11**|**Pipeline for performance evaluation of flavour tagging dedicated Graph Neural Network algorithms**|Greta Brianti et.al.|[2312.06245](http://arxiv.org/abs/2312.06245)|null|
|**2023-12-10**|**TransGlow: Attention-augmented Transduction model based on Graph Neural Networks for Water Flow Forecasting**|Naghmeh Shafiee Roudbari et.al.|[2312.05961](http://arxiv.org/abs/2312.05961)|null|
|**2023-12-10**|**Improving Subgraph-GNNs via Edge-Level Ego-Network Encodings**|Nurudin Alvarez-Gonzalez et.al.|[2312.05905](http://arxiv.org/abs/2312.05905)|**[link](https://github.com/nur-ag/elene)**|
|**2023-12-08**|**Synthesizing Traffic Datasets using Graph Neural Networks**|Daniel Rodriguez-Criado et.al.|[2312.05031](http://arxiv.org/abs/2312.05031)|**[link](https://github.com/gvogiatzis/trafficgen)**|
|**2023-12-08**|**Not All Negatives AreWorth Attending to: Meta-Bootstrapping Negative Sampling Framework for Link Prediction**|Yakun Wang et.al.|[2312.04815](http://arxiv.org/abs/2312.04815)|null|
|**2023-12-07**|**Efficient Large Language Models Fine-Tuning On Graphs**|Rui Xue et.al.|[2312.04737](http://arxiv.org/abs/2312.04737)|null|
|**2023-12-07**|**GraphMETRO: Mitigating Complex Distribution Shifts in GNNs via Mixture of Aligned Experts**|Shirley Wu et.al.|[2312.04693](http://arxiv.org/abs/2312.04693)|**[link](https://github.com/wuyxin/graphmetro)**|
|**2023-12-07**|**Constraints on the trilinear and quartic Higgs couplings from triple Higgs production at the LHC and beyond**|Panagiotis Stylianou et.al.|[2312.04646](http://arxiv.org/abs/2312.04646)|null|
|**2023-12-07**|**Relational Deep Learning: Graph Representation Learning on Relational Databases**|Matthias Fey et.al.|[2312.04615](http://arxiv.org/abs/2312.04615)|null|
|**2023-12-07**|**Graph Metanetworks for Processing Diverse Neural Architectures**|Derek Lim et.al.|[2312.04501](http://arxiv.org/abs/2312.04501)|null|
|**2023-12-07**|**GSGFormer: Generative Social Graph Transformer for Multimodal Pedestrian Trajectory Prediction**|Zhongchang Luo et.al.|[2312.04479](http://arxiv.org/abs/2312.04479)|null|
|**2023-12-07**|**Scalable Knowledge Graph Construction and Inference on Human Genome Variants**|Shivika Prasanna et.al.|[2312.04423](http://arxiv.org/abs/2312.04423)|null|
|**2023-12-07**|**Equivariant Scalar Fields for Molecular Docking with Fast Fourier Transforms**|Bowen Jing et.al.|[2312.04323](http://arxiv.org/abs/2312.04323)|**[link](https://github.com/bjing2016/scalar-fields)**|
|**2023-12-07**|**A Structural-Clustering Based Active Learning for Graph Neural Networks**|Ricky Maulana Fajri et.al.|[2312.04307](http://arxiv.org/abs/2312.04307)|**[link](https://github.com/rickymaulanafajri/spa)**|
|**2023-12-07**|**Simulating the Air Quality Impact of Prescribed Fires Using a Graph Neural Network-Based PM $_{2.5}$ Emissions Forecasting System**|Kyleen Liao et.al.|[2312.04291](http://arxiv.org/abs/2312.04291)|**[link](https://github.com/kyleenliao/Prescribed_Fire_PM2.5_Simulation)**|
|**2023-12-07**|**An Improved Scheduling with Advantage Actor-Critic for Storm Workloads**|Gaoqiang Dong et.al.|[2312.04126](http://arxiv.org/abs/2312.04126)|null|
|**2023-12-07**|**Breaking the Entanglement of Homophily and Heterophily in Semi-supervised Node Classification**|Henan Sun et.al.|[2312.04111](http://arxiv.org/abs/2312.04111)|null|
|**2023-12-07**|**Synergistic Signals: Exploiting Co-Engagement and Semantic Links via Graph Neural Networks**|Zijie Huang et.al.|[2312.04071](http://arxiv.org/abs/2312.04071)|null|
|**2023-12-07**|**Node-aware Bi-smoothing: Certified Robustness against Graph Injection Attacks**|Yuni Lai et.al.|[2312.03979](http://arxiv.org/abs/2312.03979)|null|
|**2023-12-06**|**What Planning Problems Can A Relational Neural Network Solve?**|Jiayuan Mao et.al.|[2312.03682](http://arxiv.org/abs/2312.03682)|**[link](https://github.com/concepts-ai/goal-regression-width)**|
|**2023-12-06**|**Augmenting optimization-based molecular design with graph neural networks**|Shiqiang Zhang et.al.|[2312.03613](http://arxiv.org/abs/2312.03613)|null|
|**2023-12-06**|**GraNet: A Multi-Level Graph Network for 6-DoF Grasp Pose Generation in Cluttered Scenes**|Haowen Wang et.al.|[2312.03345](http://arxiv.org/abs/2312.03345)|null|
|**2023-12-06**|**Enhancing Molecular Property Prediction via Mixture of Collaborative Experts**|Xu Yao et.al.|[2312.03292](http://arxiv.org/abs/2312.03292)|**[link](https://github.com/Hyacinth-YX/mixture-of-collaborative-experts)**|
|**2023-12-06**|**Multicoated and Folded Graph Neural Networks with Strong Lottery Tickets**|Jiale Yan et.al.|[2312.03236](http://arxiv.org/abs/2312.03236)|**[link](https://github.com/louivalley/slt-gnn)**|
|**2023-12-05**|**Neural Sign Actors: A diffusion model for 3D sign language production from text**|Vasileios Baltatzis et.al.|[2312.02702](http://arxiv.org/abs/2312.02702)|null|
|**2023-12-05**|**On the Initialization of Graph Neural Networks**|Jiahang Li et.al.|[2312.02622](http://arxiv.org/abs/2312.02622)|**[link](https://github.com/lspongebobjh/virgo_icml2023)**|
|**2023-12-05**|**A Neural Receiver for 5G NR Multi-user MIMO**|Sebastian Cammerer et.al.|[2312.02601](http://arxiv.org/abs/2312.02601)|null|
|**2023-12-05**|**MASP: Scalable GNN-based Planning for Multi-Agent Navigation**|Xinyi Yang et.al.|[2312.02522](http://arxiv.org/abs/2312.02522)|null|
|**2023-12-05**|**NeutronStream: A Dynamic GNN Training Framework with Sliding Window for Graph Streams**|Chaoyi Chen et.al.|[2312.02473](http://arxiv.org/abs/2312.02473)|null|
|**2023-12-05**|**Congestion-aware Distributed Task Offloading in Wireless Multi-hop Networks Using Graph Neural Networks**|Zhongyuan Zhao et.al.|[2312.02471](http://arxiv.org/abs/2312.02471)|**[link](https://github.com/zhongyuanzhao/multihop-offload)**|
|**2023-12-04**|**Dissecting Medical Referral Mechanisms in Health Services: Role of Physician Professional Networks**|Regina de Brito Duarte et.al.|[2312.02387](http://arxiv.org/abs/2312.02387)|null|
|**2023-12-04**|**On the Trade-Off between Stability and Representational Capacity in Graph Neural Networks**|Zhan Gao et.al.|[2312.02372](http://arxiv.org/abs/2312.02372)|null|
|**2023-12-04**|**GNN2R: Weakly-Supervised Rationale-Providing Question Answering over Knowledge Graphs**|Ruijie Wang et.al.|[2312.02317](http://arxiv.org/abs/2312.02317)|**[link](https://github.com/ruijie-wang-uzh/gnn2r)**|
|**2023-12-04**|**A Generative Self-Supervised Framework using Functional Connectivity in fMRI Data**|Jungwon Choi et.al.|[2312.01994](http://arxiv.org/abs/2312.01994)|null|
|**2023-12-04**|**HGPROMPT: Bridging Homogeneous and Heterogeneous Graphs for Few-shot Prompt Learning**|Xingtong Yu et.al.|[2312.01878](http://arxiv.org/abs/2312.01878)|null|
|**2023-12-04**|**The Self-Loop Paradox: Investigating the Impact of Self-Loops on Graph Neural Networks**|Moritz Lampert et.al.|[2312.01721](http://arxiv.org/abs/2312.01721)|**[link](https://github.com/m-lampert/self-loop-paradox)**|
|**2023-12-04**|**OCGEC: One-class Graph Embedding Classification for DNN Backdoor Detection**|Haoyu Jiang et.al.|[2312.01585](http://arxiv.org/abs/2312.01585)|**[link](https://github.com/jhy549/ocgec)**|
|**2023-12-04**|**RaftGP: Random Fast Graph Partitioning**|Yu Gao et.al.|[2312.01560](http://arxiv.org/abs/2312.01560)|null|
|**2023-12-03**|**Recurrent Distance-Encoding Neural Networks for Graph Representation Learning**|Yuhui Ding et.al.|[2312.01538](http://arxiv.org/abs/2312.01538)|**[link](https://github.com/skeletondyh/gred)**|
|**2023-12-03**|**Graph Coordinates and Conventional Neural Networks -- An Alternative for Graph Neural Networks**|Zheyi Qin et.al.|[2312.01342](http://arxiv.org/abs/2312.01342)|**[link](https://github.com/i721/GraphCoordinates)**|
|**2023-12-02**|**Mixed-Integer Optimisation of Graph Neural Networks for Computer-Aided Molecular Design**|Tom McDonald et.al.|[2312.01228](http://arxiv.org/abs/2312.01228)|null|
|**2023-12-01**|**Hypergraph Node Representation Learning with One-Stage Message Passing**|Shilin Qu et.al.|[2312.00336](http://arxiv.org/abs/2312.00336)|null|
|**2023-11-30**|**A Comparison Between Invariant and Equivariant Classical and Quantum Graph Neural Networks**|Roy T. Forestano et.al.|[2311.18672](http://arxiv.org/abs/2311.18672)|**[link](https://github.com/royforestano/2023_gsoc_ml4sci_qmlhep_gnn)**|
|**2023-11-30**|**Optimizing ZX-Diagrams with Deep Reinforcement Learning**|Maximilian Nägele et.al.|[2311.18588](http://arxiv.org/abs/2311.18588)|**[link](https://github.com/maxnaeg/zxreinforce)**|
|**2023-11-30**|**Multi-scale Iterative Refinement towards Robust and Versatile Molecular Docking**|Jiaxian Yan et.al.|[2311.18574](http://arxiv.org/abs/2311.18574)|null|
|**2023-11-30**|**Utilizing Radiomic Feature Analysis For Automated MRI Keypoint Detection: Enhancing Graph Applications**|Sahar Almahfouz Nasser et.al.|[2311.18281](http://arxiv.org/abs/2311.18281)|null|
|**2023-11-30**|**An Effective Universal Polynomial Basis for Spectral Graph Neural Networks**|Keke Huang et.al.|[2311.18177](http://arxiv.org/abs/2311.18177)|null|
|**2023-11-29**|**Enhancing Data-Assimilation in CFD using Graph Neural Networks**|Michele Quattromini et.al.|[2311.18027](http://arxiv.org/abs/2311.18027)|null|
|**2023-11-29**|**Reconstruction of electromagnetic showers in calorimeters using Deep Learning**|Polina Simkina et.al.|[2311.17914](http://arxiv.org/abs/2311.17914)|null|
|**2023-11-29**|**FastSample: Accelerating Distributed Graph Neural Network Training for Billion-Scale Graphs**|Hesham Mostafa et.al.|[2311.17847](http://arxiv.org/abs/2311.17847)|null|
|**2023-11-29**|**Propagate & Distill: Towards Effective Graph Learners Using Propagation-Embracing MLPs**|Yong-Min Shin et.al.|[2311.17781](http://arxiv.org/abs/2311.17781)|null|
|**2023-11-29**|**CrimeGNN: Harnessing the Power of Graph Neural Networks for Community Detection in Criminal Networks**|Chen Yang et.al.|[2311.17479](http://arxiv.org/abs/2311.17479)|null|
|**2023-11-29**|**GNNFlow: A Distributed Framework for Continuous Temporal GNN Learning on Dynamic Graphs**|Yuchen Zhong et.al.|[2311.17410](http://arxiv.org/abs/2311.17410)|**[link](https://github.com/jasperzhong/GNNFlow)**|
|**2023-11-29**|**The Devil is in the Data: Learning Fair Graph Neural Networks via Partial Knowledge Distillation**|Yuchang Zhu et.al.|[2311.17373](http://arxiv.org/abs/2311.17373)|**[link](https://github.com/zzoomd/fairgkd)**|
|**2023-11-29**|**How does spatial structure affect psychological restoration? A method based on Graph Neural Networks and Street View Imagery**|Haoran Ma et.al.|[2311.17361](http://arxiv.org/abs/2311.17361)|**[link](https://github.com/MMHHRR/Restoration_Topology)**|
|**2023-11-28**|**\texttt{GlycoNMR}: Dataset and benchmarks for NMR chemical shift prediction of carbohydrates with graph neural networks**|Zizhang Chen et.al.|[2311.17134](http://arxiv.org/abs/2311.17134)|null|
|**2023-11-28**|**Attentional Graph Neural Networks for Robust Massive Network Localization**|Wenzhong Yan et.al.|[2311.16856](http://arxiv.org/abs/2311.16856)|null|
|**2023-11-28**|**Hyper-Relational Knowledge Graph Neural Network for Next POI**|Jixiao Zhang et.al.|[2311.16683](http://arxiv.org/abs/2311.16683)|null|
|**2023-11-28**|**PyTorch Geometric High Order: A Unified Library for High Order Graph Neural Network**|Xiyuan Wang et.al.|[2311.16670](http://arxiv.org/abs/2311.16670)|**[link](https://github.com/graphpku/pygho)**|
|**2023-11-28**|**MultiModal-Learning for Predicting Molecular Properties: A Framework Based on Image and Graph Structures**|Zhuoyuan Wang et.al.|[2311.16666](http://arxiv.org/abs/2311.16666)|null|
|**2023-11-28**|**LasTGL: An Industrial Framework for Large-Scale Temporal Graph Learning**|Jintang Li et.al.|[2311.16605](http://arxiv.org/abs/2311.16605)|null|
|**2023-11-28**|**Evaluation of dynamic characteristics of power grid based on GNN and application on knowledge graph**|Hao Pei et.al.|[2311.16522](http://arxiv.org/abs/2311.16522)|null|
|**2023-11-27**|**A Graph Neural Network-Based QUBO-Formulated Hamiltonian-Inspired Loss Function for Combinatorial Optimization using Reinforcement Learning**|Redwan Ahmed Rizvee et.al.|[2311.16277](http://arxiv.org/abs/2311.16277)|null|
|**2023-11-27**|**Interactive Autonomous Navigation with Internal State Inference and Interactivity Estimation**|Jiachen Li et.al.|[2311.16091](http://arxiv.org/abs/2311.16091)|null|
|**2023-11-27**|**Soil Organic Carbon Estimation from Climate-related Features with Graph Neural Network**|Weiying Zhao et.al.|[2311.15979](http://arxiv.org/abs/2311.15979)|null|
|**2023-11-27**|**Over-Squashing in Riemannian Graph Neural Networks**|Julia Balla et.al.|[2311.15945](http://arxiv.org/abs/2311.15945)|null|
|**2023-11-27**|**Multi-Agent Reinforcement Learning for Power Control in Wireless Networks via Adaptive Graphs**|Lorenzo Mario Amorosa et.al.|[2311.15858](http://arxiv.org/abs/2311.15858)|null|
|**2023-11-27**|**A Social-aware Gaussian Pre-trained Model for Effective Cold-start Recommendation**|Siwei Liu et.al.|[2311.15790](http://arxiv.org/abs/2311.15790)|null|
|**2023-11-27**|**Attend Who is Weak: Enhancing Graph Condensation via Cross-Free Adversarial Training**|Xinglin Li et.al.|[2311.15772](http://arxiv.org/abs/2311.15772)|null|
|**2023-11-27**|**Out-of-Distribution Generalized Dynamic Graph Neural Network for Human Albumin Prediction**|Zeyang Zhang et.al.|[2311.15545](http://arxiv.org/abs/2311.15545)|null|
|**2023-11-26**|**Generalized Graph Prompt: Toward a Unification of Pre-Training and Downstream Tasks on Graphs**|Xingtong Yu et.al.|[2311.15317](http://arxiv.org/abs/2311.15317)|**[link](https://github.com/gmcmt/graph_prompt_extension)**|
|**2023-11-26**|**Low-Complexity Joint Beamforming for RIS-Assisted MU-MISO Systems Based on Model-Driven Deep Learning**|Weijie Jin et.al.|[2311.15313](http://arxiv.org/abs/2311.15313)|null|
|**2023-11-26**|**Solve Large-scale Unit Commitment Problems by Physics-informed Graph Learning**|Jingtao Qin et.al.|[2311.15216](http://arxiv.org/abs/2311.15216)|null|
|**2023-11-24**|**Fault Detection in Telecom Networks using Bi-level Federated Graph Neural Networks**|R. Bourgerie et.al.|[2311.14469](http://arxiv.org/abs/2311.14469)|null|
|**2023-11-24**|**Finite Volume Features, Global Geometry Representations, and Residual Training for Deep Learning-based CFD Simulation**|Loh Sher En Jessica et.al.|[2311.14464](http://arxiv.org/abs/2311.14464)|**[link](https://github.com/toggled/FvFGeo)**|
|**2023-11-24**|**BHGNN-RT: Network embedding for directed heterogeneous graphs**|Xiyang Sun et.al.|[2311.14404](http://arxiv.org/abs/2311.14404)|**[link](https://github.com/albertlordsun/bhgnn-rt)**|
|**2023-11-24**|**Cycle Invariant Positional Encoding for Graph Representation Learning**|Zuoyu Yan et.al.|[2311.14333](http://arxiv.org/abs/2311.14333)|**[link](https://github.com/pkuyzy/cyclenet)**|
|**2023-11-24**|**Large Language Models as Topological Structure Enhancers for Text-Attributed Graphs**|Shengyin Sun et.al.|[2311.14324](http://arxiv.org/abs/2311.14324)|null|
|**2023-11-24**|**AdaMedGraph: Adaboosting Graph Neural Networks for Personalized Medicine**|Jie Lian et.al.|[2311.14304](http://arxiv.org/abs/2311.14304)|null|
|**2023-11-24**|**Out-of-Distribution Generalized Dynamic Graph Neural Network with Disentangled Intervention and Invariance Promotion**|Zeyang Zhang et.al.|[2311.14255](http://arxiv.org/abs/2311.14255)|null|
|**2023-11-23**|**Exact Combinatorial Optimization with Temporo-Attentional Graph Neural Networks**|Mehdi Seyfi et.al.|[2311.13843](http://arxiv.org/abs/2311.13843)|null|
|**2023-11-22**|**Benchmarking Toxic Molecule Classification using Graph Neural Networks and Few Shot Learning**|Bhavya Mehta et.al.|[2311.13490](http://arxiv.org/abs/2311.13490)|null|
|**2023-11-22**|**Complexity-Guided Curriculum Learning for Text Graphs**|Nidhi Vakil et.al.|[2311.13472](http://arxiv.org/abs/2311.13472)|null|
|**2023-11-22**|**Accelerating Inference in Molecular Diffusion Models with Latent Representations of Protein Structure**|Ian Dunn et.al.|[2311.13466](http://arxiv.org/abs/2311.13466)|**[link](https://github.com/dunni3/keypoint-diffusion)**|
|**2023-11-22**|**From Images to Connections: Can DQN with GNNs learn the Strategic Game of Hex?**|Yannik Keller et.al.|[2311.13414](http://arxiv.org/abs/2311.13414)|**[link](https://github.com/yannikkellerde/gnn_hex)**|
|**2023-11-22**|**Comprehensive Evaluation of GNN Training Systems: A Data Management Perspective**|Hao Yuan et.al.|[2311.13279](http://arxiv.org/abs/2311.13279)|**[link](https://github.com/idc-neu/neutronbench)**|
|**2023-11-22**|**Hard Label Black Box Node Injection Attack on Graph Neural Networks**|Yu Zhou et.al.|[2311.13244](http://arxiv.org/abs/2311.13244)|**[link](https://github.com/bryanzhou008/hard_label_black_box_attack_gnn)**|
|**2023-11-22**|**NeutronOrch: Rethinking Sample-based GNN Training under CPU-GPU Heterogeneous Environments**|Xin Ai et.al.|[2311.13225](http://arxiv.org/abs/2311.13225)|null|
|**2023-11-21**|**Neural Graph Control Barrier Functions Guided Distributed Collision-avoidance Multi-agent Control**|Songyuan Zhang et.al.|[2311.13014](http://arxiv.org/abs/2311.13014)|**[link](https://github.com/MIT-REALM/gcbf-pytorch)**|
|**2023-11-21**|**Content Augmented Graph Neural Networks**|Fatemeh Gholamzadeh Nasrabadi et.al.|[2311.12741](http://arxiv.org/abs/2311.12741)|**[link](https://github.com/fatemehgholamzadeh/augss-gnn)**|
|**2023-11-21**|**Carbohydrate NMR chemical shift predictions using E(3) equivariant graph neural networks**|Maria Bånkestad et.al.|[2311.12657](http://arxiv.org/abs/2311.12657)|**[link](https://github.com/mariabankestad/geqshift)**|
|**2023-11-21**|**Careful Selection and Thoughtful Discarding: Graph Explicit Pooling Utilizing Discarded Nodes**|Chuang Liu et.al.|[2311.12644](http://arxiv.org/abs/2311.12644)|null|
|**2023-11-21**|**Hierarchical Joint Graph Learning and Multivariate Time Series Forecasting**|Juhyeon Kim et.al.|[2311.12630](http://arxiv.org/abs/2311.12630)|null|
|**2023-11-21**|**DeepTreeGAN: Fast Generation of High Dimensional Point Clouds**|Moritz Alfons Wilhelm Scham et.al.|[2311.12616](http://arxiv.org/abs/2311.12616)|**[link](https://github.com/degesim/chep23deeptreegan)**|
|**2023-11-21**|**Distilling particle knowledge for fast reconstruction at high-energy physics experiments**|Aritra Bal et.al.|[2311.12551](http://arxiv.org/abs/2311.12551)|null|
|**2023-11-21**|**A Survey of Graph Meets Large Language Model: Progress and Future Directions**|Yuhan Li et.al.|[2311.12399](http://arxiv.org/abs/2311.12399)|**[link](https://github.com/yhLeeee/Awesome-LLMs-in-Graph-tasks)**|
|**2023-11-21**|**Demystifying Graph Sparsification Algorithms in Graph Properties Preservation**|Yuhan Chen et.al.|[2311.12314](http://arxiv.org/abs/2311.12314)|**[link](https://github.com/yuhanchan/sparsification)**|
|**2023-11-21**|**Power grid operational risk assessment using graph neural network surrogates**|Yadong Zhang et.al.|[2311.12309](http://arxiv.org/abs/2311.12309)|null|
|**2023-11-21**|**ATLANTIC: Structure-Aware Retrieval-Augmented Language Model for Interdisciplinary Science**|Sai Munikoti et.al.|[2311.12289](http://arxiv.org/abs/2311.12289)|null|
|**2023-11-20**|**AMES: A Differentiable Embedding Space Selection Framework for Latent Graph Inference**|Yuan Lu et.al.|[2311.11891](http://arxiv.org/abs/2311.11891)|null|
|**2023-11-20**|**Robust Tumor Segmentation with Hyperspectral Imaging and Graph Neural Networks**|Mayar Lotfy et.al.|[2311.11782](http://arxiv.org/abs/2311.11782)|null|
|**2023-11-20**|**Unveiling the Unseen Potential of Graph Learning through MLPs: Effective Graph Learners Using Propagation-Embracing MLPs**|Yong-Min Shin et.al.|[2311.11759](http://arxiv.org/abs/2311.11759)|null|
|**2023-11-20**|**CSGNN: Conquering Noisy Node labels via Dynamic Class-wise Selection**|Yifan Li et.al.|[2311.11473](http://arxiv.org/abs/2311.11473)|null|
|**2023-11-19**|**Self-Supervised Pretraining for Heterogeneous Hypergraph Neural Networks**|Abdalgader Abubaker et.al.|[2311.11368](http://arxiv.org/abs/2311.11368)|null|
|**2023-11-19**|**Local environment-based machine learning for molecular adsorption energy prediction**|Yifan Li et.al.|[2311.11364](http://arxiv.org/abs/2311.11364)|null|
|**2023-11-19**|**A Universal Framework for Accurate and Efficient Geometric Deep Learning of Molecular Systems**|Shuo Zhang et.al.|[2311.11228](http://arxiv.org/abs/2311.11228)|**[link](https://github.com/XieResearchGroup/Physics-aware-Multiplex-GNN)**|
|**2023-11-18**|**Benchmarking Machine Learning Models for Quantum Error Correction**|Tim Fu et.al.|[2311.11167](http://arxiv.org/abs/2311.11167)|null|
|**2023-11-18**|**Environment-Aware Dynamic Graph Learning for Out-of-Distribution Generalization**|Haonan Yuan et.al.|[2311.11114](http://arxiv.org/abs/2311.11114)|**[link](https://github.com/ringbdstack/eagle)**|
|**2023-11-17**|**Multiparameter Persistent Homology for Molecular Property Prediction**|Andac Demir et.al.|[2311.10808](http://arxiv.org/abs/2311.10808)|null|
|**2023-11-17**|**TacFR-Gripper: A Reconfigurable Fin Ray-Based Compliant Robotic Gripper with Tactile Skin for In-Hand Manipulation**|Qingzheng Cong et.al.|[2311.10611](http://arxiv.org/abs/2311.10611)|null|
|**2023-11-17**|**Graph Neural Networks for Pressure Estimation in Water Distribution Systems**|Huy Truong et.al.|[2311.10579](http://arxiv.org/abs/2311.10579)|**[link](https://github.com/ditec-project/gnn-pressure-estimation)**|
|**2023-11-17**|**Graph Sparsifications using Neural Network Assisted Monte Carlo Tree Search**|Alvin Chiu et.al.|[2311.10316](http://arxiv.org/abs/2311.10316)|**[link](https://github.com/abureyanahmed/gnn-msts-sparsification)**|
|**2023-11-17**|**Multiscale Hodge Scattering Networks for Data Analysis**|Naoki Saito et.al.|[2311.10270](http://arxiv.org/abs/2311.10270)|null|
|**2023-11-16**|**Algebraic Topological Networks via the Persistent Local Homology Sheaf**|Gabriele Cesa et.al.|[2311.10156](http://arxiv.org/abs/2311.10156)|null|
|**2023-11-16**|**MEGA: A Memory-Efficient GNN Accelerator Exploiting Degree-Aware Mixed-Precision Quantization**|Zeyu Zhu et.al.|[2311.09775](http://arxiv.org/abs/2311.09775)|null|
|**2023-11-15**|**HypOp: Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks**|Nasimeh Heydaribeni et.al.|[2311.09375](http://arxiv.org/abs/2311.09375)|**[link](https://github.com/nasheydari/HypOp)**|
|**2023-11-15**|**Disentangling the Potential Impacts of Papers into Diffusion, Conformity, and Contribution Values**|Zhikai Xue et.al.|[2311.09262](http://arxiv.org/abs/2311.09262)|**[link](https://github.com/ecnu-text-computing/dppdcc)**|
|**2023-11-15**|**Emerging Drug Interaction Prediction Enabled by Flow-based Graph Neural Network with Biomedical Network**|Yongqi Zhang et.al.|[2311.09261](http://arxiv.org/abs/2311.09261)|**[link](https://github.com/lars-research/emergnn)**|
|**2023-11-15**|**Leaving No Branches Behind: Predicting Baryonic Properties of Galaxies from Merger Trees**|Chen-Yu Chuang et.al.|[2311.09162](http://arxiv.org/abs/2311.09162)|null|
|**2023-11-15**|**X-GRL: An Empirical Assessment of Explainable GNN-DRL in B5G/6G Networks**|Farhad Rezazadeh et.al.|[2311.08798](http://arxiv.org/abs/2311.08798)|null|
|**2023-11-15**|**Language Semantic Graph Guided Data-Efficient Learning**|Wenxuan Ma et.al.|[2311.08782](http://arxiv.org/abs/2311.08782)|**[link](https://github.com/bit-da/lsg)**|
|**2023-11-14**|**SceneScore: Learning a Cost Function for Object Arrangement**|Ivan Kapelyukh et.al.|[2311.08530](http://arxiv.org/abs/2311.08530)|null|
|**2023-11-14**|**Uplift Modeling based on Graph Neural Network Combined with Causal Knowledge**|Haowen Wang et.al.|[2311.08434](http://arxiv.org/abs/2311.08434)|**[link](https://github.com/xy2119/Causal_Knowledge_GNN)**|
|**2023-11-14**|**Mobility-Induced Graph Learning for WiFi Positioning**|Kyuwon Han et.al.|[2311.08271](http://arxiv.org/abs/2311.08271)|null|
|**2023-11-14**|**Evaluating Neighbor Explainability for Graph Neural Networks**|Oscar Llorente et.al.|[2311.08118](http://arxiv.org/abs/2311.08118)|**[link](https://github.com/ericssonresearch/gnn-neighbors-xai)**|
|**2023-11-14**|**Higher-Order Expander Graph Propagation**|Thomas Christie et.al.|[2311.07966](http://arxiv.org/abs/2311.07966)|null|
|**2023-11-14**|**Self-supervised Heterogeneous Graph Variational Autoencoders**|Yige Zhao et.al.|[2311.07929](http://arxiv.org/abs/2311.07929)|null|
|**2023-11-13**|**ResMGCN: Residual Message Graph Convolution Network for Fast Biomedical Interactions Discovering**|Zecheng Yin et.al.|[2311.07632](http://arxiv.org/abs/2311.07632)|**[link](https://github.com/Yonggie/ResMGCN)**|
|**2023-11-13**|**Interpretable Fine-Tuning for Graph Neural Network Surrogate Models**|Shivam Barwey et.al.|[2311.07548](http://arxiv.org/abs/2311.07548)|null|
|**2023-11-13**|**Three-dimensional granular flow simulation using graph neural network-based learned simulator**|Yongjin Choi et.al.|[2311.07416](http://arxiv.org/abs/2311.07416)|null|
|**2023-11-13**|**ADAMM: Anomaly Detection of Attributed Multi-graphs with Metadata: A Unified Neural Network Approach**|Konstantinos Sotiropoulos et.al.|[2311.07355](http://arxiv.org/abs/2311.07355)|**[link](https://github.com/konsotirop/adamm)**|
|**2023-11-13**|**Connecting the Dots: Graph Neural Network Powered Ensemble and Classification of Medical Images**|Aryan Singh et.al.|[2311.07321](http://arxiv.org/abs/2311.07321)|**[link](https://github.com/aryan-at-ul/aics_2023_submission)**|
|**2023-11-13**|**Optical Quantum Sensing for Agnostic Environments via Deep Learning**|Zeqiao Zhou et.al.|[2311.07203](http://arxiv.org/abs/2311.07203)|null|
|**2023-11-13**|**Untargeted Black-box Attacks for Social Recommendations**|Wenqi Fan et.al.|[2311.07127](http://arxiv.org/abs/2311.07127)|null|
|**2023-11-13**|**Collaborative Goal Tracking of Multiple Mobile Robots Based on Geometric Graph Neural Network**|Qingquan Lin et.al.|[2311.07105](http://arxiv.org/abs/2311.07105)|null|
|**2023-11-12**|**Contractive Systems Improve Graph Neural Networks Against Adversarial Attacks**|Moshe Eliasof et.al.|[2311.06942](http://arxiv.org/abs/2311.06942)|null|
|**2023-11-12**|**Preserving Node-level Privacy in Graph Neural Networks**|Zihang Xiang et.al.|[2311.06888](http://arxiv.org/abs/2311.06888)|null|
|**2023-11-12**|**GraNNDis: Efficient Unified Distributed Training Framework for Deep GNNs on Large Clusters**|Jaeyong Song et.al.|[2311.06837](http://arxiv.org/abs/2311.06837)|**[link](https://github.com/ais-snu/granndis_artifact)**|
|**2023-11-10**|**FourierGNN: Rethinking Multivariate Time Series Forecasting from a Pure Graph Perspective**|Kun Yi et.al.|[2311.06190](http://arxiv.org/abs/2311.06190)|**[link](https://github.com/aikunyi/fouriergnn)**|
|**2023-11-10**|**Interpretable Graph Anomaly Detection using Gradient Attention Maps**|Yifei Yang et.al.|[2311.06153](http://arxiv.org/abs/2311.06153)|null|
|**2023-11-10**|**Going beyond persistent homology using persistent homology**|Johanna Immonen et.al.|[2311.06152](http://arxiv.org/abs/2311.06152)|null|
|**2023-11-10**|**Privacy-Preserving Individual-Level COVID-19 Infection Prediction via Federated Graph Learning**|Wenjie Fu et.al.|[2311.06049](http://arxiv.org/abs/2311.06049)|**[link](https://github.com/wjfu99/fl-epidemic)**|
|**2023-11-09**|**Dirichlet Energy Enhancement of Graph Neural Networks by Framelet Augmentation**|Jialin Chen et.al.|[2311.05767](http://arxiv.org/abs/2311.05767)|null|
|**2023-11-09**|**Generative Explanations for Graph Neural Network: Methods and Evaluations**|Jialin Chen et.al.|[2311.05764](http://arxiv.org/abs/2311.05764)|null|
|**2023-11-09**|**SIRE: scale-invariant, rotation-equivariant estimation of artery orientations using graph neural networks**|Dieuwertje Alblas et.al.|[2311.05400](http://arxiv.org/abs/2311.05400)|null|
|**2023-11-09**|**Atom: Neural Traffic Compression with Spatio-Temporal Graph Neural Networks**|Paul Almasan et.al.|[2311.05337](http://arxiv.org/abs/2311.05337)|**[link](https://github.com/bnn-upc/atom_neural_traffic_compression)**|
|**2023-11-09**|**Mixture of Weak & Strong Experts on Graphs**|Hanqing Zeng et.al.|[2311.05185](http://arxiv.org/abs/2311.05185)|**[link](https://github.com/facebookresearch/mowst-gnn)**|
|**2023-11-09**|**Materials Properties Prediction (MAPP): Empowering the prediction of material properties solely based on chemical formulas**|Si-Da Xue et.al.|[2311.05133](http://arxiv.org/abs/2311.05133)|**[link](https://github.com/qjhong/mapp_api)**|
|**2023-11-08**|**Identifying Semantic Component for Robust Molecular Property Prediction**|Zijian Li et.al.|[2311.04837](http://arxiv.org/abs/2311.04837)|**[link](https://github.com/dmirlab-group/sci)**|
|**2023-11-08**|**Learning Robust Multi-Scale Representation for Neural Radiance Fields from Unposed Images**|Nishant Jain et.al.|[2311.04521](http://arxiv.org/abs/2311.04521)|null|
|**2023-11-08**|**Conversation Understanding using Relational Temporal Graph Neural Networks with Auxiliary Cross-Modality Interaction**|Cam-Van Thi Nguyen et.al.|[2311.04507](http://arxiv.org/abs/2311.04507)|**[link](https://github.com/leson502/CORECT_EMNLP2023)**|
|**2023-11-08**|**RDGCN: Reinforced Dependency Graph Convolutional Network for Aspect-based Sentiment Analysis**|Xusheng Zhao et.al.|[2311.04467](http://arxiv.org/abs/2311.04467)|**[link](https://github.com/rdgcn/rdgcn)**|
|**2023-11-08**|**PepLand: a large-scale pre-trained peptide representation model for a comprehensive landscape of both canonical and non-canonical amino acids**|Ruochi Zhang et.al.|[2311.04419](http://arxiv.org/abs/2311.04419)|**[link](https://github.com/zhangruochi/pepland)**|
|**2023-11-08**|**AI-accelerated Discovery of Altermagnetic Materials**|Ze-Feng Gao et.al.|[2311.04418](http://arxiv.org/abs/2311.04418)|**[link](https://github.com/zfgao66/mataltmag)**|
|**2023-11-07**|**GPT-ST: Generative Pre-Training of Spatio-Temporal Graph Neural Networks**|Zhonghang Li et.al.|[2311.04245](http://arxiv.org/abs/2311.04245)|**[link](https://github.com/hkuds/gpt-st)**|
|**2023-11-07**|**Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter**|Mulugeta Weldezgina Asres et.al.|[2311.04190](http://arxiv.org/abs/2311.04190)|null|
|**2023-11-07**|**Graph Neural Networks for Power Grid Operational Risk Assessment**|Yadong Zhang et.al.|[2311.03661](http://arxiv.org/abs/2311.03661)|null|
|**2023-11-07**|**GNN-Based Beamforming for Sum-Rate Maximization in MU-MISO Networks**|Yuhang Li et.al.|[2311.03659](http://arxiv.org/abs/2311.03659)|null|
|**2023-11-06**|**Brain Networks and Intelligence: A Graph Neural Network Based Approach to Resting State fMRI Data**|Bishal Thapaliya et.al.|[2311.03520](http://arxiv.org/abs/2311.03520)|**[link](https://github.com/bishalth01/Brain-ROI-Aware-Graph-Isomorphism-Networks-BrainRGIN-)**|
|**2023-11-06**|**PowerFlowNet: Leveraging Message Passing GNNs for Improved Power Flow Approximation**|Nan Lin et.al.|[2311.03415](http://arxiv.org/abs/2311.03415)|**[link](https://github.com/distributionnetworkstudelft/poweflownet)**|
|**2023-11-06**|**Exploiting Latent Attribute Interaction with Transformer on Heterogeneous Information Networks**|Zeyuan Zhao et.al.|[2311.03275](http://arxiv.org/abs/2311.03275)|**[link](https://github.com/zzyzeyuan/hetcan)**|
|**2023-11-06**|**From Coupled Oscillators to Graph Neural Networks: Reducing Over-smoothing via a Kuramoto Model-based Approach**|Tuan Nguyen et.al.|[2311.03260](http://arxiv.org/abs/2311.03260)|null|
|**2023-11-06**|**Algebraic Dynamical Systems in Machine Learning**|Iolo Jones et.al.|[2311.03118](http://arxiv.org/abs/2311.03118)|null|
|**2023-11-06**|**Equivariance Is Not All You Need: Characterizing the Utility of Equivariant Graph Neural Networks for Particle Physics Tasks**|Savannah Thais et.al.|[2311.03094](http://arxiv.org/abs/2311.03094)|null|
|**2023-11-06**|**Contrastive Multi-Level Graph Neural Networks for Session-based Recommendation**|Fuyun Wang et.al.|[2311.02938](http://arxiv.org/abs/2311.02938)|null|
|**2023-11-06**|**Edge2Node: Reducing Edge Prediction to Node Classification**|Zahed Rahmati et.al.|[2311.02921](http://arxiv.org/abs/2311.02921)|**[link](https://github.com/arahmatiiii/E2N)**|
|**2023-11-06**|**Distributed Matrix-Based Sampling for Graph Neural Network Training**|Alok Tripathy et.al.|[2311.02909](http://arxiv.org/abs/2311.02909)|null|
|**2023-11-06**|**Lightweight equivariant interaction graph neural network for accurate and efficient interatomic potential and force predictions**|Ziduo Yang et.al.|[2311.02869](http://arxiv.org/abs/2311.02869)|**[link](https://github.com/guaguabujianle/leignn)**|
|**2023-11-06**|**Prioritized Propagation in Graph Neural Networks**|Yao Cheng et.al.|[2311.02832](http://arxiv.org/abs/2311.02832)|null|
|**2023-11-05**|**ELEGANT: Certified Defense on the Fairness of Graph Neural Networks**|Yushun Dong et.al.|[2311.02757](http://arxiv.org/abs/2311.02757)|**[link](https://github.com/yushundong/elegant)**|
|**2023-11-03**|**Generalization of Graph-Based Active Learning Relaxation Strategies Across Materials**|Xiaoxiao Wang et.al.|[2311.01987](http://arxiv.org/abs/2311.01987)|**[link](https://github.com/ulissigroup/finetuna-2023-manuscript)**|
|**2023-11-03**|**Constructing Temporal Dynamic Knowledge Graphs from Interactive Text-based Games**|Keunwoo Peter Yu et.al.|[2311.01928](http://arxiv.org/abs/2311.01928)|**[link](https://github.com/yukw777/temporal-discrete-graph-updater)**|
|**2023-11-03**|**Calibrate and Boost Logical Expressiveness of GNN Over Multi-Relational and Temporal Graphs**|Yeyuan Chen et.al.|[2311.01647](http://arxiv.org/abs/2311.01647)|**[link](https://github.com/hdmmblz/multi-graph)**|
|**2023-11-02**|**Better Fair than Sorry: Adversarial Missing Data Imputation for Fair GNNs**|Debolina Halder Lina et.al.|[2311.01591](http://arxiv.org/abs/2311.01591)|null|
|**2023-11-02**|**Domain Adaptive Graph Neural Networks for Constraining Cosmological Parameters Across Multiple Data Sets**|Andrea Roncoli et.al.|[2311.01588](http://arxiv.org/abs/2311.01588)|**[link](https://github.com/deepskies/gnn_domainadapt)**|
|**2023-11-02**|**ATGNN: Audio Tagging Graph Neural Network**|Shubhr Singh et.al.|[2311.01526](http://arxiv.org/abs/2311.01526)|null|
|**2023-11-02**|**Long-Range Neural Atom Learning for Molecular Graphs**|Xuan Li et.al.|[2311.01276](http://arxiv.org/abs/2311.01276)|**[link](https://github.com/tmlr-group/neuralatom)**|
|**2023-11-02**|**Attacking Graph Neural Networks with Bit Flips: Weisfeiler and Lehman Go Indifferent**|Lorenz Kummer et.al.|[2311.01205](http://arxiv.org/abs/2311.01205)|null|
|**2023-11-02**|**Combating Bilateral Edge Noise for Robust Link Prediction**|Zhanke Zhou et.al.|[2311.01196](http://arxiv.org/abs/2311.01196)|**[link](https://github.com/tmlr-group/rgib)**|
|**2023-11-02**|**Better with Less: A Data-Active Perspective on Pre-Training Graph Neural Networks**|Jiarong Xu et.al.|[2311.01038](http://arxiv.org/abs/2311.01038)|**[link](https://github.com/galina0217/apt)**|
|**2023-11-02**|**Accelerated Data-Driven Discovery and Screening of Two-Dimensional Magnets Using Graph Neural Networks**|Ahmed Elrashidy et.al.|[2311.00939](http://arxiv.org/abs/2311.00939)|null|
|**2023-11-01**|**Rational design of oxide catalysts for OER with OC22**|Richard Tran et.al.|[2311.00784](http://arxiv.org/abs/2311.00784)|null|
|**2023-11-01**|**Kronecker-Factored Approximate Curvature for Modern Neural Network Architectures**|Runa Eschenhagen et.al.|[2311.00636](http://arxiv.org/abs/2311.00636)|null|
|**2023-11-01**|**Robust Graph Clustering via Meta Weighting for Noisy Graphs**|Hyeonsoo Jo et.al.|[2311.00322](http://arxiv.org/abs/2311.00322)|**[link](https://github.com/hyeonsoojo/metagc)**|
|**2023-11-01**|**Entity Alignment Method of Science and Technology Patent based on Graph Convolution Network and Information Fusion**|Runze Fang et.al.|[2311.00300](http://arxiv.org/abs/2311.00300)|null|
|**2023-11-01**|**Semantic Representation Learning of Scientific Literature based on Adaptive Feature and Graph Neural Network**|Hongrui Gao et.al.|[2311.00296](http://arxiv.org/abs/2311.00296)|null|
|**2023-11-01**|**Active Neural Topological Mapping for Multi-Agent Exploration**|Xinyi Yang et.al.|[2311.00252](http://arxiv.org/abs/2311.00252)|null|
|**2023-10-31**|**Graph Neural Networks for Road Safety Modeling: Datasets and Evaluations for Accident Analysis**|Abhinav Nippani et.al.|[2311.00164](http://arxiv.org/abs/2311.00164)|**[link](https://github.com/virtuosoresearch/ml4roadsafety)**|
|**2023-10-31**|**Stochastic Gradient Descent for Gaussian Processes Done Right**|Jihao Andreas Lin et.al.|[2310.20581](http://arxiv.org/abs/2310.20581)|**[link](https://github.com/cambridge-mlg/sgd-gp)**|
|**2023-10-31**|**Privacy-preserving design of graph neural networks with applications to vertical federated learning**|Ruofan Wu et.al.|[2310.20552](http://arxiv.org/abs/2310.20552)|null|
|**2023-10-31**|**Enhancing Graph Neural Networks with Quantum Computed Encodings**|Slimane Thabet et.al.|[2310.20519](http://arxiv.org/abs/2310.20519)|null|
|**2023-10-31**|**Collaborative Decision-Making Using Spatiotemporal Graphs in Connected Autonomy**|Peng Gao et.al.|[2310.20491](http://arxiv.org/abs/2310.20491)|null|
|**2023-10-31**|**Distil the informative essence of loop detector data set: Is network-level traffic forecasting hungry for more data?**|Guopeng Li et.al.|[2310.20366](http://arxiv.org/abs/2310.20366)|**[link](https://github.com/romainlitud/uncertainty-aware-traffic-speed-flow-demand-prediction)**|
|**2023-10-30**|**On the data-driven description of lattice materials mechanics**|Ismael Ben-Yelun et.al.|[2310.20056](http://arxiv.org/abs/2310.20056)|null|
|**2023-10-30**|**Interpretable Prototype-based Graph Information Bottleneck**|Sangwoo Seo et.al.|[2310.19906](http://arxiv.org/abs/2310.19906)|**[link](https://github.com/sang-woo-seo/pgib)**|
|**2023-10-30**|**Autoregressive Renaissance in Neural PDE Solvers**|Yolanne Yi Ran Lee et.al.|[2310.19763](http://arxiv.org/abs/2310.19763)|null|
|**2023-10-30**|**Modeling Dynamics over Meshes with Gauge Equivariant Nonlinear Message Passing**|Jung Yeon Park et.al.|[2310.19589](http://arxiv.org/abs/2310.19589)|null|
|**2023-10-30**|**Coarse-grained crystal graph neural networks for reticular materials design**|Vadim Korolev et.al.|[2310.19500](http://arxiv.org/abs/2310.19500)|null|
|**2023-10-29**|**MAG-GNN: Reinforcement Learning Boosted Graph Neural Network**|Lecheng Kong et.al.|[2310.19142](http://arxiv.org/abs/2310.19142)|null|
|**2023-10-29**|**The Weisfeiler-Leman Dimension of Existential Conjunctive Queries**|Andreas Göbel et.al.|[2310.19006](http://arxiv.org/abs/2310.19006)|null|
|**2023-10-29**|**Hyperbolic Graph Neural Networks at Scale: A Meta Learning Approach**|Nurendra Choudhary et.al.|[2310.18918](http://arxiv.org/abs/2310.18918)|null|
|**2023-10-29**|**Topological, or Non-topological? A Deep Learning Based Prediction**|Ashiqur Rasul et.al.|[2310.18907](http://arxiv.org/abs/2310.18907)|null|
|**2023-10-28**|**Rethinking Semi-Supervised Imbalanced Node Classification from Bias-Variance Decomposition**|Divin Yan et.al.|[2310.18765](http://arxiv.org/abs/2310.18765)|**[link](https://github.com/yanliang3612/revar)**|
|**2023-10-28**|**Curriculum Learning for Graph Neural Networks: Which Edges Should We Learn First**|Zheng Zhang et.al.|[2310.18735](http://arxiv.org/abs/2310.18735)|**[link](https://github.com/rollingstonezz/curriculum_learning_for_gnns)**|
|**2023-10-28**|**Maximum Independent Set: Self-Training through Dynamic Programming**|Lorenzo Brusca et.al.|[2310.18672](http://arxiv.org/abs/2310.18672)|**[link](https://github.com/LIONS-EPFL/dynamic-MIS)**|
|**2023-10-27**|**One Model Fits All: Cross-Region Taxi-Demand Forecasting**|Ren Ozeki et.al.|[2310.18215](http://arxiv.org/abs/2310.18215)|null|
|**2023-10-27**|**Disentangled Representation Learning with Large Language Models for Text-Attributed Graphs**|Yijian Qin et.al.|[2310.18152](http://arxiv.org/abs/2310.18152)|null|
|**2023-10-26**|**Graph Neural Networkrs for Enhanced Decoding of Quantum LDPC Codes**|Anqi Gong et.al.|[2310.17758](http://arxiv.org/abs/2310.17758)|**[link](https://github.com/gongaa/feedback-gnn)**|
|**2023-10-26**|**GNN-GMVO: Graph Neural Networks for Optimizing Gross Merchandise Value in Similar Item Recommendation**|Ramin Giahi et.al.|[2310.17732](http://arxiv.org/abs/2310.17732)|null|
|**2023-10-26**|**Improving Traffic Density Forecasting in Intelligent Transportation Systems Using Gated Graph Neural Networks**|Razib Hayat Khan et.al.|[2310.17729](http://arxiv.org/abs/2310.17729)|null|
|**2023-10-26**|**Do Graph Neural Networks Dream of Landau Damping? Insights from Kinetic Simulations of a Plasma Sheet Model**|Diogo D Carvalho et.al.|[2310.17646](http://arxiv.org/abs/2310.17646)|**[link](https://github.com/diogodcarvalho/gns-sheet-model)**|
|**2023-10-26**|**BLIS-Net: Classifying and Analyzing Signals on Graphs**|Charles Xu et.al.|[2310.17579](http://arxiv.org/abs/2310.17579)|null|
|**2023-10-26**|**A Hybrid Graph Network for Complex Activity Detection in Video**|Salman Khan et.al.|[2310.17493](http://arxiv.org/abs/2310.17493)|null|
|**2023-10-26**|**Circuit as Set of Points**|Jialv Zou et.al.|[2310.17418](http://arxiv.org/abs/2310.17418)|**[link](https://github.com/hustvl/circuitformer)**|
|**2023-10-26**|**Enhancing Graph Neural Networks with Structure-Based Prompt**|Qingqing Ge et.al.|[2310.17394](http://arxiv.org/abs/2310.17394)|**[link](https://github.com/gqq1210/psp)**|
|**2023-10-26**|**Network Intrusion Detection with Edge-Directed Graph Multi-Head Attention Networks**|Xiang Li et.al.|[2310.17348](http://arxiv.org/abs/2310.17348)|null|
|**2023-10-26**|**Graphical Object-Centric Actor-Critic**|Leonid Ugadiarov et.al.|[2310.17178](http://arxiv.org/abs/2310.17178)|null|
|**2023-10-26**|**Explainable Spatio-Temporal Graph Neural Networks**|Jiabin Tang et.al.|[2310.17149](http://arxiv.org/abs/2310.17149)|**[link](https://github.com/hkuds/stexplainer)**|
|**2023-10-26**|**Network Design through Graph Neural Networks: Identifying Challenges and Improving Performance**|Donald Loveland et.al.|[2310.17100](http://arxiv.org/abs/2310.17100)|null|
|**2023-10-25**|**RDBench: ML Benchmark for Relational Databases**|Zizhao Zhang et.al.|[2310.16837](http://arxiv.org/abs/2310.16837)|null|
|**2023-10-25**|**AI Agent as Urban Planner: Steering Stakeholder Dynamics in Urban Planning via Consensus-based Multi-Agent Reinforcement Learning**|Kejiang Qian et.al.|[2310.16772](http://arxiv.org/abs/2310.16772)|null|
|**2023-10-25**|**$\mathbb{VD}$-$\mathbb{GR}$: Boosting $\mathbb{V}$isual $\mathbb{D}$ialog with Cascaded Spatial-Temporal Multi-Modal $\mathbb{GR}$ aphs**|Adnen Abdessaied et.al.|[2310.16590](http://arxiv.org/abs/2310.16590)|null|
|**2023-10-25**|**Graph Agent: Explicit Reasoning Agent for Graphs**|Qinyong Wang et.al.|[2310.16421](http://arxiv.org/abs/2310.16421)|null|
|**2023-10-25**|**Graph Neural Networks with a Distribution of Parametrized Graphs**|See Hian Lee et.al.|[2310.16401](http://arxiv.org/abs/2310.16401)|null|
|**2023-10-25**|**DyExplainer: Explainable Dynamic Graph Neural Networks**|Tianchun Wang et.al.|[2310.16375](http://arxiv.org/abs/2310.16375)|null|
|**2023-10-24**|**Graph Deep Learning for Time Series Forecasting**|Andrea Cini et.al.|[2310.15978](http://arxiv.org/abs/2310.15978)|null|
|**2023-10-24**|**Representation Learning with Large Language Models for Recommendation**|Xubin Ren et.al.|[2310.15950](http://arxiv.org/abs/2310.15950)|**[link](https://github.com/hkuds/rlmrec)**|
|**2023-10-24**|**ABKD: Graph Neural Network Compression with Attention-Based Knowledge Distillation**|Anshul Ahluwalia et.al.|[2310.15938](http://arxiv.org/abs/2310.15938)|null|
|**2023-10-24**|**Using Causality-Aware Graph Neural Networks to Predict Temporal Centralities in Dynamic Graphs**|Franziska Heeg et.al.|[2310.15865](http://arxiv.org/abs/2310.15865)|**[link](https://github.com/pathpy/pathpyg)**|
|**2023-10-24**|**Re-Temp: Relation-Aware Temporal Representation Learning for Temporal Knowledge Graph Completion**|Kunze Wang et.al.|[2310.15722](http://arxiv.org/abs/2310.15722)|**[link](https://github.com/adlnlp/re-temp)**|
|**2023-10-24**|**Solving large flexible job shop scheduling instances by generating a diverse set of scheduling policies with deep reinforcement learning**|Imanol Echeverria et.al.|[2310.15706](http://arxiv.org/abs/2310.15706)|null|
|**2023-10-24**|**Momentum Gradient-based Untargeted Attack on Hypergraph Neural Networks**|Yang Chen et.al.|[2310.15656](http://arxiv.org/abs/2310.15656)|null|
|**2023-10-24**|**Deceptive Fairness Attacks on Graphs via Meta Learning**|Jian Kang et.al.|[2310.15653](http://arxiv.org/abs/2310.15653)|**[link](https://github.com/jiank2/fate)**|
|**2023-10-24**|**RecipeMeta: Metapath-enhanced Recipe Recommendation on Heterogeneous Recipe Network**|Jialiang Shi et.al.|[2310.15593](http://arxiv.org/abs/2310.15593)|null|
|**2023-10-24**|**Cross-view Self-localization from Synthesized Scene-graphs**|Ryogo Yamamoto et.al.|[2310.15504](http://arxiv.org/abs/2310.15504)|null|
|**2023-10-23**|**Accelerate Microstructure Evolution Simulation Using Graph Neural Networks with Adaptive Spatiotemporal Resolution**|Shaoxun Fan et.al.|[2310.15153](http://arxiv.org/abs/2310.15153)|null|
|**2023-10-23**|**Projected Stochastic Gradient Descent with Quantum Annealed Binary Gradients**|Maximilian Krahn et.al.|[2310.15128](http://arxiv.org/abs/2310.15128)|null|
|**2023-10-23**|**GRENADE: Graph-Centric Language Model for Self-Supervised Representation Learning on Text-Attributed Graphs**|Yichuan Li et.al.|[2310.15109](http://arxiv.org/abs/2310.15109)|**[link](https://github.com/bigheiniu/grenade)**|
|**2023-10-23**|**Neural Snowflakes: Universal Latent Graph Inference via Trainable Latent Geometries**|Haitz Sáez de Ocáriz Borde et.al.|[2310.15003](http://arxiv.org/abs/2310.15003)|null|
|**2023-10-23**|**A Study on Knowledge Graph Embeddings and Graph Neural Networks for Web Of Things**|Rohith Teja Mittakola et.al.|[2310.14866](http://arxiv.org/abs/2310.14866)|**[link](https://github.com/kgrl2021/submission-one)**|
|**2023-10-23**|**ULTRA-DP: Unifying Graph Pre-training with Multi-task Graph Dual Prompt**|Mouxiang Chen et.al.|[2310.14845](http://arxiv.org/abs/2310.14845)|**[link](https://github.com/keytoyze/ultra-dp)**|
|**2023-10-23**|**Rethinking Tokenizer and Decoder in Masked Graph Modeling for Molecules**|Zhiyuan Liu et.al.|[2310.14753](http://arxiv.org/abs/2310.14753)|**[link](https://github.com/syr-cn/simsgt)**|
|**2023-10-23**|**A Hybrid GNN approach for predicting node data for 3D meshes**|Shwetha Salimath et.al.|[2310.14707](http://arxiv.org/abs/2310.14707)|null|
|**2023-10-23**|**GNNEvaluator: Evaluating GNN Performance On Unseen Graphs Without Labels**|Xin Zheng et.al.|[2310.14586](http://arxiv.org/abs/2310.14586)|null|
|**2023-10-23**|**Multimodal Graph Learning for Modeling Emerging Pandemics with Big Data**|Khanh-Tung Tran et.al.|[2310.14549](http://arxiv.org/abs/2310.14549)|**[link](https://github.com/khanhtungtran/mgl4mep)**|
|**2023-10-20**|**ReLM: Leveraging Language Models for Enhanced Chemical Reaction Prediction**|Yaorui Shi et.al.|[2310.13590](http://arxiv.org/abs/2310.13590)|**[link](https://github.com/syr-cn/relm)**|
|**2023-10-20**|**SPARE: A Single-Pass Neural Model for Relational Databases**|Benjamin Hilprecht et.al.|[2310.13581](http://arxiv.org/abs/2310.13581)|null|
|**2023-10-20**|**Towards Enhancing Relational Rules for Knowledge Graph Link Prediction**|Shuhan Wu et.al.|[2310.13411](http://arxiv.org/abs/2310.13411)|**[link](https://github.com/ninggirsu/run-gnn)**|
|**2023-10-20**|**TempGNN: Temporal Graph Neural Networks for Dynamic Session-Based Recommendations**|Eunkyu Oh et.al.|[2310.13249](http://arxiv.org/abs/2310.13249)|null|
|**2023-10-20**|**FLEE-GNN: A Federated Learning System for Edge-Enhanced Graph Neural Network in Analyzing Geospatial Resilience of Multicommodity Food Flows**|Yuxiao Qu et.al.|[2310.13248](http://arxiv.org/abs/2310.13248)|**[link](https://github.com/geods/flee-gnn)**|
|**2023-10-19**|**Heterogeneous Graph Neural Networks for Data-driven Traffic Assignment**|Tong Liu et.al.|[2310.13193](http://arxiv.org/abs/2310.13193)|null|
|**2023-10-19**|**Graph Neural Networks with polynomial activations have limited expressivity**|Sammy Khalife et.al.|[2310.13139](http://arxiv.org/abs/2310.13139)|null|
|**2023-10-19**|**Agri-GNN: A Novel Genotypic-Topological Graph Neural Network Framework Built on GraphSAGE for Optimized Yield Prediction**|Aditya Gupta et.al.|[2310.13037](http://arxiv.org/abs/2310.13037)|null|
|**2023-10-19**|**Exploring Graph Neural Networks for Indian Legal Judgment Prediction**|Mann Khatri et.al.|[2310.12800](http://arxiv.org/abs/2310.12800)|null|
|**2023-10-23**|**Pretraining Language Models with Text-Attributed Heterogeneous Graphs**|Tao Zou et.al.|[2310.12580](http://arxiv.org/abs/2310.12580)|**[link](https://github.com/hope-rita/thlm)**|
|**2023-10-19**|**Open-World Lifelong Graph Learning**|Marcel Hoffmann et.al.|[2310.12565](http://arxiv.org/abs/2310.12565)|**[link](https://github.com/bobowner/open-world-lgl)**|
|**2023-10-19**|**DepWiGNN: A Depth-wise Graph Neural Network for Multi-hop Spatial Reasoning in Text**|Shuaiyi Li et.al.|[2310.12557](http://arxiv.org/abs/2310.12557)|**[link](https://github.com/syon-li/depwignn)**|
|**2023-10-19**|**WeaveNet for Approximating Two-sided Matching Problems**|Shusaku Sone et.al.|[2310.12515](http://arxiv.org/abs/2310.12515)|null|
|**2023-10-19**|**MuseGNN: Interpretable and Convergent Graph Neural Network Layers at Scale**|Haitian Jiang et.al.|[2310.12457](http://arxiv.org/abs/2310.12457)|null|
|**2023-10-19**|**Cooperative Minibatching in Graph Neural Networks**|Muhammed Fatih Balin et.al.|[2310.12403](http://arxiv.org/abs/2310.12403)|**[link](https://github.com/gt-tdalab/dgl-coop)**|
|**2023-10-18**|**Equipping Federated Graph Neural Networks with Structure-aware Group Fairness**|Nan Cui et.al.|[2310.12350](http://arxiv.org/abs/2310.12350)|**[link](https://github.com/yuening-lab/f2gnn)**|
|**2023-10-18**|**Building a Graph-based Deep Learning network model from captured traffic traces**|Carlos Güemes-Palau et.al.|[2310.11889](http://arxiv.org/abs/2310.11889)|null|
|**2023-10-18**|**Towards Graph Foundation Models: A Survey and Beyond**|Jiawei Liu et.al.|[2310.11829](http://arxiv.org/abs/2310.11829)|null|
|**2023-10-18**|**NeuroCUT: A Neural Approach for Robust Graph Partitioning**|Rishi Shah et.al.|[2310.11787](http://arxiv.org/abs/2310.11787)|**[link](https://github.com/idea-iitd/neurocut)**|
|**2023-10-19**|**A Quasi-Wasserstein Loss for Learning Graph Neural Networks**|Minjie Cheng et.al.|[2310.11762](http://arxiv.org/abs/2310.11762)|**[link](https://github.com/sds-lab/qw_loss)**|
|**2023-10-18**|**Federated Heterogeneous Graph Neural Network for Privacy-preserving Recommendation**|Bo Yan et.al.|[2310.11730](http://arxiv.org/abs/2310.11730)|null|
|**2023-10-18**|**Learning Co-Speech Gesture for Multimodal Aphasia Type Detection**|Daeun Lee et.al.|[2310.11710](http://arxiv.org/abs/2310.11710)|**[link](https://github.com/dsail-skku/multimodal-aphasia-type-detection_emnlp_2023)**|
|**2023-10-18**|**Hetero $^2$ Net: Heterophily-aware Representation Learning on Heterogenerous Graphs**|Jintang Li et.al.|[2310.11664](http://arxiv.org/abs/2310.11664)|null|
|**2023-10-17**|**RekomGNN: Visualizing, Contextualizing and Evaluating Graph Neural Networks Recommendations**|Camelia D. Brumar et.al.|[2310.11562](http://arxiv.org/abs/2310.11562)|null|
|**2023-10-17**|**VcT: Visual change Transformer for Remote Sensing Image Change Detection**|Bo Jiang et.al.|[2310.11417](http://arxiv.org/abs/2310.11417)|**[link](https://github.com/event-ahu/vct_remote_sensing_change_detection)**|
|**2023-10-17**|**Hybrid quantum-classical graph neural networks for tumor classification in digital pathology**|Anupama Ray et.al.|[2310.11353](http://arxiv.org/abs/2310.11353)|null|
|**2023-10-17**|**Self-supervision meets kernel graph neural models: From architecture to augmentations**|Jiawang Dan et.al.|[2310.11281](http://arxiv.org/abs/2310.11281)|null|
|**2023-10-18**|**Graph Neural Networks for Recommendation: Reproducibility, Graph Topology, and Node Representation**|Daniele Malitesta et.al.|[2310.11270](http://arxiv.org/abs/2310.11270)|**[link](https://github.com/sisinflab/log-2023-gnns-recsys)**|
|**2023-10-17**|**Accurate prediction of international trade flows: Leveraging knowledge graphs and their embeddings**|Diego Rincon-Yanez et.al.|[2310.11161](http://arxiv.org/abs/2310.11161)|null|
|**2023-10-17**|**CSG: Curriculum Representation Learning for Signed Graph**|Zeyu Zhang et.al.|[2310.11083](http://arxiv.org/abs/2310.11083)|**[link](https://github.com/alex-zeyu/csg)**|
|**2023-10-17**|**Multi-omics Sampling-based Graph Transformer for Synthetic Lethality Prediction**|Xusheng Zhao et.al.|[2310.11082](http://arxiv.org/abs/2310.11082)|null|
|**2023-10-17**|**Fast Graph Condensation with Structure-based Neural Tangent Kernel**|Lin Wang et.al.|[2310.11046](http://arxiv.org/abs/2310.11046)|**[link](https://github.com/wanglin0126/gcsntk)**|
|**2023-10-17**|**SignGT: Signed Attention-based Graph Transformer for Graph Representation Learning**|Jinsong Chen et.al.|[2310.11025](http://arxiv.org/abs/2310.11025)|null|
|**2023-10-17**|**Accelerating Scalable Graph Neural Network Inference with Node-Adaptive Propagation**|Xinyi Gao et.al.|[2310.10998](http://arxiv.org/abs/2310.10998)|null|
|**2023-10-13**|**Graph Condensation via Eigenbasis Matching**|Yang Liu et.al.|[2310.09202](http://arxiv.org/abs/2310.09202)|**[link](https://github.com/liuyang-tian/gdem)**|
|**2023-10-12**|**Heterophily-Based Graph Neural Network for Imbalanced Classification**|Zirui Liang et.al.|[2310.08725](http://arxiv.org/abs/2310.08725)|null|
|**2023-10-12**|**Infinite Width Graph Neural Networks for Node Regression/ Classification**|Yunus Cobanoglu et.al.|[2310.08176](http://arxiv.org/abs/2310.08176)|**[link](https://github.com/yCobanoglu/infinite-width-gnns)**|
|**2023-10-12**|**Multi-Scale Spatial-Temporal Recurrent Networks for Traffic Flow Prediction**|Haiyang Liu et.al.|[2310.08138](http://arxiv.org/abs/2310.08138)|null|
|**2023-10-12**|**Graph-SCP: Accelerating Set Cover Problems with Graph Neural Networks**|Zohair Shafi et.al.|[2310.07979](http://arxiv.org/abs/2310.07979)|**[link](https://github.com/zohairshafi/Graph-SCP)**|
|**2023-10-11**|**Enhanced sampling of Crystal Nucleation with Graph Representation Learnt Variables**|Ziyue Zou et.al.|[2310.07927](http://arxiv.org/abs/2310.07927)|null|
|**2023-10-11**|**Global Minima, Recoverability Thresholds, and Higher-Order Structure in GNNS**|Drake Brown et.al.|[2310.07667](http://arxiv.org/abs/2310.07667)|null|
|**2023-10-11**|**Graph Transformer Network for Flood Forecasting with Heterogeneous Covariates**|Jimeng Shi et.al.|[2310.07631](http://arxiv.org/abs/2310.07631)|null|
|**2023-10-11**|**GMOCAT: A Graph-Enhanced Multi-Objective Method for Computerized Adaptive Testing**|Hangyu Wang et.al.|[2310.07477](http://arxiv.org/abs/2310.07477)|**[link](https://github.com/justarter/gmocat)**|
|**2023-10-11**|**Non-backtracking Graph Neural Networks**|Seonghyun Park et.al.|[2310.07430](http://arxiv.org/abs/2310.07430)|**[link](https://github.com/seonghyun26/nba-gnn)**|
|**2023-10-11**|**Are GATs Out of Balance?**|Nimrah Mustafa et.al.|[2310.07235](http://arxiv.org/abs/2310.07235)|null|
|**2023-10-11**|**My Brother Helps Me: Node Injection Based Adversarial Attack on Social Bot Detection**|Lanjun Wang et.al.|[2310.07159](http://arxiv.org/abs/2310.07159)|null|
|**2023-10-11**|**GraphCloak: Safeguarding Task-specific Knowledge within Graph-structured Data from Unauthorized Exploitation**|Yixin Liu et.al.|[2310.07100](http://arxiv.org/abs/2310.07100)|null|
|**2023-10-10**|**Neural Relational Inference with Fast Modular Meta-learning**|Ferran Alet et.al.|[2310.07015](http://arxiv.org/abs/2310.07015)|**[link](https://github.com/FerranAlet/modular-metalearning)**|
|**2023-10-10**|**Accelerated Modelling of Interfaces for Electronic Devices using Graph Neural Networks**|Pratik Brahma et.al.|[2310.06995](http://arxiv.org/abs/2310.06995)|null|
|**2023-10-12**|**Flood and Echo: Algorithmic Alignment of GNNs with Distributed Computing**|Joël Mathys et.al.|[2310.06970](http://arxiv.org/abs/2310.06970)|null|
|**2023-10-10**|**Learning Multiplex Embeddings on Text-rich Networks with One Text Encoder**|Bowen Jin et.al.|[2310.06684](http://arxiv.org/abs/2310.06684)|**[link](https://github.com/petergriffinjin/metag)**|
|**2023-10-10**|**On the importance of catalyst-adsorbate 3D interactions for relaxed energy predictions**|Alvaro Carbonero et.al.|[2310.06682](http://arxiv.org/abs/2310.06682)|null|
|**2023-10-10**|**TANGO: Time-Reversal Latent GraphODE for Multi-Agent Dynamical Systems**|Zijie Huang et.al.|[2310.06427](http://arxiv.org/abs/2310.06427)|null|
|**2023-10-10**|**Advective Diffusion Transformers for Topological Generalization in Graph Learning**|Qitian Wu et.al.|[2310.06417](http://arxiv.org/abs/2310.06417)|null|
|**2023-10-10**|**Adversarial Robustness in Graph Neural Networks: A Hamiltonian Approach**|Kai Zhao et.al.|[2310.06396](http://arxiv.org/abs/2310.06396)|**[link](https://github.com/zknus/neurips-2023-hang-robustness)**|
|**2023-10-10**|**SCAR: Power Side-Channel Analysis at RTL-Level**|Amisha Srivastava et.al.|[2310.06257](http://arxiv.org/abs/2310.06257)|null|
|**2023-10-09**|**Robust Angular Synchronization via Directed Graph Neural Networks**|Yixuan He et.al.|[2310.05842](http://arxiv.org/abs/2310.05842)|**[link](https://github.com/sherylhyx/gnn_sync)**|
|**2023-10-09**|**Nonlinear Correct and Smooth for Semi-Supervised Learning**|Yuanhang Shao et.al.|[2310.05757](http://arxiv.org/abs/2310.05757)|null|
|**2023-10-09**|**WeatherGNN: Exploiting Complicated Relationships in Numerical Weather Prediction Bias Correction**|Binqing Wu et.al.|[2310.05517](http://arxiv.org/abs/2310.05517)|null|
|**2023-10-08**|**Tailoring Self-Attention for Graph via Rooted Subtrees**|Siyuan Huang et.al.|[2310.05296](http://arxiv.org/abs/2310.05296)|**[link](https://github.com/lumia-group/subtree-attention)**|
|**2023-10-08**|**PointGAT: A quantum chemical property prediction model integrating graph attention and 3D geometry**|Rong Zhang et.al.|[2310.05217](http://arxiv.org/abs/2310.05217)|null|
|**2023-10-08**|**GSLB: The Graph Structure Learning Benchmark**|Zhixun Li et.al.|[2310.05174](http://arxiv.org/abs/2310.05174)|**[link](https://github.com/gsl-benchmark/gslb)**|
|**2023-10-08**|**How Graph Neural Networks Learn: Lessons from Training Dynamics in Function Space**|Chenxiao Yang et.al.|[2310.05105](http://arxiv.org/abs/2310.05105)|**[link](https://github.com/chr26195/residualpropagation)**|
|**2023-10-07**|**Beyond Text: A Deep Dive into Large Language Models' Ability on Understanding Graph Data**|Yuntong Hu et.al.|[2310.04944](http://arxiv.org/abs/2310.04944)|null|
|**2023-10-07**|**Hybrid Recommendation System using Graph Neural Network and BERT Embeddings**|Shashidhar Reddy Javaji et.al.|[2310.04878](http://arxiv.org/abs/2310.04878)|null|
|**2023-10-07**|**Label-free Node Classification on Graphs with Large Language Models (LLMS)**|Zhikai Chen et.al.|[2310.04668](http://arxiv.org/abs/2310.04668)|**[link](https://github.com/currytang/llmgnn)**|
|**2023-10-06**|**Non-Redundant Graph Neural Networks with Improved Expressiveness**|Franka Bause et.al.|[2310.04190](http://arxiv.org/abs/2310.04190)|null|
|**2023-10-09**|**Dynamic Relation-Attentive Graph Neural Networks for Fraud Detection**|Heehyeon Kim et.al.|[2310.04171](http://arxiv.org/abs/2310.04171)|**[link](https://github.com/bdi-lab/drag)**|
|**2023-10-09**|**AUTOPARLLM: GNN-Guided Automatic Code Parallelization using Large Language Models**|Quazi Ishtiaque Mahmud et.al.|[2310.04047](http://arxiv.org/abs/2310.04047)|null|
|**2023-10-05**|**Fishnets: Information-Optimal, Scalable Aggregation for Sets and Graphs**|T. Lucas Makinen et.al.|[2310.03812](http://arxiv.org/abs/2310.03812)|null|
|**2023-10-05**|**GRAPES: Learning to Sample Graphs for Scalable Graph Neural Networks**|Taraneh Younesian et.al.|[2310.03399](http://arxiv.org/abs/2310.03399)|**[link](https://github.com/dfdazac/grapes)**|
|**2023-10-05**|**Fragment-based Pretraining and Finetuning on Molecular Graphs**|Kha-Dinh Luong et.al.|[2310.03274](http://arxiv.org/abs/2310.03274)|**[link](https://github.com/lvkd84/graphfp)**|
|**2023-10-04**|**Deep reinforcement learning for machine scheduling: Methodology, the state-of-the-art, and future directions**|Maziyar Khadivi et.al.|[2310.03195](http://arxiv.org/abs/2310.03195)|null|
|**2023-10-04**|**Graph data modelling for outcome prediction in oropharyngeal cancer patients**|Nithya Bhasker et.al.|[2310.02931](http://arxiv.org/abs/2310.02931)|null|
|**2023-10-05**|**Rayleigh Quotient Graph Neural Networks for Graph-level Anomaly Detection**|Xiangyu Dong et.al.|[2310.02861](http://arxiv.org/abs/2310.02861)|**[link](https://github.com/xydong127/rqgnn)**|
|**2023-10-04**|**Graph Neural Networks and Time Series as Directed Graphs for Quality Recognition**|Angelica Simonetti et.al.|[2310.02774](http://arxiv.org/abs/2310.02774)|null|
|**2023-10-04**|**Learning adjacency matrix for dynamic graph neural network**|Osama Ahmad et.al.|[2310.02606](http://arxiv.org/abs/2310.02606)|null|
|**2023-10-04**|**Neural Bayes Estimators for Irregular Spatial Data using Graph Neural Networks**|Matthew Sainsbury-Dale et.al.|[2310.02600](http://arxiv.org/abs/2310.02600)|**[link](https://github.com/msainsburydale/neuralestimatorsgnn)**|
|**2023-10-04**|**On the Stability of Expressive Positional Encodings for Graph Neural Networks**|Yinan Huang et.al.|[2310.02579](http://arxiv.org/abs/2310.02579)|**[link](https://github.com/Graph-COM/SPE)**|
|**2023-10-04**|**Stand for Something or Fall for Everything: Predict Misinformation Spread with Stance-Aware Graph Neural Networks**|Zihan Chen et.al.|[2310.02568](http://arxiv.org/abs/2310.02568)|null|
|**2023-10-03**|**EGraFFBench: Evaluation of Equivariant Graph Neural Network Force Fields for Atomistic Simulations**|Vaibhav Bihani et.al.|[2310.02428](http://arxiv.org/abs/2310.02428)|null|
|**2023-10-05**|**Probabilistically Rewired Message-Passing Neural Networks**|Chendi Qian et.al.|[2310.02156](http://arxiv.org/abs/2310.02156)|**[link](https://github.com/chendiqian/PR-MPNN)**|
|**2023-10-03**|**Graph Neural Network-based EEG Classification: A Survey**|Dominik Klepl et.al.|[2310.02152](http://arxiv.org/abs/2310.02152)|null|
|**2023-10-03**|**Controlling Topic-Focus Articulation in Meaning-to-Text Generation using Graph Neural Networks**|Chunliu Wang et.al.|[2310.02053](http://arxiv.org/abs/2310.02053)|null|
|**2023-10-03**|**SelfGraphVQA: A Self-Supervised Graph Neural Network for Scene-based Question Answering**|Bruno Souza et.al.|[2310.01842](http://arxiv.org/abs/2310.01842)|null|
|**2023-10-03**|**Towards Robust Fidelity for Evaluating Explainability of Graph Neural Networks**|Xu Zheng et.al.|[2310.01820](http://arxiv.org/abs/2310.01820)|**[link](https://github.com/AslanDing/Fidelity)**|
|**2023-10-02**|**Transformers are efficient hierarchical chemical graph learners**|Zihan Pengmei et.al.|[2310.01704](http://arxiv.org/abs/2310.01704)|**[link](https://github.com/zpengmei/SubFormer-Spec)**|
|**2023-10-02**|**Score dynamics: scaling molecular dynamics with picosecond timesteps via conditional diffusion model**|Tim Hsu et.al.|[2310.01678](http://arxiv.org/abs/2310.01678)|**[link](https://github.com/llnl/graphite)**|
|**2023-10-02**|**Locality-Aware Graph-Rewiring in GNNs**|Federico Barbero et.al.|[2310.01668](http://arxiv.org/abs/2310.01668)|null|
|**2023-10-02**|**Operator Learning Meets Numerical Analysis: Improving Neural Networks through Iterative Methods**|Emanuele Zappala et.al.|[2310.01618](http://arxiv.org/abs/2310.01618)|null|
|**2023-10-02**|**Cooperative Graph Neural Networks**|Ben Finkelshtein et.al.|[2310.01267](http://arxiv.org/abs/2310.01267)|**[link](https://github.com/benfinkelshtein/cognn)**|
|**2023-10-02**|**Learning Decentralized Flocking Controllers with Spatio-Temporal Graph Neural Network**|Siji Chen et.al.|[2309.17437](http://arxiv.org/abs/2309.17437)|null|
|**2023-09-29**|**DREAM: Decentralized Reinforcement Learning for Exploration and Efficient Energy Management in Multi-Robot Systems**|Dipam Patel et.al.|[2309.17433](http://arxiv.org/abs/2309.17433)|null|
|**2023-09-29**|**Networked Inequality: Preferential Attachment Bias in Graph Neural Network Link Prediction**|Arjun Subramonian et.al.|[2309.17417](http://arxiv.org/abs/2309.17417)|**[link](https://github.com/arjunsubramonian/link_bias_amplification)**|
|**2023-09-29**|**Machine Learning for Practical Quantum Error Mitigation**|Haoran Liao et.al.|[2309.17368](http://arxiv.org/abs/2309.17368)|**[link](https://github.com/qiskit-community/blackwater)**|
|**2023-09-29**|**Asynchronous Graph Generators**|Christopher P. Ley et.al.|[2309.17335](http://arxiv.org/abs/2309.17335)|**[link](https://github.com/christopherley/asyncgraphgenerator)**|
|**2023-09-29**|**Meta-Path Learning for Multi-relational Graph Neural Networks**|Francesco Ferrini et.al.|[2309.17113](http://arxiv.org/abs/2309.17113)|**[link](https://github.com/francescoferrini/multirelationalgnn)**|
|**2023-10-02**|**On the Power of the Weisfeiler-Leman Test for Graph Motif Parameters**|Matthias Lanzinger et.al.|[2309.17053](http://arxiv.org/abs/2309.17053)|null|
|**2023-09-29**|**Controlling Continuous Relaxation for Combinatorial Optimization**|Yuma Ichikawa et.al.|[2309.16965](http://arxiv.org/abs/2309.16965)|**[link](https://github.com/Yuma-Ichikawa/CRA4CO)**|
|**2023-09-29**|**G4SATBench: Benchmarking and Advancing SAT Solving with Graph Neural Networks**|Zhaoyu Li et.al.|[2309.16941](http://arxiv.org/abs/2309.16941)|**[link](https://github.com/zhaoyu-li/g4satbench)**|
|**2023-09-29**|**ACGAN-GNNExplainer: Auxiliary Conditional Generative Explainer for Graph Neural Networks**|Yiqiao Li et.al.|[2309.16918](http://arxiv.org/abs/2309.16918)|null|
|**2023-09-28**|**Reusability report: Prostate cancer stratification with diverse biologically-informed neural architectures**|Christian Pedersen et.al.|[2309.16645](http://arxiv.org/abs/2309.16645)|**[link](https://github.com/zhanglab-aim/cancer-net)**|
|**2023-09-28**|**MHG-GNN: Combination of Molecular Hypergraph Grammar with Graph Neural Network**|Akihiro Kishimoto et.al.|[2309.16374](http://arxiv.org/abs/2309.16374)|null|
|**2023-09-28**|**LagrangeBench: A Lagrangian Fluid Mechanics Benchmarking Suite**|Artur P. Toshev et.al.|[2309.16342](http://arxiv.org/abs/2309.16342)|**[link](https://github.com/tumaer/lagrangebench)**|
|**2023-09-28**|**GInX-Eval: Towards In-Distribution Evaluation of Graph Neural Network Explanations**|Kenza Amara et.al.|[2309.16223](http://arxiv.org/abs/2309.16223)|null|
|**2023-09-28**|**Distill to Delete: Unlearning in Graph Networks with Knowledge Distillation**|Yash Sinha et.al.|[2309.16173](http://arxiv.org/abs/2309.16173)|null|
|**2023-09-27**|**GNNHLS: Evaluating Graph Neural Network Inference via High-Level Synthesis**|Chenfeng Zhao et.al.|[2309.16022](http://arxiv.org/abs/2309.16022)|**[link](https://github.com/chenfengzhao/gnnhls)**|
|**2023-09-27**|**Line Graph Neural Networks for Link Weight Prediction**|Jinbi Liang et.al.|[2309.15728](http://arxiv.org/abs/2309.15728)|null|
|**2023-09-27**|**GPIP: Geometry-enhanced Pre-training on Interatomic Potentials**|Taoyong Cui et.al.|[2309.15718](http://arxiv.org/abs/2309.15718)|**[link](https://github.com/cuitaoyong/gpip)**|
|**2023-09-27**|**Residual Scheduling: A New Reinforcement Learning Approach to Solving Job Shop Scheduling Problem**|Kuo-Hao Ho et.al.|[2309.15517](http://arxiv.org/abs/2309.15517)|null|
|**2023-09-27**|**GNN4EEG: A Benchmark and Toolkit for Electroencephalography Classification with Graph Neural Network**|Kaiyuan Zhang et.al.|[2309.15515](http://arxiv.org/abs/2309.15515)|**[link](https://github.com/miracle-2001/gnn4eeg)**|
|**2023-09-27**|**Graph Neural Prompting with Large Language Models**|Yijun Tian et.al.|[2309.15427](http://arxiv.org/abs/2309.15427)|**[link](https://github.com/meettyj/gnp)**|
|**2023-09-27**|**Adversarial Object Rearrangement in Constrained Environments with Heterogeneous Graph Neural Networks**|Xibai Lou et.al.|[2309.15378](http://arxiv.org/abs/2309.15378)|null|
|**2023-09-26**|**Label Deconvolution for Node Representation Learning on Large-scale Attributed Graphs against Learning Bias**|Zhihao Shi et.al.|[2309.14907](http://arxiv.org/abs/2309.14907)|null|
|**2023-09-26**|**Graph Neural Network Based Method for Path Planning Problem**|Xingrong Diao et.al.|[2309.14845](http://arxiv.org/abs/2309.14845)|null|
|**2023-09-26**|**A Comparative Study of Population-Graph Construction Methods and Graph Neural Networks for Brain Age Regression**|Kyriaki-Margarita Bintsi et.al.|[2309.14816](http://arxiv.org/abs/2309.14816)|**[link](https://github.com/bintsi/brain-age-population-graphs)**|
|**2023-09-26**|**XGV-BERT: Leveraging Contextualized Language Model and Graph Neural Network for Efficient Software Vulnerability Detection**|Vu Le Anh Quan et.al.|[2309.14677](http://arxiv.org/abs/2309.14677)|null|
|**2023-09-26**|**ALEX: Towards Effective Graph Transfer Learning with Noisy Labels**|Jingyang Yuan et.al.|[2309.14673](http://arxiv.org/abs/2309.14673)|null|
|**2023-09-25**|**Learning dislocation dynamics mobility laws from large-scale MD simulations**|Nicolas Bertin et.al.|[2309.14450](http://arxiv.org/abs/2309.14450)|null|
|**2023-09-25**|**HyperTrack: Neural Combinatorics for High Energy Physics**|Mikael Mieskolainen et.al.|[2309.14113](http://arxiv.org/abs/2309.14113)|**[link](https://github.com/mieskolainen/hypertrack)**|
|**2023-09-25**|**HiGNN-TTS: Hierarchical Prosody Modeling with Graph Neural Networks for Expressive Long-form TTS**|Dake Guo et.al.|[2309.13907](http://arxiv.org/abs/2309.13907)|null|
|**2023-09-25**|**TouchUp-G: Improving Feature Representation through Graph-Centric Finetuning**|Jing Zhu et.al.|[2309.13885](http://arxiv.org/abs/2309.13885)|null|
|**2023-09-25**|**Estimating Treatment Effects Under Heterogeneous Interference**|Xiaofeng Lin et.al.|[2309.13884](http://arxiv.org/abs/2309.13884)|**[link](https://github.com/linxf208/hinite)**|
|**2023-09-23**|**Enhancing Student Performance Prediction on Learnersourced Questions with SGNN-LLM Synergy**|Lin Ni et.al.|[2309.13500](http://arxiv.org/abs/2309.13500)|null|
|**2023-09-23**|**A Model-Agnostic Graph Neural Network for Integrating Local and Global Information**|Wenzhuo Zhou et.al.|[2309.13459](http://arxiv.org/abs/2309.13459)|null|
|**2023-09-23**|**Deciphering Spatio-Temporal Graph Forecasting: A Causal Lens and Treatment**|Yutong Xia et.al.|[2309.13378](http://arxiv.org/abs/2309.13378)|null|
|**2023-09-22**|**Graph Neural Network for Stress Predictions in Stiffened Panels Under Uniform Loading**|Yuecheng Cai et.al.|[2309.13022](http://arxiv.org/abs/2309.13022)|null|
|**2023-09-22**|**Higher-order Graph Convolutional Network with Flower-Petals Laplacians on Simplicial Complexes**|Yiming Huang et.al.|[2309.12971](http://arxiv.org/abs/2309.12971)|**[link](https://github.com/yiminghh/higcn)**|
|**2023-09-22**|**ProtoEM: A Prototype-Enhanced Matching Framework for Event Relation Extraction**|Zhilei Hu et.al.|[2309.12892](http://arxiv.org/abs/2309.12892)|null|
|**2023-09-21**|**SALSA-CLRS: A Sparse and Scalable Benchmark for Algorithmic Reasoning**|Julian Minder et.al.|[2309.12253](http://arxiv.org/abs/2309.12253)|**[link](https://github.com/jkminder/salsa-clrs)**|
|**2023-09-21**|**Dynamic Hypergraph Structure Learning for Traffic Flow Forecasting**|Yusheng Zhao et.al.|[2309.12028](http://arxiv.org/abs/2309.12028)|null|
|**2023-09-21**|**Activation Compression of Graph Neural Networks using Block-wise Quantization with Improved Variance Minimization**|Sebastian Eliassen et.al.|[2309.11856](http://arxiv.org/abs/2309.11856)|**[link](https://github.com/saintslab/i-exact)**|
|**2023-09-20**|**Large-scale Pretraining Improves Sample Efficiency of Active Learning based Molecule Virtual Screening**|Zhonglin Cao et.al.|[2309.11687](http://arxiv.org/abs/2309.11687)|null|
|**2023-09-23**|**Using deep learning to construct stochastic local search SAT solvers with performance bounds**|Maximilian Kramer et.al.|[2309.11452](http://arxiv.org/abs/2309.11452)|**[link](https://github.com/porscheofficial/sls_sat_solving_with_deep_learning)**|
|**2023-09-20**|**Improving Article Classification with Edge-Heterogeneous Graph Neural Networks**|Khang Ly et.al.|[2309.11341](http://arxiv.org/abs/2309.11341)|**[link](https://github.com/lyvykhang/edgehetero-nodeproppred)**|
|**2023-09-20**|**InkStream: Real-time GNN Inference on Streaming Graphs via Incremental Update**|Dan Wu et.al.|[2309.11071](http://arxiv.org/abs/2309.11071)|**[link](https://github.com/WuDan0399/InkStream)**|
|**2023-09-21**|**Localize, Retrieve and Fuse: A Generalized Framework for Free-Form Question Answering over Tables**|Wenting Zhao et.al.|[2309.11049](http://arxiv.org/abs/2309.11049)|null|
|**2023-09-20**|**Accurate and Scalable Estimation of Epistemic Uncertainty for Graph Neural Networks**|Puja Trivedi et.al.|[2309.10976](http://arxiv.org/abs/2309.10976)|null|
|**2023-09-19**|**Crypto'Graph: Leveraging Privacy-Preserving Distributed Link Prediction for Robust Graph Learning**|Sofiane Azogagh et.al.|[2309.10890](http://arxiv.org/abs/2309.10890)|null|
|**2023-09-20**|**AI Foundation Models for Weather and Climate: Applications, Design, and Implementation**|S. Karthik Mukkavilli et.al.|[2309.10808](http://arxiv.org/abs/2309.10808)|null|
|**2023-09-19**|**Graph Neural Networks for Dynamic Modeling of Roller Bearing**|Vinay Sharma et.al.|[2309.10418](http://arxiv.org/abs/2309.10418)|null|
|**2023-09-19**|**Graph Contrastive Learning Meets Graph Meta Learning: A Unified Method for Few-shot Node Tasks**|Hao Liu et.al.|[2309.10376](http://arxiv.org/abs/2309.10376)|**[link](https://github.com/haoliu-cola/cola)**|
|**2023-09-18**|**Asynchronous Perception-Action-Communication with Graph Neural Networks**|Saurav Agarwal et.al.|[2309.10164](http://arxiv.org/abs/2309.10164)|null|
|**2023-09-18**|**Efficient Low-Rank GNN Defense Against Structural Attacks**|Abdullah Alchihabi et.al.|[2309.10136](http://arxiv.org/abs/2309.10136)|null|
|**2023-09-18**|**GDM: Dual Mixup for Graph Classification with Limited Supervision**|Abdullah Alchihabi et.al.|[2309.10134](http://arxiv.org/abs/2309.10134)|null|
|**2023-09-18**|**Deep Prompt Tuning for Graph Transformers**|Reza Shirkavand et.al.|[2309.10131](http://arxiv.org/abs/2309.10131)|null|
|**2023-09-18**|**Markov Chain-Guided Graph Construction and Sampling Depth Optimization for EEG-Based Mental Disorder Detection**|Yihan Wu et.al.|[2309.10128](http://arxiv.org/abs/2309.10128)|null|
|**2023-09-18**|**Finite Volume Graph Network(FVGN): Predicting unsteady incompressible fluid dynamics with finite volume informed neural network**|Tianyu Li et.al.|[2309.10050](http://arxiv.org/abs/2309.10050)|**[link](https://github.com/Litianyu141/FVGN-sub-Meshgraphnet)**|
|**2023-09-18**|**Hierarchical Attention and Graph Neural Networks: Toward Drift-Free Pose Estimation**|Kathia Melbouci et.al.|[2309.09934](http://arxiv.org/abs/2309.09934)|null|
|**2023-09-18**|**A Heterogeneous Graph-Based Multi-Task Learning for Fault Event Diagnosis in Smart Grid**|Dibaloke Chanda et.al.|[2309.09921](http://arxiv.org/abs/2309.09921)|null|
|**2023-09-18**|**CC-SGG: Corner Case Scenario Generation using Learned Scene Graphs**|George Drayson et.al.|[2309.09844](http://arxiv.org/abs/2309.09844)|null|
|**2023-09-19**|**FedGKD: Unleashing the Power of Collaboration in Federated Graph Neural Networks**|Qiying Pan et.al.|[2309.09517](http://arxiv.org/abs/2309.09517)|null|
|**2023-09-17**|**Mitigating Over-Smoothing and Over-Squashing using Augmentations of Forman-Ricci Curvature**|Lukas Fesser et.al.|[2309.09384](http://arxiv.org/abs/2309.09384)|**[link](https://github.com/weber-geoml/afrc_rewiring)**|
|**2023-09-17**|**Performance of Graph Neural Networks for Point Cloud Applications**|Dhruv Parikh et.al.|[2309.09142](http://arxiv.org/abs/2309.09142)|null|
|**2023-09-16**|**CNS: Correspondence Encoded Neural Image Servo Policy**|Anzhe Chen et.al.|[2309.09047](http://arxiv.org/abs/2309.09047)|null|
|**2023-09-15**|**Local Differential Privacy in Graph Neural Networks: a Reconstruction Approach**|Karuna Bhaila et.al.|[2309.08569](http://arxiv.org/abs/2309.08569)|**[link](https://github.com/karuna-bhaila/rgnn)**|
|**2023-09-15**|**XFedHunter: An Explainable Federated Learning Framework for Advanced Persistent Threat Detection in SDN**|Huynh Thai Thi et.al.|[2309.08485](http://arxiv.org/abs/2309.08485)|null|
|**2023-09-15**|**VulnSense: Efficient Vulnerability Detection in Ethereum Smart Contracts by Multimodal Learning with Graph Neural Network and Language Model**|Phan The Duy et.al.|[2309.08474](http://arxiv.org/abs/2309.08474)|null|
|**2023-09-15**|**Silent Vulnerability-fixing Commit Identification Based on Graph Neural Networks**|Hieu Dinh Vo et.al.|[2309.08225](http://arxiv.org/abs/2309.08225)|null|
|**2023-09-14**|**Naturalistic Robot Arm Trajectory Generation via Representation Learning**|Jayjun Lee et.al.|[2309.07550](http://arxiv.org/abs/2309.07550)|null|
|**2023-09-14**|**SC-MAD: Mixtures of Higher-order Networks for Data Augmentation**|Madeline Navarro et.al.|[2309.07453](http://arxiv.org/abs/2309.07453)|null|
|**2023-09-14**|**Is Solving Graph Neural Tangent Kernel Equivalent to Training Graph Neural Network?**|Lianke Qin et.al.|[2309.07452](http://arxiv.org/abs/2309.07452)|null|
|**2023-09-14**|**HIGT: Hierarchical Interaction Graph-Transformer for Whole Slide Image Analysis**|Ziyu Guo et.al.|[2309.07400](http://arxiv.org/abs/2309.07400)|**[link](https://github.com/hku-medai/higt)**|
|**2023-09-14**|**Domain-adaptive Graph Attention-supervised Network for Cross-network Edge Classification**|Xiao Shen et.al.|[2309.07380](http://arxiv.org/abs/2309.07380)|**[link](https://github.com/qqqq-shao/dgasn)**|
|**2023-09-13**|**Predicting Expressibility of Parameterized Quantum Circuits using Graph Neural Network**|Shamminuj Aktar et.al.|[2309.06975](http://arxiv.org/abs/2309.06975)|null|
|**2023-09-13**|**Multi-behavior Recommendation with SVD Graph Neural Networks**|Shengxi Fu et.al.|[2309.06912](http://arxiv.org/abs/2309.06912)|null|
|**2023-09-15**|**Uncertainty-aware Traffic Prediction under Missing Data**|Hao Mei et.al.|[2309.06800](http://arxiv.org/abs/2309.06800)|**[link](https://github.com/lijunxian111/UIGNN)**|
|**2023-09-13**|**Scalable neural network models and terascale datasets for particle-flow reconstruction**|Joosep Pata et.al.|[2309.06782](http://arxiv.org/abs/2309.06782)|null|
|**2023-09-12**|**Bregman Graph Neural Network**|Jiayu Zhai et.al.|[2309.06645](http://arxiv.org/abs/2309.06645)|**[link](https://github.com/jiayuzhai1207/bregmangnn)**|
|**2023-09-12**|**Explainable Graph Neural Network for Alzheimer's Disease And Related Dementias Risk Prediction**|Xinyue Hu et.al.|[2309.06584](http://arxiv.org/abs/2309.06584)|null|
|**2023-09-12**|**Bayesian topology inference on partially known networks from input-output pairs**|Martín Sevilla et.al.|[2309.06532](http://arxiv.org/abs/2309.06532)|**[link](https://github.com/tenceto/inference_langevin)**|
|**2023-09-13**|**Accelerating Defect Predictions in Semiconductors Using Graph Neural Networks**|Md Habibur Rahman et.al.|[2309.06423](http://arxiv.org/abs/2309.06423)|**[link](https://github.com/msehabibur/defect_gnn_gen_1)**|
|**2023-09-12**|**Fg-T2M: Fine-Grained Text-Driven Human Motion Generation via Diffusion Model**|Yin Wang et.al.|[2309.06284](http://arxiv.org/abs/2309.06284)|null|
|**2023-09-12**|**Information Flow in Graph Neural Networks: A Clinical Triage Use Case**|Víctor Valls et.al.|[2309.06081](http://arxiv.org/abs/2309.06081)|null|
|**2023-09-12**|**GLAD: Content-aware Dynamic Graphs For Log Anomaly Detection**|Yufei Li et.al.|[2309.05953](http://arxiv.org/abs/2309.05953)|**[link](https://github.com/yul091/graphlogad)**|
|**2023-09-12**|**MatSciML: A Broad, Multi-Task Benchmark for Solid-State Materials Modeling**|Kin Long Kelvin Lee et.al.|[2309.05934](http://arxiv.org/abs/2309.05934)|**[link](https://github.com/intellabs/matsciml)**|
|**2023-09-11**|**Predicting Interloper Fraction with Graph Neural Networks**|Elena Massara et.al.|[2309.05850](http://arxiv.org/abs/2309.05850)|null|
|**2023-09-11**|**Learning the Geodesic Embedding with Graph Neural Networks**|Bo Pang et.al.|[2309.05613](http://arxiv.org/abs/2309.05613)|**[link](https://github.com/intelligentgeometry/gegnn)**|
|**2023-09-11**|**Advancing Federated Learning in 6G: A Trusted Architecture with Graph-based Analysis**|Wenxuan Ye et.al.|[2309.05525](http://arxiv.org/abs/2309.05525)|null|
|**2023-09-11**|**A parameterised model for link prediction using node centrality and similarity measure based on graph embedding**|Haohui Lu et.al.|[2309.05434](http://arxiv.org/abs/2309.05434)|null|
|**2023-09-11**|**Fully-Connected Spatial-Temporal Graph for Multivariate Time Series Data**|Yucheng Wang et.al.|[2309.05305](http://arxiv.org/abs/2309.05305)|**[link](https://github.com/Frank-Wang-oss/FCSTGNN)**|
|**2023-09-10**|**Spatiotemporal Graph Neural Networks with Uncertainty Quantification for Traffic Incident Risk Prediction**|Xiaowei Gao et.al.|[2309.05072](http://arxiv.org/abs/2309.05072)|**[link](https://github.com/sttdanonymous/sttd)**|
|**2023-09-10**|**Distance-Restricted Folklore Weisfeiler-Leman GNNs with Provable Cycle Counting Power**|Junru Zhou et.al.|[2309.04941](http://arxiv.org/abs/2309.04941)|**[link](https://github.com/zml72062/dr-fwl-2)**|
|**2023-09-09**|**Symplectic Structure-Aware Hamiltonian (Graph) Embeddings**|Jiaxu Liu et.al.|[2309.04885](http://arxiv.org/abs/2309.04885)|null|
|**2023-09-09**|**Chemical Properties from Graph Neural Network-Predicted Electron Densities**|Ethan M. Sunshine et.al.|[2309.04811](http://arxiv.org/abs/2309.04811)|null|
|**2023-09-09**|**Redundancy-Free Self-Supervised Relational Learning for Graph Clustering**|Si-Yu Yi et.al.|[2309.04694](http://arxiv.org/abs/2309.04694)|**[link](https://github.com/yisiyu95/r2fgc)**|
|**2023-09-08**|**Motif-aware Attribute Masking for Molecular Graph Pre-training**|Eric Inae et.al.|[2309.04589](http://arxiv.org/abs/2309.04589)|**[link](https://github.com/einae-nd/moama-dev)**|
|**2023-09-08**|**Graph Neural Networks Use Graphs When They Shouldn't**|Maya Bechler-Speicher et.al.|[2309.04332](http://arxiv.org/abs/2309.04332)|**[link](https://github.com/mayabechlerspeicher/Graph_Neural_Networks_Overfit_Graphs)**|
|**2023-09-08**|**A Long-Tail Friendly Representation Framework for Artist and Music Similarity**|Haoran Xiang et.al.|[2309.04182](http://arxiv.org/abs/2309.04182)|null|
|**2023-09-08**|**Curve Your Attention: Mixed-Curvature Transformers for Graph Representation Learning**|Sungjun Cho et.al.|[2309.04082](http://arxiv.org/abs/2309.04082)|null|
|**2023-09-07**|**Extending Transductive Knowledge Graph Embedding Models for Inductive Logical Relational Inference**|Thomas Gebhart et.al.|[2309.03773](http://arxiv.org/abs/2309.03773)|**[link](https://github.com/tgebhart/sheaf_kg_transind)**|
|**2023-09-07**|**Characterizing Lipschitz Stability of GNN for Fairness**|Yaning Jia et.al.|[2309.03648](http://arxiv.org/abs/2309.03648)|null|
|**2023-09-07**|**Filtration Surfaces for Dynamic Graph Classification**|Franz Srambical et.al.|[2309.03616](http://arxiv.org/abs/2309.03616)|**[link](https://github.com/aidos-lab/filtration_surfaces)**|
|**2023-09-07**|**Enhancing 5G Radio Planning with Graph Representations and Deep Learning**|Paul Almasan et.al.|[2309.03603](http://arxiv.org/abs/2309.03603)|null|
|**2023-09-07**|**DGC: Training Dynamic Graphs with Spatio-Temporal Non-Uniformity using Graph Partitioning by Chunks**|Fahao Chen et.al.|[2309.03523](http://arxiv.org/abs/2309.03523)|null|
|**2023-09-07**|**Blink: Link Local Differential Privacy in Graph Neural Networks via Bayesian Estimation**|Xiaochen Zhu et.al.|[2309.03190](http://arxiv.org/abs/2309.03190)|**[link](https://github.com/zhxchd/blink_gnn)**|
|**2023-09-07**|**Impression-Informed Multi-Behavior Recommender System: A Hierarchical Graph Attention Approach**|Dong Li et.al.|[2309.03169](http://arxiv.org/abs/2309.03169)|null|
|**2023-09-06**|**Using Multiple Vector Channels Improves E(n)-Equivariant Graph Neural Networks**|Daniel Levy et.al.|[2309.03139](http://arxiv.org/abs/2309.03139)|null|
|**2023-09-06**|**Knowledge Solver: Teaching LLMs to Search for Domain Knowledge from Knowledge Graphs**|Chao Feng et.al.|[2309.03118](http://arxiv.org/abs/2309.03118)|null|
|**2023-09-06**|**Prompt-based Node Feature Extractor for Few-shot Learning on Text-Attributed Graphs**|Xuanwen Huang et.al.|[2309.02848](http://arxiv.org/abs/2309.02848)|null|
|**2023-09-06**|**Unifying over-smoothing and over-squashing in graph neural networks: A physics informed approach and beyond**|Zhiqi Shao et.al.|[2309.02769](http://arxiv.org/abs/2309.02769)|null|
|**2023-09-06**|**Towards Unsupervised Graph Completion Learning on Graphs with Features and Structure Missing**|Sichao Fu et.al.|[2309.02762](http://arxiv.org/abs/2309.02762)|null|
|**2023-09-06**|**Reinforcement Learning of Action and Query Policies with LTL Instructions under Uncertain Event Detector**|Wataru Hatanaka et.al.|[2309.02722](http://arxiv.org/abs/2309.02722)|null|
|**2023-09-05**|**Black-Box Attacks against Signed Graph Analysis via Balance Poisoning**|Jialong Zhou et.al.|[2309.02396](http://arxiv.org/abs/2309.02396)|**[link](https://github.com/jialongzhou666/balance-attack)**|
|**2023-09-05**|**STGIN: Spatial-Temporal Graph Interaction Network for Large-scale POI Recommendation**|Shaohua Liu et.al.|[2309.02251](http://arxiv.org/abs/2309.02251)|null|
|**2023-09-05**|**Diffusion Generative Inverse Design**|Marin Vlastelica et.al.|[2309.02040](http://arxiv.org/abs/2309.02040)|null|
|**2023-09-05**|**VFFINDER: A Graph-based Approach for Automated Silent Vulnerability-Fix Identification**|Son Nguyen et.al.|[2309.01971](http://arxiv.org/abs/2309.01971)|null|
|**2023-09-04**|**Hierarchical Grammar-Induced Geometry for Data-Efficient Molecular Property Prediction**|Minghao Guo et.al.|[2309.01788](http://arxiv.org/abs/2309.01788)|**[link](https://github.com/gmh14/geo-deg)**|
|**2023-09-04**|**On the Robustness of Post-hoc GNN Explainers to Label Noise**|Zhiqiang Zhong et.al.|[2309.01706](http://arxiv.org/abs/2309.01706)|null|
|**2023-09-04**|**Layer-wise training for self-supervised learning on graphs**|Oscar Pina et.al.|[2309.01503](http://arxiv.org/abs/2309.01503)|null|
|**2023-09-04**|**ReOnto: A Neuro-Symbolic Approach for Biomedical Relation Extraction**|Monika Jain et.al.|[2309.01370](http://arxiv.org/abs/2309.01370)|**[link](https://github.com/kracr/reonto-relation-extraction)**|
|**2023-09-03**|**Financial Fraud Detection using Quantum Graph Neural Networks**|Nouhaila Innan et.al.|[2309.01127](http://arxiv.org/abs/2309.01127)|null|
|**2023-09-02**|**SEPAL: Spatial Gene Expression Prediction from Local Graphs**|Gabriel Mejia et.al.|[2309.01036](http://arxiv.org/abs/2309.01036)|**[link](https://github.com/bcv-uniandes/sepal)**|
|**2023-09-01**|**Catalyst Property Prediction with CatBERTa: Unveiling Feature Exploration Strategies through Large Language Models**|Janghoon Ock et.al.|[2309.00563](http://arxiv.org/abs/2309.00563)|**[link](https://github.com/hoon-ock/catberta)**|
|**2023-09-01**|**Application of Deep Learning Methods in Monitoring and Optimization of Electric Power Systems**|Ognjen Kundacina et.al.|[2309.00498](http://arxiv.org/abs/2309.00498)|null|
|**2023-09-04**|**A Locality-based Neural Solver for Optical Motion Capture**|Xiaoyu Pan et.al.|[2309.00428](http://arxiv.org/abs/2309.00428)|**[link](https://github.com/non-void/localmocap)**|
|**2023-08-31**|**Pose-Graph Attentional Graph Neural Network for Lidar Place Recognition**|Milad Ramezani et.al.|[2309.00168](http://arxiv.org/abs/2309.00168)|**[link](https://github.com/csiro-robotics/p-gat)**|
|**2023-08-31**|**Self-pruning Graph Neural Network for Predicting Inflammatory Disease Activity in Multiple Sclerosis from Brain MR Images**|Chinmay Prabhakar et.al.|[2308.16863](http://arxiv.org/abs/2308.16863)|**[link](https://github.com/chinmay5/ms_ida)**|
|**2023-08-31**|**Rank Collapse Causes Over-Smoothing and Over-Correlation in Graph Neural Networks**|Andreas Roth et.al.|[2308.16800](http://arxiv.org/abs/2308.16800)|**[link](https://github.com/roth-andreas/rank_collapse)**|
|**2023-08-31**|**Curvature-based Pooling within Graph Neural Networks**|Cedric Sanders et.al.|[2308.16516](http://arxiv.org/abs/2308.16516)|**[link](https://gitlab.com/cedric_sanders/masterarbeit)**|
|**2023-08-31**|**Domain-adaptive Message Passing Graph Neural Network**|Xiao Shen et.al.|[2308.16470](http://arxiv.org/abs/2308.16470)|**[link](https://github.com/shenxiaocam/dm_gnn)**|
|**2023-08-31**|**CktGNN: Circuit Graph Neural Network for Electronic Design Automation**|Zehao Dong et.al.|[2308.16406](http://arxiv.org/abs/2308.16406)|**[link](https://github.com/zehao-dong/CktGNN)**|
|**2023-08-31**|**BenchTemp: A General Benchmark for Evaluating Temporal Graph Neural Networks**|Qiang Huang et.al.|[2308.16385](http://arxiv.org/abs/2308.16385)|**[link](https://github.com/qianghuangwhu/benchtemp)**|
|**2023-08-31**|**A Survey on Privacy in Graph Neural Networks: Attacks, Preservation, and Applications**|Yi Zhang et.al.|[2308.16375](http://arxiv.org/abs/2308.16375)|**[link](https://github.com/nds-vu/awesome-gnn-privacy)**|
|**2023-08-30**|**Spatial Graph Coarsening: Weather and Weekday Prediction with London's Bike-Sharing Service using GNN**|Yuta Sato et.al.|[2308.16122](http://arxiv.org/abs/2308.16122)|null|
|**2023-08-30**|**Learning Structure-from-Motion with Graph Attention Networks**|Lucas Brynte et.al.|[2308.15984](http://arxiv.org/abs/2308.15984)|**[link](https://github.com/lucasbrynte/gasfm)**|
|**2023-08-30**|**Adaptive Multi-Modalities Fusion in Sequential Recommendation Systems**|Hengchang Hu et.al.|[2308.15980](http://arxiv.org/abs/2308.15980)|**[link](https://github.com/holdenhu/mmsr)**|
|**2023-08-30**|**MSGNN: Multi-scale Spatio-temporal Graph Neural Network for Epidemic Forecasting**|Mingjie Qiu et.al.|[2308.15840](http://arxiv.org/abs/2308.15840)|null|
|**2023-08-30**|**Efficient and Explainable Graph Neural Architecture Search via Monte-Carlo Tree Search**|Yuya Sasaki et.al.|[2308.15734](http://arxiv.org/abs/2308.15734)|**[link](https://github.com/onizukalab/autognn_mcts)**|
|**2023-08-29**|**Everything Perturbed All at Once: Enabling Differentiable Graph Attacks**|Haoran Liu et.al.|[2308.15614](http://arxiv.org/abs/2308.15614)|null|
|**2023-08-29**|**An Experimental Comparison of Partitioning Strategies for Distributed Graph Neural Network Training**|Nikolai Merkel et.al.|[2308.15602](http://arxiv.org/abs/2308.15602)|null|
|**2023-08-29**|**Over-Squashing in Graph Neural Networks: A Comprehensive survey**|Singh Akansha et.al.|[2308.15568](http://arxiv.org/abs/2308.15568)|null|
|**2023-08-29**|**A Comparative Study of Loss Functions: Traffic Predictions in Regular and Congestion Scenarios**|Yangxinyu Xie et.al.|[2308.15464](http://arxiv.org/abs/2308.15464)|**[link](https://github.com/xieyangxinyu/a-comparative-study-of-loss-functions-traffic-predictions-in-regular-and-congestion-scenarios)**|
|**2023-08-29**|**How Faithful are Self-Explainable GNNs?**|Marc Christiansen et.al.|[2308.15096](http://arxiv.org/abs/2308.15096)|null|
|**2023-08-29**|**Low-bit Quantization for Deep Graph Neural Networks with Smoothness-aware Message Propagation**|Shuang Wang et.al.|[2308.14949](http://arxiv.org/abs/2308.14949)|**[link](https://github.com/publiccoderepo/SMP_GNN_Quant)**|
|**2023-08-28**|**Matbench Discovery -- An evaluation framework for machine learning crystal stability prediction**|Janosh Riebesell et.al.|[2308.14920](http://arxiv.org/abs/2308.14920)|**[link](https://github.com/janosh/matbench-discovery)**|
|**2023-08-28**|**Fairness Through Domain Awareness: Mitigating Popularity Bias For Music Discovery**|Rebecca Salganik et.al.|[2308.14601](http://arxiv.org/abs/2308.14601)|null|
|**2023-08-28**|**Multimodal Detection of Social Spambots in Twitter using Transformers**|Loukas Ilias et.al.|[2308.14484](http://arxiv.org/abs/2308.14484)|null|
|**2023-08-28**|**Can Transformer and GNN Help Each Other?**|Peiyan Zhang et.al.|[2308.14355](http://arxiv.org/abs/2308.14355)|**[link](https://github.com/peiyance/transgnn-torch)**|
|**2023-08-28**|**HRGCN: Heterogeneous Graph-level Anomaly Detection with Hierarchical Relation-augmented Graph Neural Networks**|Jiaxi Li et.al.|[2308.14340](http://arxiv.org/abs/2308.14340)|**[link](https://github.com/jiaxililearn/hrgcn)**|
|**2023-08-27**|**Universal Graph Continual Learning**|Thanh Duc Hoang et.al.|[2308.13982](http://arxiv.org/abs/2308.13982)|null|
|**2023-08-27**|**Understanding the Usage of QUBO-based Hamiltonian Function in Combinatorial Optimization over Graphs: A Discussion Using Max Cut (MC) Problem**|Redwan Ahmed Rizvee et.al.|[2308.13978](http://arxiv.org/abs/2308.13978)|null|
|**2023-08-26**|**Graph Edit Distance Learning via Different Attention**|Jiaxi Lv et.al.|[2308.13871](http://arxiv.org/abs/2308.13871)|null|
|**2023-08-25**|**Unveiling the Role of Message Passing in Dual-Privacy Preservation on GNNs**|Tianyi Zhao et.al.|[2308.13513](http://arxiv.org/abs/2308.13513)|null|
|**2023-08-25**|**Staleness-Alleviated Distributed GNN Training via Online Dynamic-Embedding Prediction**|Guangji Bai et.al.|[2308.13466](http://arxiv.org/abs/2308.13466)|null|
|**2023-08-25**|**Physics-Inspired Neural Graph ODE for Long-term Dynamical Simulation**|Yang Liu et.al.|[2308.13212](http://arxiv.org/abs/2308.13212)|null|
|**2023-08-24**|**SurGNN: Explainable visual scene understanding and assessment of surgical skill using graph neural networks**|Shuja Khalid et.al.|[2308.13073](http://arxiv.org/abs/2308.13073)|null|
|**2023-08-24**|**Hydrogen jet diffusion modeling by using physics-informed graph neural network and sparsely-distributed sensor data**|Xinqi Zhang et.al.|[2308.12621](http://arxiv.org/abs/2308.12621)|null|
|**2023-08-23**|**MolGrapher: Graph-based Visual Recognition of Chemical Structures**|Lucas Morin et.al.|[2308.12234](http://arxiv.org/abs/2308.12234)|**[link](https://github.com/ds4sd/molgrapher)**|
|**2023-08-23**|**Cached Operator Reordering: A Unified View for Fast GNN Training**|Julia Bazinska et.al.|[2308.12093](http://arxiv.org/abs/2308.12093)|null|
|**2023-08-23**|**Will More Expressive Graph Neural Networks do Better on Generative Tasks?**|Xiandong Zou et.al.|[2308.11978](http://arxiv.org/abs/2308.11978)|null|
|**2023-08-25**|**Pose Modulated Avatars from Video**|Chunjin Song et.al.|[2308.11951](http://arxiv.org/abs/2308.11951)|null|
|**2023-08-23**|**Learning Bottleneck Transformer for Event Image-Voxel Feature Fusion based Classification**|Chengguo Yuan et.al.|[2308.11937](http://arxiv.org/abs/2308.11937)|**[link](https://github.com/event-ahu/efv_event_classification)**|
|**2023-08-22**|**Multi-Instance Adversarial Attack on GNN-Based Malicious Domain Detection**|Mahmoud Nazzal et.al.|[2308.11754](http://arxiv.org/abs/2308.11754)|**[link](https://github.com/mahmoudkanazzal/minta)**|
|**2023-08-22**|**Graph Neural Network-Enhanced Expectation Propagation Algorithm for MIMO Turbo Receivers**|Xingyu Zhou et.al.|[2308.11335](http://arxiv.org/abs/2308.11335)|**[link](https://github.com/STARainZ/GNN-enhanced-EP-for-Turbo-MIMO)**|
|**2023-08-24**|**Predicting Transition Temperature of Superconductors with Graph Neural Networks**|Liang Gu et.al.|[2308.11160](http://arxiv.org/abs/2308.11160)|**[link](https://github.com/glinustb/bsgnn)**|
|**2023-08-22**|**Graph Encoding and Neural Network Approaches for Volleyball Analytics: From Game Outcome to Individual Play Predictions**|Rhys Tracy et.al.|[2308.11142](http://arxiv.org/abs/2308.11142)|null|
|**2023-08-22**|**How Expressive are Graph Neural Networks in Recommendation?**|Xuheng Cai et.al.|[2308.11127](http://arxiv.org/abs/2308.11127)|**[link](https://github.com/hkuds/gte)**|
|**2023-08-21**|**Topological Graph Signal Compression**|Guillermo Bernárdez et.al.|[2308.11068](http://arxiv.org/abs/2308.11068)|null|
|**2023-08-21**|**Enhancing Recommender Systems with Large Language Model Reasoning Graphs**|Yan Wang et.al.|[2308.10835](http://arxiv.org/abs/2308.10835)|null|
|**2023-08-21**|**Graph Neural Bandits**|Yunzhe Qi et.al.|[2308.10808](http://arxiv.org/abs/2308.10808)|null|
|**2023-08-21**|**Spear and Shield: Adversarial Attacks and Defense Methods for Model-Based Link Prediction on Continuous-Time Dynamic Graphs**|Dongjin Lee et.al.|[2308.10779](http://arxiv.org/abs/2308.10779)|**[link](https://github.com/wooner49/t-spear-shield)**|
|**2023-08-21**|**A Topology-aware Analysis of Graph Collaborative Filtering**|Daniele Malitesta et.al.|[2308.10778](http://arxiv.org/abs/2308.10778)|**[link](https://github.com/sisinflab/graph-characteristics)**|
|**2023-08-21**|**UGSL: A Unified Framework for Benchmarking Graph Structure Learning**|Bahare Fatemi et.al.|[2308.10737](http://arxiv.org/abs/2308.10737)|**[link](https://github.com/google-research/google-research)**|
|**2023-08-21**|**ST-RAP: A Spatio-Temporal Framework for Real Estate Appraisal**|Hojoon Lee et.al.|[2308.10609](http://arxiv.org/abs/2308.10609)|**[link](https://github.com/dojeon-ai/strap)**|
|**2023-08-21**|**Approximately Equivariant Graph Networks**|Ningyuan Huang et.al.|[2308.10436](http://arxiv.org/abs/2308.10436)|**[link](https://github.com/nhuang37/approx_equivariant_graph_nets)**|
|**2023-08-20**|**Preserving Specificity in Federated Graph Learning for fMRI-based Neurological Disorder Identification**|Junhao Zhang et.al.|[2308.10302](http://arxiv.org/abs/2308.10302)|null|
|**2023-08-20**|**Minimalist Traffic Prediction: Linear Layer Is All You Need**|Wenying Duan et.al.|[2308.10276](http://arxiv.org/abs/2308.10276)|null|
|**2023-08-19**|**Geometric instability of graph neural networks on large graphs**|Emily Morris et.al.|[2308.10099](http://arxiv.org/abs/2308.10099)|**[link](https://github.com/brs96/geometric-instability-gnn-large-graphs)**|
|**2023-08-18**|**A Potts model approach to unsupervised graph clustering with Graph Neural Networks**|Co Tran et.al.|[2308.09644](http://arxiv.org/abs/2308.09644)|null|
|**2023-08-18**|**Disparity, Inequality, and Accuracy Tradeoffs in Graph Neural Networks for Node Classification**|Arpit Merchant et.al.|[2308.09596](http://arxiv.org/abs/2308.09596)|**[link](https://github.com/arpitdm/gnn_accuracy_fairness_tradeoff)**|
|**2023-08-18**|**Transitivity-Preserving Graph Representation Learning for Bridging Local Connectivity and Role-based Similarity**|Van Thuy Hoang et.al.|[2308.09517](http://arxiv.org/abs/2308.09517)|**[link](https://github.com/nslab-cuk/unified-graph-transformer)**|
|**2023-08-18**|**Bridged-GNN: Knowledge Bridge Learning for Effective Knowledge Transfer**|Wendong Bi et.al.|[2308.09499](http://arxiv.org/abs/2308.09499)|null|
|**2023-08-18**|**Boosting Few-shot Action Recognition with Graph-guided Hybrid Matching**|Jiazheng Xing et.al.|[2308.09346](http://arxiv.org/abs/2308.09346)|**[link](https://github.com/jiazheng-xing/gghm)**|
|**2023-08-18**|**Distribution shift mitigation at test time with performance guarantees**|Rui Ding et.al.|[2308.09259](http://arxiv.org/abs/2308.09259)|null|
|**2023-08-17**|**Interpretable Graph Neural Networks for Tabular Data**|Amr Alkhatib et.al.|[2308.08945](http://arxiv.org/abs/2308.08945)|**[link](https://github.com/amrmalkhatib/ignnet)**|
|**2023-08-17**|**Mitigating Semantic Confusion from Hostile Neighborhood for Graph Active Learning**|Tianmeng Yang et.al.|[2308.08823](http://arxiv.org/abs/2308.08823)|**[link](https://github.com/YoungTimmy/SAG)**|
|**2023-08-17**|**Graph Neural Network Backend for Speaker Recognition**|Liang He et.al.|[2308.08767](http://arxiv.org/abs/2308.08767)|null|
|**2023-08-16**|**Group Identification via Transitional Hypergraph Convolution with Cross-view Self-supervised Learning**|Mingdai Yang et.al.|[2308.08620](http://arxiv.org/abs/2308.08620)|null|
|**2023-08-16**|**Graph Out-of-Distribution Generalization with Controllable Data Augmentation**|Bin Lu et.al.|[2308.08344](http://arxiv.org/abs/2308.08344)|null|
|**2023-08-16**|**The Expressive Power of Graph Neural Networks: A Survey**|Bingxu Zhang et.al.|[2308.08235](http://arxiv.org/abs/2308.08235)|null|
|**2023-08-16**|**DeSCo: Towards Generalizable and Scalable Deep Subgraph Counting**|Tianyu Fu et.al.|[2308.08198](http://arxiv.org/abs/2308.08198)|**[link](https://github.com/fuvty/DeSCo)**|
|**2023-08-16**|**Accelerating Generic Graph Neural Networks via Architecture, Compiler, Partition Method Co-Design**|Shuwen Lu et.al.|[2308.08174](http://arxiv.org/abs/2308.08174)|null|
|**2023-08-16**|**Expressivity of Graph Neural Networks Through the Lens of Adversarial Robustness**|Francesco Campi et.al.|[2308.08173](http://arxiv.org/abs/2308.08173)|**[link](https://github.com/francesco-campi/rob-subgraphs)**|
|**2023-08-16**|**S-Mixup: Structural Mixup for Graph Neural Networks**|Junghurn Kim et.al.|[2308.08097](http://arxiv.org/abs/2308.08097)|**[link](https://github.com/sukwonyun/s-mixup)**|
|**2023-08-15**|**Decentralized Graph Neural Network for Privacy-Preserving Recommendation**|Xiaolin Zheng et.al.|[2308.08072](http://arxiv.org/abs/2308.08072)|null|
|**2023-08-15**|**Freshness or Accuracy, Why Not Both? Addressing Delayed Feedback via Dynamic Graph Neural Networks**|Xiaolin Zheng et.al.|[2308.08071](http://arxiv.org/abs/2308.08071)|null|
|**2023-08-15**|**Towards Temporal Edge Regression: A Case Study on Agriculture Trade Between Nations**|Lekang Jiang et.al.|[2308.07883](http://arxiv.org/abs/2308.07883)|**[link](https://github.com/scylj1/gnn_edge_regression)**|
|**2023-08-15**|**Simple and Efficient Partial Graph Adversarial Attack: A New Perspective**|Guanghui Zhu et.al.|[2308.07834](http://arxiv.org/abs/2308.07834)|**[link](https://github.com/pasalab/pga)**|
|**2023-08-15**|**A Graph Encoder-Decoder Network for Unsupervised Anomaly Detection**|Mahsa Mesgaran et.al.|[2308.07774](http://arxiv.org/abs/2308.07774)|null|
|**2023-08-15**|**Self-Supervised Dynamic Hypergraph Recommendation based on Hyper-Relational Knowledge Graph**|Yi Liu et.al.|[2308.07752](http://arxiv.org/abs/2308.07752)|null|
|**2023-08-14**|**ST-MLP: A Cascaded Spatio-Temporal Linear Framework with Channel-Independence Strategy for Traffic Forecasting**|Zepu Wang et.al.|[2308.07496](http://arxiv.org/abs/2308.07496)|null|
|**2023-08-16**|**Interaction-Aware Personalized Vehicle Trajectory Prediction Using Temporal Graph Neural Networks**|Amr Abdelraouf et.al.|[2308.07439](http://arxiv.org/abs/2308.07439)|null|
|**2023-08-14**|**Conformal Predictions Enhanced Expert-guided Meshing with Graph Neural Networks**|Amin Heyrani Nobari et.al.|[2308.07358](http://arxiv.org/abs/2308.07358)|**[link](https://github.com/ahnobari/autosurf)**|
|**2023-08-14**|**Search to Fine-tune Pre-trained Graph Neural Networks for Graph-level Tasks**|Zhili Wang et.al.|[2308.06960](http://arxiv.org/abs/2308.06960)|**[link](https://github.com/zwangeo/icde2024)**|
|**2023-08-13**|**Generalizing Topological Graph Neural Networks with Paths**|Quang Truong et.al.|[2308.06838](http://arxiv.org/abs/2308.06838)|null|
|**2023-08-15**|**SAILOR: Structural Augmentation Based Tail Node Representation Learning**|Jie Liao et.al.|[2308.06801](http://arxiv.org/abs/2308.06801)|**[link](https://github.com/jie-re/sailor)**|
|**2023-08-13**|**Learning on Graphs with Out-of-Distribution Nodes**|Yu Song et.al.|[2308.06714](http://arxiv.org/abs/2308.06714)|**[link](https://github.com/songyyyy/kdd22-oodgat)**|
|**2023-08-10**|**$\mathcal{G}^2Pxy$ : Generative Open-Set Node Classification on Graphs with Proxy Unknowns**|Qin Zhang et.al.|[2308.05463](http://arxiv.org/abs/2308.05463)|null|
|**2023-08-10**|**DegUIL: Degree-aware Graph Neural Networks for Long-tailed User Identity Linkage**|Meixiu Long et.al.|[2308.05322](http://arxiv.org/abs/2308.05322)|**[link](https://github.com/longmeix/deguil)**|
|**2023-08-10**|**RLSAC: Reinforcement Learning enhanced Sample Consensus for End-to-End Robust Estimation**|Chang Nie et.al.|[2308.05318](http://arxiv.org/abs/2308.05318)|**[link](https://github.com/irmvlab/rlsac)**|
|**2023-08-11**|**Homophily-enhanced Structure Learning for Graph Clustering**|Ming Gu et.al.|[2308.05309](http://arxiv.org/abs/2308.05309)|**[link](https://github.com/galogm/hole)**|
|**2023-08-10**|**Cross-heterogeneity Graph Few-shot Learning**|Pengfei Ding et.al.|[2308.05275](http://arxiv.org/abs/2308.05275)|null|
|**2023-08-10**|**Geometric Learning-Based Transformer Network for Estimation of Segmentation Errors**|Sneha Sree C et.al.|[2308.05068](http://arxiv.org/abs/2308.05068)|null|
|**2023-08-13**|**Kairos: Practical Intrusion Detection and Investigation using Whole-system Provenance**|Zijun Cheng et.al.|[2308.05034](http://arxiv.org/abs/2308.05034)|**[link](https://github.com/provenanceanalytics/kairos)**|
|**2023-08-09**|**Differentially Private Graph Neural Network with Importance-Grained Noise Adaption**|Yuxin Qi et.al.|[2308.04943](http://arxiv.org/abs/2308.04943)|null|
|**2023-08-09**|**GraphCC: A Practical Graph Learning-based Approach to Congestion Control in Datacenters**|Guillermo Bernárdez et.al.|[2308.04905](http://arxiv.org/abs/2308.04905)|null|
|**2023-08-08**|**Semantic Interpretation and Validation of Graph Attention-based Explanations for GNN Models**|Efimia Panagiotaki et.al.|[2308.04220](http://arxiv.org/abs/2308.04220)|null|
|**2023-08-08**|**Predicting Drug-Drug Interactions Using Knowledge Graphs**|Lizzy Farrugia et.al.|[2308.04172](http://arxiv.org/abs/2308.04172)|null|
|**2023-08-07**|**Uncertainty-aware Consistency Learning for Cold-Start Item Recommendation**|Taichi Liu et.al.|[2308.03470](http://arxiv.org/abs/2308.03470)|null|
|**2023-08-07**|**Friedrichs' systems discretized with the Discontinuous Galerkin method: domain decomposable model order reduction and Graph Neural Networks approximating vanishing viscosity solutions**|Francesco Romor et.al.|[2308.03378](http://arxiv.org/abs/2308.03378)|null|
|**2023-08-07**|**Implicit Graph Neural Diffusion Based on Constrained Dirichlet Energy Minimization**|Guoji Fu et.al.|[2308.03306](http://arxiv.org/abs/2308.03306)|**[link](https://github.com/guoji-fu/dignn)**|
|**2023-08-07**|**Local Structure-aware Graph Contrastive Representation Learning**|Kai Yang et.al.|[2308.03271](http://arxiv.org/abs/2308.03271)|null|
|**2023-08-07**|**Learning a Graph Neural Network with Cross Modality Interaction for Image Fusion**|Jiawei Li et.al.|[2308.03256](http://arxiv.org/abs/2308.03256)|**[link](https://github.com/lok-18/ignet)**|
|**2023-08-06**|**Communication-Free Distributed GNN Training with Vertex Cut**|Kaidi Cao et.al.|[2308.03209](http://arxiv.org/abs/2308.03209)|null|
|**2023-08-05**|**Adversarial Erasing with Pruned Elements: Towards Better Graph Lottery Ticket**|Yuwen Wang et.al.|[2308.02916](http://arxiv.org/abs/2308.02916)|**[link](https://github.com/wangyuwen0627/ace-glt)**|
|**2023-08-09**|**Anomaly Detection in Global Financial Markets with Graph Neural Networks and Nonextensive Entropy**|Kleyton da Costa et.al.|[2308.02914](http://arxiv.org/abs/2308.02914)|null|
|**2023-08-04**|**Exploiting On-chip Heterogeneity of Versal Architecture for GNN Inference Acceleration**|Paul Chen et.al.|[2308.02749](http://arxiv.org/abs/2308.02749)|null|
|**2023-08-04**|**BlindSage: Label Inference Attacks against Node-level Vertical Federated Graph Neural Networks**|Marco Arazzi et.al.|[2308.02465](http://arxiv.org/abs/2308.02465)|null|
|**2023-08-04**|**Stability and Generalization of Hypergraph Collaborative Networks**|Michael Ng et.al.|[2308.02347](http://arxiv.org/abs/2308.02347)|null|
|**2023-08-04**|**RAHNet: Retrieval Augmented Hybrid Network for Long-tailed Graph Classification**|Zhengyang Mao et.al.|[2308.02335](http://arxiv.org/abs/2308.02335)|null|
|**2023-08-04**|**VQGraph: Graph Vector-Quantization for Bridging GNNs and MLPs**|Ling Yang et.al.|[2308.02117](http://arxiv.org/abs/2308.02117)|**[link](https://github.com/yangling0818/vqgraph)**|
|**2023-08-03**|**A Graphical Approach to Document Layout Analysis**|Jilin Wang et.al.|[2308.02051](http://arxiv.org/abs/2308.02051)|null|
|**2023-08-03**|**Evaluating Link Prediction Explanations for Graph Neural Networks**|Claudio Borile et.al.|[2308.01682](http://arxiv.org/abs/2308.01682)|**[link](https://github.com/cborile/eval_lp_xai)**|
|**2023-08-03**|**UniG-Encoder: A Universal Feature Encoder for Graph and Hypergraph Node Classification**|Minhao Zou et.al.|[2308.01650](http://arxiv.org/abs/2308.01650)|**[link](https://github.com/minhzou/unig-encoder)**|
|**2023-08-03**|**Deep Learning-based surrogate models for parametrized PDEs: handling geometric variability through graph neural networks**|Nicola Rares Franco et.al.|[2308.01602](http://arxiv.org/abs/2308.01602)|null|
|**2023-08-02**|**VertexSerum: Poisoning Graph Neural Networks for Link Inference**|Ruyi Ding et.al.|[2308.01469](http://arxiv.org/abs/2308.01469)|null|
|**2023-08-01**|**Graph Neural Networks for Forecasting Multivariate Realized Volatility with Spillover Effects**|Chao Zhang et.al.|[2308.01419](http://arxiv.org/abs/2308.01419)|null|
|**2023-08-02**|**Stereo Visual Odometry with Deep Learning-Based Point and Line Feature Matching using an Attention Graph Neural Network**|Shenbagaraj Kannapiran et.al.|[2308.01125](http://arxiv.org/abs/2308.01125)|null|
|**2023-08-02**|**Tango: rethinking quantization for graph neural network training on GPUs**|Shiyang Chen et.al.|[2308.00890](http://arxiv.org/abs/2308.00890)|null|
|**2023-08-02**|**Factor Graph Neural Networks**|Zhen Zhang et.al.|[2308.00887](http://arxiv.org/abs/2308.00887)|null|
|**2023-08-01**|**Reinforcement Learning-based Non-Autoregressive Solver for Traveling Salesman Problems**|Yubin Xiao et.al.|[2308.00560](http://arxiv.org/abs/2308.00560)|**[link](https://github.com/xybfight/nar4tsp)**|
|**2023-08-01**|**Graph Contrastive Learning with Generative Adversarial Network**|Cheng Wu et.al.|[2308.00535](http://arxiv.org/abs/2308.00535)|null|
|**2023-08-01**|**Challenging the Myth of Graph Collaborative Filtering: a Reasoned and Reproducibility-driven Analysis**|Vito Walter Anelli et.al.|[2308.00404](http://arxiv.org/abs/2308.00404)|**[link](https://github.com/sisinflab/graph-rss-reproducibility)**|
|**2023-07-31**|**TFE-GNN: A Temporal Fusion Encoder Using Graph Neural Networks for Fine-grained Encrypted Traffic Classification**|Haozhen Zhang et.al.|[2307.16713](http://arxiv.org/abs/2307.16713)|**[link](https://github.com/ViktorAxelsen/TFE-GNN)**|
|**2023-07-31**|**Graph Structure from Point Clouds: Geometric Attention is All You Need**|Daniel Murnane et.al.|[2307.16662](http://arxiv.org/abs/2307.16662)|**[link](https://github.com/murnanedaniel/geometricattention)**|
|**2023-07-31**|**MRA-GNN: Minutiae Relation-Aware Model over Graph Neural Network for Fingerprint Embedding**|Yapeng Su et.al.|[2307.16416](http://arxiv.org/abs/2307.16416)|null|
|**2023-07-31**|**Multi-modal Graph Neural Network for Early Diagnosis of Alzheimer's Disease from sMRI and PET Scans**|Yanteng Zhanga et.al.|[2307.16366](http://arxiv.org/abs/2307.16366)|null|
|**2023-07-29**|**ADR-GNN: Advection-Diffusion-Reaction Graph Neural Networks**|Moshe Eliasof et.al.|[2307.16092](http://arxiv.org/abs/2307.16092)|null|
|**2023-07-29**|**Graph Condensation for Inductive Node Representation Learning**|Xinyi Gao et.al.|[2307.15967](http://arxiv.org/abs/2307.15967)|null|
|**2023-07-29**|**Opportunistic Air Quality Monitoring and Forecasting with Expandable Graph Neural Networks**|Jingwei Zuo et.al.|[2307.15916](http://arxiv.org/abs/2307.15916)|null|
|**2023-07-28**|**Co-attention Graph Pooling for Efficient Pairwise Graph Interaction Learning**|Junhyun Lee et.al.|[2307.15377](http://arxiv.org/abs/2307.15377)|**[link](https://github.com/leejunhyun/coattentiongraphpooling)**|
|**2023-07-28**|**A universal equivariant graph neural network for the elasticity tensors of any crystal system**|Mingjian Wen et.al.|[2307.15242](http://arxiv.org/abs/2307.15242)|**[link](https://github.com/wengroup/matten)**|
|**2023-07-27**|**TimeGNN: Temporal Dynamic Graph Learning for Time Series Forecasting**|Nancy Xu et.al.|[2307.14680](http://arxiv.org/abs/2307.14680)|**[link](https://github.com/xun468/Time-GNN)**|
|**2023-07-27**|**HUTFormer: Hierarchical U-Net Transformer for Long-Term Traffic Forecasting**|Zezhi Shao et.al.|[2307.14596](http://arxiv.org/abs/2307.14596)|null|
|**2023-07-26**|**Improving Reliable Navigation under Uncertainty via Predictions Informed by Non-Local Information**|Raihan Islam Arnob et.al.|[2307.14501](http://arxiv.org/abs/2307.14501)|**[link](https://github.com/RAIL-group/RAIL-group-software/tree/main/modules/lsp_gnn)**|
|**2023-07-26**|**Distributed Computing of Functions of Structured Sources with Helper Side Information**|Derya Malak et.al.|[2307.13987](http://arxiv.org/abs/2307.13987)|null|
|**2023-07-26**|**Towards a cosmic ray composition measurement with the IceAct telescopes at the IceCube Neutrino Observatory**|Larissa Paul et.al.|[2307.13965](http://arxiv.org/abs/2307.13965)|null|
|**2023-07-26**|**Graph Neural Networks-based Hybrid Framework For Predicting Particle Crushing Strength**|Tongya Zheng et.al.|[2307.13909](http://arxiv.org/abs/2307.13909)|**[link](https://github.com/doujiang-zheng/gnn-for-particle-crushing)**|
|**2023-07-25**|**Uncertainty Quantification in the Road-level Traffic Risk Prediction by Spatial-Temporal Zero-Inflated Negative Binomial Graph Neural Network(STZINB-GNN)**|Xiaowei Gao et.al.|[2307.13816](http://arxiv.org/abs/2307.13816)|null|
|**2023-07-25**|**Multi-GPU Approach for Training of Graph ML Models on large CFD Meshes**|Sebastian Strönisch et.al.|[2307.13592](http://arxiv.org/abs/2307.13592)|null|
|**2023-07-25**|**Node Injection Link Stealing Attack**|Oualid Zari et.al.|[2307.13548](http://arxiv.org/abs/2307.13548)|null|
|**2023-07-25**|**Differentiable Turbulence II**|Varun Shankar et.al.|[2307.13533](http://arxiv.org/abs/2307.13533)|null|
|**2023-07-25**|**Finding Money Launderers Using Heterogeneous Graph Neural Networks**|Fredrik Johannessen et.al.|[2307.13499](http://arxiv.org/abs/2307.13499)|**[link](https://github.com/fredjo89/heterogeneous-mpnn)**|
|**2023-07-25**|**Combinatorial Auctions and Graph Neural Networks for Local Energy Flexibility Markets**|Awadelrahman M. A. Ahmed et.al.|[2307.13470](http://arxiv.org/abs/2307.13470)|null|
|**2023-07-25**|**Gaussian Graph with Prototypical Contrastive Learning in E-Commerce Bundle Recommendation**|Zhao-Yang Liu et.al.|[2307.13468](http://arxiv.org/abs/2307.13468)|null|
|**2023-07-25**|**Transferability of Graph Neural Networks using Graphon and Sampling Theories**|A. Martina Neuman et.al.|[2307.13206](http://arxiv.org/abs/2307.13206)|null|
|**2023-07-24**|**MARIO: Model Agnostic Recipe for Improving OOD Generalization of Graph Contrastive Learning**|Yun Zhu et.al.|[2307.13055](http://arxiv.org/abs/2307.13055)|**[link](https://github.com/zhuyun97/mario)**|
|**2023-07-24**|**Graph Neural Networks For Mapping Variables Between Programs -- Extended Version**|Pedro Orvalho et.al.|[2307.13014](http://arxiv.org/abs/2307.13014)|**[link](https://github.com/pmorvalho/ecai23-gnns-for-mapping-variables-between-programs)**|
|**2023-07-24**|**Comprehending Semantic Types in JSON Data with Graph Neural Networks**|Shuang Wei et.al.|[2307.12807](http://arxiv.org/abs/2307.12807)|null|
|**2023-07-24**|**Compact & Capable: Harnessing Graph Neural Networks and Edge Convolution for Medical Image Classification**|Aryan Singh et.al.|[2307.12790](http://arxiv.org/abs/2307.12790)|**[link](https://github.com/anonrepo-keeper/gcnn-ec)**|
|**2023-07-24**|**HiHGNN: Accelerating HGNNs through Parallelism and Data Reusability Exploitation**|Runzhen Xue et.al.|[2307.12765](http://arxiv.org/abs/2307.12765)|null|
|**2023-07-24**|**Addressing the Impact of Localized Training Data in Graph Neural Networks**|Singh Akansha et.al.|[2307.12689](http://arxiv.org/abs/2307.12689)|**[link](https://github.com/akanshaaga/reg_appnp)**|
|**2023-07-24**|**Learning Resource Allocation Policy: Vertex-GNN or Edge-GNN?**|Yao Peng et.al.|[2307.12480](http://arxiv.org/abs/2307.12480)|null|
|**2023-07-23**|**EchoGLAD: Hierarchical Graph Neural Networks for Left Ventricle Landmark Detection on Echocardiograms**|Masoud Mokhtari et.al.|[2307.12229](http://arxiv.org/abs/2307.12229)|**[link](https://github.com/masoudmo/echoglad)**|
|**2023-07-22**|**Collaborative Graph Neural Networks for Attributed Network Embedding**|Qiaoyu Tan et.al.|[2307.11981](http://arxiv.org/abs/2307.11981)|**[link](https://github.com/qiaoyut/conn)**|
|**2023-07-21**|**Prompt-Based Zero- and Few-Shot Node Classification: A Multimodal Approach**|Yuexin Li et.al.|[2307.11572](http://arxiv.org/abs/2307.11572)|null|
|**2023-07-20**|**A Novel Unsupervised Graph Wavelet Autoencoder for Mechanical System Fault Detection**|Tianfu Li et.al.|[2307.10676](http://arxiv.org/abs/2307.10676)|**[link](https://github.com/HazeDT/ARGWAE)**|
|**2023-07-22**|**Air Traffic Controller Workload Level Prediction using Conformalized Dynamical Graph Learning**|Yutian Pang et.al.|[2307.10559](http://arxiv.org/abs/2307.10559)|**[link](https://github.com/ymlasu/para-atm-collection)**|
|**2023-07-23**|**Power Allocation for Device-to-Device Interference Channel Using Truncated Graph Transformers**|Dohoon Kim et.al.|[2307.10538](http://arxiv.org/abs/2307.10538)|null|
|**2023-07-19**|**Uncertainty Quantification for Molecular Property Predictions with Graph Neural Architecture Search**|Shengli Jiang et.al.|[2307.10438](http://arxiv.org/abs/2307.10438)|**[link](https://github.com/zavalab/ML)**|
|**2023-07-19**|**AutoAMG( $θ$ ): An Auto-tuned AMG Method Based on Deep Learning for Strong Threshold**|Haifeng Zou et.al.|[2307.09879](http://arxiv.org/abs/2307.09879)|null|
|**2023-07-19**|**Detecting Vulnerable Nodes in Urban Infrastructure Interdependent Network**|Jinzhu Mao et.al.|[2307.09866](http://arxiv.org/abs/2307.09866)|**[link](https://github.com/tsinghua-fib-lab/kdd2023-id546-urbaninfra)**|
|**2023-07-19**|**How Curvature Enhance the Adaptation Power of Framelet GCNs**|Dai Shi et.al.|[2307.09768](http://arxiv.org/abs/2307.09768)|**[link](https://github.com/dshi3553usyd/curvature_enhanced_graph_convolution)**|
|**2023-07-18**|**Anticipating Technical Expertise and Capability Evolution in Research Communities using Dynamic Graph Transformers**|Sameera Horawalavithana et.al.|[2307.09665](http://arxiv.org/abs/2307.09665)|null|
|**2023-07-18**|**Neural Priority Queues for Graph Neural Networks**|Rishabh Jain et.al.|[2307.09660](http://arxiv.org/abs/2307.09660)|null|
|**2023-07-18**|**Rumor Detection with Diverse Counterfactual Evidence**|Kaiwei Zhang et.al.|[2307.09296](http://arxiv.org/abs/2307.09296)|**[link](https://github.com/vicinity111/dce-rd)**|
|**2023-07-18**|**Learning Adaptive Neighborhoods for Graph Neural Networks**|Avishkar Saha et.al.|[2307.09065](http://arxiv.org/abs/2307.09065)|null|
|**2023-07-18**|**Sharpness-Aware Graph Collaborative Filtering**|Huiyuan Chen et.al.|[2307.08910](http://arxiv.org/abs/2307.08910)|null|
|**2023-07-17**|**Disentangling Node Attributes from Graph Topology for Improved Generalizability in Link Prediction**|Ayan Chatterjee et.al.|[2307.08877](http://arxiv.org/abs/2307.08877)|**[link](https://github.com/chatterjeeayan/upna)**|
|**2023-07-17**|**Latent Space Representations of Neural Algorithmic Reasoners**|Vladimir V. Mirjanić et.al.|[2307.08874](http://arxiv.org/abs/2307.08874)|**[link](https://github.com/mirjanic/nar-latent-spaces)**|
|**2023-07-17**|**Curriculum Learning for Graph Neural Networks: A Multiview Competence-based Approach**|Nidhi Vakil et.al.|[2307.08859](http://arxiv.org/abs/2307.08859)|null|
|**2023-07-17**|**PolyGNN: Polyhedron-based Graph Neural Network for 3D Building Reconstruction from Point Clouds**|Zhaiyu Chen et.al.|[2307.08636](http://arxiv.org/abs/2307.08636)|**[link](https://github.com/chenzhaiyu/polygnn)**|
|**2023-07-17**|**G-Scan: Graph Neural Networks for Line-Level Vulnerability Identification in Smart Contracts**|Christoph Sendner et.al.|[2307.08549](http://arxiv.org/abs/2307.08549)|null|
|**2023-07-17**|**Towards eXplainable AI for Mobility Data Science**|Anahid Jalali et.al.|[2307.08461](http://arxiv.org/abs/2307.08461)|null|
|**2023-07-17**|**Long-range Dependency based Multi-Layer Perceptron for Heterogeneous Information Networks**|Chao Li et.al.|[2307.08430](http://arxiv.org/abs/2307.08430)|**[link](https://github.com/jhl-hust/ldmlp)**|
|**2023-07-17**|**Correlation-aware Spatial-Temporal Graph Learning for Multivariate Time-series Anomaly Detection**|Yu Zheng et.al.|[2307.08390](http://arxiv.org/abs/2307.08390)|**[link](https://github.com/astha-chem/mvts-ano-eval)**|
|**2023-07-16**|**Heterogeneous graphs model spatial relationships between biological entities for breast cancer diagnosis**|Akhila Krishna K et.al.|[2307.08132](http://arxiv.org/abs/2307.08132)|null|
|**2023-07-16**|**INFLECT-DGNN: Influencer Prediction with Dynamic Graph Neural Networks**|Elena Tiukhova et.al.|[2307.08131](http://arxiv.org/abs/2307.08131)|**[link](https://github.com/banking-analytics-lab/inflect)**|
|**2023-07-16**|**MaGNAS: A Mapping-Aware Graph Neural Architecture Search Framework for Heterogeneous MPSoC Deployment**|Mohanad Odema et.al.|[2307.08065](http://arxiv.org/abs/2307.08065)|null|
|**2023-07-16**|**Automated Polynomial Filter Learning for Graph Neural Networks**|Wendi Yu et.al.|[2307.07956](http://arxiv.org/abs/2307.07956)|null|
|**2023-07-15**|**RegExplainer: Generating Explanations for Graph Neural Networks in Regression Task**|Jiaxing Zhang et.al.|[2307.07840](http://arxiv.org/abs/2307.07840)|**[link](https://github.com/jz48/regexplainer)**|
|**2023-07-14**|**Real-time Graph Building on FPGAs for Machine Learning Trigger Applications in Particle Physics**|Marc Neu et.al.|[2307.07289](http://arxiv.org/abs/2307.07289)|null|
|**2023-07-13**|**MaxCorrMGNN: A Multi-Graph Neural Network Framework for Generalized Multimodal Fusion of Medical Data for Outcome Prediction**|Niharika S. D'Souza et.al.|[2307.07093](http://arxiv.org/abs/2307.07093)|null|
|**2023-07-13**|**Espaloma-0.3.0: Machine-learned molecular mechanics force field for the simulation of protein-ligand systems and beyond**|Kenichiro Takaba et.al.|[2307.07085](http://arxiv.org/abs/2307.07085)|**[link](https://github.com/choderalab/refit-espaloma)**|
|**2023-07-13**|**Privacy-Utility Trade-offs in Neural Networks for Medical Population Graphs: Insights from Differential Privacy and Graph Structure**|Tamara T. Mueller et.al.|[2307.06760](http://arxiv.org/abs/2307.06760)|null|
|**2023-07-13**|**Frameless Graph Knowledge Distillation**|Dai Shi et.al.|[2307.06631](http://arxiv.org/abs/2307.06631)|**[link](https://github.com/dshi3553usyd/frameless_graph_distillation)**|
|**2023-07-15**|**Going Beyond Local: Global Graph-Enhanced Personalized News Recommendations**|Boming Yang et.al.|[2307.06576](http://arxiv.org/abs/2307.06576)|**[link](https://github.com/tinyrolls/glory)**|
|**2023-07-12**|**Improved selective background Monte Carlo simulation at Belle II with graph attention networks and weighted events**|Boyang Yu et.al.|[2307.06434](http://arxiv.org/abs/2307.06434)|null|
|**2023-07-12**|**Differentially Private Decoupled Graph Convolutions for Multigranular Topology Protection**|Eli Chien et.al.|[2307.06422](http://arxiv.org/abs/2307.06422)|**[link](https://github.com/thupchnsky/dp-gnn)**|
|**2023-07-12**|**Learning Stochastic Dynamical Systems as an Implicit Regularization with Graph Neural Networks**|Jin Guo et.al.|[2307.06097](http://arxiv.org/abs/2307.06097)|null|
|**2023-07-12**|**An OOD Multi-Task Perspective for Link Prediction with New Relation Types and Nodes**|Jincheng Zhou et.al.|[2307.06046](http://arxiv.org/abs/2307.06046)|null|
|**2023-07-12**|**An Effective and Efficient Time-aware Entity Alignment Framework via Two-aspect Three-view Label Propagation**|Li Cai et.al.|[2307.06013](http://arxiv.org/abs/2307.06013)|**[link](https://github.com/lcai2/lighttea)**|
|**2023-07-12**|**FIS-ONE: Floor Identification System with One Label for Crowdsourced RF Signals**|Weipeng Zhuo et.al.|[2307.05914](http://arxiv.org/abs/2307.05914)|**[link](https://github.com/stevezhuo/fis-one)**|
|**2023-07-12**|**Knowledge-Driven Resource Allocation for D2D Networks: A WMMSE Unrolled Graph Neural Network Approach**|Hao Yang et.al.|[2307.05882](http://arxiv.org/abs/2307.05882)|null|
|**2023-07-11**|**Influential Simplices Mining via Simplicial Convolutional Network**|Yujie Zeng et.al.|[2307.05841](http://arxiv.org/abs/2307.05841)|null|
|**2023-07-11**|**Weisfeiler and Lehman Go Measurement Modeling: Probing the Validity of the WL Test**|Arjun Subramonian et.al.|[2307.05775](http://arxiv.org/abs/2307.05775)|**[link](https://github.com/arjunsubramonian/wl-test-exploration)**|
|**2023-07-11**|**Discovering Symbolic Laws Directly from Trajectories with Hamiltonian Graph Neural Networks**|Suresh Bishnoi et.al.|[2307.05299](http://arxiv.org/abs/2307.05299)|null|
|**2023-07-11**|**Supervised Attention Using Homophily in Graph Neural Networks**|Michail Chatzianastasis et.al.|[2307.05217](http://arxiv.org/abs/2307.05217)|null|
|**2023-07-11**|**ResMatch: Residual Attention Learning for Local Feature Matching**|Yuxin Deng et.al.|[2307.05180](http://arxiv.org/abs/2307.05180)|**[link](https://github.com/acuooooo/resmatch)**|
|**2023-07-11**|**A Modal Logic for Explaining some Graph Neural Networks**|Pierre Nunn et.al.|[2307.05150](http://arxiv.org/abs/2307.05150)|null|
|**2023-07-11**|**Transaction Fraud Detection via Spatial-Temporal-Aware Graph Transformer**|Yue Tian et.al.|[2307.05121](http://arxiv.org/abs/2307.05121)|null|
|**2023-07-11**|**Neural-Symbolic Recommendation with Graph-Enhanced Information**|Bang Chen et.al.|[2307.05036](http://arxiv.org/abs/2307.05036)|**[link](https://github.com/hanzo2020/gnnlr)**|
|**2023-07-11**|**Intrinsically motivated graph exploration using network theories of human curiosity**|Shubhankar P. Patankar et.al.|[2307.04962](http://arxiv.org/abs/2307.04962)|**[link](https://github.com/spatank/curiosity-graphs)**|
|**2023-07-10**|**Improving Fairness of Graph Neural Networks: A Graph Counterfactual Perspective**|Zhimeng Guo et.al.|[2307.04937](http://arxiv.org/abs/2307.04937)|**[link](https://github.com/timelovercc/caf-gnn)**|
|**2023-07-10**|**Learning to Solve Constraint Satisfaction Problems with Recurrent Transformer**|Zhun Yang et.al.|[2307.04895](http://arxiv.org/abs/2307.04895)|**[link](https://github.com/azreasoners/recurrent_transformer)**|
|**2023-07-10**|**On the power of graph neural networks and the role of the activation function**|Sammy Khalife et.al.|[2307.04661](http://arxiv.org/abs/2307.04661)|null|
|**2023-07-10**|**Multi-modal Graph Learning over UMLS Knowledge Graphs**|Manuel Burger et.al.|[2307.04461](http://arxiv.org/abs/2307.04461)|**[link](https://github.com/ratschlab/mmugl)**|
|**2023-07-10**|**Privacy-Preserving Graph Machine Learning from Data to Computation: A Survey**|Dongqi Fu et.al.|[2307.04338](http://arxiv.org/abs/2307.04338)|null|
|**2023-07-10**|**Generalizing Graph ODE for Learning Complex System Dynamics across Environments**|Zijie Huang et.al.|[2307.04287](http://arxiv.org/abs/2307.04287)|null|
|**2023-07-08**|**Fairness-Aware Graph Neural Networks: A Survey**|April Chen et.al.|[2307.03929](http://arxiv.org/abs/2307.03929)|null|
|**2023-07-08**|**The relationship between activated H2 bond length and adsorption distance on MXenes identified with graph neural network and resonating valence bond theory**|Jiewei Cheng et.al.|[2307.03907](http://arxiv.org/abs/2307.03907)|null|
|**2023-07-07**|**A Survey on Graph Neural Networks for Time Series: Forecasting, Classification, Imputation, and Anomaly Detection**|Ming Jin et.al.|[2307.03759](http://arxiv.org/abs/2307.03759)|**[link](https://github.com/kimmeen/awesome-gnn4ts)**|
|**2023-07-07**|**DE-TGN: Uncertainty-Aware Human Motion Forecasting using Deep Ensembles**|Kareem A. Eltouny et.al.|[2307.03610](http://arxiv.org/abs/2307.03610)|null|
|**2023-07-07**|**GEANN: Scalable Graph Augmentations for Multi-Horizon Time Series Forecasting**|Sitan Yang et.al.|[2307.03595](http://arxiv.org/abs/2307.03595)|null|
|**2023-07-07**|**Roman Numeral Analysis with Graph Neural Networks: Onset-wise Predictions from Note-wise Features**|Emmanouil Karystinaios et.al.|[2307.03544](http://arxiv.org/abs/2307.03544)|**[link](https://github.com/manoskary/chordgnn)**|
|**2023-07-07**|**Learning from Heterogeneity: A Dynamic Learning Framework for Hypergraphs**|Tiehua Zhang et.al.|[2307.03411](http://arxiv.org/abs/2307.03411)|**[link](https://github.com/papercodeeric/lfh)**|
|**2023-07-10**|**Exploring the Potential of Large Language Models (LLMs) in Learning on Graphs**|Zhikai Chen et.al.|[2307.03393](http://arxiv.org/abs/2307.03393)|**[link](https://github.com/CurryTang/Graph-LLM)**|
|**2023-07-06**|**CPDG: A Contrastive Pre-Training Method for Dynamic Graph Neural Networks**|Yuanchen Bei et.al.|[2307.02813](http://arxiv.org/abs/2307.02813)|null|
|**2023-07-05**|**Exploring Multimodal Approaches for Alzheimer's Disease Detection Using Patient Speech Transcript and Audio Data**|Hongmin Cai et.al.|[2307.02514](http://arxiv.org/abs/2307.02514)|**[link](https://github.com/shui-dun/multimodal_ad)**|
|**2023-07-05**|**Equivariant graph neural network interatomic potential for Green-Kubo thermal conductivity in phase change materials**|Sung-Ho Lee et.al.|[2307.02327](http://arxiv.org/abs/2307.02327)|null|
|**2023-07-10**|**ChiENN: Embracing Molecular Chirality with Graph Neural Networks**|Piotr Gaiński et.al.|[2307.02198](http://arxiv.org/abs/2307.02198)|**[link](https://github.com/gmum/chienn)**|
|**2023-07-05**|**Robust Graph Structure Learning with the Alignment of Features and Adjacency Matrix**|Shaogao Lv et.al.|[2307.02126](http://arxiv.org/abs/2307.02126)|null|
|**2023-07-05**|**Graph Contrastive Topic Model**|Zheheng Luo et.al.|[2307.02078](http://arxiv.org/abs/2307.02078)|**[link](https://github.com/zhehengluok/gctm)**|
|**2023-07-05**|**Graph Neural Network-based Power Flow Model**|Mingjian Tuo et.al.|[2307.02049](http://arxiv.org/abs/2307.02049)|null|
|**2023-07-05**|**Muti-scale Graph Neural Network with Signed-attention for Social Bot Detection: A Frequency Perspective**|Shuhao Shi et.al.|[2307.01968](http://arxiv.org/abs/2307.01968)|null|
|**2023-07-04**|**A Neural Collapse Perspective on Feature Evolution in Graph Neural Networks**|Vignesh Kothapalli et.al.|[2307.01951](http://arxiv.org/abs/2307.01951)|**[link](https://github.com/kvignesh1420/gnn_collapse)**|
|**2023-07-04**|**Euclidean Equivariant Models for Generative Graphical Inverse Kinematics**|Oliver Limoyo et.al.|[2307.01902](http://arxiv.org/abs/2307.01902)|null|
|**2023-07-04**|**GHOST: A Graph Neural Network Accelerator using Silicon Photonics**|Salma Afifi et.al.|[2307.01782](http://arxiv.org/abs/2307.01782)|null|
|**2023-07-04**|**Serving Graph Neural Networks With Distributed Fog Servers For Smart IoT Services**|Liekang Zeng et.al.|[2307.01684](http://arxiv.org/abs/2307.01684)|null|
|**2023-07-03**|**PlanE: Representation Learning over Planar Graphs**|Radoslav Dimitrov et.al.|[2307.01180](http://arxiv.org/abs/2307.01180)|**[link](https://github.com/zzysonny/plane)**|
|**2023-07-03**|**A Survey on Graph Classification and Link Prediction based on GNN**|Xingyu Liu et.al.|[2307.00865](http://arxiv.org/abs/2307.00865)|null|
|**2023-07-04**|**CardiGraphormer: Unveiling the Power of Self-Supervised Learning in Revolutionizing Drug Discovery**|Abhijit Gupta et.al.|[2307.00859](http://arxiv.org/abs/2307.00859)|null|
|**2023-07-03**|**Beyond the Snapshot: Brain Tokenized Graph Transformer for Longitudinal Brain Functional Connectome Embedding**|Zijian Dong et.al.|[2307.00858](http://arxiv.org/abs/2307.00858)|**[link](https://github.com/zijiand/brain-tokengt)**|
|**2023-07-03**|**GA-DRL: Graph Neural Network-Augmented Deep Reinforcement Learning for DAG Task Scheduling over Dynamic Vehicular Clouds**|Zhang Liu et.al.|[2307.00777](http://arxiv.org/abs/2307.00777)|null|
|**2023-07-02**|**Shared Growth of Graph Neural Networks via Free-direction Knowledge Distillation**|Kaituo Feng et.al.|[2307.00534](http://arxiv.org/abs/2307.00534)|null|
|**2023-07-02**|**Graph Neural Network based Log Anomaly Detection and Explanation**|Zhong Li et.al.|[2307.00527](http://arxiv.org/abs/2307.00527)|**[link](https://github.com/zhonglifr/logs2graph)**|
|**2023-07-02**|**STG4Traffic: A Survey and Benchmark of Spatial-Temporal Graph Neural Networks for Traffic Prediction**|Xunlian Luo et.al.|[2307.00495](http://arxiv.org/abs/2307.00495)|**[link](https://github.com/trainingl/stg4traffic)**|
|**2023-07-01**|**MobileViG: Graph-Based Sparse Attention for Mobile Vision Applications**|Mustafa Munir et.al.|[2307.00395](http://arxiv.org/abs/2307.00395)|**[link](https://github.com/sldgroup/mobilevig)**|
|**2023-07-01**|**Recursive Algorithmic Reasoning**|Dulhan Jayalath et.al.|[2307.00337](http://arxiv.org/abs/2307.00337)|**[link](https://github.com/DJayalath/gnn-call-stack)**|
|**2023-06-30**|**Topologically Attributed Graphs for Shape Discrimination**|Justin Curry et.al.|[2306.17805](http://arxiv.org/abs/2306.17805)|**[link](https://github.com/trneedham/Topologically-Attributed-Graphs)**|
|**2023-06-30**|**Graphtester: Exploring Theoretical Boundaries of GNNs on Graph Datasets**|Eren Akbiyik et.al.|[2306.17482](http://arxiv.org/abs/2306.17482)|**[link](https://github.com/meakbiyik/graphtester)**|
|**2023-07-03**|**LMBot: Distilling Graph Knowledge into Language Model for Graph-less Deployment in Twitter Bot Detection**|Zijian Cai et.al.|[2306.17408](http://arxiv.org/abs/2306.17408)|**[link](https://github.com/czjdsg/lmbot)**|
|**2023-06-29**|**A Neural Separation Algorithm for the Rounded Capacity Inequalities**|Hyeonah Kim et.al.|[2306.17283](http://arxiv.org/abs/2306.17283)|**[link](https://github.com/hyeonahkimm/neuralsep)**|
|**2023-06-29**|**Sparsity exploitation via discovering graphical models in multi-variate time-series forecasting**|Ngoc-Dung Do et.al.|[2306.17090](http://arxiv.org/abs/2306.17090)|**[link](https://github.com/hysonlab/graphlasso)**|
|**2023-06-29**|**Diffusion-Jump GNNs: Homophiliation via Learnable Metric Filters**|Ahmed Begga et.al.|[2306.16976](http://arxiv.org/abs/2306.16976)|**[link](https://github.com/AhmedBegggaUA/TFM)**|
|**2023-06-30**|**Dynamic-Resolution Model Learning for Object Pile Manipulation**|Yixuan Wang et.al.|[2306.16700](http://arxiv.org/abs/2306.16700)|null|
|**2023-06-28**|**Accelerating Sampling and Aggregation Operations in GNN Frameworks with GPU Initiated Direct Storage Accesses**|Jeongmin Brian Park et.al.|[2306.16384](http://arxiv.org/abs/2306.16384)|**[link](https://github.com/jeongminpark417/gids)**|
|**2023-06-28**|**Enhancing Dialogue Generation via Dynamic Graph Knowledge Aggregation**|Chen Tang et.al.|[2306.16195](http://arxiv.org/abs/2306.16195)|**[link](https://github.com/tangg555/sabart)**|
|**2023-06-28**|**Mass Spectra Prediction with Structural Motif-based Graph Neural Networks**|Jiwon Park et.al.|[2306.16085](http://arxiv.org/abs/2306.16085)|null|
|**2023-06-28**|**Graph neural networks for sound source localization on distributed microphone networks**|Eric Grinstein et.al.|[2306.16081](http://arxiv.org/abs/2306.16081)|**[link](https://github.com/egrinstein/gnn_ssl)**|
|**2023-06-28**|**Graph Interpolation via Fast Fused-Gromovization**|Xinyu Ma et.al.|[2306.15963](http://arxiv.org/abs/2306.15963)|**[link](https://github.com/arthurleom/fgwmixup)**|
|**2023-06-28**|**Learning Dynamic Graphs from All Contextual Information for Accurate Point-of-Interest Visit Forecasting**|Arash Hajisafi et.al.|[2306.15927](http://arxiv.org/abs/2306.15927)|**[link](https://github.com/USC-InfoLab/busyness-graph-neural-network)**|
|**2023-06-28**|**Hierarchical Graph Neural Networks for Proprioceptive 6D Pose Estimation of In-hand Objects**|Alireza Rezazadeh et.al.|[2306.15858](http://arxiv.org/abs/2306.15858)|null|
|**2023-06-27**|**Physics-inspired spatiotemporal-graph AI ensemble for gravitational wave detection**|Minyang Tian et.al.|[2306.15728](http://arxiv.org/abs/2306.15728)|**[link](https://github.com/mtian8/gw_spatiotemporal_gnn)**|
|**2023-06-28**|**Asynchronous Algorithmic Alignment with Cocycles**|Andrew Dudzik et.al.|[2306.15632](http://arxiv.org/abs/2306.15632)|null|
|**2023-06-27**|**Higher-order Graph Attention Network for Stock Selection with Joint Analysis**|Yang Qiao et.al.|[2306.15526](http://arxiv.org/abs/2306.15526)|null|
|**2023-06-27**|**Adversarial Training for Graph Neural Networks**|Lukas Gosch et.al.|[2306.15427](http://arxiv.org/abs/2306.15427)|null|
|**2023-06-27**|**Input-sensitive dense-sparse primitive compositions for GNN acceleration**|Damitha Lenadora et.al.|[2306.15155](http://arxiv.org/abs/2306.15155)|null|
|**2023-06-27**|**Metapopulation Graph Neural Networks: Deep Metapopulation Epidemic Modeling with Human Mobility**|Qi Cao et.al.|[2306.14857](http://arxiv.org/abs/2306.14857)|null|
|**2023-06-26**|**Accelerating Molecular Graph Neural Networks via Knowledge Distillation**|Filip Ekström Kelvinius et.al.|[2306.14818](http://arxiv.org/abs/2306.14818)|**[link](https://github.com/gasteigerjo/ocp)**|
|**2023-06-26**|**RoboCook: Long-Horizon Elasto-Plastic Object Manipulation with Diverse Tools**|Haochen Shi et.al.|[2306.14447](http://arxiv.org/abs/2306.14447)|null|
|**2023-06-26**|**Interpretable Sparsification of Brain Graphs: Better Practices and Effective Designs for Graph Neural Networks**|Gaotang Li et.al.|[2306.14375](http://arxiv.org/abs/2306.14375)|**[link](https://github.com/motivationss/igs)**|
|**2023-06-25**|**GPatcher: A Simple and Adaptive MLP Model for Alleviating Graph Heterophily**|Shuaicheng Zhang et.al.|[2306.14340](http://arxiv.org/abs/2306.14340)|null|
|**2023-06-25**|**Real-time Seismic Intensity Prediction using Self-supervised Contrastive GNN for Earthquake Early Warning**|Rafid Umayer Murshed et.al.|[2306.14336](http://arxiv.org/abs/2306.14336)|null|
|**2023-06-25**|**GPT-assisted learning of structure-property relationships by graph neural networks: Application to rare-earth doped phosphors**|Xiang Zhang et.al.|[2306.14238](http://arxiv.org/abs/2306.14238)|**[link](https://github.com/xiangzhang1-yysun/2306.14238.notebooks.public)**|
|**2023-06-25**|**Weisfeiler-Lehman Graph Kernel Method: A New Approach to Weak Chemical Tagging**|Yuan-Sen Ting et.al.|[2306.14206](http://arxiv.org/abs/2306.14206)|null|
|**2023-06-24**|**Leveraging Brain Modularity Prior for Interpretable Representation Learning of fMRI**|Qianqian Wang et.al.|[2306.14080](http://arxiv.org/abs/2306.14080)|null|
|**2023-06-24**|**Modeling Graphs Beyond Hyperbolic: Graph Neural Networks in Symmetric Positive Definite Matrices**|Wei Zhao et.al.|[2306.14064](http://arxiv.org/abs/2306.14064)|**[link](https://github.com/andyweizhao/spd4gnns)**|
|**2023-06-23**|**Torsion Graph Neural Networks**|Cong Shen et.al.|[2306.13541](http://arxiv.org/abs/2306.13541)|**[link](https://github.com/cs-bio/torgnn)**|
|**2023-06-23**|**PathMLP: Smooth Path Towards High-order Homophily**|Chenxuan Xie et.al.|[2306.13532](http://arxiv.org/abs/2306.13532)|**[link](https://github.com/graph4sec-team/pathmlp)**|
|**2023-06-23**|**A Graph Neural Network Approach for Temporal Mesh Blending and Correspondence**|Aalok Gangopadhyay et.al.|[2306.13452](http://arxiv.org/abs/2306.13452)|null|
|**2023-06-23**|**TrustGuard: GNN-based Robust and Explainable Trust Evaluation with Dynamicity Support**|Jie Wang et.al.|[2306.13339](http://arxiv.org/abs/2306.13339)|**[link](https://github.com/jieerbobo/trustguard)**|
|**2023-06-22**|**A Decade of Scholarly Research on Open Knowledge Graphs**|Houcemeddine Turki et.al.|[2306.13186](http://arxiv.org/abs/2306.13186)|**[link](https://github.com/data-engineering-and-semantics/openkgbiblio)**|
|**2023-06-22**|**Evolving Computation Graphs**|Andreea Deac et.al.|[2306.12943](http://arxiv.org/abs/2306.12943)|null|
|**2023-06-22**|**StrainNet: Predicting crystal structure elastic properties using SE(3)-equivariant graph neural networks**|Teerachote Pakornchote et.al.|[2306.12818](http://arxiv.org/abs/2306.12818)|**[link](https://github.com/trachote/predict_elastic_tensor)**|
|**2023-06-22**|**On Addressing the Limitations of Graph Neural Networks**|Sitao Luan et.al.|[2306.12640](http://arxiv.org/abs/2306.12640)|null|
|**2023-06-21**|**DGC-GNN: Descriptor-free Geometric-Color Graph Neural Network for 2D-3D Matching**|Shuzhe Wang et.al.|[2306.12547](http://arxiv.org/abs/2306.12547)|**[link](https://github.com/aaltovision/dgc-gnn-release)**|
|**2023-06-21**|**Learning the galaxy-environment connection with graph neural networks**|John F. Wu et.al.|[2306.12327](http://arxiv.org/abs/2306.12327)|**[link](https://github.com/jwuphysics/halo-gnns)**|
|**2023-06-21**|**GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection**|Jianheng Tang et.al.|[2306.12251](http://arxiv.org/abs/2306.12251)|**[link](https://github.com/squareroot3/gadbench)**|
|**2023-06-21**|**Predicting protein variants with equivariant graph neural networks**|Antonia Boca et.al.|[2306.12231](http://arxiv.org/abs/2306.12231)|**[link](https://github.com/semiluna/partiii-amino-acid-prediction)**|
|**2023-06-21**|**Spatial Heterophily Aware Graph Neural Networks**|Congxi Xiao et.al.|[2306.12139](http://arxiv.org/abs/2306.12139)|**[link](https://github.com/paddlepaddle/paddlespatial)**|
|**2023-06-20**|**Principles for Initialization and Architecture Selection in Graph Neural Networks with ReLU Activations**|Gage DeZoort et.al.|[2306.11668](http://arxiv.org/abs/2306.11668)|null|
|**2023-06-20**|**Provably Powerful Graph Neural Networks for Directed Multigraphs**|Béni Egressy et.al.|[2306.11586](http://arxiv.org/abs/2306.11586)|null|
|**2023-06-20**|**Hypergraph Classification via Persistent Homology**|Mehmet Emin Aktas et.al.|[2306.11484](http://arxiv.org/abs/2306.11484)|null|
|**2023-06-20**|**Graph Neural Stochastic Differential Equations for Learning Brownian Dynamics**|Suresh Bishnoi et.al.|[2306.11435](http://arxiv.org/abs/2306.11435)|null|
|**2023-06-20**|**Hierarchical GNNs for Large Graph Generation**|Alex O. Davies et.al.|[2306.11412](http://arxiv.org/abs/2306.11412)|null|
|**2023-06-20**|**Low Latency Edge Classification GNN for Particle Trajectory Tracking on FPGAs**|Shi-Yu Huang et.al.|[2306.11330](http://arxiv.org/abs/2306.11330)|null|
|**2023-06-20**|**Deep graph kernel point processes**|Zheng Dong et.al.|[2306.11313](http://arxiv.org/abs/2306.11313)|null|
|**2023-06-20**|**GraphGLOW: Universal and Generalizable Structure Learning for Graph Neural Networks**|Wentao Zhao et.al.|[2306.11264](http://arxiv.org/abs/2306.11264)|**[link](https://github.com/wtaozhao/graphglow)**|
|**2023-06-19**|**Learning Models of Adversarial Agent Behavior under Partial Observability**|Sean Ye et.al.|[2306.11168](http://arxiv.org/abs/2306.11168)|**[link](https://github.com/core-robotics-lab/opponent-modeling)**|
|**2023-06-19**|**Graph Self-Supervised Learning for Endoscopic Image Matching**|Manel Farhat et.al.|[2306.11141](http://arxiv.org/abs/2306.11141)|**[link](https://github.com/abenhamadou/graph-self-supervised-learning-for-endoscopic-image-matching)**|
|**2023-06-16**|**Uncertainty Quantification via Spatial-Temporal Tweedie Model for Zero-inflated and Long-tail Travel Demand Prediction**|Xinke Jiang et.al.|[2306.09882](http://arxiv.org/abs/2306.09882)|**[link](https://github.com/sttdanonymous/sttd)**|
|**2023-06-16**|**Learning CO $_2$ plume migration in faulted reservoirs with Graph Neural Networks**|Xin Ju et.al.|[2306.09648](http://arxiv.org/abs/2306.09648)|null|
|**2023-06-19**|**From Hypergraph Energy Functions to Hypergraph Neural Networks**|Yuxin Wang et.al.|[2306.09623](http://arxiv.org/abs/2306.09623)|**[link](https://github.com/yxzwang/phenomnn)**|
|**2023-06-16**|**GraphSHA: Synthesizing Harder Samples for Class-Imbalanced Node Classification**|Wen-Zhi Li et.al.|[2306.09612](http://arxiv.org/abs/2306.09612)|**[link](https://github.com/wenzhilics/graphsha)**|
|**2023-06-15**|**Kriging Convolutional Networks**|Gabriel Appleby et.al.|[2306.09463](http://arxiv.org/abs/2306.09463)|**[link](https://github.com/tufts-ml/kcn-torch)**|
|**2023-06-19**|**Spatiotemporal-Augmented Graph Neural Networks for Human Mobility Simulation**|Yu Wang et.al.|[2306.09381](http://arxiv.org/abs/2306.09381)|**[link](https://github.com/star607/star-tkde)**|
|**2023-06-15**|**The Split Matters: Flat Minima Methods for Improving the Performance of GNNs**|Nicolas Lell et.al.|[2306.09121](http://arxiv.org/abs/2306.09121)|**[link](https://github.com/foisunt/fmms-in-gnns)**|
|**2023-06-15**|**On Strengthening and Defending Graph Reconstruction Attack with Markov Chain Approximation**|Zhanke Zhou et.al.|[2306.09104](http://arxiv.org/abs/2306.09104)|**[link](https://github.com/tmlr-group/mc-gra)**|
|**2023-06-20**|**Scalable Resource Management for Dynamic MEC: An Unsupervised Link-Output Graph Neural Network Approach**|Xiucheng Wang et.al.|[2306.08938](http://arxiv.org/abs/2306.08938)|**[link](https://github.com/UNIC-Lab/LOGNN)**|
|**2023-06-15**|**Multi-Temporal Relationship Inference in Urban Areas**|Shuangli Li et.al.|[2306.08921](http://arxiv.org/abs/2306.08921)|**[link](https://github.com/agave233/seenet)**|
|**2023-06-14**|**A Unified Framework of Graph Information Bottleneck for Robustness and Membership Privacy**|Enyan Dai et.al.|[2306.08604](http://arxiv.org/abs/2306.08604)|null|
|**2023-06-14**|**Self-supervised Learning and Graph Classification under Heterophily**|Yilin Ding et.al.|[2306.08469](http://arxiv.org/abs/2306.08469)|null|
|**2023-06-14**|**NodeFormer: A Scalable Graph Structure Learning Transformer for Node Classification**|Qitian Wu et.al.|[2306.08385](http://arxiv.org/abs/2306.08385)|**[link](https://github.com/qitianwu/nodeformer)**|
|**2023-06-14**|**Carbon emissions and sustainability of launching 5G mobile networks in China**|Tong Li et.al.|[2306.08337](http://arxiv.org/abs/2306.08337)|**[link](https://github.com/tong89/sustainability_5g)**|
|**2023-06-14**|**FRIGATE: Frugal Spatio-temporal Forecasting on Road Networks**|Mridul Gupta et.al.|[2306.08277](http://arxiv.org/abs/2306.08277)|**[link](https://github.com/idea-iitd/frigate)**|
|**2023-06-14**|**Uncertainty-Aware Robust Learning on Noisy Graphs**|Shuyi Chen et.al.|[2306.08210](http://arxiv.org/abs/2306.08210)|null|
|**2023-06-13**|**Vector-Quantized Graph Auto-Encoder**|Yoann Boget et.al.|[2306.07735](http://arxiv.org/abs/2306.07735)|null|
|**2023-06-15**|**Hyperbolic Graph Diffusion Model for Molecule Generation**|Lingfeng Wen et.al.|[2306.07618](http://arxiv.org/abs/2306.07618)|**[link](https://github.com/lf-wen/hgdm)**|
|**2023-06-13**|**Von Mises Mixture Distributions for Molecular Conformation Generation**|Kirk Swanson et.al.|[2306.07472](http://arxiv.org/abs/2306.07472)|**[link](https://github.com/thejonaslab/vonmises-icml-2023)**|
|**2023-06-12**|**Operator Learning with Neural Fields: Tackling PDEs on General Geometries**|Louis Serrano et.al.|[2306.07266](http://arxiv.org/abs/2306.07266)|**[link](https://github.com/louisserrano/coral)**|
|**2023-06-12**|**LIVABLE: Exploring Long-Tailed Classification of Software Vulnerability Types**|Xin-Cheng Wen et.al.|[2306.06935](http://arxiv.org/abs/2306.06935)|**[link](https://github.com/livable01/livable)**|
|**2023-06-15**|**Localised Adaptive Spatial-Temporal Graph Neural Network**|Wenying Duan et.al.|[2306.06930](http://arxiv.org/abs/2306.06930)|null|
|**2023-06-12**|**Graph Agent Network: Empowering Nodes with Decentralized Communications Capabilities for Adversarial Resilience**|Ao Liu et.al.|[2306.06909](http://arxiv.org/abs/2306.06909)|null|
|**2023-06-11**|**Graph Mixup with Soft Alignments**|Hongyi Ling et.al.|[2306.06788](http://arxiv.org/abs/2306.06788)|**[link](https://github.com/divelab/DIG)**|
|**2023-06-11**|**Between-Sample Relationship in Learning Tabular Data Using Graph and Attention Networks**|Shourav B. Rabbani et.al.|[2306.06772](http://arxiv.org/abs/2306.06772)|null|
|**2023-06-11**|**Local-to-global Perspectives on Graph Neural Networks**|Chen Cai et.al.|[2306.06547](http://arxiv.org/abs/2306.06547)|**[link](https://github.com/chen-cai-osu/mpnn-gt-connection)**|

<p align=right>(<a href=#Updated-on-20250328>back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[contributors-url]: https://github.com/Vincentqyw/cv-arxiv-daily/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[forks-url]: https://github.com/Vincentqyw/cv-arxiv-daily/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[stars-url]: https://github.com/Vincentqyw/cv-arxiv-daily/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincentqyw/cv-arxiv-daily.svg?style=for-the-badge
[issues-url]: https://github.com/Vincentqyw/cv-arxiv-daily/issues

