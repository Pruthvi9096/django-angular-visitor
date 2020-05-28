import { Component, OnInit, ViewChild } from '@angular/core';
import { VisitorServiceService } from '../services/visitor-service.service';
import { Router } from '@angular/router';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator, PageEvent } from '@angular/material/paginator';


@Component({
  selector: 'app-visit-list',
  templateUrl: './visit-list.component.html',
  styleUrls: ['./visit-list.component.scss']
})
export class VisitListComponent implements OnInit {
  baseUrl = 'http://127.0.0.1:8000/v1/visits';
  visitorUrl = 'http://127.0.0.1:8000/v1/visitors';
  departmentUrl = 'http://127.0.0.1:8000/v1/departments';
  employeeUrl = 'http://127.0.0.1:8000/v1/employees';

  displayedColumns = ['visitor_name', 'emp', 'department', 'purpose', 'checkin', 'checkout'];
  datasource = null;


  result: any;
  type: string;
  visitors: any;
  departments: any;
  employees: any;
  selectedVisitor = {
    id: null,
    name: null,
    email: null,
    phone: null,
    address: null,
    image: null,
  };
  selectedEmp = {
    department: null,
    id: null,
    name: null,
  };
  purpose: string;
  pageEvent: PageEvent;
  pageIndex = 0;
  pageSize = 5;
  length = 100;
  filterValue: any;

  constructor(private service: VisitorServiceService, private router: Router) { }
  @ViewChild(MatPaginator) paginator: MatPaginator;
  ngOnInit(): void {
    this.getVisitData(this.baseUrl);
    this.getVisitorData(this.visitorUrl);
    this.getEmployeeData(this.employeeUrl);
    this.getDepartmentData(this.departmentUrl);
    this.resetForm();
  }

  getVisitData(url) {
    this.service.getVisitList(url).subscribe(data => {
      this.result = data;
      console.log(this.result);
      this.datasource = new MatTableDataSource(this.result.results);
      setTimeout(() => {
        this.datasource.paginator = this.paginator;
        this.datasource.pageSize = this.pageSize;
        this.datasource.pageIndex = this.pageIndex;
      });
      // this.datasource.data.visitor_name.forEach(element => {
      //   element.toString();
      // });
    },
      error => {
        console.log(error);
      });
  }

  getVisitorData(url) {
    this.service.getVisitorList(url).subscribe(data => {
      this.visitors = data;
    },
      error => {
        console.log(error);
      });
  }

  getDepartmentData(url) {
    this.service.getDepartmentList(url).subscribe(data => {
      this.departments = data;
    },
      error => {
        console.log(error);
      });
  }

  getEmployeeData(url) {
    this.service.getEmployeeList(url).subscribe(data => {
      this.employees = data;
    },
      error => {
        console.log(error);
      });
  }

  changeEvent(event) {
    this.type = event.target.value;
  }

  resetForm() {
    this.selectedVisitor = {
      id: null,
      name: null,
      email: null,
      phone: null,
      address: null,
      image: null,
    };
    this.selectedEmp = {
      id: null,
      department: null,
      name: null,
    };
    this.purpose = null;
    this.type = null;
  }

  onSubmit(modal) {
    const visit = {
      visitor_name: this.selectedVisitor.id,
      visit_to: this.selectedEmp.id,
      purpose: this.purpose
    };
    // alert('SUCCESS!! :-)\n\n' + JSON.stringify(visit, null, 4));
    this.service.createVisit(`${this.baseUrl}/create`, visit).subscribe(response => {
      console.log('Record Created', response);
      // this.router.navigate(['/']); 
      this.ngOnInit();
    },
      // tslint:disable-next-line: no-shadowed-variable
      error => {
        console.log(error);
      });
  }

  getNextPageData(nextPage) {
    console.log(nextPage);
    this.getVisitData(nextPage);
  }

  getPreviousPageData(previousPage) {
    this.getVisitData(previousPage);
  }

  applyFilter(filterValue: string) {
    filterValue = filterValue.trim();
    filterValue = filterValue.toLowerCase();
    this.datasource.filter = filterValue;
  }

  setupFilter() {

    this.datasource.filterPredicate = (d: any, filter: string) => {
      const textToSearch = JSON.stringify({
        visitor_name: d.visitor_name.name.toLowerCase(),
        visit_to: d.visit_to.name.toLowerCase(),
        department: d.department.toLowerCase(),
        purpose: d.purpose.toLowerCase()
      });
      return textToSearch.indexOf(filter) !== -1;
    };

  }

  checkIn(visit) {
    console.log(visit);
    const date = new Date().toISOString();
    visit.checkIn = date;
    console.log(visit)
    this.service.updateVisit(`${this.baseUrl}/${visit.id}`, visit).subscribe(respose =>{
      console.log(respose);
    },
    error => {
      console.log(error);
    });
  }
}
