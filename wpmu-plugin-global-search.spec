%define		plugin	global-search
Summary:	WordPressMU Global Search
Name:		wpmu-plugin-%{plugin}
Version:	1.1
Release:	0.5
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://downloads.wordpress.org/plugin/wpmu-global-search.zip
# Source0-md5:	6132d081987834cc72412a7c92ba6853
Patch0:		localize.patch
Patch1:		results_limit.patch
URL:		http://wordpress.org/extend/plugins/wpmu-global-search/
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	wpmu >= 2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins
%define		plugindir	%{pluginsdir}/wpmu-%{plugin}
%define		_sysconfdir	/etc/webapps/wpmu

%description
Easily search through all blogs into your WordPress MU posts by post
title, post content or post author. WPMU Global Search can manage
multiple contact forms.

%prep
%setup -qn wpmu-%{plugin}
%undos readme.txt
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{plugindir},%{_sysconfdir}}
cp -a . $RPM_BUILD_ROOT%{plugindir}
mv $RPM_BUILD_ROOT{%{plugindir},%{pluginsdir}}/wpmu-global-search-loader.php
rm $RPM_BUILD_ROOT%{plugindir}/readme.txt
rm $RPM_BUILD_ROOT%{plugindir}/langs/{*.pot,*.po}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{pluginsdir}/*.php
%{plugindir}
