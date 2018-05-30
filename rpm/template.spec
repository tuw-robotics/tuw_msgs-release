Name:           ros-kinetic-tuw-geometry-msgs
Version:        0.0.7
Release:        2%{?dist}
Summary:        ROS tuw_geometry_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-std-msgs

%description
The tuw_geometry_msgs package

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
* Wed May 30 2018 George Todoran <george.todoran@tuwien.ac.at> - 0.0.7-2
- Autogenerated by Bloom

* Wed May 30 2018 George Todoran <george.todoran@tuwien.ac.at> - 0.0.7-1
- Autogenerated by Bloom

* Wed May 30 2018 George Todoran <george.todoran@tuwien.ac.at> - 0.0.7-0
- Autogenerated by Bloom

* Thu May 03 2018 George Todoran <george.todoran@tuwien.ac.at> - 0.0.6-0
- Autogenerated by Bloom

* Wed Jan 31 2018 George Todoran <george.todoran@tuwien.ac.at> - 0.0.5-0
- Autogenerated by Bloom

* Wed Jan 31 2018 George Todoran <george.todoran@tuwien.ac.at> - 0.0.4-0
- Autogenerated by Bloom

