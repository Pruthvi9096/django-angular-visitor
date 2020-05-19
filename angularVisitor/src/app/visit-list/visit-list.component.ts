import { Component, OnInit } from '@angular/core';
import { VisitorServiceService } from '../services/visitor-service.service';
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

  result: any;
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
  visit: any = {
    visitor_name: this.selectedVisitor.id,
    visit_to: this.selectedEmp.id,
    purpose: this.purpose
  };

  constructor(private service: VisitorServiceService) { }

  ngOnInit(): void {
    this.getVisitData(this.baseUrl);
    this.getVisitorData(this.visitorUrl);
    this.getEmployeeData(this.employeeUrl);
    this.getDepartmentData(this.departmentUrl);
  }

  getVisitData(url) {
    this.service.getVisitList(url).subscribe( data => {
      this.result = data;
      console.log(this.result.results);
    },
    error => {
      console.log(error);
    });
  }

  getVisitorData(url) {
    this.service.getVisitorList(url).subscribe( data => {
      this.visitors = data;
      console.log(this.visitors);
    },
    error => {
      console.log(error);
    });
  }

  getDepartmentData(url) {
    this.service.getDepartmentList(url).subscribe( data => {
      this.departments = data;
    },
    error => {
      console.log(error);
    });
  }

  getEmployeeData(url) {
    this.service.getEmployeeList(url).subscribe( data => {
      this.employees = data;
    },
    error => {
      console.log(error);
    });
  }

  createVisit() {
    console.log('pop');
  }

  resetForm(form) {
    console.log(form);
    this.selectedVisitor = {
      id: null,
      name: null,
      email: null,
      phone: null,
      address: null,
      image: null,
    };
  }

  onSubmit() {
    alert('SUCCESS!! :-)\n\n' + JSON.stringify(this.visit, null, 4));
  }

}
