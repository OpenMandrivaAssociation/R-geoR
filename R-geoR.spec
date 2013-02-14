%bcond_with bootstrap
%global packname  geoR
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.7_4
Release:          1
Summary:          Analysis of geostatistical data
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-4.tar.gz
Requires:         R-stats R-sp R-methods R-MASS R-splancs R-RandomFields
Requires:         R-scatterplot3d R-tcltk R-lattice R-graphics
%if %{without bootstrap}
Requires:         R-geoRglm
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats R-sp R-methods R-MASS R-splancs R-RandomFields
BuildRequires:    R-scatterplot3d R-tcltk R-lattice R-graphics
%if %{without bootstrap}
BuildRequires:    R-geoRglm
%endif

%description
Geostatistical analysis including traditional, likelihood-based and
Bayesian methods.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
