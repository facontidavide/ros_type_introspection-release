Name:           ros-indigo-ros-type-introspection
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS ros_type_introspection package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_type_introspection
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rosbag
Requires:       ros-indigo-rosbag-storage
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roscpp-serialization
Requires:       ros-indigo-rostime
Requires:       ros-indigo-topic-tools
BuildRequires:  gtest-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-rosbag-storage
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roscpp-serialization
BuildRequires:  ros-indigo-rostime
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-topic-tools

%description
The ros_type_introspection package allows the user to parse and deserialize ROS
messages which type is unknown at compilation time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Jun 26 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.3-0
- Autogenerated by Bloom

* Fri Jun 23 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.2-0
- Autogenerated by Bloom

* Thu Jun 22 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.1-1
- Autogenerated by Bloom

* Thu Jun 22 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.1-0
- Autogenerated by Bloom

* Tue Jun 20 2017 Davide Faconti <faconti@icarustechnology.com> - 0.6.0-0
- Autogenerated by Bloom

* Sun Apr 02 2017 Davide Faconti <faconti@icarustechnology.com> - 0.5.1-0
- Autogenerated by Bloom

* Mon Feb 13 2017 Davide Faconti <faconti@icarustechnology.com> - 0.4.3-0
- Autogenerated by Bloom

* Thu Feb 09 2017 Davide Faconti <faconti@icarustechnology.com> - 0.4.2-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Davide Faconti <faconti@icarustechnology.com> - 0.4.0-0
- Autogenerated by Bloom

* Fri Nov 04 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.3-2
- Autogenerated by Bloom

* Fri Nov 04 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.3-1
- Autogenerated by Bloom

* Fri Nov 04 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.3-0
- Autogenerated by Bloom

* Wed Oct 26 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.2-0
- Autogenerated by Bloom

* Thu Oct 20 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.1-0
- Autogenerated by Bloom

* Mon Oct 17 2016 Davide Faconti <faconti@icarustechnology.com> - 0.3.0-0
- Autogenerated by Bloom

* Mon Oct 17 2016 Davide Faconti <faconti@icarustechnology.com> - 0.2.0-0
- Autogenerated by Bloom

