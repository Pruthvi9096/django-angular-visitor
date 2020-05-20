import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const baseUrl = 'http://127.0.0.1:8000/v1';
@Injectable({
  providedIn: 'root'
})
export class VisitorServiceService {
  constructor(private http: HttpClient) { }

  getVisitList(url: string) {
    return this.http.get(url);
  }

  getVisitorList(url: string) {
    return this.http.get(url);
  }

  getDepartmentList(url: string) {
    return this.http.get(url);
  }

  getDepartmentDetail(url: string, id: number) {
    return this.http.get(`${url}/${id}`);
  }

  getEmployeeList(url: string) {
    return this.http.get(url);
  }

  createVisit(url: string , data: any) {
    return this.http.post(url, data);
  }
}

