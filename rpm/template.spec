Name:           ros-melodic-ros-type-introspection
Version:        2.0.1
Release:        1%{?dist}
Summary:        ROS ros_type_introspection package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_type_introspection
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roscpp-serialization
Requires:       ros-melodic-rostime
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roscpp-serialization
BuildRequires:  ros-melodic-rostime

%description
The ros_type_introspection package allows the user to parse and deserialize ROS
messages which type is unknown at compilation time.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Tue Oct 01 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.1-1
- Autogenerated by Bloom

* Tue Oct 01 2019 Davide Faconti <davide.faconti@gmail.com> - 2.0.0-1
- Autogenerated by Bloom

* Fri May 10 2019 Davide Faconti <faconti@icarustechnology.com> - 1.3.3-1
- Autogenerated by Bloom

* Wed Apr 17 2019 Davide Faconti <faconti@icarustechnology.com> - 1.3.2-1
- Autogenerated by Bloom

* Sun Mar 24 2019 Davide Faconti <faconti@icarustechnology.com> - 1.3.1-0
- Autogenerated by Bloom

* Fri Jan 25 2019 Davide Faconti <faconti@icarustechnology.com> - 1.3.0-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Davide Faconti <faconti@icarustechnology.com> - 1.1.1-0
- Autogenerated by Bloom

