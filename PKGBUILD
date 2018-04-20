# Script generated with Bloom
pkgdesc="ROS - Gazebo Plugins for various PR2-specific sensors and actuators on the robot."
url='http://ros.org/wiki/pr2_gazebo_plugins'

pkgname='ros-kinetic-pr2-gazebo-plugins'
pkgver='2.0.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gazebo'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-cv-bridge'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-gazebo-msgs'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-nav-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-polled-camera'
'ros-kinetic-pr2-controller-manager'
'ros-kinetic-pr2-hardware-interface'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-pr2-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
)

depends=('gazebo'
'ros-kinetic-angles'
'ros-kinetic-cv-bridge'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-gazebo-msgs'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-gazebo-ros'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-transport'
'ros-kinetic-message-generation'
'ros-kinetic-message-runtime'
'ros-kinetic-nav-msgs'
'ros-kinetic-orocos-kdl'
'ros-kinetic-polled-camera'
'ros-kinetic-pr2-controller-manager'
'ros-kinetic-pr2-hardware-interface'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-pr2-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=pr2_gazebo_plugins
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_gazebo_plugins $srcdir/pr2_gazebo_plugins
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

