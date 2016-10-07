Name:           opencl-headers
Version:        2.1
Release:        1%{?dist}
Summary:        Khronos OpenCL development headers

License:        MIT
URL:            https://github.com/KhronosGroup/OpenCL-Headers
Source0:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl.h
Source1:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_d3d10.h
Source2:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_d3d11.h
Source3:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_dx9_media_sharing.h
Source4:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_egl.h
Source5:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_ext.h
Source6:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_gl.h
Source7:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_gl_ext.h
Source8:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/cl_platform.h
Source9:        https://github.com/KhronosGroup/OpenCL-Headers/raw/opencl21/opencl.h

BuildArch:      noarch

%description
Khronos OpenCL development headers.


%prep


%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE0} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE3} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE4} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE5} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE6} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE7} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE8} %{buildroot}/%{_includedir}/CL/
install -m644 %{SOURCE9} %{buildroot}/%{_includedir}/CL/


%files
%{_includedir}/CL/


%changelog
* Fri Oct 07 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.1-1
- Public release
