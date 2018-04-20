# Script generated with Bloom
pkgdesc="ROS - Launch scripts for simulating the PR2 in <a href="http://ros.org/wiki/gazebo">gazebo</a>. The simulation equivalent of pr2.launch is found here. pr2_fingertip_pressure_contact_translator produces the same ROS topics as fingertip_pressure package for simulated PR2."
url='http://ros.org/wiki/pr2_gazebo'

pkgname='ros-kinetic-pr2-gazebo'
pkgver='2.0.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gazebo'
'ros-kinetic-catkin'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-pr2-gazebo-plugins'
)

depends=('gazebo'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-fingertip-pressure'
'ros-kinetic-gazebo-plugins'
'ros-kinetic-geometry-msgs'
'ros-kinetic-image-proc'
'ros-kinetic-joint-trajectory-action'
'ros-kinetic-pr2-controller-configuration-gazebo'
'ros-kinetic-pr2-dashboard-aggregator'
'ros-kinetic-pr2-description'
'ros-kinetic-pr2-gazebo-plugins'
'ros-kinetic-pr2-gripper-action'
'ros-kinetic-pr2-head-action'
'ros-kinetic-pr2-mechanism-controllers'
'ros-kinetic-pr2-msgs'
'ros-kinetic-robot-mechanism-controllers'
'ros-kinetic-robot-pose-ekf'
'ros-kinetic-rospy'
'ros-kinetic-single-joint-position-action'
'ros-kinetic-std-msgs'
'ros-kinetic-stereo-image-proc'
'ros-kinetic-tf2-ros'
'ros-kinetic-topic-tools'
'ros-kinetic-xacro'
)

conflicts=()
replaces=()

_dir=pr2_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_gazebo $srcdir/pr2_gazebo
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

