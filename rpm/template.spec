Name:           ros-kinetic-pr2-gazebo
Version:        2.0.9
Release:        0%{?dist}
Summary:        ROS pr2_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-kinetic-diagnostic-aggregator
Requires:       ros-kinetic-fingertip-pressure
Requires:       ros-kinetic-gazebo-plugins
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-proc
Requires:       ros-kinetic-joint-trajectory-action
Requires:       ros-kinetic-pr2-controller-configuration-gazebo
Requires:       ros-kinetic-pr2-dashboard-aggregator
Requires:       ros-kinetic-pr2-description
Requires:       ros-kinetic-pr2-gazebo-plugins
Requires:       ros-kinetic-pr2-gripper-action
Requires:       ros-kinetic-pr2-head-action
Requires:       ros-kinetic-pr2-mechanism-controllers
Requires:       ros-kinetic-pr2-msgs
Requires:       ros-kinetic-robot-mechanism-controllers
Requires:       ros-kinetic-robot-pose-ekf
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-single-joint-position-action
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-stereo-image-proc
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-topic-tools
Requires:       ros-kinetic-xacro
BuildRequires:  gazebo-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-gazebo-plugins
BuildRequires:  ros-kinetic-pr2-gazebo-plugins

%description
Launch scripts for simulating the PR2 in gazebo. The simulation equivalent of
pr2.launch is found here. pr2_fingertip_pressure_contact_translator produces the
same ROS topics as fingertip_pressure package for simulated PR2.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Feb 18 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 2.0.9-0
- Autogenerated by Bloom

* Thu Feb 15 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 2.0.8-0
- Autogenerated by Bloom

