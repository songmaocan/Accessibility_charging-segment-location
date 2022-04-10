class Read_data:
    def __init__(self,multiplier):
        self.multiplier=multiplier

    def read_nodes(self):
        self.node_list=[]
        self.g_number_of_nodes=0
        with open("nodes.txt","r") as fl:
            lines=fl.readlines()
            for line in lines[1:]:
                str_list=line.strip().split("\t")
                node=Node()
                node.node_id=self.g_number_of_nodes
                self.node_list.append(node)
                self.g_number_of_nodes+=1
        print("Node file is okay")


    def read_links(self):
        self.link_list = []
        self.g_number_of_links=0
        #1.read available links
        with open("links.txt","r") as fl:
            lines=fl.readlines()
            for line in lines[1:]:
                str_list = line.strip().split("\t")
                link=Link()
                link.link_id=self.g_number_of_links
                # link.link_type=0
                link.from_node_id=int(str_list[1])-1
                link.to_node_id=int(str_list[2])-1

                link.travel_time=int(str_list[3])
                link.consumed_electricity=int(str_list[4])

                self.link_list.append(link)
                self.g_number_of_links+=1

                self.node_list[link.from_node_id].outbound_nodes_list.append(link.to_node_id)
                self.node_list[link.from_node_id].outbound_links_list.append(link)
                self.node_list[link.from_node_id].outbound_nodes_number = len(self.node_list[link.from_node_id].outbound_nodes_list)

                self.node_list[link.to_node_id].inbound_nodes_list.append(link.from_node_id)
                self.node_list[link.to_node_id].inbound_links_list.append(link)
                self.node_list[link.to_node_id].inbound_nodes_number = len(self.node_list[link.to_node_id].inbound_nodes_list)
        print("Link file is done!")


    def read_candidate_wireless_charging_lanes(self):
        self.read_nodes()
        self.read_links()

        with open("OD pairs.txt","r") as fl:
            self.OD_pair_list = []
            self.g_number_of_ODs = 0
            self.SP_list = []
            lines = fl.readlines()
            for line in lines[1:]:
                str_list = line.strip().split("\t")
                od_pair = (int(str_list[1]) - 1, int(str_list[2]) - 1)
                self.OD_pair_list.append(od_pair)
                self.SP_list.append(int(str_list[3]))
                self.g_number_of_ODs += 1

        with open("Candidate_charging_lanes.txt","r") as fl:
            line=fl.readlines()
            self.candidate_wireless_charging_lanes=[]
            self.candidate_wireless_charging_link_id=[]
            self.g_number_of_wireless_charging_lanes=0
            line_str = line[0].split(";")
            self.g_number_of_wireless_charging_lanes=len(line_str)
            flag=1
            total_construction_cost=0
            for item in line_str:
                link_id=int(item)-1
                self.candidate_wireless_charging_link_id.append(link_id)
                link=self.link_list[link_id]
                link.wireless_charging_lane_flag=flag
                link.base_profit_for_lagrangian=[self.multiplier]*self.g_number_of_ODs
                self.candidate_wireless_charging_lanes.append(link)
                flag+=1
                total_construction_cost+=link.travel_time

            print(total_construction_cost)
            return self.node_list, self.link_list, self.OD_pair_list, \
                   self.g_number_of_links, self.g_number_of_nodes, self.g_number_of_ODs,self.candidate_wireless_charging_lanes,\
                    self.candidate_wireless_charging_link_id,self.g_number_of_wireless_charging_lanes,self.SP_list


class Node:
    def __init__(self):
        # self.node_index=None    #From 0
        self.node_id=None  #from 0
        self.outbound_nodes_list=[]
        self.outbound_nodes_number=0
        self.outbound_links_list=[]
        self.inbound_nodes_list = []
        self.inbound_nodes_number=0
        self.inbound_links_list = []



class Link:
    def __init__(self):
        self.link_id=None
        self.wireless_charging_lane_flag=0  #candidate wireless charging lane id  ; 0 o.w.
        self.construction_Flag=0 #according to the KS
        self.from_node_id=None
        self.to_node_id=None
        self.travel_time=None
        self.consumed_electricity=None
        self.base_profit_for_lagrangian = None