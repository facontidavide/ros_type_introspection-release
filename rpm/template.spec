Name:           ros-kinetic-ros-type-introspection
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS ros_type_introspection package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_type_introspection
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosbag-storage
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roscpp-serialization
Requires:       ros-kinetic-rostime
Requires:       ros-kinetic-topic-tools
BuildRequires:  gtest-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-rosbag
BuildRequires:  ros-kinetic-rosbag-storage
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roscpp-serialization
BuildRequires:  ros-kinetic-rostime
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-tf2
BuildRequires:  ros-kinetic-topic-tools

%description
The ros_type_introspection package allows the user to parse and deserialize ROS
messages which type is unknown at compilation time.

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
* Wed Oct 26 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.2-0
- Autogenerated by Bloom

* Thu Oct 20 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.1-0
- Autogenerated by Bloom

* Mon Oct 17 2016 Davide Faconti <faconti@icarustechnology.com> - 0.2.0-0
- Autogenerated by Bloom

