%define version 0.4.13
%define release 1

Summary:	Password manager for GNOME 2
Name:		revelation
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		File tools
URL:		http://oss.codepoet.no/revelation/
Source0:	https://bitbucket.org/erikg/%name/downloads/%name-%version.tar.xz 
Source1:	%name.png

BuildRequires:	pygtk2.0-devel
BuildRequires:	%{_lib}crack2-python
BuildRequires:	gnome-python-devel
BuildRequires:	gnome-python-extras
BuildRequires:	gnome-python-desktop
BuildRequires:	gnome-python-gconf
BuildRequires:	gnome-python-gnomevfs
BuildRequires:	python-dbus
BuildRequires:	cracklib-devel
BuildRequires:	pycrypto >= 1.9
BuildRequires:	gnome-panel-devel >= 2.9.4
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
Requires:	gnome-python
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomevfs
Requires:	python-dbus
Requires:	python-libxml2
Requires:	pycrypto >= 1.9
Requires:	pygtk2.0 >= 2.3.91
Requires(post):	desktop-file-utils shared-mime-info
Requires(postun):desktop-file-utils shared-mime-info

%description
Revelation is a password manager for the GNOME 3 desktop, released under
the GNU GPL license. It organizes accounts in a tree structure, and
stores them as AES-encrypted XML files.

%prep
%setup -q

%build
%configure2_5x \
	--disable-mime-update \
	--disable-desktop-update

%make WARN_CFLAGS=""

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std UPDATE_MIME_DATABASE=true UPDATE_DESKTOP_DATABASE=true
%{__rm} -f %buildroot%{_libdir}/python%pyver/site-packages/%name/*.pyc

# menu entry
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-Other" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


# icons
#install -m 644 -D pixmaps/revelation.png %{buildroot}%{_liconsdir}/%{name}.png
#convert -geometry 32x32 pixmaps/revelation.png %{buildroot}%{_iconsdir}/%{name}.png
#install -m 644 -D pixmaps/revelation-16x16.png %{buildroot}%{_miconsdir}/%{name}.png
mkdir -p %buildroot/{%_liconsdir,%_iconsdir,%_miconsdir}
mkdir -p %buildroot/%{_datadir}/pixmaps
install -m 644 %SOURCE1 %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 %SOURCE1 %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 %SOURCE1 %{buildroot}%{_miconsdir}/%{name}.png
cp %SOURCE1 %buildroot/%{_datadir}/pixmaps
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{py_platsitedir}/%{name}
%dir %{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/%name.xml
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png




%changelog
* Tue May 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.13-1
+ Revision: 801099
- version update 0.4.13

* Mon Nov 21 2011 Götz Waschk <waschk@mandriva.org> 0.4.12-1
+ Revision: 732153
- new version
- xz tarball
- drop patches
- update deps
- remove panel applet

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.4.11-7
+ Revision: 677909
- fix build
- br intltool
- rebuild to add gconftool as req

* Sun Sep 20 2009 Funda Wang <fwang@mandriva.org> 0.4.11-6mdv2011.0
+ Revision: 444850
- fix broken menu generation (bug#53772)

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.4.11-5mdv2010.0
+ Revision: 442697
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.4.11-4mdv2009.1
+ Revision: 319711
- rebuild with python 2.6

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.11-3mdv2009.0
+ Revision: 222748
- patch 0: fix 'error: value "0.4.11" for key "Version" in group "Desktop
  Entry" is not a known version'
- buildrequires gnome-python-devel
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

