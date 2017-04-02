Name:           ros-jade-ros-type-introspection
Version:        0.5.1
Release:        0%{?dist}
Summary:        ROS ros_type_introspection package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_type_introspection
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-rosbag
Requires:       ros-jade-rosbag-storage
Requires:       ros-jade-roscpp
Requires:       ros-jade-roscpp-serialization
Requires:       ros-jade-rostime
Requires:       ros-jade-topic-tools
BuildRequires:  gtest-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-rosbag
BuildRequires:  ros-jade-rosbag-storage
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roscpp-serialization
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-tf2
BuildRequires:  ros-jade-topic-tools

%description
The ros_type_introspection package allows the user to parse and deserialize ROS
messages which type is unknown at compilation time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Apr 02 2017 Davide Faconti <faconti@icarustechnology.com> - 0.5.1-0
- Autogenerated by Bloom

* Tue Feb 21 2017 Davide Faconti <faconti@icarustechnology.com> - 0.4.3-0
- Autogenerated by Bloom

* Thu Feb 09 2017 Davide Faconti <faconti@icarustechnology.com> - 0.4.2-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Davide Faconti <faconti@icarustechnology.com> - 0.4.0-0
- Autogenerated by Bloom

* Wed Oct 26 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.2-0
- Autogenerated by Bloom

* Thu Oct 20 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.1-0
- Autogenerated by Bloom

